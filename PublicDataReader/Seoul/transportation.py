"""
서울 열린데이터 광장 OpenAPI

1. 교통
    01.서울시 지하철호선별 역별 승하차 인원 정보
    02.서울시 버스노선별 정류장별 승하차 인원 정보
"""
import pandas as pd
import logging
import requests
from bs4 import BeautifulSoup


class Transportation:
    """
    서울 열린데이터 광장 교통 관련 정보 조회 클래스

    서울 열린데이터 광장에서 발급받은 Service Key를 입력받아 초기화합니다.

    parameters
    ----------
        serviceKey: 서비스 인증키 문자열
        debug: True이면 모든 로깅 메시지 출력, False이면 에러 로깅 메시지만 출력
    """

    def __init__(self, serviceKey, debug=False):
        # 로거 설정
        self.logger = logging.getLogger("root")
        # 로깅 레벨 설정
        if debug == True:
            self.logger.setLevel(logging.INFO)
        else:
            self.logger.setLevel(logging.ERROR)
        # 출력 포매팅 설정 - 시간, 로거이름, 로깅레벨, 메세지
        formatter = logging.Formatter("[%(levelname)s] %(message)s")
        if len(self.logger.handlers) == 0:
            # 스트림 핸들러 설정 - 콘솔에 출력
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)

        # OpenAPI 서비스 키 초기화
        self.serviceKey = serviceKey

        # ServiceKey 등록
        self.endpoint = f"http://openapi.seoul.go.kr:8088/"

        # 오퍼레이션별 URL 및 컬럼 매핑 딕셔너리
        self.metaDict = {

            "지하철승하차": {
                "url": f"{self.endpoint}{self.serviceKey}/xml/CardSubwayStatsNew/",
                "columns": ["USE_DT", "LINE_NUM", "SUB_STA_NM", "RIDE_PASGR_NUM", "ALIGHT_PASGR_NUM", "WORK_DT"]
            },

            "버스승하차": {
                "url": f"{self.endpoint}{self.serviceKey}/xml/CardBusStatisticsServiceNew/",
                "columns": ['USE_DT', 'BUS_ROUTE_ID', 'BUS_ROUTE_NO', 'BUS_ROUTE_NM', 'STND_BSST_ID', 'BSST_ARS_NO', 'BUS_STA_NM', 'RIDE_PASGR_NUM', 'ALIGHT_PASGR_NUM', 'WORK_DT']
            },

        }

    def read_data(self, category, **kwargs):
        """
        데이터 조회
        """

        # 엔드포인트, 파라미터 및 컬럼 목록 매핑
        try:
            endpoint = self.metaDict[category]['url']
            columns = self.metaDict[category]['columns']
        except:
            _error_message = f"{category} 참조 오류"
            self.logger.error(_error_message)
            return _error_message

        try:
            params = ""
            for key, value in kwargs.items():
                params += f"/{value}"
        except:
            _error_message = f"{category} 파라미터 파싱 오류"
            self.logger.error(_error_message)
            return _error_message

        try:
            check_code = "INFO-000"
            startIdx, endIdx = 1, 1000
            items = []
            while check_code == "INFO-000":

                url = f"""{endpoint}{startIdx}/{endIdx}{params}"""

                # OpenAPI 호출
                result = requests.get(url, verify=False)
                xmlsoup = BeautifulSoup(result.text, "lxml-xml")
                header = xmlsoup.find("RESULT")
                result_code = header.find("CODE").text
                result_msg = header.find("MESSAGE").text
                rows = xmlsoup.findAll("row")
                items = items + rows

                check_code = result_code
                startIdx += 1000
                endIdx += 1000

        except:
            _error_message = f"HTTP 요청 혹은 파싱 오류"
            self.logger.error(_error_message)
            return _error_message

        # 데이터프레임 생성
        try:
            df = pd.DataFrame(columns=columns)
            for item in items:
                row = {}
                for col in columns:
                    try:
                        tag = item.find(col)
                        row[col] = tag.text.strip()
                    except:
                        row[col] = ""
                df_ = pd.DataFrame([row])[columns]
                df = pd.concat([df, df_], axis=0).reset_index(drop=True)

            df = self.ChangeCols(df)
            return df

        except:
            _error_message = f"전처리 오류"
            self.logger.error(_error_message)
            return _error_message

    def ChangeCols(self, df):
        """
        영문 컬럼명을 국문 컬럼명으로 변경
        """

        self.colDict = {
            'USE_DT': '사용일자',

            'LINE_NUM': '호선명',
            'SUB_STA_NM': '역명',

            'BUS_ROUTE_ID': '노선ID',
            'BUS_ROUTE_NO': '노선번호',
            'BUS_ROUTE_NM': '노선명',
            'STND_BSST_ID': '표준버스정류장ID',
            'BSST_ARS_NO': '버스정류장ARS번호',
            'BUS_STA_NM': '역명',

            'RIDE_PASGR_NUM': '승차총승객수',
            'ALIGHT_PASGR_NUM': '하차총승객수',
            'WORK_DT': '등록일자'
        }

        df = df.rename(columns=self.colDict)
        return df

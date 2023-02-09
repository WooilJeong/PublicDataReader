"""
소상공인 진흥공단 OpenAPI
semas(Small Enterprise And Market Service)

1. StoreInfo 클래스: 소상공인시장진흥공단_상가(상권)정보_API
    01.지정 상권조회
    02.반경내 상권조회
    03.사각형내 상권조회
    04.행정구역 단위 상권조회
    05.단일 상가업소 조회
    06.건물단위 상가업소 조회
    07.지번단위 상가업소 조회
    08.행정동 단위 상가업소 조회
    09.상권내 상가업소 조회
    10.반경내 상가업소 조회
    11.사각형내 상가업소 조회
    12.다각형내 상가업소 조회
    13.업종별 상가업소 조회
    14.수정일자기준 상가업소 조회
    15.상권정보 업종 대분류 조회
    16.상권정보 업종 중분류 조회
    17.상권정보 업종 소분류 조회
"""
import pandas as pd
import logging
import requests
import xmltodict
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()


class SmallShop:

    def __init__(self, service_key=None):

        self.service_key = service_key
        self.meta_dict = {
            "지정상권": {
                "url": f"http://apis.data.go.kr/B553077/api/open/sdsc2/storeZoneOne",
                "columns": ['trarNo', 'mainTrarNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'trarArea', 'coordNum', 'coords', 'stdrDt'],
            },
            "반경상권": {
                "url": f"http://apis.data.go.kr/B553077/api/open/sdsc2/storeZoneInRadius",
                "columns": ['trarNo', 'mainTrarNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'trarArea', 'coordNum', 'coords', 'stdrDt'],
            },
            "사각형상권": {
                "url": f"http://apis.data.go.kr/B553077/api/open/sdsc2/storeZoneInRectangle",
                "columns": ['trarNo', 'mainTrarNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'trarArea', 'coordNum', 'coords', 'stdrDt'],
            },
            "행정구역상권": {
                "url": f"http://apis.data.go.kr/B553077/api/open/sdsc2/storeZoneInAdmi",
                "columns": ['trarNo', 'mainTrarNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'trarArea', 'coordNum', 'coords', 'stdrDt'],
            },
            "단일상가": {
                "url": f"http://apis.data.go.kr/B553077/api/open/sdsc2/storeOne",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },
            "건물상가": {
                "url": f"http://apis.data.go.kr/B553077/api/open/sdsc2/storeListInBuilding",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },
            "지번상가": {
                "url": f"http://apis.data.go.kr/B553077/api/open/sdsc2/storeListInPnu",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },
            "행정동상가": {
                "url": f"http://apis.data.go.kr/B553077/api/open/sdsc2/storeListInDong",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },
            "상권상가": {
                "url": f"http://apis.data.go.kr/B553077/api/open/sdsc2/storeListInArea",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },
            "반경상가": {
                "url": f"http://apis.data.go.kr/B553077/api/open/sdsc2/storeListInRadius",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },
            "사각형상가": {
                "url": f"http://apis.data.go.kr/B553077/api/open/sdsc2/storeListInRectangle",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },
            "다각형상가": {
                "url": f"http://apis.data.go.kr/B553077/api/open/sdsc2/storeListInPolygon",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },
            "업종별상가": {
                "url": f"http://apis.data.go.kr/B553077/api/open/sdsc2/storeListInUpjong",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },
            "수정일자상가": {
                "url": f"http://apis.data.go.kr/B553077/api/open/sdsc2/storeListByDate",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },
            "업종대분류": {
                "url": f"http://apis.data.go.kr/B553077/api/open/sdsc2/largeUpjongList",
                "columns": ["indsLclsCd", "indsLclsNm", "stdrDt"],
            },
            "업종중분류": {
                "url": f"http://apis.data.go.kr/B553077/api/open/sdsc2/middleUpjongList",
                "columns": ["indsLclsCd", "indsLclsNm", "indsMclsCd", "indsMclsNm", "stdrDt"],
            },
            "업종소분류": {
                "url": f"http://apis.data.go.kr/B553077/api/open/sdsc2/smallUpjongList",
                "columns": ['indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'stdrDt'],
            },
        }

    def get_data(self,
                 service_name,
                 key=None,
                 divId=None,
                 radius=None,
                 cx=None,
                 cy=None,
                 minx=None,
                 miny=None,
                 maxx=None,
                 maxy=None,
                 translate=True,
                 verbose=False,
                 **kwargs
                 ):
        try:
            # 서비스명으로 API URL 선택 (ex. 지정상권, 반경상권, 사각형상권 등)
            url = self.meta_dict.get(service_name).get("url")
            # 서비스명으로 API 컬럼 선택 (ex. 지정상권, 반경상권, 사각형상권 등)
            columns = self.meta_dict.get(service_name).get("columns")
        except AttributeError:
            raise AttributeError("서비스명을 확인해주세요.")
        # 서비스키, 행수, 시군구코드, 법정동코드 설정
        params = {
            "serviceKey": requests.utils.unquote(self.service_key),
            "pageNo": 1,
            "numOfRows": 99999,
            "key": key,
            "divId": divId,
            "radius": radius,
            "cx": cx,
            "cy": cy,
            "minx": minx,
            "miny": miny,
            "maxx": maxx,
            "maxy": maxy,
        }
        # 선택 파라미터 추가 설정
        params.update(kwargs)
        # 빈 데이터 프레임 생성
        df = pd.DataFrame(columns=columns)
        # API 요청
        res = requests.get(url, params=params, verify=False)
        # 요청 결과 JSON 변환
        res_json = xmltodict.parse(res.text)
        # 응답 키 존재 확인
        if not res_json.get("response"):
            if verbose:
                print(res_json)
            raise Exception("API 요청이 실패했습니다.")
        # 결과코드가 정상이 아닌 경우
        if res_json['response']['header']['resultCode'] != '00':
            if res_json['response']['header']['resultCode'] == '03':
                if verbose:
                    print("조회 결과가 없습니다.")
                return pd.DataFrame(columns=columns)
            else:
                error_message = res_json['response']['header']['resultMsg']
                raise Exception(error_message)
        items = res_json['response']['body']['items']
        if not items:
            return pd.DataFrame(columns=columns)
        data = items['item']
        if isinstance(data, list):
            sub = pd.DataFrame(data)
        elif isinstance(data, dict):
            sub = pd.DataFrame([data])
        df = pd.concat([df, sub], axis=0, ignore_index=True)
        if len(df) >= 99999:
            print("행수가 99999개를 초과했습니다. 다음 페이지를 조회하세요.")
        # 컬럼명 한글로 변경
        if translate:
            df = self.translate_columns(df)
        return df

    def translate_columns(self, df):
        """
        영문 컬럼명을 한글로 변경
        """
        rename_columns = {
            'adongCd': '행정동코드',
            'adongNm': '행정동명',
            'bizesId': '상가업소번호',
            'bizesNm': '상호명',
            'bldMngNo': '건물관리번호',
            'bldMnno': '건물본번지',
            'bldNm': '건물명',
            'bldSlno': '건물부번지',
            'brchNm': '지점명',
            'coordNum': '좌표개수',
            'coords': '좌표값',
            'ctprvnCd': '시도코드',
            'ctprvnNm': '시도명',
            'dongNo': '동정보',
            'flrNo': '층정보',
            'hoNo': '호정보',
            'indsLclsCd': '상권업종대분류코드',
            'indsLclsNm': '상권업종대분류명',
            'indsMclsCd': '상권업종중분류코드',
            'indsMclsNm': '상권업종중분류명',
            'indsSclsCd': '상권업종소분류코드',
            'indsSclsNm': '상권업종소분류명',
            'ksicCd': '표준산업분류코드',
            'ksicNm': '표준산업분류명',
            'lat': '위도',
            'ldongCd': '법정동코드',
            'ldongNm': '법정동명',
            'lnoAdr': '지번주소',
            'lnoCd': 'PNU코드',
            'lnoMnno': '지번본번지',
            'lnoSlno': '지번부번지',
            'lon': '경도',
            'mainTrarNm': '상권명',
            'newZipcd': '신우편번호',
            'oldZipcd': '구우편번호',
            'plotSctCd': '대지구분코드',
            'plotSctNm': '대지구분명',
            'rdnm': '도로명',
            'rdnmAdr': '도로명주소',
            'rdnmCd': '도로명코드',
            'signguCd': '시군구코드',
            'signguNm': '시군구명',
            'stdrDt': '데이터기준일자',
            'trarArea': '면적',
            'trarNo': '상권번호'
        }
        return df.rename(columns=rename_columns)


# (Deprecated Class)


class StoreInfo:
    """
    소상공인 상가업소 정보 조회 클래스

    공공 데이터 포털에서 발급받은 Service Key를 입력받아 초기화합니다.

    parameters
    ----------
        serviceKey: 서비스 인증키 문자열
        debug: True이면 모든 로깅 메시지 출력, False이면 에러 로깅 메시지만 출력
    """

    def __init__(self, serviceKey=None, debug=False):
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
        self.endpoint = f"http://apis.data.go.kr/B553077/api/open/sdsc2/"

        # 오퍼레이션별 URL 및 컬럼 매핑 딕셔너리
        self.metaDict = {

            "지정상권": {
                "url": f"{self.endpoint}storeZoneOne?serviceKey={self.serviceKey}",
                "columns": ['trarNo', 'mainTrarNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'trarArea', 'coordNum', 'coords', 'stdrDt'],
            },

            "반경상권": {
                "url": f"{self.endpoint}storeZoneInRadius?serviceKey={self.serviceKey}",
                "columns": ['trarNo', 'mainTrarNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'trarArea', 'coordNum', 'coords', 'stdrDt'],
            },

            "사각형상권": {
                "url": f"{self.endpoint}storeZoneInRectangle?serviceKey={self.serviceKey}",
                "columns": ['trarNo', 'mainTrarNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'trarArea', 'coordNum', 'coords', 'stdrDt'],
            },

            "행정구역상권": {
                "url": f"{self.endpoint}storeZoneInAdmi?serviceKey={self.serviceKey}",
                "columns": ['trarNo', 'mainTrarNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'trarArea', 'coordNum', 'coords', 'stdrDt'],
            },

            "단일상가": {
                "url": f"{self.endpoint}storeOne?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "건물상가": {
                "url": f"{self.endpoint}storeListInBuilding?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "지번상가": {
                "url": f"{self.endpoint}storeListInPnu?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "행정동상가": {
                "url": f"{self.endpoint}storeListInDong?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "상권상가": {
                "url": f"{self.endpoint}storeListInArea?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "반경상가": {
                "url": f"{self.endpoint}storeListInRadius?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "사각형상가": {
                "url": f"{self.endpoint}storeListInRectangle?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "다각형상가": {
                "url": f"{self.endpoint}storeListInPolygon?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "업종별상가": {
                "url": f"{self.endpoint}storeListInUpjong?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "수정일자상가": {
                "url": f"{self.endpoint}storeListByDate?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "업종대분류": {
                "url": f"{self.endpoint}largeUpjongList?serviceKey={self.serviceKey}",
                "columns": ["indsLclsCd", "indsLclsNm", "stdrDt"],
            },

            "업종중분류": {
                "url": f"{self.endpoint}middleUpjongList?serviceKey={self.serviceKey}",
                "columns": ["indsLclsCd", "indsLclsNm", "indsMclsCd", "indsMclsNm", "stdrDt"],
            },

            "업종소분류": {
                "url": f"{self.endpoint}smallUpjongList?serviceKey={self.serviceKey}",
                "columns": ['indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'stdrDt'],
            },

        }

    def read_data(self, category, **kwargs):
        """
        데이터 조회

        parameters
        ----------
            category: 오퍼레이션 종류 (ex. 지정상권, 반경상권, 사각형상권, 행정구역상권 등)
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
                params += f"&{key}={value}"
        except:
            _error_message = f"{category} 파라미터 파싱 오류"
            self.logger.error(_error_message)
            return _error_message

        try:
            # URL
            url = f"""{endpoint}{params}&numOfRows=99999"""

            # OpenAPI 호출
            result = requests.get(url, verify=False)
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            header = xmlsoup.find("header")
            result_code = header.find("resultCode").text
            result_msg = header.find("resultMsg").text
            items = xmlsoup.findAll("item")

        except:
            _error_message = f"HTTP 요청 혹은 파싱 오류"
            self.logger.error(_error_message)
            return _error_message

        if result_code == "00":
            """
            결과 정상
            """
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

        else:
            """
            결과 에러
            """
            _error_message = f"({result_code}) {result_msg}"
            self.logger.error(_error_message)
            return _error_message

    def ChangeCols(self, df):
        """
        영문 컬럼명을 국문 컬럼명으로 변경
        """

        self.colDict = {
            'adongCd': '행정동코드',
            'adongNm': '행정동명',
            'bizesId': '상가업소번호',
            'bizesNm': '상호명',
            'bldMngNo': '건물관리번호',
            'bldMnno': '건물본번지',
            'bldNm': '건물명',
            'bldSlno': '건물부번지',
            'brchNm': '지점명',
            'coordNum': '좌표개수',
            'coords': '좌표값',
            'ctprvnCd': '시도코드',
            'ctprvnNm': '시도명',
            'dongNo': '동정보',
            'flrNo': '층정보',
            'hoNo': '호정보',
            'indsLclsCd': '상권업종대분류코드',
            'indsLclsNm': '상권업종대분류명',
            'indsMclsCd': '상권업종중분류코드',
            'indsMclsNm': '상권업종중분류명',
            'indsSclsCd': '상권업종소분류코드',
            'indsSclsNm': '상권업종소분류명',
            'ksicCd': '표준산업분류코드',
            'ksicNm': '표준산업분류명',
            'lat': '위도',
            'ldongCd': '법정동코드',
            'ldongNm': '법정동명',
            'lnoAdr': '지번주소',
            'lnoCd': 'PNU코드',
            'lnoMnno': '지번본번지',
            'lnoSlno': '지번부번지',
            'lon': '경도',
            'mainTrarNm': '상권명',
            'newZipcd': '신우편번호',
            'oldZipcd': '구우편번호',
            'plotSctCd': '대지구분코드',
            'plotSctNm': '대지구분명',
            'rdnm': '도로명',
            'rdnmAdr': '도로명주소',
            'rdnmCd': '도로명코드',
            'signguCd': '시군구코드',
            'signguNm': '시군구명',
            'stdrDt': '데이터기준일자',
            'trarArea': '면적',
            'trarNo': '상권번호'
        }

        df = df.rename(columns=self.colDict)
        return df

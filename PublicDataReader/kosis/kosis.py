"""
KOSIS Open API Python Module
"""
import json
import requests
import pandas as pd

requests.packages.urllib3.disable_warnings()


class Kosis:
    """KOSIS 공유서비스 클래스

    KOSIS 공유서비스에서 발급받은 사용자 인증키를 입력받아 초기화합니다.

    Parameters
    ----------
    service_key : str
        KOSIS 공유서비스에서 발급받은 사용자 인증키
    """

    def __init__(self, service_key=None):
        self.service_key = service_key
        self.meta_dict = {
            "KOSIS통합검색": {
                "url": "https://kosis.kr/openapi/statisticsSearch.do?method=getList",
                "columns": ['ORG_ID', 'ORG_NM', 'TBL_ID', 'TBL_NM', 'STAT_ID', 'STAT_NM', 'VW_CD', 'MT_ATITLE', 'FULL_PATH_ID', 'CONTENTS', 'STRT_PRD_DE', 'END_PRD_DE', 'ITEM03', 'REC_TBL_SE', 'TBL_VIEW_URL', 'LINK_URL', 'STAT_DB_CNT', 'QUERY'],
            },
            "통계설명": {
                "url": "https://kosis.kr/openapi/statisticsExplData.do?method=getList",
                "columns": ['statsNm', 'statsKind', 'statsContinue', 'basisLaw', 'writingPurps', 'statsPeriod', 'writingSystem', 'pubExtent', 'pubPeriod', 'writingTel', 'statsField', 'examinObjrange', 'examinObjArea', 'josaUnit', 'applyGroup', 'josaItm', 'publictMth', 'examinTrgetPd', 'examinPd', 'dataUserNote', 'mainTermExpl', 'dataCollectMth', 'examinHistory', 'confmNo', 'confmDt', 'statsEnd',]
            },
            "통계표설명": {
                "url": "https://kosis.kr/openapi/statisticsData.do?method=getMeta",
                "columns": {
                    "통계표명칭": ['TBL_NM', 'TBL_NM_ENG',],
                    "기관명칭": ['ORG_NM', 'ORG_NM_ENG',],
                    "수록정보": ['PRD_SE', 'STRT_PRD_DE', 'END_PRD_DE', 'PRD_DE',],
                    "분류항목": ['ORG_ID', 'TBL_ID', 'CD_ID', 'CD_NM', 'OBJ_ID', 'OBJ_NM', 'OBJ_NM_ENG', 'ITM_ID', 'ITM_NM', 'ITM_NM_ENG', 'UP_ITM_ID', 'OBJ_ID_SN', 'UNIT_ID', 'UNIT_NM', 'UNIT_ENG_NM',],
                    "주석": ['CMMT_NM', 'CMMT_DC', 'OBJ_ID', 'OBJ_NM', 'ITM_ID', 'ITM_NM', ],
                    "단위": ['UNIT_NM', 'UNIT_NM_ENG',],
                    "출처": ['JOSA_NM', 'DEPT_NM', 'DEPT_PHONE',],
                    "가중치": ['C1', 'C1_NM', 'C2', 'C2_NM', 'C3', 'C3_NM', 'C4', 'C4_NM', 'C5', 'C5_NM', 'C6', 'C6_NM', 'C7', 'C7_NM', 'C8', 'C8_NM', 'ITM_ID', 'ITM_NM', 'WGT_CO',],
                    "자료갱신일": ['ORG_NM', 'TBL_NM', 'PRD_SE', 'PRD_DE', 'SEND_DE',],
                },
            },
            "통계목록": {
                "url": "https://kosis.kr/openapi/statisticsList.do?method=getList",
                "columns": ['VW_CD', 'VW_NM', 'LIST_ID', 'LIST_NM', 'ORG_ID', 'TBL_ID', 'TBL_NM', 'REC_TBL_SE']
            },
            "통계자료": {
                "url": "https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList",
                "columns": ['ORG_ID', 'TBL_ID', 'TBL_NM', 'C1_OBJ_NM', 'C1_OBJ_NM_ENG', 'C1_NM', 'C1_NM_ENG', 'C1', 'C2_OBJ_NM', 'C2_OBJ_NM_ENG', 'C2_NM', 'C2_NM_ENG', 'C2', 'C3_OBJ_NM', 'C3_OBJ_NM_ENG', 'C3_NM', 'C3_NM_ENG', 'C3', 'C4_OBJ_NM', 'C4_OBJ_NM_ENG', 'C4_NM', 'C4_NM_ENG', 'C4', 'C5_OBJ_NM', 'C5_OBJ_NM_ENG', 'C5_NM', 'C5_NM_ENG', 'C5', 'C6_OBJ_NM', 'C6_OBJ_NM_ENG', 'C6_NM', 'C6_NM_ENG', 'C6', 'C7_OBJ_NM', 'C7_OBJ_NM_ENG', 'C7_NM', 'C7_NM_ENG', 'C7', 'C8_OBJ_NM', 'C8_OBJ_NM_ENG', 'C8_NM', 'C8_NM_ENG', 'C8', 'ITM_ID', 'ITM_NM', 'ITM_NM_ENG', 'UNIT_ID', 'UNIT_NM', 'UNIT_NM_ENG', 'PRD_SE', 'PRD_DE', 'DT',]
            },
        }
        self.type_dict = {
            "통계표명칭": "TBL",
            "기관명칭": "ORG",
            "수록정보": "PRD",
            "분류항목": "ITM",
            "주석": "CMMT",
            "단위": "UNIT",
            "출처": "SOURCE",
            "가중치": "WGT",
            "자료갱신일": "NCD",
        }

    def get_data(self,
                 service_name,
                 detail_service_name=None,
                 translate=True,
                 **kwargs):
        """
        API 호출

        KOSIS 공유서비스 API를 호출하여 데이터를 반환합니다.

        Parameters
        ----------
        service_name : str
            API 호출에 필요한 서비스명 (ex. KOSIS통합검색, 통계설명, 통계표설명, 통계목록, 통계자료)
        detail_service_name : str
            *통계표설명 서비스에만 적용됩니다.
            API 호출에 필요한 상세 서비스명 (ex. 통계표명칭, 기관명칭, 수록정보, 분류항목, 주석, 단위, 출처, 가중치, 자료갱신일)
        translate : bool
            한글 컬럼명으로 변환 여부 (기본값: True)
        **kwargs : dict
            API 호출에 필요한 파라미터

        Returns
        -------
        DataFrame
            API 호출 결과를 DataFrame 형태로 반환합니다.
        """
        try:
            # 서비스명으로 API URL 선택 (ex. KOSIS통합검색, 통계설명, 통계표설명, 통계목록, 통계자료)
            url = self.meta_dict.get(service_name).get("url")
            # 서비스명으로 API Columns 선택 (ex. KOSIS통합검색, 통계설명, 통계표설명, 통계목록, 통계자료)
            if not service_name == "통계표설명":
                columns = self.meta_dict.get(service_name).get("columns")
            else:
                columns = self.meta_dict.get(service_name).get(
                    "columns").get(detail_service_name)
        except AttributeError:
            raise AttributeError(
                "서비스명을 확인해주세요. (ex. KOSIS통합검색, 통계설명, 통계표설명, 통계목록, 통계자료)")

        params = {
            "apiKey": requests.utils.unquote(self.service_key),
            "format": "json",
            "jsonVD": "Y",
            "jsonMVD": "Y",
        }
        if service_name == "통계표설명" and detail_service_name:
            # 상세 서비스명으로 파라미터 추가 (ex. 통계표명칭, 기관명칭, 수록정보, 분류항목, 주석, 단위, 출처, 가중치, 자료갱신일)
            params["type"] = self.type_dict.get(detail_service_name)
        params.update(kwargs)

        # 빈 데이터 프레임 생성
        df = pd.DataFrame(columns=columns)

        try:
            # API 요청
            res = requests.get(url, params=params, verify=False)
            # API 응답 결과를 JSON 형태로 변환
            try:
                res_json = res.json()
            except Exception as e:
                res_json = json.loads(res.text.replace("\t", "SEND_DE"))
        except Exception as e:
            print("API 요청이 실패했습니다.")
            print(e)
            return None

        try:
            if type(res_json) == dict:
                if res_json.get("errMsg"):
                    print(res_json.get("errMsg"))
                    return None
            else:
                sub = pd.DataFrame(res_json)
                df = pd.concat([df, sub], axis=0, ignore_index=True).dropna(
                    axis=1, how="all")
            if translate:
                df = self.translate_columns(
                    df, service_name, detail_service_name)
            return df
        except:
            print("Data Frame Failed!")
            return None

    def translate_columns(self, df, service_name, detail_service_name=None):
        """
        영문 컬럼명을 한글로 변경
        """
        rename_columns = {
            "KOSIS통합검색": {
                'ORG_ID': '기관ID',
                'ORG_NM': '기관명',
                'TBL_ID': '통계표ID',
                'TBL_NM': '통계표명',
                'STAT_ID': '조사ID',
                'STAT_NM': '조사명',
                'VW_CD': 'KOSIS목록구분',
                'MT_ATITLE': 'KOSIS통계표위치',
                'FULL_PATH_ID': '통계표위치',
                'CONTENTS': '통계표주요내용',
                'STRT_PRD_DE': '수록기간시작일',
                'END_PRD_DE': '수록기간종료일',
                'ITEM03': '통계표주석',
                'REC_TBL_SE': '추천통계표여부',
                'TBL_VIEW_URL': 'KOSIS목록URL',
                'LINK_URL': 'KOSIS통계표URL',
                'STAT_DB_CNT': '검색결과건수',
                'QUERY': '검색어명',
            },
            "통계설명": {
                'statsNm': '조사명',
                'statsKind': '통계종류',
                'statsContinue': '계속여부',
                'basisLaw': '법적근거',
                'writingPurps': '조사목적',
                'statsPeriod': '조사주기',
                'writingSystem': '조사체계',
                'pubExtent': '공표범위',
                'pubPeriod': '공표주기',
                'writingTel': '연락처',
                'statsField': '통계활용분야실태',
                'examinObjrange': '조사대상범위',
                'examinObjArea': '조사대상지역',
                'josaUnit': '조사단위및조사대상규모',
                'applyGroup': '적용분류',
                'josaItm': '조사항목',
                'publictMth': '공표방법및URL',
                'examinTrgetPd': '조사대상기간및조사기준시점',
                'examinPd': '조사기간',
                'dataUserNote': '자료이용자유의사항',
                'mainTermExpl': '주요용어해설',
                'dataCollectMth': '자료수집방법',
                'examinHistory': '조사연혁',
                'confmNo': '승인번호',
                'confmDt': '승인일자',
                'statsEnd': '통계종료',
            },
            "통계표설명": {
                "통계표명칭": {
                    'TBL_NM': '통계표명',
                    'TBL_NM_ENG': '통계표영문명',
                },
                "기관명칭": {
                    'ORG_NM': '기관명',
                    'ORG_NM_ENG': '기관영문명',
                },
                "수록정보": {
                    'PRD_SE': '수록주기',
                    'STRT_PRD_DE': '수록기간시작일',
                    'END_PRD_DE': '수록기간종료일',
                    'PRD_DE': '수록시점',
                },
                "분류항목": {
                    'ORG_ID': '기관ID',
                    'TBL_ID': '통계표ID',
                    'CD_ID': '코드ID',
                    'CD_NM': '코드명',
                    'OBJ_ID': '분류ID',
                    'OBJ_NM': '분류명',
                    'OBJ_NM_ENG': '분류영문명',
                    'ITM_ID': '분류값ID',
                    'ITM_NM': '분류값명',
                    'ITM_NM_ENG': '분류값영문명',
                    'UP_ITM_ID': '상위분류값ID',
                    'OBJ_ID_SN': '분류값순번',
                    'UNIT_ID': '단위ID',
                    'UNIT_NM': '단위명',
                    'UNIT_ENG_NM': '단위영문명',
                },
                "주석": {
                    'CMMT_NM': '주석유형',
                    'CMMT_DC': '주석',
                    'OBJ_ID': '분류ID',
                    'OBJ_NM': '분류명',
                    'ITM_ID': '분류값ID',
                    'ITM_NM': '분류값명',
                },
                "단위": {
                    'UNIT_NM': '단위명',
                    'UNIT_NM_ENG': '단위영문명',
                },
                "출처": {
                    'JOSA_NM': '조사명',
                    'DEPT_NM': '통계표담당부서',
                    'DEPT_PHONE': '통계표담당부서전화번호',
                },
                "가중치": {
                    'C1': '분류값ID1',
                    'C1_NM': '분류값명1',
                    'C2': '분류값ID2',
                    'C2_NM': '분류값명2',
                    'C3': '분류값ID3',
                    'C3_NM': '분류값명3',
                    'C4': '분류값ID4',
                    'C4_NM': '분류값명4',
                    'C5': '분류값ID5',
                    'C5_NM': '분류값명5',
                    'C6': '분류값ID6',
                    'C6_NM': '분류값명6',
                    'C7': '분류값ID7',
                    'C7_NM': '분류값명7',
                    'C8': '분류값ID8',
                    'C8_NM': '분류값명8',
                    'ITM_ID': '항목ID',
                    'ITM_NM': '항목명',
                    'WGT_CO': '가중치',
                },
                "자료갱신일": {
                    'ORG_NM': '기관명',
                    'TBL_NM': '통계표명',
                    'PRD_SE': '수록주기',
                    'PRD_DE': '수록시점',
                    'SEND_DE': '자료갱신일',
                },
            },
            "통계목록": {
                'VW_CD': '서비스뷰ID',
                'VW_NM': '서비스뷰명',
                'LIST_ID': '목록ID',
                'LIST_NM': '목록명',
                'ORG_ID': '기관ID',
                'TBL_ID': '통계표ID',
                'TBL_NM': '통계표명',
                'REC_TBL_SE': '추천통계표여부',
            },
            "통계자료": {
                'ORG_ID': '기관ID',
                'TBL_ID': '통계표ID',
                'TBL_NM': '통계표명',
                'C1_OBJ_NM': '분류명1',
                'C1_OBJ_NM_ENG': '분류영문명1',
                'C1_NM': '분류값명1',
                'C1_NM_ENG': '분류값영문명1',
                'C1': '분류값ID1',
                'C2_OBJ_NM': '분류명2',
                'C2_OBJ_NM_ENG': '분류영문명2',
                'C2_NM': '분류값명2',
                'C2_NM_ENG': '분류값영문명2',
                'C2': '분류값ID2',
                'C3_OBJ_NM': '분류명3',
                'C3_OBJ_NM_ENG': '분류영문명3',
                'C3_NM': '분류값명3',
                'C3_NM_ENG': '분류값영문명3',
                'C3': '분류값ID3',
                'C4_OBJ_NM': '분류명4',
                'C4_OBJ_NM_ENG': '분류영문명4',
                'C4_NM': '분류값명4',
                'C4_NM_ENG': '분류값영문명4',
                'C4': '분류값ID4',
                'C5_OBJ_NM': '분류명5',
                'C5_OBJ_NM_ENG': '분류영문명5',
                'C5_NM': '분류값명5',
                'C5_NM_ENG': '분류값영문명5',
                'C5': '분류값ID5',
                'C6_OBJ_NM': '분류명6',
                'C6_OBJ_NM_ENG': '분류영문명6',
                'C6_NM': '분류값명6',
                'C6_NM_ENG': '분류값영문명6',
                'C6': '분류값ID6',
                'C7_OBJ_NM': '분류명7',
                'C7_OBJ_NM_ENG': '분류영문명7',
                'C7_NM': '분류값명7',
                'C7_NM_ENG': '분류값영문명7',
                'C7': '분류값ID7',
                'C8_OBJ_NM': '분류명8',
                'C8_OBJ_NM_ENG': '분류영문명8',
                'C8_NM': '분류값명8',
                'C8_NM_ENG': '분류값영문명8',
                'C8': '분류값ID8',
                'ITM_ID': '항목ID',
                'ITM_NM': '항목명',
                'ITM_NM_ENG': '항목영문명',
                'UNIT_ID': '단위ID',
                'UNIT_NM': '단위명',
                'UNIT_NM_ENG': '단위영문명',
                'PRD_SE': '수록주기',
                'PRD_DE': '수록시점',
                'DT': '수치값',
            },
        }
        try:
            if service_name == "통계표설명" and detail_service_name:
                rename_columns = rename_columns.get(
                    service_name).get(detail_service_name)
            else:
                rename_columns = rename_columns.get(service_name)
        except AttributeError:
            raise AttributeError(
                "서비스명을 확인해주세요. (ex. KOSIS통합검색, 통계설명, 통계표설명, 통계목록, 통계자료)")

        return df.rename(columns=rename_columns)

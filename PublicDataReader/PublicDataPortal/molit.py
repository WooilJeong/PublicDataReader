"""
국토교통부 Open API
molit(Ministry of Land, Infrastructure and Transport)

1. Transaction 클래스: 부동산 실거래가 조회
    - AptTrade: 아파트매매 실거래자료 조회
    - AptTradeDetail: 아파트매매 실거래 상세 자료 조회
    - AptRent: 아파트 전월세 자료 조회
    - AptOwnership: 아파트 분양권전매 신고 자료 조회
    - OffiTrade: 오피스텔 매매 신고 조회
    - OffiRent: 오피스텔 전월세 신고 조회
    - RHTrade: 연립다세대 매매 실거래자료 조회
    - RHRent: 연립다세대 전월세 실거래자료 조회
    - DHTrade: 단독/다가구 매매 실거래 조회
    - DHRent: 단독/다가구 전월세 자료 조회
    - LandTrade: 토지 매매 신고 조회
    - BizTrade: 상업업무용 부동산 매매 신고 자료 조회

2. Building 클래스: 건축물대장정보 서비스
    01 건축물대장 기본개요 조회: getBrBasisOulnInfo
    02 건축물대장 총괄표제부 조회: getBrRecapTitleInfo
    03 건축물대장 표제부 조회: getBrTitleInfo
    04 건축물대장 층별개요 조회: getBrFlrOulnInfo
    05 건축물대장 부속지번 조회: getBrAtchJibunInfo
    06 건축물대장 전유공용면적 조회: getBrExposPubuseAreaInfo
    07 건축물대장 오수정화시설 조회: getBrWclfInfo
    08 건축물대장 주택가격 조회: getBrHsprcInfo
    09 건축물대장 전유부 조회: getBrExposInfo
    10 건축물대장 지역지구구역 조회: getBrJijiguInfo
"""

import pandas as pd
import numpy as np
import datetime
import requests
from bs4 import BeautifulSoup


class Transaction:
    """
    부동산 실거래가 조회 클래스
    """

    def __init__(self, serviceKey):
        """
        공공 데이터 포털에서 발급받은 Service Key를 입력받아 초기화합니다.
        """
        # Open API 서비스 키 초기화
        self.serviceKey = serviceKey

        # ServiceKey 유효성 검사
        self.urlAptTrade = (
            "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?serviceKey="
            + self.serviceKey
        )
        self.urlAptTradeDetail = (
            "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?serviceKey="
            + self.serviceKey
        )
        self.urlAptRent = (
            "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent?serviceKey="
            + self.serviceKey
        )
        self.urlAptOwnership = (
            "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSilvTrade?serviceKey="
            + self.serviceKey
        )
        self.urlOffiTrade = (
            "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcOffiTrade?serviceKey="
            + self.serviceKey
        )
        self.urlOffiRent = (
            "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcOffiRent?serviceKey="
            + self.serviceKey
        )
        self.urlRHTrade = (
            "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHTrade?serviceKey="
            + self.serviceKey
        )
        self.urlRHRent = (
            "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHRent?serviceKey="
            + self.serviceKey
        )
        self.urlDHTrade = (
            "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSHTrade?serviceKey="
            + self.serviceKey
        )
        self.urlDHRent = (
            "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSHRent?serviceKey="
            + self.serviceKey
        )
        self.urlLandTrade = (
            "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcLandTrade?serviceKey="
            + self.serviceKey
        )
        self.urlBizTrade = (
            "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcNrgTrade?serviceKey="
            + self.serviceKey
        )

        # Open API URL Dict
        urlDict = {
            "아파트매매 실거래자료 조회": self.urlAptTrade,
            "아파트매매 실거래 상세 자료 조회": self.urlAptTradeDetail,
            "아파트 전월세 자료 조회": self.urlAptRent,
            "아파트 분양권전매 신고 자료 조회": self.urlAptOwnership,
            "오피스텔 매매 신고 조회": self.urlOffiTrade,
            "오피스텔 전월세 신고 조회": self.urlOffiRent,
            "연립다세대 매매 실거래자료 조회": self.urlRHTrade,
            "연립다세대 전월세 실거래자료 조회": self.urlRHRent,
            "단독/다가구 매매 실거래 조회": self.urlDHTrade,
            "단독/다가구 전월세 자료 조회": self.urlDHRent,
            "토지 매매 신고 조회": self.urlLandTrade,
            "상업업무용 부동산 매매 신고 자료 조회": self.urlBizTrade,
        }

        # 서비스 정상 작동 여부 확인
        for serviceName, url in urlDict.items():
            result = requests.get(url, verify=False)
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            te = xmlsoup.findAll("header")
            if te[0].find("resultCode").text == "00":
                print(f">>> {serviceName} 서비스가 정상 작동합니다.")
            else:
                print(f">>> {serviceName} 서비스키 미등록 오류입니다.")

        # 지역 코드 초기화
        # 법정동 코드 출처 : https://code.go.kr
        path_code = "https://raw.githubusercontent.com/WooilJeong/PublicDataReader/f14e4de3410cc0f798a83ee5934070d651cbd67b/docs/%EB%B2%95%EC%A0%95%EB%8F%99%EC%BD%94%EB%93%9C%20%EC%A0%84%EC%B2%B4%EC%9E%90%EB%A3%8C.txt"
        code = pd.read_csv(path_code, encoding="cp949", sep="\t")
        code = code.loc[code["폐지여부"] == "존재"]
        code["법정구코드"] = list(map(lambda a: str(a)[:5], list(code["법정동코드"])))
        self.code = code

    def CodeFinder(self, name):
        """
        국토교통부 실거래가 정보 오픈API는 법정동코드 10자리 중 앞 5자리인 구를 나타내는 지역코드를 사용합니다.
        API에 사용할 구 별 코드를 조회하는 메서드이며, 문자열 지역 명을 입력받고, 조회 결과를 Pandas DataFrame형식으로 출력합니다.
        """
        result = self.code[self.code["법정동명"].str.contains(name)][["법정동명", "법정구코드"]]
        result.index = range(len(result))
        return result

    def DataCollector(self, service, LAWD_CD, start_date, end_date):
        """
        서비스별 기간별 조회
        입력: 서비스별 조회 메서드, 지역코드, 시작월(YYYYmm), 종료월(YYYYmm)
        """
        start_date = datetime.datetime.strptime(str(start_date), "%Y%m")
        start_date = datetime.datetime.strftime(start_date, "%Y-%m")

        end_date = datetime.datetime.strptime(str(end_date), "%Y%m")
        end_date = end_date + datetime.timedelta(days=31)
        end_date = datetime.datetime.strftime(end_date, "%Y-%m")

        ts = pd.date_range(start=start_date, end=end_date, freq="m")
        date_list = list(ts.strftime("%Y%m"))

        df = pd.DataFrame()
        df_sum = pd.DataFrame()
        for m in date_list:
            print(">>> LAWD_CD :", LAWD_CD, "DEAL_YMD :", m)
            DEAL_YMD = m
            df = service(LAWD_CD, DEAL_YMD)
            df_sum = pd.concat([df_sum, df])
        df_sum.index = range(len(df_sum))

        return df_sum

    def AptTrade(self, LAWD_CD, DEAL_YMD):
        """
        01 아파트매매 실거래자료 조회
        입력: 지역코드(법정동코드 5자리), 계약월(YYYYmm)
        """
        # URL
        url_1 = self.urlAptTrade + "&LAWD_CD=" + str(LAWD_CD)
        url_2 = "&DEAL_YMD=" + str(DEAL_YMD)
        url_3 = "&numOfRows=99999"
        url = url_1 + url_2 + url_3

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")
            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = ["법정동", "지역코드", "아파트", "지번", "년", "월", "일", "건축년도", "전용면적", "층", "거래금액"]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [[법정동, 지역코드, 아파트, 지번, 년, 월, 일, 건축년도, 전용면적, 층, 거래금액]], columns=variables
                )
                df = pd.concat([df, data])

            # Set Columns
            colNames = ["지역코드", "법정동", "거래일", "아파트", "지번", "전용면적", "층", "건축년도", "거래금액"]

            # Feature Engineering
            try:
                if len(df["년"] != 0) & len(df["월"] != 0) & len(df["일"] != 0):
                    df["거래일"] = df["년"] + "-" + df["월"] + "-" + df["일"]
                    df["거래일"] = pd.to_datetime(df["거래일"])
                    df["거래금액"] = pd.to_numeric(df["거래금액"].str.replace(",", ""))
            except:
                df = pd.DataFrame(columns=colNames)
                print("조회할 자료가 없습니다.")

            # Arange Columns
            df = df[colNames]
            df = df.sort_values(["법정동", "거래일"])
            df["법정동"] = df["법정동"].str.strip()
            df["아파트"] = df["아파트"].str.strip()
            df.index = range(len(df))

            # 형 변환
            cols = df.columns.drop(["법정동", "거래일", "아파트", "지번"])
            df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")

            return df

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

    def AptTradeDetail(self, LAWD_CD, DEAL_YMD):
        """
        02 아파트매매 실거래 상세 자료 조회
        입력: 지역코드(법정동코드 5자리), 계약월(YYYYmm)
        """
        # URL
        url_1 = self.urlAptTradeDetail + "&LAWD_CD=" + str(LAWD_CD)
        url_2 = "&DEAL_YMD=" + str(DEAL_YMD)
        url_3 = "&numOfRows=99999"
        url = url_1 + url_2 + url_3

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")
            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "거래금액",
                "건축년도",
                "년",
                "도로명",
                "도로명건물본번호코드",
                "도로명건물부번호코드",
                "도로명시군구코드",
                "도로명일련번호코드",
                "도로명지상지하코드",
                "도로명코드",
                "법정동",
                "법정동본번코드",
                "법정동부번코드",
                "법정동시군구코드",
                "법정동읍면동코드",
                "법정동지번코드",
                "아파트",
                "월",
                "일",
                "전용면적",
                "지번",
                "지역코드",
                "층",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            거래금액,
                            건축년도,
                            년,
                            도로명,
                            도로명건물본번호코드,
                            도로명건물부번호코드,
                            도로명시군구코드,
                            도로명일련번호코드,
                            도로명지상지하코드,
                            도로명코드,
                            법정동,
                            법정동본번코드,
                            법정동부번코드,
                            법정동시군구코드,
                            법정동읍면동코드,
                            법정동지번코드,
                            아파트,
                            월,
                            일,
                            전용면적,
                            지번,
                            지역코드,
                            층,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])

            # Set Columns
            colNames = [
                "지역코드",
                "법정동",
                "거래일",
                "아파트",
                "지번",
                "전용면적",
                "층",
                "건축년도",
                "거래금액",
                "법정동본번코드",
                "법정동부번코드",
                "법정동시군구코드",
                "법정동읍면동코드",
                "법정동지번코드",
                "도로명",
                "도로명건물본번호코드",
                "도로명건물부번호코드",
                "도로명시군구코드",
                "도로명일련번호코드",
                "도로명지상지하코드",
                "도로명코드",
            ]
            # Feature Engineering
            try:
                if len(df["년"] != 0) & len(df["월"] != 0) & len(df["일"] != 0):

                    df["거래일"] = df["년"] + "-" + df["월"] + "-" + df["일"]
                    df["거래일"] = pd.to_datetime(df["거래일"])
                    df["거래금액"] = pd.to_numeric(df["거래금액"].str.replace(",", ""))

            except:
                df = pd.DataFrame(columns=colNames)
                print("조회할 자료가 없습니다.")

            # Arange Columns
            df = df[colNames]
            df = df.sort_values(["법정동", "거래일"])
            df["법정동"] = df["법정동"].str.strip()
            df["아파트"] = df["아파트"].str.strip()
            df.index = range(len(df))

            # 숫자형 변환
            cols = df.columns.drop(["법정동", "거래일", "아파트", "지번", "도로명"])
            df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")

            return df

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

    def AptRent(self, LAWD_CD, DEAL_YMD):
        """
        03 아파트 전월세 자료 조회
        입력: 지역코드(법정동코드 5자리), 계약월(YYYYmm)
        """
        # URL
        url_1 = self.urlAptRent + "&LAWD_CD=" + str(LAWD_CD)
        url_2 = "&DEAL_YMD=" + str(DEAL_YMD)
        url_3 = "&numOfRows=99999"
        url = url_1 + url_2 + url_3

        try:
            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "법정동",
                "지역코드",
                "아파트",
                "지번",
                "년",
                "월",
                "일",
                "건축년도",
                "전용면적",
                "층",
                "보증금액",
                "월세금액",
            ]
            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [[법정동, 지역코드, 아파트, 지번, 년, 월, 일, 건축년도, 전용면적, 층, 보증금액, 월세금액]], columns=variables
                )
                df = pd.concat([df, data])

            # Set Columns
            colNames = ["지역코드", "법정동", "거래일", "아파트", "지번", "전용면적", "층", "건축년도", "보증금액", "월세금액"]

            # Feature Engineering
            try:
                if len(df["년"] != 0) & len(df["월"] != 0) & len(df["일"] != 0):

                    df["거래일"] = df["년"] + "-" + df["월"] + "-" + df["일"]
                    df["거래일"] = pd.to_datetime(df["거래일"])
                    df["보증금액"] = pd.to_numeric(df["보증금액"].str.replace(",", ""))
                    df["월세금액"] = pd.to_numeric(df["월세금액"].str.replace(",", ""))

            except:
                df = pd.DataFrame(columns=colNames)
                print("조회할 자료가 없습니다.")

            # Arange Columns
            df = df[colNames]
            df = df.sort_values(["법정동", "거래일"])
            df["법정동"] = df["법정동"].str.strip()
            df.index = range(len(df))

            # 숫자형 변환
            cols = df.columns.drop(["법정동", "거래일", "지번", "아파트"])
            df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")

            return df

        except:

            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("header")

            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")

            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))

            pass

    def AptOwnership(self, LAWD_CD, DEAL_YMD):
        """
        04 아파트 분양권전매 신고 자료 조회
        입력: 지역코드(법정동코드 5자리), 계약월(YYYYmm)
        """
        # URL
        url_1 = self.urlAptOwnership + "&LAWD_CD=" + str(LAWD_CD)
        url_2 = "&DEAL_YMD=" + str(DEAL_YMD)
        url_3 = "&numOfRows=99999"
        url = url_1 + url_2 + url_3

        try:
            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = ["법정동", "지역코드", "시군구", "단지", "지번", "구분", "년", "월", "일", "전용면적", "층", "거래금액"]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [[법정동, 지역코드, 시군구, 단지, 지번, 구분, 년, 월, 일, 전용면적, 층, 거래금액]], columns=variables
                )
                df = pd.concat([df, data])

            # Set Columns
            colNames = ["지역코드", "법정동", "거래일", "시군구", "단지", "지번", "구분", "전용면적", "층", "거래금액"]

            # Feature Engineering
            try:
                if len(df["년"] != 0) & len(df["월"] != 0) & len(df["일"] != 0):

                    df["거래일"] = df["년"] + "-" + df["월"] + "-" + df["일"]
                    df["거래일"] = pd.to_datetime(df["거래일"])
                    df["거래금액"] = pd.to_numeric(df["거래금액"].str.replace(",", ""))

            except:
                df = pd.DataFrame(columns=colNames)
                print("조회할 자료가 없습니다.")

            # Arange Columns
            df = df[colNames]
            df = df.sort_values(["법정동", "거래일"])
            df["법정동"] = df["법정동"].str.strip()
            df.index = range(len(df))

            # 숫자형 변환
            cols = df.columns.drop(["법정동", "거래일", "시군구", "단지", "지번", "구분"])
            df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")

            return df

        except:

            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("header")

            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")

            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))

            pass

    def OffiTrade(self, LAWD_CD, DEAL_YMD):
        """
        05 오피스텔 매매 신고 조회
        입력: 지역코드(법정동코드 5자리), 계약월(YYYYmm)
        """
        # URL
        url_1 = self.urlOffiTrade + "&LAWD_CD=" + str(LAWD_CD)
        url_2 = "&DEAL_YMD=" + str(DEAL_YMD)
        url_3 = "&numOfRows=99999"
        url = url_1 + url_2 + url_3

        try:
            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = ["법정동", "지역코드", "시군구", "단지", "지번", "년", "월", "일", "전용면적", "층", "거래금액"]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [[법정동, 지역코드, 시군구, 단지, 지번, 년, 월, 일, 전용면적, 층, 거래금액]], columns=variables
                )
                df = pd.concat([df, data])

            # Set Columns
            colNames = ["지역코드", "법정동", "거래일", "시군구", "단지", "지번", "전용면적", "층", "거래금액"]

            # Feature Engineering
            try:
                if len(df["년"] != 0) & len(df["월"] != 0) & len(df["일"] != 0):

                    df["거래일"] = df["년"] + "-" + df["월"] + "-" + df["일"]
                    df["거래일"] = pd.to_datetime(df["거래일"])
                    df["거래금액"] = pd.to_numeric(df["거래금액"].str.replace(",", ""))

            except:
                df = pd.DataFrame(columns=colNames)
                print("조회할 자료가 없습니다.")

            # Arange Columns
            df = df[colNames]
            df = df.sort_values(["법정동", "거래일"])
            df["법정동"] = df["법정동"].str.strip()
            df.index = range(len(df))

            # 숫자형 변환
            cols = df.columns.drop(["법정동", "거래일", "시군구", "단지", "지번"])
            df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")

            return df

        except:

            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("header")

            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")

            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))

            pass

    def OffiRent(self, LAWD_CD, DEAL_YMD):
        """
        06 오피스텔 전월세 신고 조회
        입력: 지역코드(법정동코드 5자리), 계약월(YYYYmm)
        """
        # URL
        url_1 = self.urlOffiRent + "&LAWD_CD=" + str(LAWD_CD)
        url_2 = "&DEAL_YMD=" + str(DEAL_YMD)
        url_3 = "&numOfRows=99999"
        url = url_1 + url_2 + url_3

        try:
            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = ["법정동", "지역코드", "시군구", "단지", "지번", "년", "월", "일", "전용면적", "층", "보증금", "월세"]
            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [[법정동, 지역코드, 시군구, 단지, 지번, 년, 월, 일, 전용면적, 층, 보증금, 월세]], columns=variables
                )
                df = pd.concat([df, data])

            # Set Columns
            colNames = ["지역코드", "법정동", "거래일", "시군구", "단지", "지번", "전용면적", "층", "보증금", "월세"]

            # Feature Engineering
            try:
                if len(df["년"] != 0) & len(df["월"] != 0) & len(df["일"] != 0):

                    df["거래일"] = df["년"] + "-" + df["월"] + "-" + df["일"]
                    df["거래일"] = pd.to_datetime(df["거래일"])
                    df["보증금"] = pd.to_numeric(df["보증금"].str.replace(",", ""))
                    df["월세"] = pd.to_numeric(df["월세"].str.replace(",", ""))

            except:
                df = pd.DataFrame(columns=colNames)
                print("조회할 자료가 없습니다.")

            # Arange Columns
            df = df[colNames]
            df = df.sort_values(["법정동", "거래일"])
            df["법정동"] = df["법정동"].str.strip()
            df.index = range(len(df))

            # 숫자형 변환
            cols = df.columns.drop(["법정동", "거래일", "시군구", "단지", "지번"])
            df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")

            return df

        except:

            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("header")

            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")

            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))

            pass

    def RHTrade(self, LAWD_CD, DEAL_YMD):
        """
        07 연립다세대 매매 실거래자료 조회
        입력: 지역코드(법정동코드 5자리), 계약월(YYYYmm)
        """
        # URL
        url_1 = self.urlRHTrade + "&LAWD_CD=" + str(LAWD_CD)
        url_2 = "&DEAL_YMD=" + str(DEAL_YMD)
        url_3 = "&numOfRows=99999"
        url = url_1 + url_2 + url_3

        try:
            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = ["법정동", "지역코드", "연립다세대", "지번", "년", "월", "일", "전용면적", "건축년도", "층", "거래금액"]
            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [[법정동, 지역코드, 연립다세대, 지번, 년, 월, 일, 전용면적, 건축년도, 층, 거래금액]], columns=variables
                )
                df = pd.concat([df, data])

            # Set Columns
            colNames = ["지역코드", "법정동", "거래일", "연립다세대", "지번", "전용면적", "건축년도", "층", "거래금액"]

            # Feature Engineering
            try:
                if len(df["년"] != 0) & len(df["월"] != 0) & len(df["일"] != 0):

                    df["거래일"] = df["년"] + "-" + df["월"] + "-" + df["일"]
                    df["거래일"] = pd.to_datetime(df["거래일"])
                    df["거래금액"] = pd.to_numeric(df["거래금액"].str.replace(",", ""))

            except:
                df = pd.DataFrame(columns=colNames)
                print("조회할 자료가 없습니다.")

            # Arange Columns
            df = df[colNames]
            df = df.sort_values(["법정동", "거래일"])
            df["법정동"] = df["법정동"].str.strip()
            df.index = range(len(df))

            # 숫자형 변환
            cols = df.columns.drop(["법정동", "거래일", "연립다세대", "지번"])
            df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")

            return df

        except:

            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("header")

            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")

            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))

            pass

    def RHRent(self, LAWD_CD, DEAL_YMD):
        """
        08 연립다세대 전월세 실거래자료 조회
        입력: 지역코드(법정동코드 5자리), 계약월(YYYYmm)
        """
        # URL
        url_1 = self.urlRHRent + "&LAWD_CD=" + str(LAWD_CD)
        url_2 = "&DEAL_YMD=" + str(DEAL_YMD)
        url_3 = "&numOfRows=99999"
        url = url_1 + url_2 + url_3

        try:
            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "법정동",
                "지역코드",
                "연립다세대",
                "지번",
                "년",
                "월",
                "일",
                "전용면적",
                "건축년도",
                "층",
                "보증금액",
                "월세금액",
            ]
            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [[법정동, 지역코드, 연립다세대, 지번, 년, 월, 일, 전용면적, 건축년도, 층, 보증금액, 월세금액]], columns=variables
                )
                df = pd.concat([df, data])

            # Set Columns
            colNames = ["지역코드", "법정동", "거래일", "연립다세대", "지번", "전용면적", "건축년도", "층", "보증금액", "월세금액"]

            # Feature Engineering
            try:
                if len(df["년"] != 0) & len(df["월"] != 0) & len(df["일"] != 0):

                    df["거래일"] = df["년"] + "-" + df["월"] + "-" + df["일"]
                    df["거래일"] = pd.to_datetime(df["거래일"])
                    df["보증금액"] = pd.to_numeric(df["보증금액"].str.replace(",", ""))
                    df["월세금액"] = pd.to_numeric(df["월세금액"].str.replace(",", ""))

            except:
                df = pd.DataFrame(columns=colNames)
                print("조회할 자료가 없습니다.")

            # Arange Columns
            df = df[colNames]
            df = df.sort_values(["법정동", "거래일"])
            df["법정동"] = df["법정동"].str.strip()
            df.index = range(len(df))

            # 숫자형 변환
            cols = df.columns.drop(["법정동", "거래일", "연립다세대", "지번"])
            df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")

            return df

        except:

            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("header")

            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")

            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))

            pass

    def DHTrade(self, LAWD_CD, DEAL_YMD):
        """
        09 단독/다가구 매매 실거래 조회
        입력: 지역코드(법정동코드 5자리), 계약월(YYYYmm)
        """
        # URL
        url_1 = self.urlDHTrade + "&LAWD_CD=" + str(LAWD_CD)
        url_2 = "&DEAL_YMD=" + str(DEAL_YMD)
        url_3 = "&numOfRows=99999"
        url = url_1 + url_2 + url_3

        try:
            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = ["법정동", "지역코드", "주택유형", "년", "월", "일", "대지면적", "연면적", "건축년도", "거래금액"]
            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [[법정동, 지역코드, 주택유형, 년, 월, 일, 대지면적, 연면적, 건축년도, 거래금액]], columns=variables
                )
                df = pd.concat([df, data])

            # Set Columns
            colNames = ["지역코드", "법정동", "거래일", "주택유형", "대지면적", "연면적", "건축년도", "거래금액"]

            # Feature Engineering
            try:
                if len(df["년"] != 0) & len(df["월"] != 0) & len(df["일"] != 0):

                    df["거래일"] = df["년"] + "-" + df["월"] + "-" + df["일"]
                    df["거래일"] = pd.to_datetime(df["거래일"])
                    df["거래금액"] = pd.to_numeric(df["거래금액"].str.replace(",", ""))

            except:
                df = pd.DataFrame(columns=colNames)
                print("조회할 자료가 없습니다.")

            # Arange Columns
            df = df[colNames]
            df = df.sort_values(["법정동", "거래일"])
            df["법정동"] = df["법정동"].str.strip()
            df.index = range(len(df))

            # 숫자형 변환
            cols = df.columns.drop(["법정동", "거래일", "주택유형"])
            df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")

            return df

        except:

            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("header")

            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")

            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))

            pass

    def DHRent(self, LAWD_CD, DEAL_YMD):
        """
        10 단독/다가구 전월세 자료 조회
        입력: 지역코드(법정동코드 5자리), 계약월(YYYYmm)
        """
        # URL
        url_1 = self.urlDHRent + "&LAWD_CD=" + str(LAWD_CD)
        url_2 = "&DEAL_YMD=" + str(DEAL_YMD)
        url_3 = "&numOfRows=99999"
        url = url_1 + url_2 + url_3

        try:
            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = ["법정동", "지역코드", "년", "월", "일", "계약면적", "보증금액", "월세금액"]
            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame([[법정동, 지역코드, 년, 월, 일, 계약면적, 보증금액, 월세금액]], columns=variables)
                df = pd.concat([df, data])

            # Set Columns
            colNames = ["지역코드", "법정동", "거래일", "계약면적", "보증금액", "월세금액"]

            # Feature Engineering
            try:
                if len(df["년"] != 0) & len(df["월"] != 0) & len(df["일"] != 0):

                    df["거래일"] = df["년"] + "-" + df["월"] + "-" + df["일"]
                    df["거래일"] = pd.to_datetime(df["거래일"])
                    df["보증금액"] = pd.to_numeric(df["보증금액"].str.replace(",", ""))
                    df["월세금액"] = pd.to_numeric(df["월세금액"].str.replace(",", ""))

            except:
                df = pd.DataFrame(columns=colNames)
                print("조회할 자료가 없습니다.")

            # Arange Columns
            df = df[colNames]
            df = df.sort_values(["법정동", "거래일"])
            df["법정동"] = df["법정동"].str.strip()
            df.index = range(len(df))

            # 숫자형 변환
            cols = df.columns.drop(["법정동", "거래일"])
            df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")

            return df

        except:

            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("header")

            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")

            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))

            pass

    def LandTrade(self, LAWD_CD, DEAL_YMD):
        """
        11 토지 매매 신고 조회
        입력: 지역코드(법정동코드 5자리), 계약월(YYYYmm)
        """
        # URL
        url_1 = self.urlLandTrade + "&LAWD_CD=" + str(LAWD_CD)
        url_2 = "&DEAL_YMD=" + str(DEAL_YMD)
        url_3 = "&numOfRows=99999"
        url = url_1 + url_2 + url_3

        try:
            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "법정동",
                "지역코드",
                "시군구",
                "용도지역",
                "지목",
                "년",
                "월",
                "일",
                "지분거래구분",
                "거래면적",
                "거래금액",
            ]
            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [[법정동, 지역코드, 시군구, 용도지역, 지목, 년, 월, 일, 지분거래구분, 거래면적, 거래금액]], columns=variables
                )
                df = pd.concat([df, data])

            # Set Columns
            colNames = ["지역코드", "법정동", "거래일", "시군구", "용도지역", "지목", "지분거래구분", "거래면적", "거래금액"]

            # Feature Engineering
            try:
                if len(df["년"] != 0) & len(df["월"] != 0) & len(df["일"] != 0):

                    df["거래일"] = df["년"] + "-" + df["월"] + "-" + df["일"]
                    df["거래일"] = pd.to_datetime(df["거래일"])
                    df["거래금액"] = pd.to_numeric(df["거래금액"].str.replace(",", ""))

            except:
                df = pd.DataFrame(columns=colNames)
                print("조회할 자료가 없습니다.")

            # Arange Columns
            df = df[colNames]
            df = df.sort_values(["법정동", "거래일"])
            df["법정동"] = df["법정동"].str.strip()
            df.index = range(len(df))

            # 숫자형 변환
            cols = df.columns.drop(["법정동", "거래일", "시군구", "용도지역", "지목", "지분거래구분"])
            df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")

            return df

        except:

            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("header")

            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")

            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))

            pass

    def BizTrade(self, LAWD_CD, DEAL_YMD):
        """
        12 상업업무용 부동산 매매 신고 자료 조회
        입력: 지역코드(법정동코드 5자리), 계약월(YYYYmm)
        """
        # URL
        url_1 = self.urlBizTrade + "&LAWD_CD=" + str(LAWD_CD)
        url_2 = "&DEAL_YMD=" + str(DEAL_YMD)
        url_3 = "&numOfRows=99999"
        url = url_1 + url_2 + url_3

        try:
            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "거래금액",
                "건물면적",
                "건물주용도",
                "건축년도",
                "구분",
                "년",
                "월",
                "일",
                "대지면적",
                "법정동",
                "시군구",
                "용도지역",
                "유형",
                "지역코드",
                "층",
            ]
            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [[거래금액, 건물면적, 건물주용도, 건축년도, 구분, 년, 월, 일, 대지면적, 법정동, 시군구, 용도지역, 유형, 지역코드, 층]],
                    columns=variables,
                )
                df = pd.concat([df, data])

            # Set Columns
            colNames = [
                "지역코드",
                "법정동",
                "거래일",
                "시군구",
                "용도지역",
                "유형",
                "대지면적",
                "구분",
                "건물면적",
                "건물주용도",
                "건축년도",
                "층",
                "거래금액",
            ]

            # Feature Engineering
            try:
                if len(df["년"] != 0) & len(df["월"] != 0) & len(df["일"] != 0):

                    df["거래일"] = df["년"] + "-" + df["월"] + "-" + df["일"]
                    df["거래일"] = pd.to_datetime(df["거래일"])
                    df["거래금액"] = pd.to_numeric(df["거래금액"].str.replace(",", ""))

            except:
                df = pd.DataFrame(columns=colNames)
                print("조회할 자료가 없습니다.")

            # Arange Columns
            df = df[colNames]
            df = df.sort_values(["법정동", "거래일"])
            df["법정동"] = df["법정동"].str.strip()
            df.index = range(len(df))

            # 숫자형 변환
            cols = df.columns.drop(["법정동", "거래일", "시군구", "용도지역", "유형", "건물주용도"])
            df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")

            return df

        except:

            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")

            # Filtering
            te = xmlsoup.findAll("header")

            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")

            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))

            pass


class Building:
    """
    건축물대장정보 서비스
    """

    def __init__(self, serviceKey):
        """
        공공 데이터 포털에서 발급받은 Service Key를 입력받아 초기화합니다.
        """
        # Open API 서비스 키 초기화
        self.serviceKey = serviceKey

        # ServiceKey 유효성 검사
        self.baseUrl = "http://apis.data.go.kr/1613000/BldRgstService_v2/"

        self.url_getBrBasisOulnInfo = (
            self.baseUrl + "getBrBasisOulnInfo" + f"?serviceKey={self.serviceKey}"
        )
        self.url_getBrRecapTitleInfo = (
            self.baseUrl + "getBrRecapTitleInfo" + f"?serviceKey={self.serviceKey}"
        )
        self.url_getBrTitleInfo = self.baseUrl + "getBrTitleInfo" + f"?serviceKey={self.serviceKey}"
        self.url_getBrFlrOulnInfo = (
            self.baseUrl + "getBrFlrOulnInfo" + f"?serviceKey={self.serviceKey}"
        )
        self.url_getBrAtchJibunInfo = (
            self.baseUrl + "getBrAtchJibunInfo" + f"?serviceKey={self.serviceKey}"
        )

        self.url_getBrExposPubuseAreaInfo = (
            self.baseUrl + "getBrExposPubuseAreaInfo" + f"?serviceKey={self.serviceKey}"
        )
        self.url_getBrWclfInfo = self.baseUrl + "getBrWclfInfo" + f"?serviceKey={self.serviceKey}"
        self.url_getBrHsprcInfo = self.baseUrl + "getBrHsprcInfo" + f"?serviceKey={self.serviceKey}"
        self.url_getBrExposInfo = self.baseUrl + "getBrExposInfo" + f"?serviceKey={self.serviceKey}"
        self.url_getBrJijiguInfo = (
            self.baseUrl + "getBrJijiguInfo" + f"?serviceKey={self.serviceKey}"
        )

        # Open API URL Dict
        urlDict = {
            "건축물대장 기본개요 조회": self.url_getBrBasisOulnInfo,
            "건축물대장 총괄표제부 조회": self.url_getBrRecapTitleInfo,
            "건축물대장 표제부 조회": self.url_getBrTitleInfo,
            "건축물대장 층별개요 조회": self.url_getBrFlrOulnInfo,
            "건축물대장 부속지번 조회": self.url_getBrAtchJibunInfo,
            "건축물대장 전유공용면적 조회": self.url_getBrExposPubuseAreaInfo,
            "건축물대장 오수정화시설 조회": self.url_getBrWclfInfo,
            "건축물대장 주택가격 조회": self.url_getBrHsprcInfo,
            "건축물대장 전유부 조회": self.url_getBrExposInfo,
            "건축물대장 지역지구구역 조회": self.url_getBrJijiguInfo,
        }

        # 서비스 정상 작동 여부 확인
        for serviceName, url in urlDict.items():
            result = requests.get(url, verify=False)
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            te = xmlsoup.findAll("header")
            if te[0].find("resultCode").text == "00":
                print(f">>> {serviceName} 서비스가 정상 작동합니다.")
            else:
                print(f">>> {serviceName} 서비스키 미등록 오류입니다.")

        # 지역 코드 초기화
        # 법정동 코드 출처 : https://code.go.kr
        path_code = "https://raw.githubusercontent.com/WooilJeong/PublicDataReader/f14e4de3410cc0f798a83ee5934070d651cbd67b/docs/%EB%B2%95%EC%A0%95%EB%8F%99%EC%BD%94%EB%93%9C%20%EC%A0%84%EC%B2%B4%EC%9E%90%EB%A3%8C.txt"
        code = pd.read_csv(path_code, encoding="cp949", sep="\t")
        code = code.loc[code["폐지여부"] == "존재"]
        code["법정구코드"] = list(map(lambda a: str(a)[:5], list(code["법정동코드"])))
        self.code = code

    def CodeFinder(self, name):
        """
        국토교통부 실거래가 정보 오픈API는 법정동코드 10자리 중 앞 5자리인 구를 나타내는 지역코드를 사용합니다.
        API에 사용할 구 별 코드를 조회하는 메서드이며, 문자열 지역 명을 입력받고, 조회 결과를 Pandas DataFrame형식으로 출력합니다.
        """
        result = self.code[self.code["법정동명"].str.contains(name)][["법정동명", "법정구코드"]]
        result.index = range(len(result))
        return result

    def getBrBasisOulnInfo(
        self, sigunguCd, bjdongCd, platGbCd="", bun="", ji="", startDate="", endDate=""
    ):
        """
        01 건축물대장 기본개요 조회
        입력: 시군구코드, 법정동코드, 대지구분코드, 번, 지
        """
        # URL
        url = f"{self.url_getBrBasisOulnInfo}&sigunguCd={sigunguCd}&bjdongCd={bjdongCd}&platGbCd={platGbCd}&bun={bun}&ji={ji}&startDate={startDate}&endDate={endDate}&numOfRows=99999"

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")
            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "bjdongCd",
                "bldNm",
                "block",
                "bun",
                "bylotCnt",
                "crtnDay",
                "guyukCd",
                "guyukCdNm",
                "ji",
                "jiguCd",
                "jiguCdNm",
                "jiyukCd",
                "jiyukCdNm",
                "lot",
                "mgmBldrgstPk",
                "mgmUpBldrgstPk",
                "naBjdongCd",
                "naMainBun",
                "naRoadCd",
                "naSubBun",
                "naUgrndCd",
                "newPlatPlc",
                "platGbCd",
                "platPlc",
                "regstrGbCd",
                "regstrGbCdNm",
                "regstrKindCd",
                "regstrKindCdNm",
                "rnum",
                "sigunguCd",
                "splotNm",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            bjdongCd,
                            bldNm,
                            block,
                            bun,
                            bylotCnt,
                            crtnDay,
                            guyukCd,
                            guyukCdNm,
                            ji,
                            jiguCd,
                            jiguCdNm,
                            jiyukCd,
                            jiyukCdNm,
                            lot,
                            mgmBldrgstPk,
                            mgmUpBldrgstPk,
                            naBjdongCd,
                            naMainBun,
                            naRoadCd,
                            naSubBun,
                            naUgrndCd,
                            newPlatPlc,
                            platGbCd,
                            platPlc,
                            regstrGbCd,
                            regstrGbCdNm,
                            regstrKindCd,
                            regstrKindCdNm,
                            rnum,
                            sigunguCd,
                            splotNm,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])
                df.index = range(len(df))

            return df

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

    def getBrRecapTitleInfo(
        self, sigunguCd, bjdongCd, platGbCd="", bun="", ji="", startDate="", endDate=""
    ):
        """
        02 건축물대장 총괄표제부 조회
        입력: 시군구코드, 법정동코드, 대지구분코드, 번, 지, 검색시작일, 검색종료일
        """
        # URL
        url = f"{self.url_getBrRecapTitleInfo}&sigunguCd={sigunguCd}&bjdongCd={bjdongCd}&platGbCd={platGbCd}&bun={bun}&ji={ji}&startDate={startDate}&endDate={endDate}&numOfRows=99999"
        print(url)
        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")
            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "archArea",
                "atchBldArea",
                "atchBldCnt",
                "bcRat",
                "bjdongCd",
                "bldNm",
                "block",
                "bun",
                "bylotCnt",
                "crtnDay",
                "engrEpi",
                "engrGrade",
                "engrRat",
                "etcPurps",
                "fmlyCnt",
                "gnBldCert",
                "gnBldGrade",
                "hhldCnt",
                "hoCnt",
                "indrAutoArea",
                "indrAutoUtcnt",
                "indrMechArea",
                "indrMechUtcnt",
                "itgBldCert",
                "itgBldGrade",
                "ji",
                "lot",
                "mainBldCnt",
                "mainPurpsCd",
                "mainPurpsCdNm",
                "mgmBldrgstPk",
                "naBjdongCd",
                "naMainBun",
                "naRoadCd",
                "naSubBun",
                "naUgrndCd",
                "newOldRegstrGbCd",
                "newOldRegstrGbCdNm",
                "newPlatPlc",
                "oudrAutoArea",
                "oudrAutoUtcnt",
                "oudrMechArea",
                "oudrMechUtcnt",
                "platArea",
                "platGbCd",
                "platPlc",
                "pmsDay",
                "pmsnoGbCd",
                "pmsnoGbCdNm",
                "pmsnoKikCd",
                "pmsnoKikCdNm",
                "pmsnoYear",
                "regstrGbCd",
                "regstrGbCdNm",
                "regstrKindCd",
                "regstrKindCdNm",
                "rnum",
                "sigunguCd",
                "splotNm",
                "stcnsDay",
                "totArea",
                "totPkngCnt",
                "useAprDay",
                "vlRat",
                "vlRatEstmTotArea",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            archArea,
                            atchBldArea,
                            atchBldCnt,
                            bcRat,
                            bjdongCd,
                            bldNm,
                            block,
                            bun,
                            bylotCnt,
                            crtnDay,
                            engrEpi,
                            engrGrade,
                            engrRat,
                            etcPurps,
                            fmlyCnt,
                            gnBldCert,
                            gnBldGrade,
                            hhldCnt,
                            hoCnt,
                            indrAutoArea,
                            indrAutoUtcnt,
                            indrMechArea,
                            indrMechUtcnt,
                            itgBldCert,
                            itgBldGrade,
                            ji,
                            lot,
                            mainBldCnt,
                            mainPurpsCd,
                            mainPurpsCdNm,
                            mgmBldrgstPk,
                            naBjdongCd,
                            naMainBun,
                            naRoadCd,
                            naSubBun,
                            naUgrndCd,
                            newOldRegstrGbCd,
                            newOldRegstrGbCdNm,
                            newPlatPlc,
                            oudrAutoArea,
                            oudrAutoUtcnt,
                            oudrMechArea,
                            oudrMechUtcnt,
                            platArea,
                            platGbCd,
                            platPlc,
                            pmsDay,
                            pmsnoGbCd,
                            pmsnoGbCdNm,
                            pmsnoKikCd,
                            pmsnoKikCdNm,
                            pmsnoYear,
                            regstrGbCd,
                            regstrGbCdNm,
                            regstrKindCd,
                            regstrKindCdNm,
                            rnum,
                            sigunguCd,
                            splotNm,
                            stcnsDay,
                            totArea,
                            totPkngCnt,
                            useAprDay,
                            vlRat,
                            vlRatEstmTotArea,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])
                df.index = range(len(df))

            return df

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

    def getBrTitleInfo(
        self, sigunguCd, bjdongCd, platGbCd="", bun="", ji="", startDate="", endDate=""
    ):
        """
        03 건축물대장 표제부 조회: getBrTitleInfo
        입력: 시군구코드, 법정동코드, 대지구분코드, 번, 지, 검색시작일, 검색종료일
        """
        # URL
        url = f"{self.url_getBrTitleInfo}&sigunguCd={sigunguCd}&bjdongCd={bjdongCd}&platGbCd={platGbCd}&bun={bun}&ji={ji}&startDate={startDate}&endDate={endDate}&numOfRows=99999"
        print(url)
        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")
            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "archArea",
                "atchBldArea",
                "atchBldCnt",
                "bcRat",
                "bjdongCd",
                "bldNm",
                "block",
                "bun",
                "bylotCnt",
                "crtnDay",
                "dongNm",
                "emgenUseElvtCnt",
                "engrEpi",
                "engrGrade",
                "engrRat",
                "etcPurps",
                "etcRoof",
                "etcStrct",
                "fmlyCnt",
                "gnBldCert",
                "gnBldGrade",
                "grndFlrCnt",
                "heit",
                "hhldCnt",
                "hoCnt",
                "indrAutoArea",
                "indrAutoUtcnt",
                "indrMechArea",
                "indrMechUtcnt",
                "itgBldCert",
                "itgBldGrade",
                "ji",
                "lot",
                "mainAtchGbCd",
                "mainAtchGbCdNm",
                "mainPurpsCd",
                "mainPurpsCdNm",
                "mgmBldrgstPk",
                "naBjdongCd",
                "naMainBun",
                "naRoadCd",
                "naSubBun",
                "naUgrndCd",
                "newPlatPlc",
                "oudrAutoArea",
                "oudrAutoUtcnt",
                "oudrMechArea",
                "oudrMechUtcnt",
                "platArea",
                "platGbCd",
                "platPlc",
                "pmsDay",
                "pmsnoGbCd",
                "pmsnoGbCdNm",
                "pmsnoKikCd",
                "pmsnoKikCdNm",
                "pmsnoYear",
                "regstrGbCd",
                "regstrGbCdNm",
                "regstrKindCd",
                "regstrKindCdNm",
                "rideUseElvtCnt",
                "rnum",
                "roofCd",
                "roofCdNm",
                "rserthqkAblty",
                "rserthqkDsgnApplyYn",
                "sigunguCd",
                "splotNm",
                "stcnsDay",
                "strctCd",
                "strctCdNm",
                "totArea",
                "totDongTotArea",
                "ugrndFlrCnt",
                "useAprDay",
                "vlRat",
                "vlRatEstmTotArea",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            archArea,
                            atchBldArea,
                            atchBldCnt,
                            bcRat,
                            bjdongCd,
                            bldNm,
                            block,
                            bun,
                            bylotCnt,
                            crtnDay,
                            dongNm,
                            emgenUseElvtCnt,
                            engrEpi,
                            engrGrade,
                            engrRat,
                            etcPurps,
                            etcRoof,
                            etcStrct,
                            fmlyCnt,
                            gnBldCert,
                            gnBldGrade,
                            grndFlrCnt,
                            heit,
                            hhldCnt,
                            hoCnt,
                            indrAutoArea,
                            indrAutoUtcnt,
                            indrMechArea,
                            indrMechUtcnt,
                            itgBldCert,
                            itgBldGrade,
                            ji,
                            lot,
                            mainAtchGbCd,
                            mainAtchGbCdNm,
                            mainPurpsCd,
                            mainPurpsCdNm,
                            mgmBldrgstPk,
                            naBjdongCd,
                            naMainBun,
                            naRoadCd,
                            naSubBun,
                            naUgrndCd,
                            newPlatPlc,
                            oudrAutoArea,
                            oudrAutoUtcnt,
                            oudrMechArea,
                            oudrMechUtcnt,
                            platArea,
                            platGbCd,
                            platPlc,
                            pmsDay,
                            pmsnoGbCd,
                            pmsnoGbCdNm,
                            pmsnoKikCd,
                            pmsnoKikCdNm,
                            pmsnoYear,
                            regstrGbCd,
                            regstrGbCdNm,
                            regstrKindCd,
                            regstrKindCdNm,
                            rideUseElvtCnt,
                            rnum,
                            roofCd,
                            roofCdNm,
                            rserthqkAblty,
                            rserthqkDsgnApplyYn,
                            sigunguCd,
                            splotNm,
                            stcnsDay,
                            strctCd,
                            strctCdNm,
                            totArea,
                            totDongTotArea,
                            ugrndFlrCnt,
                            useAprDay,
                            vlRat,
                            vlRatEstmTotArea,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])
                df.index = range(len(df))

            return df

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

    def getBrFlrOulnInfo(
        self, sigunguCd, bjdongCd, platGbCd="", bun="", ji="", startDate="", endDate=""
    ):
        """
        04 건축물대장 층별개요 조회
        입력: 시군구코드, 법정동코드, 대지구분코드, 번, 지, 검색시작일, 검색종료일
        """
        # URL
        url = f"{self.url_getBrFlrOulnInfo}&sigunguCd={sigunguCd}&bjdongCd={bjdongCd}&platGbCd={platGbCd}&bun={bun}&ji={ji}&startDate={startDate}&endDate={endDate}&numOfRows=99999"
        print(url)
        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")
            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "area",
                "areaExctYn",
                "bjdongCd",
                "bldNm",
                "block",
                "bun",
                "crtnDay",
                "dongNm",
                "etcPurps",
                "etcStrct",
                "flrGbCd",
                "flrGbCdNm",
                "flrNo",
                "flrNoNm",
                "ji",
                "lot",
                "mainAtchGbCd",
                "mainAtchGbCdNm",
                "mainPurpsCd",
                "mainPurpsCdNm",
                "mgmBldrgstPk",
                "naBjdongCd",
                "naMainBun",
                "naRoadCd",
                "naSubBun",
                "naUgrndCd",
                "newPlatPlc",
                "platGbCd",
                "platPlc",
                "rnum",
                "sigunguCd",
                "splotNm",
                "strctCd",
                "strctCdNm",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            area,
                            areaExctYn,
                            bjdongCd,
                            bldNm,
                            block,
                            bun,
                            crtnDay,
                            dongNm,
                            etcPurps,
                            etcStrct,
                            flrGbCd,
                            flrGbCdNm,
                            flrNo,
                            flrNoNm,
                            ji,
                            lot,
                            mainAtchGbCd,
                            mainAtchGbCdNm,
                            mainPurpsCd,
                            mainPurpsCdNm,
                            mgmBldrgstPk,
                            naBjdongCd,
                            naMainBun,
                            naRoadCd,
                            naSubBun,
                            naUgrndCd,
                            newPlatPlc,
                            platGbCd,
                            platPlc,
                            rnum,
                            sigunguCd,
                            splotNm,
                            strctCd,
                            strctCdNm,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])
                df.index = range(len(df))

            return df

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

    def getBrAtchJibunInfo(
        self, sigunguCd, bjdongCd, platGbCd="", bun="", ji="", startDate="", endDate=""
    ):
        """
        05 건축물대장 부속지번 조회: getBrAtchJibunInfo
        입력: 시군구코드, 법정동코드, 대지구분코드, 번, 지, 검색시작일, 검색종료일
        """
        # URL
        url = f"{self.url_getBrAtchJibunInfo}&sigunguCd={sigunguCd}&bjdongCd={bjdongCd}&platGbCd={platGbCd}&bun={bun}&ji={ji}&startDate={startDate}&endDate={endDate}&numOfRows=99999"
        print(url)
        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")
            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "atchBjdongCd",
                "atchBlock",
                "atchBun",
                "atchEtcJibunNm",
                "atchJi",
                "atchLot",
                "atchPlatGbCd",
                "atchRegstrGbCd",
                "atchRegstrGbCdNm",
                "atchSigunguCd",
                "atchSplotNm",
                "bjdongCd",
                "bldNm",
                "block",
                "bun",
                "crtnDay",
                "ji",
                "lot",
                "mgmBldrgstPk",
                "naBjdongCd",
                "naMainBun",
                "naRoadCd",
                "naSubBun",
                "naUgrndCd",
                "newPlatPlc",
                "platGbCd",
                "platPlc",
                "regstrGbCd",
                "regstrGbCdNm",
                "regstrKindCd",
                "regstrKindCdNm",
                "rnum",
                "sigunguCd",
                "splotNm",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            atchBjdongCd,
                            atchBlock,
                            atchBun,
                            atchEtcJibunNm,
                            atchJi,
                            atchLot,
                            atchPlatGbCd,
                            atchRegstrGbCd,
                            atchRegstrGbCdNm,
                            atchSigunguCd,
                            atchSplotNm,
                            bjdongCd,
                            bldNm,
                            block,
                            bun,
                            crtnDay,
                            ji,
                            lot,
                            mgmBldrgstPk,
                            naBjdongCd,
                            naMainBun,
                            naRoadCd,
                            naSubBun,
                            naUgrndCd,
                            newPlatPlc,
                            platGbCd,
                            platPlc,
                            regstrGbCd,
                            regstrGbCdNm,
                            regstrKindCd,
                            regstrKindCdNm,
                            rnum,
                            sigunguCd,
                            splotNm,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])
                df.index = range(len(df))

            return df

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

    def getBrExposPubuseAreaInfo(
        self,
        sigunguCd,
        bjdongCd,
        platGbCd="",
        bun="",
        ji="",
        startDate="",
        endDate="",
        dongNm="",
        hoNm="",
    ):
        """
        06 건축물대장 전유공용면적 조회: getBrExposPubuseAreaInfo
        입력: 시군구코드, 법정동코드, 대지구분코드, 번, 지, 검색시작일, 검색종료일, 동명칭, 호명칭
        """
        # URL
        url = f"{self.url_getBrExposPubuseAreaInfo}&sigunguCd={sigunguCd}&bjdongCd={bjdongCd}&platGbCd={platGbCd}&bun={bun}&ji={ji}&startDate={startDate}&endDate={endDate}&dongNm={dongNm}&hoNm={hoNm}&numOfRows=99999"
        print(url)
        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")
            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "area",
                "bjdongCd",
                "bldNm",
                "block",
                "bun",
                "crtnDay",
                "dongNm",
                "etcPurps",
                "etcStrct",
                "exposPubuseGbCd",
                "exposPubuseGbCdNm",
                "flrGbCd",
                "flrGbCdNm",
                "flrNo",
                "flrNoNm",
                "hoNm",
                "ji",
                "lot",
                "mainAtchGbCd",
                "mainAtchGbCdNm",
                "mainPurpsCd",
                "mainPurpsCdNm",
                "mgmBldrgstPk",
                "naBjdongCd",
                "naMainBun",
                "naRoadCd",
                "naSubBun",
                "naUgrndCd",
                "newPlatPlc",
                "platGbCd",
                "platPlc",
                "regstrGbCd",
                "regstrGbCdNm",
                "regstrKindCd",
                "regstrKindCdNm",
                "rnum",
                "sigunguCd",
                "splotNm",
                "strctCd",
                "strctCdNm",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            area,
                            bjdongCd,
                            bldNm,
                            block,
                            bun,
                            crtnDay,
                            dongNm,
                            etcPurps,
                            etcStrct,
                            exposPubuseGbCd,
                            exposPubuseGbCdNm,
                            flrGbCd,
                            flrGbCdNm,
                            flrNo,
                            flrNoNm,
                            hoNm,
                            ji,
                            lot,
                            mainAtchGbCd,
                            mainAtchGbCdNm,
                            mainPurpsCd,
                            mainPurpsCdNm,
                            mgmBldrgstPk,
                            naBjdongCd,
                            naMainBun,
                            naRoadCd,
                            naSubBun,
                            naUgrndCd,
                            newPlatPlc,
                            platGbCd,
                            platPlc,
                            regstrGbCd,
                            regstrGbCdNm,
                            regstrKindCd,
                            regstrKindCdNm,
                            rnum,
                            sigunguCd,
                            splotNm,
                            strctCd,
                            strctCdNm,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])
                df.index = range(len(df))

            return df

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

    def getBrWclfInfo(
        self, sigunguCd, bjdongCd, platGbCd="", bun="", ji="", startDate="", endDate=""
    ):
        """
        07 건축물대장 오수정화시설 조회: getBrWclfInfo
        입력: 시군구코드, 법정동코드, 대지구분코드, 번, 지, 검색시작일, 검색종료일
        """
        # URL
        url = f"{self.url_getBrWclfInfo}&sigunguCd={sigunguCd}&bjdongCd={bjdongCd}&platGbCd={platGbCd}&bun={bun}&ji={ji}&startDate={startDate}&endDate={endDate}&numOfRows=99999"
        print(url)
        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")
            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "bjdongCd",
                "bldNm",
                "block",
                "bun",
                "capaLube",
                "capaPsper",
                "crtnDay",
                "etcMode",
                "ji",
                "lot",
                "mgmBldrgstPk",
                "modeCd",
                "modeCdNm",
                "naBjdongCd",
                "naMainBun",
                "naRoadCd",
                "naSubBun",
                "naUgrndCd",
                "newPlatPlc",
                "platGbCd",
                "platPlc",
                "regstrGbCd",
                "regstrGbCdNm",
                "regstrKindCd",
                "regstrKindCdNm",
                "rnum",
                "sigunguCd",
                "splotNm",
                "unitGbCd",
                "unitGbCdNm",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            bjdongCd,
                            bldNm,
                            block,
                            bun,
                            capaLube,
                            capaPsper,
                            crtnDay,
                            etcMode,
                            ji,
                            lot,
                            mgmBldrgstPk,
                            modeCd,
                            modeCdNm,
                            naBjdongCd,
                            naMainBun,
                            naRoadCd,
                            naSubBun,
                            naUgrndCd,
                            newPlatPlc,
                            platGbCd,
                            platPlc,
                            regstrGbCd,
                            regstrGbCdNm,
                            regstrKindCd,
                            regstrKindCdNm,
                            rnum,
                            sigunguCd,
                            splotNm,
                            unitGbCd,
                            unitGbCdNm,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])
                df.index = range(len(df))

            return df

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

    def getBrHsprcInfo(
        self, sigunguCd, bjdongCd, platGbCd="", bun="", ji="", startDate="", endDate=""
    ):
        """
        08 건축물대장 주택가격 조회: getBrHsprcInfo
        입력: 시군구코드, 법정동코드, 대지구분코드, 번, 지, 검색시작일, 검색종료일
        """
        # URL
        url = f"{self.url_getBrHsprcInfo}&sigunguCd={sigunguCd}&bjdongCd={bjdongCd}&platGbCd={platGbCd}&bun={bun}&ji={ji}&startDate={startDate}&endDate={endDate}&numOfRows=99999"
        print(url)
        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")
            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "bjdongCd",
                "bldNm",
                "block",
                "bun",
                "bylotCnt",
                "crtnDay",
                "hsprc",
                "ji",
                "lot",
                "mgmBldrgstPk",
                "naBjdongCd",
                "naMainBun",
                "naRoadCd",
                "naSubBun",
                "naUgrndCd",
                "newPlatPlc",
                "platGbCd",
                "platPlc",
                "regstrGbCd",
                "regstrGbCdNm",
                "regstrKindCd",
                "regstrKindCdNm",
                "rnum",
                "sigunguCd",
                "splotNm",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            bjdongCd,
                            bldNm,
                            block,
                            bun,
                            bylotCnt,
                            crtnDay,
                            hsprc,
                            ji,
                            lot,
                            mgmBldrgstPk,
                            naBjdongCd,
                            naMainBun,
                            naRoadCd,
                            naSubBun,
                            naUgrndCd,
                            newPlatPlc,
                            platGbCd,
                            platPlc,
                            regstrGbCd,
                            regstrGbCdNm,
                            regstrKindCd,
                            regstrKindCdNm,
                            rnum,
                            sigunguCd,
                            splotNm,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])
                df.index = range(len(df))

            return df

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

    def getBrExposInfo(
        self, sigunguCd, bjdongCd, platGbCd="", bun="", ji="", startDate="", endDate=""
    ):
        """
        09 건축물대장 전유부 조회: getBrExposInfo
        입력: 시군구코드, 법정동코드, 대지구분코드, 번, 지, 검색시작일, 검색종료일
        """
        # URL
        url = f"{self.url_getBrExposInfo}&sigunguCd={sigunguCd}&bjdongCd={bjdongCd}&platGbCd={platGbCd}&bun={bun}&ji={ji}&startDate={startDate}&endDate={endDate}&numOfRows=99999"
        print(url)
        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")
            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "bjdongCd",
                "bldNm",
                "block",
                "bun",
                "crtnDay",
                "dongNm",
                "flrGbCd",
                "flrGbCdNm",
                "flrNo",
                "hoNm",
                "ji",
                "lot",
                "mgmBldrgstPk",
                "naBjdongCd",
                "naMainBun",
                "naRoadCd",
                "naSubBun",
                "naUgrndCd",
                "newPlatPlc",
                "platGbCd",
                "platPlc",
                "regstrGbCd",
                "regstrGbCdNm",
                "regstrKindCd",
                "regstrKindCdNm",
                "rnum",
                "sigunguCd",
                "splotNm",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            bjdongCd,
                            bldNm,
                            block,
                            bun,
                            crtnDay,
                            dongNm,
                            flrGbCd,
                            flrGbCdNm,
                            flrNo,
                            hoNm,
                            ji,
                            lot,
                            mgmBldrgstPk,
                            naBjdongCd,
                            naMainBun,
                            naRoadCd,
                            naSubBun,
                            naUgrndCd,
                            newPlatPlc,
                            platGbCd,
                            platPlc,
                            regstrGbCd,
                            regstrGbCdNm,
                            regstrKindCd,
                            regstrKindCdNm,
                            rnum,
                            sigunguCd,
                            splotNm,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])
                df.index = range(len(df))

            return df

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

    def getBrJijiguInfo(
        self, sigunguCd, bjdongCd, platGbCd="", bun="", ji="", startDate="", endDate=""
    ):
        """
        10 건축물대장 지역지구구역 조회: getBrJijiguInfo
        입력: 시군구코드, 법정동코드, 대지구분코드, 번, 지, 검색시작일, 검색종료일
        """
        # URL
        url = f"{self.url_getBrJijiguInfo}&sigunguCd={sigunguCd}&bjdongCd={bjdongCd}&platGbCd={platGbCd}&bun={bun}&ji={ji}&startDate={startDate}&endDate={endDate}&numOfRows=99999"
        print(url)
        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")
            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "bjdongCd",
                "block",
                "bun",
                "crtnDay",
                "etcJijigu",
                "ji",
                "jijiguCd",
                "jijiguCdNm",
                "jijiguGbCd",
                "jijiguGbCdNm",
                "lot",
                "mgmBldrgstPk",
                "newPlatPlc",
                "platGbCd",
                "platPlc",
                "reprYn",
                "rnum",
                "sigunguCd",
                "splotNm",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            bjdongCd,
                            block,
                            bun,
                            crtnDay,
                            etcJijigu,
                            ji,
                            jijiguCd,
                            jijiguCdNm,
                            jijiguGbCd,
                            jijiguGbCdNm,
                            lot,
                            mgmBldrgstPk,
                            newPlatPlc,
                            platGbCd,
                            platPlc,
                            reprYn,
                            rnum,
                            sigunguCd,
                            splotNm,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])
                df.index = range(len(df))

            return df

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

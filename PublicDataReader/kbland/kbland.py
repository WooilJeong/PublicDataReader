"""
KB부동산 데이터 API
"""
import requests
import pandas as pd

requests.packages.urllib3.disable_warnings()


class Kbland:

    def __init__(self):

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
        }

        self.월간주간구분코드 = {
            "01": "월간",
            "02": "주간",
        }
        self.매물종별구분 = {
            "01": "아파트",
            "08": "연립",
            "09": "단독",
            "98": "주택종합",
        }
        self.매매전세코드 = {
            "01": "매매",
            "02": "전세",
        }
        self.메뉴코드 = {
            "01": "매수우위지수",
            "02": "매매거래활발지수",
            "03": "전세수급지수",
            "04": "전세거래활발지수",
            "05": "매매가격전망지수",
            "06": "전세가격전망지수",
        }
        self.메뉴코드별컬럼목록 = {
            "01": ['매수자많음', '비슷함', '매도자많음', '매수우위지수'],
            "02": ['활발함', '보통', '한산함', '매매거래지수'],
            "03": ['공급충분', '공급적절', '공급부족', '전세수급지수'],
            "04": ['활발함', '보통', '한산함', '전세거래지수'],
            "05": ['상승', '약상승', '보통', '약하락', '하락', '매매상승하락전망지수'],
            "06": ['상승', '약상승', '보통', '약하락', '하락', '전세상승하락전망지수'],
        }
        self.면적별코드 = {
            "01": "전용면적별(구)",
            "02": "전용면적별",
        }
        self.평균가격메뉴코드 = {
            "01": "아파트 평균가격",
            "02": "주택종합 평균가격",
            "03": "아파트 아파트 ㎡당 평균가격",
        }
        self.PIR메뉴코드 = {
            "01": "PIR",
            "02": "J-PIR",
        }

    # ==============================================================================
    # 주택가격동향조사 - 가격지수
    # ==============================================================================

    def get_price_index(self, 월간주간구분코드, 매물종별구분, 매매전세코드, **kwargs):
        """
        KB통계 - 주택가격동향조사 - 가격지수

        Parameters
        ----------
        월간주간구분코드 : str
            월간주간구분코드
            01: 월간
            02: 주간
        매물종별구분 : str
            매물종별구분
            01: 아파트
            08: 연립
            09: 단독
            98: 주택종합
        매매전세코드 : str
            매매전세코드
            01: 매매
            02: 전세
        **kwargs : dict
            그 외 필요한 파라미터
            지역코드 : str
        """
        url = "https://data-api.kbland.kr/bfmstat/weekMnthlyHuseTrnd/priceIndex"

        # 매물종별구분이 '01'이 아니면 월간주간구분코드는 '01'
        if 매물종별구분 != "01":
            월간주간구분코드 = "01"
        params = {
            "월간주간구분코드": 월간주간구분코드,
            "매물종별구분": 매물종별구분,
            "매매전세코드": 매매전세코드,
        }
        params.update(kwargs)
        try:
            res = requests.get(url, params=params, verify=False)
            data = res.json()['dataBody']['data']
        except Exception as e:
            print(e)
            return
        result_code = res.json()['dataBody']['resultCode']
        if str(result_code) != "11000":
            print(data['message'])
            return
        n_data_list = len(data['데이터리스트'][0]['dataList'])
        n_date_list = len(data['날짜리스트'])
        n_date_str = len(data['날짜리스트'][0])
        columns = data['날짜리스트']
        df = pd.DataFrame(data['데이터리스트'])
        values = pd.DataFrame(
            df['dataList'].values.tolist()).iloc[:, :n_date_list]
        values.columns = columns
        df = pd.concat([df[['지역코드', '지역명']], values], axis=1)
        df2 = pd.melt(df, id_vars=['지역코드', '지역명']).rename(
            columns={'variable': '날짜', 'value': '가격지수'})
        if n_date_str == 6:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m')
        elif n_date_str == 8:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m%d')
        df2 = df2.sort_values(['지역코드', '날짜'], ascending=[
                              True, True]).reset_index(drop=True)
        # 코드 정보 부여
        code_df = pd.DataFrame({
            "월간주간구분": [self.월간주간구분코드[월간주간구분코드]],
            "매물종별구분": [self.매물종별구분[매물종별구분]],
            "거래구분": [self.매매전세코드[매매전세코드]],
        })
        code_df = pd.concat([code_df] * len(df2), ignore_index=True)
        df2 = pd.concat([code_df, df2], axis=1)
        return df2

    def get_monthly_apartment_wolse_index(self, **kwargs):
        """
        KB통계 - 주택가격동향조사 - 월간 아파트 월세가격지수

        Parameters
        ----------
        **kwargs : dict
            선택 파라미터
        """
        url = "https://data-api.kbland.kr/bfmstat/weekMnthlyHuseTrnd/mntlyAptMrpayPrcIndx"
        params = {}
        params.update(kwargs)
        try:
            res = requests.get(url, params=params, verify=False)
            data = res.json()['dataBody']['data']
        except Exception as e:
            print(e)
            return
        result_code = res.json()['dataBody']['resultCode']
        if str(result_code) != "11000":
            print(data['message'])
            return
        n_data_list = len(data['데이터리스트'][0]['dataList'])
        n_date_list = len(data['날짜리스트'])
        n_date_str = len(data['날짜리스트'][0])
        columns = data['날짜리스트']
        df = pd.DataFrame(data['데이터리스트'])
        values = pd.DataFrame(
            df['dataList'].values.tolist()).iloc[:, :n_date_list]
        values.columns = columns
        df = pd.concat([df[['지역코드', '지역명']], values], axis=1)
        df2 = pd.melt(df, id_vars=['지역코드', '지역명']).rename(
            columns={'variable': '날짜', 'value': '가격지수'})
        if n_date_str == 6:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m')
        elif n_date_str == 8:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m%d')
        df2 = df2.sort_values(['지역코드', '날짜'], ascending=[
                              True, True]).reset_index(drop=True)
        # 코드 정보 부여
        code_df = pd.DataFrame({
            "월간주간구분": ["월간"],
            "매물종별구분": ["아파트"],
            "거래구분": ["월세"],
        })
        code_df = pd.concat([code_df] * len(df2), ignore_index=True)
        df2 = pd.concat([code_df, df2], axis=1)
        return df2

    def get_lead_apartment_50_index(self, **kwargs):
        """
        KB통계 - 주택가격동향조사 - KB선도아파트 50 지수

        Parameters
        ----------
        **kwargs : dict
            선택 파라미터
        """
        url = "https://data-api.kbland.kr/bfmstat/weekMnthlyHuseTrnd/leadApt50Indx"
        params = {}
        params.update(kwargs)
        try:
            res = requests.get(url, params=params, verify=False)
            data = res.json()['dataBody']['data']
        except Exception as e:
            print(e)
            return
        result_code = res.json()['dataBody']['resultCode']
        if str(result_code) != "11000":
            print(data['message'])
            return
        n_data_list = len(data['선도50지수리스트'])
        n_date_list = len(data['날짜리스트'])
        n_date_str = len(data['날짜리스트'][0])
        columns = data['날짜리스트']

        df = pd.DataFrame({
            "날짜": data['날짜리스트'],
            "선도50지수": data['선도50지수리스트'],
            "전월대비증감률": data['전월대비증감률리스트'],
            "전년동월대비증감률": data['전년동월대비증감률리스트'],
        })

        if n_date_str == 6:
            df['날짜'] = pd.to_datetime(df['날짜'], format='%Y%m')
        elif n_date_str == 8:
            df['날짜'] = pd.to_datetime(df['날짜'], format='%Y%m%d')
        df = df.sort_values(['날짜'], ascending=[True]).reset_index(drop=True)
        return df

    # ==============================================================================
    # 주택가격동향조사 - 가격지수증감률
    # ==============================================================================

    def get_price_index_change_rate(self, 월간주간구분코드, 매물종별구분, 매매전세코드, **kwargs):
        """
        KB통계 - 주택가격동향조사 - 가격지수증감률

        Parameters
        ----------
        월간주간구분코드 : str
            월간주간구분코드
            01: 월간
            02: 주간
        매물종별구분 : str
            매물종별구분
            01: 아파트
            08: 연립
            09: 단독
            98: 주택종합
        매매전세코드 : str
            매매전세코드
            01: 매매
            02: 전세
        **kwargs : dict
            그 외 필요한 파라미터
            지역코드 : str
        """
        url = "https://data-api.kbland.kr/bfmstat/weekMnthlyHuseTrnd/prcIndxInxrdcRt"
        # 매물종별구분이 '01'이 아니면 월간주간구분코드는 '01'
        if 매물종별구분 != "01":
            월간주간구분코드 = "01"
        params = {
            "월간주간구분코드": 월간주간구분코드,
            "매물종별구분": 매물종별구분,
            "매매전세코드": 매매전세코드,
        }
        params.update(kwargs)
        try:
            res = requests.get(url, params=params, verify=False)
            data = res.json()['dataBody']['data']
        except Exception as e:
            print(e)
            return
        result_code = res.json()['dataBody']['resultCode']
        if str(result_code) != "11000":
            print(data['message'])
            return
        n_data_list = len(data['데이터리스트'][0]['dataList'])
        n_date_list = len(data['날짜리스트'])
        n_date_str = len(data['날짜리스트'][0])
        columns = data['날짜리스트']
        df = pd.DataFrame(data['데이터리스트'])
        values = pd.DataFrame(
            df['dataList'].values.tolist()).iloc[:, :n_date_list]
        values.columns = columns
        df = pd.concat([df[['지역코드', '지역명']], values], axis=1)
        df2 = pd.melt(df, id_vars=['지역코드', '지역명']).rename(
            columns={'variable': '날짜', 'value': '가격지수증감률'})
        if n_date_str == 6:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m')
        elif n_date_str == 8:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m%d')
        df2 = df2.sort_values(['지역코드', '날짜'], ascending=[
                              True, True]).reset_index(drop=True)
        # 코드 정보 부여
        code_df = pd.DataFrame({
            "월간주간구분": [self.월간주간구분코드[월간주간구분코드]],
            "매물종별구분": [self.매물종별구분[매물종별구분]],
            "거래구분": [self.매매전세코드[매매전세코드]],
        })
        code_df = pd.concat([code_df] * len(df2), ignore_index=True)
        df2 = pd.concat([code_df, df2], axis=1)
        return df2

    # ==============================================================================
    # 주택가격동향조사 - 전세가격비율
    # ==============================================================================

    def get_jeonse_price_ratio(self, 매물종별구분, **kwargs):
        """
        KB통계 - 주택가격동향조사 - 전세가격비율

        Parameters
        ----------
        매물종별구분 : str
            매물종별구분
            01: 아파트
            08: 연립
            09: 단독
            98: 주택종합
        **kwargs : dict
            그 외 필요한 파라미터
            지역코드 : str
        """
        url = "https://data-api.kbland.kr/bfmstat/weekMnthlyHuseTrnd/dealCntstTnantRato"
        params = {
            "매물종별구분": 매물종별구분,
        }
        params.update(kwargs)
        try:
            res = requests.get(url, params=params, verify=False)
            data = res.json()['dataBody']['data']
        except Exception as e:
            print(e)
            return
        result_code = res.json()['dataBody']['resultCode']
        if str(result_code) != "11000":
            print(data['message'])
            return
        n_data_list = len(data['데이터리스트'][0]['dataList'])
        n_date_list = len(data['날짜리스트'])
        n_date_str = len(data['날짜리스트'][0])
        columns = data['날짜리스트']
        df = pd.DataFrame(data['데이터리스트'])
        values = pd.DataFrame(
            df['dataList'].values.tolist()).iloc[:, :n_date_list]
        values.columns = columns
        df = pd.concat([df[['지역코드', '지역명']], values], axis=1)
        df2 = pd.melt(df, id_vars=['지역코드', '지역명']).rename(
            columns={'variable': '날짜', 'value': '전세가격비율'})
        if n_date_str == 6:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m')
        elif n_date_str == 8:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m%d')
        df2 = df2.sort_values(['지역코드', '날짜'], ascending=[
                              True, True]).reset_index(drop=True)
        # 코드 정보 부여
        code_df = pd.DataFrame({
            "매물종별구분": [self.매물종별구분[매물종별구분]],
        })
        code_df = pd.concat([code_df] * len(df2), ignore_index=True)
        df2 = pd.concat([code_df, df2], axis=1)
        return df2

    def get_jeonwolse_conversion_rate(self, **kwargs):
        """
        KB통계 - 주택가격동향조사 - 전월세전환율

        Parameters
        ----------
        **kwargs : dict
            선택 파라미터
        """
        url = "https://data-api.kbland.kr/bfmstat/weekMnthlyHuseTrnd/jnmnrnCnvsnRt"
        params = {}
        params.update(kwargs)
        try:
            res = requests.get(url, params=params, verify=False)
            data = res.json()['dataBody']['data']
        except Exception as e:
            print(e)
            return
        result_code = res.json()['dataBody']['resultCode']
        if str(result_code) != "11000":
            print(data['message'])
            return
        n_data_list = len(data['데이터리스트'][0]['dataList'])
        n_date_list = len(data['날짜리스트'])
        n_date_str = len(data['날짜리스트'][0])
        columns = data['날짜리스트']
        df = pd.DataFrame(data['데이터리스트'])
        values = pd.DataFrame(
            df['dataList'].values.tolist()).iloc[:, :n_date_list]
        values.columns = columns
        df = pd.concat([df[['지역코드', '지역명']], values], axis=1)
        df2 = pd.melt(df, id_vars=['지역코드', '지역명']).rename(
            columns={'variable': '날짜', 'value': '전월세전환율'})
        if n_date_str == 6:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m')
        elif n_date_str == 8:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m%d')
        df2 = df2.sort_values(['지역코드', '날짜'], ascending=[
                              True, True]).reset_index(drop=True)
        return df2

    # ==============================================================================
    # 주택가격동향조사 - 시장동향/설문조사
    # ==============================================================================

    def get_market_trend(self, 메뉴코드, 월간주간구분코드, **kwargs):
        """
        KB통계 - 주택가격동향조사 - 시장동향/설문조사

        Parameters
        ----------
        메뉴코드 : str
            메뉴코드
            01: 매수우위지수
            02: 매매거래활발지수
            03: 전세수급지수
            04: 전세거래활발지수
            05: 매매가격전망지수
            06: 전세가격전망지수
        월간주간구분코드 : str
            월간주간구분코드
            01: 월간
            02: 주간
        **kwargs : dict
            그 외 선택 파라미터
            기간: str
        """
        url = "https://data-api.kbland.kr/bfmstat/weekMnthlyHuseTrnd/maktTrnd"
        # 메뉴코드가 05 혹은 06 이면 월간주간구분코드를 01로 변경
        if 메뉴코드 in ['05', '06']:
            월간주간구분코드 = '01'
        params = {
            "메뉴코드": 메뉴코드,
            "월간주간구분코드": 월간주간구분코드,
        }
        params.update(kwargs)
        try:
            res = requests.get(url, params=params, verify=False)
            data = res.json()['dataBody']['data']
        except Exception as e:
            print(e)
            return
        result_code = res.json()['dataBody']['resultCode']
        if str(result_code) != "11000":
            print(data['message'])
            return
        n_data_list = len(data['데이터리스트'][0]['dataList'])
        n_date_list = len(data['날짜리스트'])
        n_date_str = len(data['날짜리스트'][0])
        columns = data['날짜리스트']
        df = pd.DataFrame(data['데이터리스트'])
        values = pd.DataFrame(
            df['dataList'].values.tolist()).iloc[:, :n_date_list]
        values.columns = columns
        df = pd.concat([df[['지역코드', '지역명']], values], axis=1)
        df2 = pd.melt(df, id_vars=['지역코드', '지역명']).rename(
            columns={'variable': '날짜', 'value': '값'})
        if n_date_str == 6:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m')
        elif n_date_str == 8:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m%d')
        df2 = df2.sort_values(['지역코드', '날짜'], ascending=[
                              True, True]).reset_index(drop=True)
        # Flatten Nested Column
        tmp = df2['값'].apply(pd.Series)[self.메뉴코드별컬럼목록[메뉴코드]]
        df3 = pd.concat([df2.drop('값', axis=1), tmp], axis=1)
        # 코드 정보 부여
        code_df = pd.DataFrame({
            "메뉴코드": [self.메뉴코드[메뉴코드]],
            "월간주간구분": [self.월간주간구분코드[월간주간구분코드]],
        })
        code_df = pd.concat([code_df] * len(df3), ignore_index=True)
        df3 = pd.concat([code_df, df3], axis=1)
        return df3

    # ==============================================================================
    # 주택가격동향조사 - 면적별 가격지수
    # ==============================================================================

    def get_price_index_by_area(self, 월간주간구분코드, 매물종별구분, 면적별코드, 매매전세코드, **kwargs):
        """
        주택가격동향조사 - 면적별 가격지수

        Parameters
        ----------
        월간주간구분코드 : str
            월간주간구분코드
            01: 월간
            02: 주간
        매물종별구분 : str
            매물종별구분
            01: 아파트
            08: 연립
            09: 단독
            98: 주택종합
        면적별코드: str
            면적별코드
            01: 전용면적별(구)
            02: 전용면적별
        매매전세코드 : str
            매매전세코드
            01: 매매
            02: 전세
        **kwargs : dict
            그 외 필요한 파라미터
            기간 : str
        """
        url = "https://data-api.kbland.kr/bfmstat/weekMnthlyHuseTrnd/prcIndxPerSqrmsr"
        # 매물종별구분이 '01'이 아니면 면적별코드를 '02'로 고정하고 월간주간구분코드를 '01'로 고정
        if 매물종별구분 != '01':
            면적별코드 = '02'
            월간주간구분코드 = '01'
        params = {
            "메뉴코드": "2",
            "월간주간구분코드": 월간주간구분코드,
            "매물종별구분": 매물종별구분,
            "면적별코드": 면적별코드,
            "매매전세코드": 매매전세코드,
        }
        params.update(kwargs)
        try:
            res = requests.get(url, params=params, verify=False)
            data = res.json()['dataBody']['data']
        except Exception as e:
            print(e)
            return
        result_code = res.json()['dataBody']['resultCode']
        if str(result_code) != "11000":
            print(data['message'])
            return
        n_date_list = len(data['날짜리스트'])
        n_date_str = len(data['날짜리스트'][0])
        columns = data['날짜리스트']
        df = pd.DataFrame(data['데이터리스트'])
        tmp = df['dataList'].apply(pd.Series)
        df2 = pd.concat([df.drop(['dataList'], axis=1), tmp], axis=1)
        df3 = pd.melt(df2, id_vars=['지역코드', '지역명'])
        tmp = df3['value'].apply(pd.Series)
        df4 = pd.concat([df3.drop(['variable', 'value'], axis=1), tmp], axis=1)
        tmp = df4['데이터리스트'].apply(pd.Series).iloc[:, :n_date_list]
        tmp.columns = columns
        df5 = pd.concat([df4.drop(['데이터리스트'], axis=1), tmp], axis=1)
        tot = pd.melt(df5, id_vars=['지역코드', '지역명', '면적크기', '면적크기코드']).rename(
            columns={'variable': '날짜', 'value': '가격지수'})
        if n_date_str == 6:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m')
        elif n_date_str == 8:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m%d')
        # 피벗 테이블 생성
        pv = tot.pivot(index=['지역코드', '지역명', '날짜'], columns=['면적크기코드', '면적크기'], values=[
                       '가격지수']).droplevel([0, 1], axis=1).reset_index()
        pv.columns.name = None
        # 코드 정보 부여
        code_df = pd.DataFrame({
            "월간주간구분": [self.월간주간구분코드[월간주간구분코드]],
            "매물종별구분": [self.매물종별구분[매물종별구분]],
            "면적별코드": [self.면적별코드[면적별코드]],
            "매매전세코드": [self.매매전세코드[매매전세코드]],
        })
        code_df = pd.concat([code_df] * len(pv), ignore_index=True)
        pv = pd.concat([code_df, pv], axis=1)
        return pv

    # ==============================================================================
    # 주택가격동향조사 - 평균가격
    # ==============================================================================

    def get_average_price(self, 매물종별구분, 매매전세코드, **kwargs):
        """
        주택가격동향조사 - 평균가격

        Parameters
        ----------
        매물종별구분 : str
            매물종별구분
            01: 아파트
            08: 연립
            09: 단독
            98: 주택종합
        매매전세코드 : str
            매매전세코드
            01: 매매
            02: 전세
        """
        url = "https://data-api.kbland.kr/bfmstat/weekMnthlyHuseTrnd/avgPrc"

        params = {
            "매물종별구분": 매물종별구분,
            "매매전세코드": 매매전세코드,
        }
        params.update(kwargs)
        try:
            res = requests.get(url, params=params, verify=False)
            data = res.json()['dataBody']['data']
        except Exception as e:
            print(e)
            return
        result_code = res.json()['dataBody']['resultCode']
        if str(result_code) != "11000":
            print(data['message'])
            return

        n_date_list = len(data['날짜리스트'])
        n_date_str = len(data['날짜리스트'][0])
        columns = data['날짜리스트']

        df = pd.DataFrame(data['데이터리스트'])
        tmp = df['dataList'].apply(pd.Series)
        tmp.columns = columns
        df2 = pd.concat([df.drop(['dataList'], axis=1), tmp], axis=1)
        tot = pd.melt(df2, id_vars=['지역코드', '지역명']).rename(
            columns={'variable': '날짜', 'value': '평균가격'})
        if n_date_str == 6:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m')
        elif n_date_str == 8:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m%d')
        # 코드 정보 부여
        code_df = pd.DataFrame({
            "매물종별구분": [self.매물종별구분[매물종별구분]],
            "매매전세코드": [self.매매전세코드[매매전세코드]],
        })
        code_df = pd.concat([code_df] * len(tot), ignore_index=True)
        tot = pd.concat([code_df, tot], axis=1)
        return tot

    # ==============================================================================
    # 주택가격동향조사 - ㎡당 평균가격
    # ==============================================================================

    def get_average_price_per_squaremeter(self, 매물종별구분, 매매전세코드, **kwargs):
        """
        주택가격동향조사 - ㎡당 평균가격

        Parameters
        ----------
        매물종별구분 : str
            매물종별구분
            01: 아파트
            08: 연립
            09: 단독
            98: 주택종합
        매매전세코드 : str
            매매전세코드
            01: 매매
            02: 전세
        """
        url = "https://data-api.kbland.kr/bfmstat/weekMnthlyHuseTrnd/avgPrcPerSqmt"

        params = {
            "매물종별구분": 매물종별구분,
            "매매전세코드": 매매전세코드,
        }
        params.update(kwargs)
        try:
            res = requests.get(url, params=params, verify=False)
            data = res.json()['dataBody']['data']
        except Exception as e:
            print(e)
            return
        result_code = res.json()['dataBody']['resultCode']
        if str(result_code) != "11000":
            print(data['message'])
            return

        n_date_list = len(data['날짜리스트'])
        n_date_str = len(data['날짜리스트'][0])
        columns = data['날짜리스트']

        df = pd.DataFrame(data['데이터리스트'])[['지역코드', '지역명', 'dataList']]
        tmp = df['dataList'].apply(pd.Series)
        tmp.columns = columns
        df2 = pd.concat([df.drop(['dataList'], axis=1), tmp], axis=1)
        tot = pd.melt(df2, id_vars=['지역코드', '지역명']).rename(
            columns={'variable': '날짜', 'value': '㎡당 평균가격'})
        if n_date_str == 6:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m')
        elif n_date_str == 8:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m%d')
        # 코드 정보 부여
        code_df = pd.DataFrame({
            "매물종별구분": [self.매물종별구분[매물종별구분]],
            "매매전세코드": [self.매매전세코드[매매전세코드]],
        })
        code_df = pd.concat([code_df] * len(tot), ignore_index=True)
        tot = pd.concat([code_df, tot], axis=1)
        return tot

    # ==============================================================================
    # 주택가격동향조사 - 5분위 평균가격
    # ==============================================================================

    def get_average_price_by_quintile(self, 메뉴코드, 매매전세코드, **kwargs):
        """
        주택가격동향조사 - 5분위 평균가격

        Parameters
        ----------
        메뉴코드: str
            메뉴코드
            01: 아파트 평균가격
            02: 주택종합 평균가격
            08: 아파트 ㎡당 평균가격

        매매전세코드 : str
            매매전세코드
            01: 매매
            02: 전세
        """
        url = "https://data-api.kbland.kr/bfmstat/weekMnthlyHuseTrnd/avgPrcPerPorela"

        params = {
            "메뉴코드": 메뉴코드,
            "매매전세코드": 매매전세코드,
        }
        params.update(kwargs)
        try:
            res = requests.get(url, params=params, verify=False)
            data = res.json()['dataBody']['data']
        except Exception as e:
            print(e)
            return
        result_code = res.json()['dataBody']['resultCode']
        if str(result_code) != "11000":
            print(data['message'])
            return
        df = pd.DataFrame(data['데이터리스트'])
        tmp = df['dataList'].apply(pd.Series)
        df2 = pd.concat([df.drop(['dataList'], axis=1), tmp], axis=1)
        df3 = pd.melt(df2, id_vars=['지역코드', '지역명'])
        tmp = df3['value'].apply(pd.Series)
        df4 = pd.concat([df3.drop(['variable', 'value'], axis=1), tmp], axis=1)[
            ['지역코드', '지역명', '기준날짜', '5분위', '4분위', '3분위', '2분위', '1분위', '5분위배율']]
        df4['기준날짜'] = pd.to_datetime(df4['기준날짜'], format="%Y%m")
        df4 = df4.rename(columns={"기준날짜": "날짜"})
        # 코드 정보 부여
        code_df = pd.DataFrame({
            "구분": [self.평균가격메뉴코드[메뉴코드]],
            "매매전세코드": [self.매매전세코드[매매전세코드]],
        })
        code_df = pd.concat([code_df] * len(df4), ignore_index=True)
        df4 = pd.concat([code_df, df4], axis=1)
        return df4

    # ==============================================================================
    # 주택가격동향조사 - 면적별 평균가격
    # ==============================================================================

    def get_average_price_by_area(self, 매매전세코드, 면적별코드, **kwargs):
        """
        주택가격동향조사 - 면적별 평균가격

        Parameters
        ----------
        매매전세코드 : str
            매매전세코드
            01: 매매
            02: 전세
        면적별코드: str
            면적별코드
            01: 전용면적별(구)
            02: 전용면적별
        """
        url = "https://data-api.kbland.kr/bfmstat/weekMnthlyHuseTrnd/avgPrcPerAptSmeu"
        params = {
            "매매전세코드": 매매전세코드,
            "면적별코드": 면적별코드,
        }
        params.update(kwargs)
        try:
            res = requests.get(url, params=params, verify=False)
            data = res.json()['dataBody']['data']
        except Exception as e:
            print(e)
            return
        result_code = res.json()['dataBody']['resultCode']
        if str(result_code) != "11000":
            print(data['message'])
            return
        n_date_list = len(data['날짜리스트'])
        n_date_str = len(data['날짜리스트'][0])
        columns = data['날짜리스트']

        df = pd.DataFrame(data['데이터리스트'])
        tmp = df['dataList'].apply(pd.Series)
        df2 = pd.concat([df.drop(['dataList'], axis=1), tmp], axis=1)
        df3 = pd.melt(df2, id_vars=['지역코드', '지역명'])
        tmp = df3['value'].apply(pd.Series)
        df4 = pd.concat([df3.drop(['variable', 'value'], axis=1), tmp], axis=1)
        tmp = df4['데이터리스트'].apply(pd.Series).iloc[:, :n_date_list]
        tmp.columns = columns
        df5 = pd.concat([df4.drop(['데이터리스트'], axis=1), tmp], axis=1)
        tot = pd.melt(df5, id_vars=['지역코드', '지역명', '면적크기', '면적크기코드']).rename(
            columns={'variable': '날짜', 'value': '평균가격'})
        if n_date_str == 6:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m')
        elif n_date_str == 8:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m%d')
        # 피벗 테이블 생성
        pv = tot.pivot(index=['지역코드', '지역명', '날짜'], columns=['면적크기코드', '면적크기'], values=[
                       '평균가격']).droplevel([0, 1], axis=1).reset_index()
        pv.columns.name = None
        # 코드 정보 부여
        code_df = pd.DataFrame({
            "매매전세코드": [self.매매전세코드[매매전세코드]],
            "면적별코드": [self.면적별코드[면적별코드]],
        })
        code_df = pd.concat([code_df] * len(pv), ignore_index=True)
        pv = pd.concat([code_df, pv], axis=1)
        return pv

    # ==============================================================================
    # 주택가격동향조사 - 중위가격
    # ==============================================================================

    def get_median_price(self, 매물종별구분, 매매전세코드, **kwargs):
        """
        주택가격동향조사 - 중위가격

        Parameters
        ----------
        매물종별구분 : str
            매물종별구분
            01: 아파트
            08: 연립
            09: 단독
            98: 주택종합
        매매전세코드 : str
            매매전세코드
            01: 매매
            02: 전세
        """
        url = "https://data-api.kbland.kr/bfmstat/weekMnthlyHuseTrnd/mdpsPrc"

        params = {
            "매물종별구분": 매물종별구분,
            "매매전세코드": 매매전세코드,
        }
        params.update(kwargs)
        try:
            res = requests.get(url, params=params, verify=False)
            data = res.json()['dataBody']['data']
        except Exception as e:
            print(e)
            return
        result_code = res.json()['dataBody']['resultCode']
        if str(result_code) != "11000":
            print(data['message'])
            return

        n_date_list = len(data['날짜리스트'])
        n_date_str = len(data['날짜리스트'][0])
        columns = data['날짜리스트']

        df = pd.DataFrame(data['데이터리스트'])
        tmp = df['dataList'].apply(pd.Series)
        tmp.columns = columns
        df2 = pd.concat([df.drop(['dataList'], axis=1), tmp], axis=1)
        tot = pd.melt(df2, id_vars=['지역코드', '지역명']).rename(
            columns={'variable': '날짜', 'value': '중위가격'})
        if n_date_str == 6:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m')
        elif n_date_str == 8:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m%d')
        # 코드 정보 부여
        code_df = pd.DataFrame({
            "매물종별구분": [self.매물종별구분[매물종별구분]],
            "매매전세코드": [self.매매전세코드[매매전세코드]],
        })
        code_df = pd.concat([code_df] * len(tot), ignore_index=True)
        tot = pd.concat([code_df, tot], axis=1)
        return tot

    # ==============================================================================
    # 주택가격동향조사 - 소득연계
    # ==============================================================================

    def get_pir(self, 메뉴코드, **kwargs):
        """
        주택가격동향조사 - 소득연계 - PIR 및 J-PIR

        Parameters
        ----------
        메뉴코드 : str
            메뉴코드
            01: PIR
            02: J-PIR
        **kwargs : dict
            그 외 필요한 파라미터
            기간 : str
        """
        url = "https://data-api.kbland.kr/bfmstat/weekMnthlyHuseTrnd/pir"

        params = {
            "메뉴코드": 메뉴코드,
        }
        params.update(kwargs)
        try:
            res = requests.get(url, params=params, verify=False)
            data = res.json()['dataBody']['data']
        except Exception as e:
            print(e)
            return
        result_code = res.json()['dataBody']['resultCode']
        if str(result_code) != "11000":
            print(data['message'])
            return
        n_date_list = len(data['날짜리스트'])
        n_date_str = len(data['날짜리스트'][0])
        columns = data['날짜리스트']
        df = pd.DataFrame(data['데이터리스트'])
        tmp = df['주택분위구분'].apply(pd.Series)
        df2 = pd.concat([df.drop('주택분위구분', axis=1), tmp], axis=1)
        df3 = pd.melt(df2, id_vars=['지역코드', '지역명'])
        tmp = df3['value'].apply(pd.Series)
        df4 = pd.concat([df3.drop(['variable', 'value'], axis=1), tmp], axis=1)
        tmp = df4['소득분위구분'].apply(pd.Series)
        df5 = pd.concat([df4.drop('소득분위구분', axis=1), tmp], axis=1)
        df6 = pd.melt(df5, id_vars=['지역코드', '지역명', '주택분위'])
        tmp = df6['value'].apply(pd.Series).iloc[:, :n_date_str]
        df7 = pd.concat([df6.drop(['variable', 'value'], axis=1), tmp], axis=1)
        tmp = df7['dataList'].apply(pd.Series).iloc[:, :n_date_list]
        tmp.columns = columns
        df8 = pd.concat([df7.drop('dataList', axis=1), tmp], axis=1)
        tot = pd.melt(df8, id_vars=['지역코드', '지역명', '주택분위', '소득분위']).rename(
            columns={'variable': '날짜', 'value': 'PIR'})
        if n_date_str == 6:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m')
        elif n_date_str == 8:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m%d')
        # 코드 정보 부여
        code_df = pd.DataFrame({
            "구분": [self.PIR메뉴코드[메뉴코드]],
        })
        code_df = pd.concat([code_df] * len(tot), ignore_index=True)
        tot = pd.concat([code_df, tot], axis=1)
        return tot

    def get_hai(self, **kwargs):
        """
        주택가격동향조사 - 소득연계 - 주택구매력지수

        Parameters
        ----------
        **kwargs : dict
            그 외 필요한 파라미터
            기간 : str
        """
        url = "https://data-api.kbland.kr/bfmstat/weekMnthlyHuseTrnd/HAI"
        params = {}
        params.update(kwargs)
        try:
            res = requests.get(url, params=params, verify=False)
            data = res.json()['dataBody']['data']
        except Exception as e:
            print(e)
            return
        result_code = res.json()['dataBody']['resultCode']
        if str(result_code) != "11000":
            print(data['message'])
            return
        n_date_str = len(data['날짜리스트'][0])
        columns = data['날짜리스트']
        df = pd.DataFrame(data['주택구매력리스트'])
        tmp = df['지역구분리스트'].apply(pd.Series)
        df2 = pd.concat([df.drop('지역구분리스트', axis=1), tmp], axis=1)
        df3 = pd.melt(df2, id_vars=['지역코드', '지역명'])
        tmp = df3['value'].apply(pd.Series)
        df4 = pd.concat([df3.drop(['variable', 'value'], axis=1), tmp], axis=1)
        tmp = df4['매물종별구분리스트'].apply(pd.Series)
        tmp.columns = columns
        df5 = pd.concat([df4.drop('매물종별구분리스트', axis=1), tmp], axis=1)
        tot = pd.melt(df5, id_vars=['지역코드', '지역명', '매물종별구분']).rename(
            columns={'variable': '날짜', 'value': 'HAI'})
        if n_date_str == 6:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m')
        elif n_date_str == 8:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m%d')
        pv = tot.pivot(index=['지역코드', '지역명', '날짜'],
                       columns='매물종별구분', values='HAI').reset_index()
        pv.columns.name = None
        pv = pv[['지역코드', '지역명', '날짜', '종합', '아파트', '단독', '연립']]
        return pv

    def get_median_household_monthly_income(self, **kwargs):
        """
        (비노출) 주택가격동향조사 - 소득연계 - 중위가구월소득금액

        Parameters
        ----------
        **kwargs : dict
            그 외 필요한 파라미터
            기간 : str
        """
        url = "https://data-api.kbland.kr/bfmstat/weekMnthlyHuseTrnd/HAI"
        params = {}
        params.update(kwargs)
        try:
            res = requests.get(url, params=params, verify=False)
            data = res.json()['dataBody']['data']
        except Exception as e:
            print(e)
            return
        result_code = res.json()['dataBody']['resultCode']
        if str(result_code) != "11000":
            print(data['message'])
            return
        df = pd.DataFrame(data['주담보월소득리스트'])
        df['기준날짜'] = pd.to_datetime(df['기준날짜'], format='%Y%m')
        df = df.rename(columns={'기준날짜': '날짜'})
        return df

    def get_kb_housing_purchase_potential_index(self, **kwargs):
        """
        주택가격동향조사 - 소득연계 - KB주택구입잠재력지수

        Parameters
        ----------
        **kwargs : dict
            그 외 필요한 파라미터
            기간 : str
        """
        url = "https://data-api.kbland.kr/bfmstat/weekMnthlyHuseTrnd/kbHusePurcPotenStrthIndx"
        params = {}
        params.update(kwargs)
        try:
            res = requests.get(url, params=params, verify=False)
            data = res.json()['dataBody']['data']
        except Exception as e:
            print(e)
            return
        result_code = res.json()['dataBody']['resultCode']
        if str(result_code) != "11000":
            print(data['message'])
            return
        n_date_str = len(data['날짜리스트'][0])
        columns = data['날짜리스트']
        df = pd.DataFrame(data['데이터리스트'])
        tmp = df['dataList'].apply(pd.Series)
        tmp.columns = columns
        df2 = pd.concat([df.drop('dataList', axis=1), tmp], axis=1)
        df3 = pd.melt(df2, id_vars=['지역코드', '지역명'])
        tmp = df3['value'].apply(pd.Series)
        df4 = pd.concat([df3.drop(['value'], axis=1), tmp],
                        axis=1).rename(columns={"variable": "날짜"})
        if n_date_str == 6:
            df4['날짜'] = pd.to_datetime(df4['날짜'], format='%Y%m')
        elif n_date_str == 8:
            df4['날짜'] = pd.to_datetime(df4['날짜'], format='%Y%m%d')
        return df4

    def get_apartment_mortgage_loan_pir(self, **kwargs):
        """
        주택가격동향조사 - 소득연계 - KB아파트주택담보대출 PIR

        Parameters
        ----------
        **kwargs : dict
            그 외 필요한 파라미터
            기간 : str
        """
        url = "https://data-api.kbland.kr/bfmstat/weekMnthlyHuseTrnd/husScurlnPir"
        params = {}
        params.update(kwargs)
        try:
            res = requests.get(url, params=params, verify=False)
            data = res.json()['dataBody']['data']
        except Exception as e:
            print(e)
            return
        result_code = res.json()['dataBody']['resultCode']
        if str(result_code) != "11000":
            print(data['message'])
            return
        n_date_str = len(data['날짜리스트'][0])
        columns = data['날짜리스트']
        df = pd.DataFrame(data['데이터리스트'])
        tmp = df['dataList'].apply(pd.Series)
        tmp.columns = columns
        df2 = pd.concat([df.drop('dataList', axis=1), tmp], axis=1)
        df3 = pd.melt(df2, id_vars=['지역코드', '지역명'])
        tmp = df3['value'].apply(pd.Series)
        df4 = pd.concat([df3.drop(['value'], axis=1), tmp],
                        axis=1).rename(columns={"variable": "날짜"})
        if n_date_str == 6:
            df4['날짜'] = pd.to_datetime(df4['날짜'], format='%Y%m')
        elif n_date_str == 8:
            df4['날짜'] = pd.to_datetime(df4['날짜'], format='%Y%m%d')
        return df4

    # ==============================================================================
    # 공공통계 - 주택공급
    # ==============================================================================

    def 아파트_분양물량(self, 상세비중구분, 기간구분, 법정동코드, verbose=True, **kwargs):
        """아파트 분양물량 API
        
        params
        ------
        상세비중구분: 0: 총세대수, 1: 유형별 세대수
        기간구분: 0: 월별, 1: 년별, 2: 반기별
        법정동코드: 법정동코드 10자리
        """
        상세비중구분 = str(상세비중구분)
        기간구분 = str(기간구분)
        법정동코드 = str(법정동코드).ljust(10, "0")

        url = "https://api.kbland.kr/land-extra/lots/v1/api/aptSelotCnt"

        params = {
            "기간구분": 기간구분,
            "상세비중구분": 상세비중구분,
            "법정동코드": 법정동코드,
        }
        params.update(kwargs)
        
        try:
            res = requests.get(url, headers=self.headers, params=params, verify=False)
            data = res.json()['dataBody']['data']
            지역명 = data['지역명']
            df = pd.json_normalize(data['차트데이터'])
        except Exception as e:
            print(e)
            return

        try:
            if verbose is True:
                _API = "아파트 분양물량"
                _상세비중구분 = {"0": "총세대수", "1": "유형별 세대수"}
                _기간구분 = {"0": "월별", "1": "년별", "2": "반기별"}
                msg = f"""{_API}({지역명})-{_상세비중구분.get(상세비중구분, "null")}-{_기간구분.get(기간구분, "null")}"""
                print(msg)
        except Exception as e:
            print(e)
            return
        
        try:
            if 상세비중구분 == "1":
                new_column_order = [
                    '일정', '상하반기구분', 
                    '일반.세대수', '일반.비율',
                    '조합.세대수', '조합.비율', 
                    '임대.세대수', '임대.비율', 
                    '기타.세대수', '기타.비율', 
                    '합계.단지개수', '합계.세대수', 
                ]
                df = df.reindex(columns=new_column_order)
        except Exception as e:
            print(e)
            return
        
        try:
            if 상세비중구분 == "0" and 법정동코드 == "0000000000":
                new_column_order = [
                    '일정', '상하반기구분', 
                    '수도권.단지개수',
                    '수도권.세대수',
                    '비수도권.단지개수',
                    '비수도권.세대수',
                    '합계.단지개수',
                    '합계.세대수',
                ]
                df = df.reindex(columns=new_column_order)
        except Exception as e:
            print(e)
            return
        
        try:
            df.insert(0, '지역코드', 법정동코드)
            df.insert(0, '지역명', 지역명)
        except Exception as e:
            print(e)
            return
        
        return df
    
    def 아파트_입주물량(self, 기간구분, 법정동코드, verbose=True, **kwargs):
        """아파트 입주물량 API
        
        params
        ------
        기간구분: 0: 월별, 1: 년별, 2: 반기별
        법정동코드: 법정동코드 10자리
        """
        기간구분 = str(기간구분)
        법정동코드 = str(법정동코드).ljust(10, "0")

        url = "https://api.kbland.kr/land-extra/lots/v1/api/aptMovinCnt"

        params = {
            "기간구분": 기간구분,
            "법정동코드": 법정동코드,
        }
        params.update(kwargs)
        
        try:
            res = requests.get(url, headers=self.headers, params=params, verify=False)
            data = res.json()['dataBody']['data']
            지역명 = data['지역명']
            df = pd.json_normalize(data['차트데이터'])
        except Exception as e:
            print(e)
            return

        try:
            if verbose is True:
                _API = "아파트 입주물량"
                _기간구분 = {"0": "월별", "1": "년별", "2": "반기별"}
                msg = f"""{_API}({지역명})-{_기간구분.get(기간구분, "null")}"""
                print(msg)
        except Exception as e:
            print(e)
            return
        
        try:
            if 법정동코드 == "0000000000":
                new_column_order = [
                    '일정', '상하반기구분', 
                    '수도권.단지개수',
                    '수도권.세대수',
                    '비수도권.단지개수', 
                    '비수도권.세대수', 
                    '합계.단지개수', 
                    '합계.세대수', 
                ]
                df = df.reindex(columns=new_column_order)
        except Exception as e:
            print(e)
            return
        
        try:
            df.insert(0, '지역코드', 법정동코드)
            df.insert(0, '지역명', 지역명)
        except Exception as e:
            print(e)
            return
        
        return df
    
    def 아파트_단지_분양(self, 법정동코드, 임대포함여부, 정렬구분, 정렬순서, 조회시작년월, 조회종료년월, 페이지번호=1, 페이지목록수=100000, verbose=True, **kwargs):
        """아파트 단지 분양 API
        
        params
        ------
        법정동코드: 법정동코드 10자리
        임대포함여부: 0: 제외, 1: 포함
        정렬구분: 1: 청약임박순, 2: 분양일정순, 3: 분양가순, 4: 세대수순
        정렬순서: 0: 오름차순, 1: 내림차순
        조회시작년월: e.g. 202401
        조회종료년월: e.g. 202407
        페이지번호: default: 1
        페이지목록수: default: 100000
        """
        임대포함여부 = str(임대포함여부)
        정렬구분 = str(정렬구분)
        정렬순서 = str(정렬순서)
        조회시작년월 = str(조회시작년월)
        조회종료년월 = str(조회종료년월)
        페이지번호 = str(페이지번호)
        페이지목록수 = str(페이지목록수)
        법정동코드 = str(법정동코드).ljust(10, "0")

        url = "https://api.kbland.kr/land-extra/lots/v1/api/aptSelotInfoList"

        params = {
            "법정동코드": 법정동코드,
            "임대포함여부": 임대포함여부,
            "정렬구분": 정렬구분,
            "정렬순서": 정렬순서,
            "조회시작년월": 조회시작년월,
            "조회종료년월": 조회종료년월,
            "페이지번호": 페이지번호,
            "페이지목록수": 페이지목록수,    
        }
        params.update(kwargs)

        try:
            res = requests.get(url, headers=self.headers, params=params, verify=False)
            data = res.json()['dataBody']['data']
            지역명 = data['지역명']
            건수 = data['total_count']
            df = pd.json_normalize(data['데이터'])
        except Exception as e:
            print(e)
            return

        try:
            if verbose is True:
                _API = "아파트 단지 분양"
                _임대포함여부 = {"0": "임대제외", "1": "임대포함",}
                _정렬구분 = {"1": "청약임박순", "2": "분양일정순", "3": "분양가순", "4": "세대수순"}
                _정렬순서 = {"0": "오름차순", "1": "내림차순",}
                
                msg = f"""{_API}({지역명}:{건수:,}건 중 {len(df):,}건 조회 완료)\n{조회시작년월} ~ {조회종료년월}\n- {_임대포함여부.get(임대포함여부, "null")}\n- {_정렬구분.get(정렬구분, "null")}({_정렬순서.get(정렬순서, "null")})"""
                print(msg)
        except Exception as e:
            print(e)
            return
        
        try:
            new_column_order = [
                '단지명', '주소', '법정동코드', '공급방식', '총세대수', '일반세대수', 
                '최저분양가', '최대분양가', '분양일정시작', '분양일정종료', '입주일정', 
                '분양일정구분명', '분양중', '다음분양일정일자', '분양최근일자', 
                'wgs84중심위도', 'wgs84중심경도', '일련번호', '분양일정정렬순서',
            ]
            df = df.reindex(columns=new_column_order)
        except Exception as e:
            print(e)
            return
        
        try:
            df.insert(0, '지역코드', 법정동코드)
            df.insert(0, '지역명', 지역명)
        except Exception as e:
            print(e)
            return
        
        return df
        
    def 아파트_단지_입주(self, 법정동코드, 임대포함여부, 정렬구분, 정렬순서, 조회시작년월, 조회종료년월, 페이지번호=1, 페이지목록수=100000, verbose=True, **kwargs):
        """아파트 단지 입주 API
        
        params
        ------
        법정동코드: 법정동코드 10자리
        임대포함여부: 0: 제외, 1: 포함
        정렬구분: 1: 입주일순, 2: 세대수순
        정렬순서: 0: 오름차순, 1: 내림차순
        조회시작년월: 202401
        조회종료년월: 202407
        페이지번호: default: 1
        페이지목록수: default: 100000
        """
        임대포함여부 = str(임대포함여부)
        정렬구분 = str(정렬구분)
        정렬순서 = str(정렬순서)
        조회시작년월 = str(조회시작년월)
        조회종료년월 = str(조회종료년월)
        페이지번호 = str(페이지번호)
        페이지목록수 = str(페이지목록수)
        법정동코드 = str(법정동코드).ljust(10, "0")

        url = "https://api.kbland.kr/land-extra/lots/v1/api/aptMovinPlanHscmList"

        params = {
            "법정동코드": 법정동코드,
            "임대포함여부": 임대포함여부,
            "정렬구분": 정렬구분,
            "정렬순서": 정렬순서,
            "조회시작년월": 조회시작년월,
            "조회종료년월": 조회종료년월,
            "페이지번호": 페이지번호,
            "페이지목록수": 페이지목록수,    
        }
        params.update(kwargs)

        try:
            res = requests.get(url, headers=self.headers, params=params, verify=False)
            data = res.json()['dataBody']['data']
            지역명 = data['지역명']
            건수 = data['total_count']
            df = pd.json_normalize(data['데이터'])
        except Exception as e:
            print(e)
            return

        try:
            if verbose is True:
                _API = "아파트 단지 입주"
                _임대포함여부 = {"0": "임대제외", "1": "임대포함",}
                _정렬구분 = {"1": "입주일순", "2": "세대수순",}
                _정렬순서 = {"0": "오름차순", "1": "내림차순",}
                
                msg = f"""{_API}({지역명}:{건수:,}건 중 {len(df):,}건 조회 완료)\n{조회시작년월} ~ {조회종료년월}\n- {_임대포함여부.get(임대포함여부, "null")}\n- {_정렬구분.get(정렬구분, "null")}({_정렬순서.get(정렬순서, "null")})"""
                print(msg)
        except Exception as e:
            print(e)
            return
        
        try:
            new_column_order = [
                '단지명', '주소', '법정동코드', '총세대수', '임대분양여부', '분양단지여부', 
                '입주일정', '전매제한년월일', 'wgs84중심위도', 'wgs84중심경도', '일련번호',
            ]
            df = df.reindex(columns=new_column_order)
        except Exception as e:
            print(e)
            return
        
        try:
            df.insert(0, '지역코드', 법정동코드)
            df.insert(0, '지역명', 지역명)
        except Exception as e:
            print(e)
            return
        
        return df
    
    def 주택공급실적(self, dtailDataSelct, 법정동코드, verbose=True, **kwargs):
        """주택공급실적 API
        
        params
        ------
        dtailDataSelct: 1: 전체, 2: 공급단계별, 3: 주택유형별
        법정동코드: 법정동코드 10자리
        
        optional
        --------
        splyStge: (dtailDataSelct이 2인 경우) 01: 인허가, 02: 착공, 03: 분양, 04: 준공
        husePtm: (dtailDataSelect이 3인 경우) 1: 아파트, 2: 비아파트
        """
        dtailDataSelct = str(dtailDataSelct)
        법정동코드 = str(법정동코드).ljust(10, "0")
        
        url = "https://data-api.kbland.kr/bfmpub/huse/huseSplyArsltInqury"

        params = {
            "dtailDataSelct": dtailDataSelct,
            "법정동코드": 법정동코드,
        }
        params.update(kwargs)

        try:
            res = requests.get(url, headers=self.headers, params=params, verify=False)
            data = res.json()['dataBody']['data']
            df = pd.json_normalize(data)
        except Exception as e:
            print(e)
            return

        try:
            if verbose is True:
                _API = "주택공급실적"
                _dtailDataSelct = {"1": "전체", "2": "공급단계별", "3": "주택유형별",}
                _splyStge = {"01": "인허가", "02": "착공", "03": "분양", "04": "준공",}
                _husePtrn = {"1": "아파트", "2": "비아파트",}
                
                msg = f"""{_API}(지역코드: {법정동코드} 조회 완료)\n- 데이터: {_dtailDataSelct.get(dtailDataSelct)}\n"""
                
                if dtailDataSelct == "2":
                    msg += f"""- 공급단계: {_splyStge.get(kwargs.get("splyStge"))}"""
                elif dtailDataSelct == "3":
                    msg += f"""- 주택유형: {_husePtrn.get(kwargs.get("husePtrn"))}"""
                print(msg)
        except Exception as e:
            print(e)
            return
        
        try:
            new_column_order = [
                "기준년도",
                "공통코드명",
                "공급단계코드",
                "실적",
            ]
            df = df.reindex(columns=new_column_order)
        except Exception as e:
            print(e)
            return
        
        try:
            df.insert(0, '지역코드', 법정동코드)
        except Exception as e:
            print(e)
            return
        
        return df
    
    def 청약통장가입현황(self, scipClsfiDstic, 법정동코드, verbose=True, **kwargs):
        """청약통장가입현황 API
        
        params
        ------
        scipClsfiDstic: 00: 전체, 01: 주택청약종합저축, 03: 청약부금, 04: 청약예금
        법정동코드: 법정동코드 10자리
        """
        scipClsfiDstic = str(scipClsfiDstic)
        법정동코드 = str(법정동코드).ljust(10, "0")
        
        url = "https://data-api.kbland.kr/bfmpub/huse/scipJoinPrstusInqury"

        params = {
            "scipClsfiDstic": scipClsfiDstic,
            "법정동코드": 법정동코드,
        }
        params.update(kwargs)

        try:
            res = requests.get(url, headers=self.headers, params=params, verify=False)
            data = res.json()['dataBody']['data']
            df = pd.json_normalize(data)
        except Exception as e:
            print(e)
            return

        try:
            if verbose is True:
                _API = "청약통장가입현황"
                _scipClsfiDstic = {"00": "전체", "01": "주택청약종합저축", "03": "청약부금", "04": "청약예금",}
                msg = f"""{_API}(지역코드: {법정동코드} 조회 완료)\n- 데이터: {_scipClsfiDstic.get(scipClsfiDstic)}"""
                print(msg)
        except Exception as e:
            print(e)
            return
        
        try:
            new_column_order = ['기준일자', '업무공통코드', '공통코드명', '청약가입건수',]
            df = df.reindex(columns=new_column_order)
        except Exception as e:
            print(e)
            return
        
        try:
            df.insert(0, '지역코드', 법정동코드)
        except Exception as e:
            print(e)
            return
        
        return df
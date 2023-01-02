"""
KB부동산 데이터 API
"""
import requests
import pandas as pd

class Kbland:

    def __init__(self):
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
            "01": ['매수자많음','비슷함','매도자많음','매수우위지수'],
            "02": ['활발함','보통','한산함','매매거래지수'],
            "03": ['공급충분','공급적절','공급부족','전세수급지수'],
            "04": ['활발함','보통','한산함','전세거래지수'],
            "05": ['상승','약상승','보통','약하락','하락','매매상승하락전망지수'],
            "06": ['상승','약상승','보통','약하락','하락','전세상승하락전망지수'],
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


    #==============================================================================
    # 주택가격동향조사 - 가격지수
    #==============================================================================

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
            res = requests.get(url, params=params)
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
        values = pd.DataFrame(df['dataList'].values.tolist()).iloc[:, :n_date_list]
        values.columns = columns
        df = pd.concat([df[['지역코드','지역명']], values], axis=1)
        df2 = pd.melt(df, id_vars=['지역코드','지역명']).rename(columns={'variable':'날짜', 'value':'가격지수'})
        if n_date_str == 6:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m')
        elif n_date_str == 8:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m%d')
        df2 = df2.sort_values(['지역코드','날짜'], ascending=[True, True]).reset_index(drop=True)
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
            res = requests.get(url, params=params)
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
        values = pd.DataFrame(df['dataList'].values.tolist()).iloc[:, :n_date_list]
        values.columns = columns
        df = pd.concat([df[['지역코드','지역명']], values], axis=1)
        df2 = pd.melt(df, id_vars=['지역코드','지역명']).rename(columns={'variable':'날짜', 'value':'가격지수'})
        if n_date_str == 6:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m')
        elif n_date_str == 8:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m%d')
        df2 = df2.sort_values(['지역코드','날짜'], ascending=[True, True]).reset_index(drop=True)
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
            res = requests.get(url, params=params)
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


    #==============================================================================
    # 주택가격동향조사 - 가격지수증감률
    #==============================================================================

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
            res = requests.get(url, params=params)
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
        values = pd.DataFrame(df['dataList'].values.tolist()).iloc[:, :n_date_list]
        values.columns = columns
        df = pd.concat([df[['지역코드','지역명']], values], axis=1)
        df2 = pd.melt(df, id_vars=['지역코드','지역명']).rename(columns={'variable':'날짜', 'value':'가격지수증감률'})
        if n_date_str == 6:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m')
        elif n_date_str == 8:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m%d')
        df2 = df2.sort_values(['지역코드','날짜'], ascending=[True, True]).reset_index(drop=True)
        # 코드 정보 부여
        code_df = pd.DataFrame({
            "월간주간구분": [self.월간주간구분코드[월간주간구분코드]],
            "매물종별구분": [self.매물종별구분[매물종별구분]],
            "거래구분": [self.매매전세코드[매매전세코드]],
            })
        code_df = pd.concat([code_df] * len(df2), ignore_index=True)
        df2 = pd.concat([code_df, df2], axis=1)
        return df2


    #==============================================================================
    # 주택가격동향조사 - 전세가격비율
    #==============================================================================

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
            res = requests.get(url, params=params)
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
        values = pd.DataFrame(df['dataList'].values.tolist()).iloc[:, :n_date_list]
        values.columns = columns
        df = pd.concat([df[['지역코드','지역명']], values], axis=1)
        df2 = pd.melt(df, id_vars=['지역코드','지역명']).rename(columns={'variable':'날짜', 'value':'전세가격비율'})
        if n_date_str == 6:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m')
        elif n_date_str == 8:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m%d')
        df2 = df2.sort_values(['지역코드','날짜'], ascending=[True, True]).reset_index(drop=True)
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
            res = requests.get(url, params=params)
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
        values = pd.DataFrame(df['dataList'].values.tolist()).iloc[:, :n_date_list]
        values.columns = columns
        df = pd.concat([df[['지역코드','지역명']], values], axis=1)
        df2 = pd.melt(df, id_vars=['지역코드','지역명']).rename(columns={'variable':'날짜', 'value':'전세가격비율'})
        if n_date_str == 6:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m')
        elif n_date_str == 8:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m%d')
        df2 = df2.sort_values(['지역코드','날짜'], ascending=[True, True]).reset_index(drop=True)
        return df2


    #==============================================================================
    # 주택가격동향조사 - 시장동향/설문조사
    #==============================================================================
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
            res = requests.get(url, params=params)
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
        values = pd.DataFrame(df['dataList'].values.tolist()).iloc[:, :n_date_list]
        values.columns = columns
        df = pd.concat([df[['지역코드','지역명']], values], axis=1)
        df2 = pd.melt(df, id_vars=['지역코드','지역명']).rename(columns={'variable':'날짜', 'value':'값'})
        if n_date_str == 6:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m')
        elif n_date_str == 8:
            df2['날짜'] = pd.to_datetime(df2['날짜'], format='%Y%m%d')
        df2 = df2.sort_values(['지역코드','날짜'], ascending=[True, True]).reset_index(drop=True)
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


    #==============================================================================
    # 주택가격동향조사 - 면적별 가격지수
    #==============================================================================
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
            res = requests.get(url, params=params)
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
        df3 = pd.melt(df2, id_vars=['지역코드','지역명'])
        tmp = df3['value'].apply(pd.Series)
        df4 = pd.concat([df3.drop(['variable','value'], axis=1), tmp], axis=1)
        tmp = df4['데이터리스트'].apply(pd.Series).iloc[:,:n_date_list]
        tmp.columns = columns
        df5 = pd.concat([df4.drop(['데이터리스트'], axis=1), tmp], axis=1)
        tot = pd.melt(df5, id_vars=['지역코드','지역명','면적크기','면적크기코드']).rename(columns={'variable':'날짜','value':'가격지수'})
        if n_date_str == 6:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m')
        elif n_date_str == 8:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m%d')
        # 피벗 테이블 생성
        pv = tot.pivot(index=['지역코드','지역명','날짜'], columns=['면적크기코드','면적크기'], values=['가격지수']).droplevel([0,1], axis=1).reset_index()
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


    #==============================================================================
    # 주택가격동향조사 - 평균가격
    #==============================================================================
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
            res = requests.get(url, params=params)
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
        tot = pd.melt(df2, id_vars=['지역코드','지역명']).rename(columns={'variable':'날짜','value':'평균가격'})
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


    #==============================================================================
    # 주택가격동향조사 - ㎡당 평균가격
    #==============================================================================
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
            res = requests.get(url, params=params)
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

        df = pd.DataFrame(data['데이터리스트'])[['지역코드','지역명','dataList']]
        tmp = df['dataList'].apply(pd.Series)
        tmp.columns = columns
        df2 = pd.concat([df.drop(['dataList'], axis=1), tmp], axis=1)
        tot = pd.melt(df2, id_vars=['지역코드','지역명']).rename(columns={'variable':'날짜','value':'㎡당 평균가격'})
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


    #==============================================================================
    # 주택가격동향조사 - 5분위 평균가격
    #==============================================================================
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
            res = requests.get(url, params=params)
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
        df3 = pd.melt(df2, id_vars=['지역코드','지역명'])
        tmp = df3['value'].apply(pd.Series)
        df4 = pd.concat([df3.drop(['variable','value'], axis=1), tmp], axis=1)[['지역코드','지역명','기준날짜','5분위','4분위','3분위','2분위','1분위','5분위배율']]
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


    #==============================================================================
    # 주택가격동향조사 - 면적별 평균가격
    #==============================================================================
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
            res = requests.get(url, params=params)
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
        df3 = pd.melt(df2, id_vars=['지역코드','지역명'])
        tmp = df3['value'].apply(pd.Series)
        df4 = pd.concat([df3.drop(['variable','value'], axis=1), tmp], axis=1)
        tmp = df4['데이터리스트'].apply(pd.Series).iloc[:,:n_date_list]
        tmp.columns = columns
        df5 = pd.concat([df4.drop(['데이터리스트'], axis=1), tmp], axis=1)
        tot = pd.melt(df5, id_vars=['지역코드','지역명','면적크기','면적크기코드']).rename(columns={'variable':'날짜','value':'평균가격'})
        if n_date_str == 6:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m')
        elif n_date_str == 8:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m%d')
        # 피벗 테이블 생성
        pv = tot.pivot(index=['지역코드','지역명','날짜'], columns=['면적크기코드','면적크기'], values=['평균가격']).droplevel([0,1], axis=1).reset_index()
        pv.columns.name = None
        # 코드 정보 부여
        code_df = pd.DataFrame({
            "매매전세코드": [self.매매전세코드[매매전세코드]],
            "면적별코드": [self.면적별코드[면적별코드]],
            })
        code_df = pd.concat([code_df] * len(pv), ignore_index=True)
        pv = pd.concat([code_df, pv], axis=1)
        return pv


    #==============================================================================
    # 주택가격동향조사 - 중위가격
    #==============================================================================
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
            res = requests.get(url, params=params)
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
        tot = pd.melt(df2, id_vars=['지역코드','지역명']).rename(columns={'variable':'날짜','value':'중위가격'})
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


    #==============================================================================
    # 주택가격동향조사 - 소득연계
    #==============================================================================

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
            res = requests.get(url, params=params)
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
        df3 = pd.melt(df2, id_vars=['지역코드','지역명'])
        tmp = df3['value'].apply(pd.Series)
        df4 = pd.concat([df3.drop(['variable','value'], axis=1), tmp], axis=1)
        tmp = df4['소득분위구분'].apply(pd.Series)
        df5 = pd.concat([df4.drop('소득분위구분', axis=1), tmp], axis=1)
        df6 = pd.melt(df5, id_vars=['지역코드','지역명','주택분위'])
        tmp = df6['value'].apply(pd.Series).iloc[:,:n_date_str]
        df7 = pd.concat([df6.drop(['variable','value'], axis=1), tmp], axis=1)
        tmp = df7['dataList'].apply(pd.Series).iloc[:,:n_date_list]
        tmp.columns = columns
        df8 = pd.concat([df7.drop('dataList', axis=1), tmp], axis=1)
        tot = pd.melt(df8, id_vars=['지역코드','지역명','주택분위','소득분위']).rename(columns={'variable':'날짜','value':'PIR'})
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
            res = requests.get(url, params=params)
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
        df3 = pd.melt(df2, id_vars=['지역코드','지역명'])
        tmp = df3['value'].apply(pd.Series)
        df4 = pd.concat([df3.drop(['variable','value'], axis=1), tmp], axis=1)
        tmp = df4['매물종별구분리스트'].apply(pd.Series)
        tmp.columns = columns
        df5 = pd.concat([df4.drop('매물종별구분리스트', axis=1), tmp], axis=1)
        tot = pd.melt(df5, id_vars=['지역코드','지역명','매물종별구분']).rename(columns={'variable':'날짜','value':'HAI'})
        if n_date_str == 6:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m')
        elif n_date_str == 8:
            tot['날짜'] = pd.to_datetime(tot['날짜'], format='%Y%m%d')
        pv = tot.pivot(index=['지역코드','지역명','날짜'], columns='매물종별구분', values='HAI').reset_index()
        pv.columns.name = None
        pv = pv[['지역코드','지역명','날짜','종합','아파트','단독','연립']]
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
            res = requests.get(url, params=params)
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
        df = df.rename(columns={'기준날짜':'날짜'})
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
            res = requests.get(url, params=params)
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
        df3 = pd.melt(df2, id_vars=['지역코드','지역명'])
        tmp = df3['value'].apply(pd.Series)
        df4 = pd.concat([df3.drop(['value'], axis=1), tmp], axis=1).rename(columns={"variable": "날짜"})
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
            res = requests.get(url, params=params)
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
        df3 = pd.melt(df2, id_vars=['지역코드','지역명'])
        tmp = df3['value'].apply(pd.Series)
        df4 = pd.concat([df3.drop(['value'], axis=1), tmp], axis=1).rename(columns={"variable": "날짜"})
        if n_date_str == 6:
            df4['날짜'] = pd.to_datetime(df4['날짜'], format='%Y%m')
        elif n_date_str == 8:
            df4['날짜'] = pd.to_datetime(df4['날짜'], format='%Y%m%d')
        return df4
# FRED(Federal Reserve Economic Data) 사용 가이드

[FRED(Federal Reserve Economic Data)](https://fred.stlouisfed.org/)는 세인트루이스 연방준비은행(Federal Reserve Bank of St. Louis)에서 제공하는 경제 데이터입니다. FRED API를 사용하려면 인증키가 필요합니다. 인증키를 얻기 위해서는 [FRED API Key](https://fredaccount.stlouisfed.org/apikey)에서 간단한 신청서를 작성하면 됩니다. 구체적인 FRED API 신청 방법과 실제 주요 경제 지표를 조회 사례를 확인하려면 [Python으로 주요 경제 지표 조회하기(feat.FRED)](https://wooiljeong.github.io/python/pdr-fred/)를 참고하세요.


## 라이브러리 인포트하기

```python
from PublicDataReader import Fred

# FRED API 키
api_key = "YOUR FRED API KEY"

# 인스턴스 생성하기
api = Fred(api_key)
```


## 시리즈 검색하기

FRED의 '시리즈'는 시간에 따른 특정 경제 지표의 변화를 나타내는 데이터 세트입니다. 이러한 시리즈는 일련의 연속적인 데이터 포인트를 포함하여 경제 지표의 시간 경과에 따른 변화를 표현합니다. 각 시리즈는 특정 경제 지표(예: 실업률, GDP, 인플레이션 등)를 대표하며, 이 데이터는 특정 기간(일, 월, 분기, 연도 등) 동안 수집됩니다. 이러한 시리즈는 경제적 패턴과 경향을 분석하고 이해하는 데 도움이 됩니다. 이와 같은 시리즈를 검색하려면 `api.get_data()` 메서드의 인자인 `api_name`에 `series_search`를 입력하고, `search_text`에 검색할 시리즈의 키워드를 입력하면 됩니다. 검색 결과에서 원하는 시리즈의 ID 값을 확인할 수 있습니다. 이 시리즈의 ID 값은 시리즈 데이터를 조회할 때 사용합니다. 예를 들어, 인플레이션과 관련된 지표인 소비자 가격 지수(consumer price index)의 시리즈 ID 값을 확인하려면 다음과 같이 `search_text`에 `consumer price index`라고 입력하면 됩니다.

```python
search_text = "consumer price index"
result = api.get_data(api_name="series_search", search_text=search_text)
result.head()
```


## 시리즈 데이터 조회하기

시리즈 데이터를 조회하려면 `api_get_data()` 메서드의 인자인 `api_name`에 `series_observations`를 입력하고, `search_id`에 시리즈 ID 값을 입력하면 됩니다. 예를 들어, 소비자 가격 지수의 시리즈 데이터를 조회하려면 다음과 같이 `search_id`에 `CPIAUCNS`라고 입력하면 됩니다. 참고로 이 데이터는 [FRED 웹사이트](https://fred.stlouisfed.org/series/CPIAUCNS)에서도 확인할 수 있습니다.

```python
# 시리즈 ID 값
series_id = "CPIAUCNS"

# 시리즈 데이터 조회
df = api.get_data(api_name="series_observations", series_id=series_id)
df.tail()
```
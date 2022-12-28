# PublicDataReader - KB부동산 데이터허브 API 사용방법

- [KB부동산 데이터허브](https://data.kbland.kr/)


<br>

# KB부동산 API 인스턴스 생성


```python
from PublicDataReader import Kbland
api = Kbland()
```

# 주택가격동향조사

## 주요 파라미터 정리

- 월간주간구분코드
    - 01: 월간
    - 02: 주간
- 매물종별구분
    - 01: 아파트
    - 08: 연립
    - 09: 단독
    - 98: 주택종합
- 매매전세코드
    - 01: 매매
    - 02: 전세
- 면적별코드
    - 01: 전용면적별(구)
    - 02: 전용면적별
- (PIR) 메뉴코드
    - 01: PIR
    - 02: J-PIR

## 가격지수

- 주간 아파트 매매가격지수
- 주간 아파트 전세가격지수
- 월간 아파트 매매가격지수
- 월간 아파트 전세가격지수
- 단독 매매가격지수
- 단독 전세가격지수
- 연립 매매가격지수
- 연립 전세가격지수
- 주택종합 매매가격지수
- 주택종합 전세가격지수


```python
params = {
    "월간주간구분코드": "01",
    "매물종별구분": "01",
    "매매전세코드": "01",
    # "지역코드": "11",
    "기간": 1,
}
df = api.get_price_index(**params)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>월간주간구분</th>
      <th>매물종별구분</th>
      <th>거래구분</th>
      <th>지역코드</th>
      <th>지역명</th>
      <th>날짜</th>
      <th>가격지수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>307</th>
      <td>월간</td>
      <td>아파트</td>
      <td>매매</td>
      <td>5000000000</td>
      <td>제주</td>
      <td>2022-08-01</td>
      <td>105.170226</td>
    </tr>
    <tr>
      <th>308</th>
      <td>월간</td>
      <td>아파트</td>
      <td>매매</td>
      <td>5000000000</td>
      <td>제주</td>
      <td>2022-09-01</td>
      <td>105.253394</td>
    </tr>
    <tr>
      <th>309</th>
      <td>월간</td>
      <td>아파트</td>
      <td>매매</td>
      <td>5000000000</td>
      <td>제주</td>
      <td>2022-10-01</td>
      <td>105.159935</td>
    </tr>
    <tr>
      <th>310</th>
      <td>월간</td>
      <td>아파트</td>
      <td>매매</td>
      <td>5000000000</td>
      <td>제주</td>
      <td>2022-11-01</td>
      <td>105.138961</td>
    </tr>
    <tr>
      <th>311</th>
      <td>월간</td>
      <td>아파트</td>
      <td>매매</td>
      <td>5000000000</td>
      <td>제주</td>
      <td>2022-12-01</td>
      <td>104.559209</td>
    </tr>
  </tbody>
</table>
</div>



- 월간 아파트 월세가격지수


```python
params = {
    "기간": 1
}
df = api.get_monthly_apartment_wolse_index(**params)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>월간주간구분</th>
      <th>매물종별구분</th>
      <th>거래구분</th>
      <th>지역코드</th>
      <th>지역명</th>
      <th>날짜</th>
      <th>가격지수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>73</th>
      <td>월간</td>
      <td>아파트</td>
      <td>월세</td>
      <td>4100000000</td>
      <td>경기도</td>
      <td>2022-08-01</td>
      <td>105.904649</td>
    </tr>
    <tr>
      <th>74</th>
      <td>월간</td>
      <td>아파트</td>
      <td>월세</td>
      <td>4100000000</td>
      <td>경기도</td>
      <td>2022-09-01</td>
      <td>106.492218</td>
    </tr>
    <tr>
      <th>75</th>
      <td>월간</td>
      <td>아파트</td>
      <td>월세</td>
      <td>4100000000</td>
      <td>경기도</td>
      <td>2022-10-01</td>
      <td>107.347923</td>
    </tr>
    <tr>
      <th>76</th>
      <td>월간</td>
      <td>아파트</td>
      <td>월세</td>
      <td>4100000000</td>
      <td>경기도</td>
      <td>2022-11-01</td>
      <td>107.957964</td>
    </tr>
    <tr>
      <th>77</th>
      <td>월간</td>
      <td>아파트</td>
      <td>월세</td>
      <td>4100000000</td>
      <td>경기도</td>
      <td>2022-12-01</td>
      <td>107.956571</td>
    </tr>
  </tbody>
</table>
</div>



- KB선도아파트 50 지수


```python
params = {
    "기간": 1
}
df = api.get_lead_apartment_50_index(**params)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>날짜</th>
      <th>선도50지수</th>
      <th>전월대비증감률</th>
      <th>전년동월대비증감률</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>2022-08-01</td>
      <td>100.451199</td>
      <td>-0.718366</td>
      <td>6.258222</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2022-09-01</td>
      <td>99.322158</td>
      <td>-1.123969</td>
      <td>3.105370</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2022-10-01</td>
      <td>97.584598</td>
      <td>-1.749418</td>
      <td>-0.118113</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2022-11-01</td>
      <td>94.517070</td>
      <td>-3.143456</td>
      <td>-4.390270</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2022-12-01</td>
      <td>92.074998</td>
      <td>-2.583736</td>
      <td>-7.554604</td>
    </tr>
  </tbody>
</table>
</div>



## 가격지수증감률

- 주간 아파트 매매가격지수 증감률
- 주간 아파트 전세가격지수 증감률
- 월간 아파트 매매가격지수 증감률
- 월간 아파트 전세가격지수 증감률
- 단독 매매가격지수 증감률
- 단독 전세가격지수 증감률
- 연립 매매가격지수 증감률
- 연립 전세가격지수 증감률
- 주택종합 매매가격지수 증감률
- 주택종합 전세가격지수 증감률


```python
params = {
    "월간주간구분코드": "01",
    "매물종별구분": "01",
    "매매전세코드": "01",
    # "지역코드": "11",
    "기간": 1,
}
df = api.get_price_index_change_rate(**params)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>월간주간구분</th>
      <th>매물종별구분</th>
      <th>거래구분</th>
      <th>지역코드</th>
      <th>지역명</th>
      <th>날짜</th>
      <th>가격지수증감률</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>307</th>
      <td>월간</td>
      <td>아파트</td>
      <td>매매</td>
      <td>5000000000</td>
      <td>제주</td>
      <td>2022-08-01</td>
      <td>0.062061</td>
    </tr>
    <tr>
      <th>308</th>
      <td>월간</td>
      <td>아파트</td>
      <td>매매</td>
      <td>5000000000</td>
      <td>제주</td>
      <td>2022-09-01</td>
      <td>0.079079</td>
    </tr>
    <tr>
      <th>309</th>
      <td>월간</td>
      <td>아파트</td>
      <td>매매</td>
      <td>5000000000</td>
      <td>제주</td>
      <td>2022-10-01</td>
      <td>-0.088794</td>
    </tr>
    <tr>
      <th>310</th>
      <td>월간</td>
      <td>아파트</td>
      <td>매매</td>
      <td>5000000000</td>
      <td>제주</td>
      <td>2022-11-01</td>
      <td>-0.019944</td>
    </tr>
    <tr>
      <th>311</th>
      <td>월간</td>
      <td>아파트</td>
      <td>매매</td>
      <td>5000000000</td>
      <td>제주</td>
      <td>2022-12-01</td>
      <td>-0.551415</td>
    </tr>
  </tbody>
</table>
</div>



## 전세가격비율

- 아파트 매매가격대비 전세가격비율
- 단독 매매가격대비 전세가격비율
- 연립 매매가격대비 전세가격비율
- 주택종합 매매가격대비 전세가격비율


```python
params = {
    "매물종별구분": "98",
    "기간": 1,
    # "지역코드": "11",
}

df = api.get_jeonse_price_ratio(**params)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>매물종별구분</th>
      <th>지역코드</th>
      <th>지역명</th>
      <th>날짜</th>
      <th>전세가격비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>307</th>
      <td>주택종합</td>
      <td>5000000000</td>
      <td>제주특별자치도</td>
      <td>2022-08-01</td>
      <td>57.317359</td>
    </tr>
    <tr>
      <th>308</th>
      <td>주택종합</td>
      <td>5000000000</td>
      <td>제주특별자치도</td>
      <td>2022-09-01</td>
      <td>58.499050</td>
    </tr>
    <tr>
      <th>309</th>
      <td>주택종합</td>
      <td>5000000000</td>
      <td>제주특별자치도</td>
      <td>2022-10-01</td>
      <td>60.535311</td>
    </tr>
    <tr>
      <th>310</th>
      <td>주택종합</td>
      <td>5000000000</td>
      <td>제주특별자치도</td>
      <td>2022-11-01</td>
      <td>58.380322</td>
    </tr>
    <tr>
      <th>311</th>
      <td>주택종합</td>
      <td>5000000000</td>
      <td>제주특별자치도</td>
      <td>2022-12-01</td>
      <td>58.378539</td>
    </tr>
  </tbody>
</table>
</div>



- 전월세 전환율


```python
params = {
    "기간": 1,
}
df = api.get_jeonwolse_conversion_rate(**params)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역코드</th>
      <th>지역명</th>
      <th>날짜</th>
      <th>전세가격비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>73</th>
      <td>4100000000</td>
      <td>경기도</td>
      <td>2022-08-01</td>
      <td>4.028560</td>
    </tr>
    <tr>
      <th>74</th>
      <td>4100000000</td>
      <td>경기도</td>
      <td>2022-09-01</td>
      <td>4.051587</td>
    </tr>
    <tr>
      <th>75</th>
      <td>4100000000</td>
      <td>경기도</td>
      <td>2022-10-01</td>
      <td>4.119020</td>
    </tr>
    <tr>
      <th>76</th>
      <td>4100000000</td>
      <td>경기도</td>
      <td>2022-11-01</td>
      <td>4.366276</td>
    </tr>
    <tr>
      <th>77</th>
      <td>4100000000</td>
      <td>경기도</td>
      <td>2022-12-01</td>
      <td>4.556344</td>
    </tr>
  </tbody>
</table>
</div>



## 시장동향/설문조사

- 주간 매수우위지수
- 주간 매매거래활발지수
- 주간 전세수급지수
- 주간 전세거래활발지수
- 월간 매수우위지수
- 월간 매매거래활발지수
- 월간 전세수급지수
- 월간 전세거래활발지수
- 월간 매매가격전망지수
- 월간 전세가격전망지수


```python
params = {
    "메뉴코드": "01",
    "월간주간구분코드": "01",
    "기간": 1,
}
df = api.get_market_trend(**params)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>메뉴코드</th>
      <th>월간주간구분</th>
      <th>지역코드</th>
      <th>지역명</th>
      <th>날짜</th>
      <th>매수자많음</th>
      <th>비슷함</th>
      <th>매도자많음</th>
      <th>매수우위지수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>307</th>
      <td>매수우위지수</td>
      <td>월간</td>
      <td>5000000000</td>
      <td>제주특별자치도</td>
      <td>2022-08-01</td>
      <td>4.347826</td>
      <td>39.130435</td>
      <td>56.521739</td>
      <td>47.826087</td>
    </tr>
    <tr>
      <th>308</th>
      <td>매수우위지수</td>
      <td>월간</td>
      <td>5000000000</td>
      <td>제주특별자치도</td>
      <td>2022-09-01</td>
      <td>0.000000</td>
      <td>32.193142</td>
      <td>67.806858</td>
      <td>32.193142</td>
    </tr>
    <tr>
      <th>309</th>
      <td>매수우위지수</td>
      <td>월간</td>
      <td>5000000000</td>
      <td>제주특별자치도</td>
      <td>2022-10-01</td>
      <td>0.000000</td>
      <td>35.496914</td>
      <td>64.503086</td>
      <td>35.496914</td>
    </tr>
    <tr>
      <th>310</th>
      <td>매수우위지수</td>
      <td>월간</td>
      <td>5000000000</td>
      <td>제주특별자치도</td>
      <td>2022-11-01</td>
      <td>0.000000</td>
      <td>39.967654</td>
      <td>60.032346</td>
      <td>39.967654</td>
    </tr>
    <tr>
      <th>311</th>
      <td>매수우위지수</td>
      <td>월간</td>
      <td>5000000000</td>
      <td>제주특별자치도</td>
      <td>2022-12-01</td>
      <td>0.000000</td>
      <td>30.013714</td>
      <td>69.986286</td>
      <td>30.013714</td>
    </tr>
  </tbody>
</table>
</div>



## 면적별 가격지수

- 주간 아파트 전용면적별 매매가격지수
- 주간 아파트 전용면적별 전세가격지수
- 월간 아파트 전용면적별 매매가격지수
- 월간 아파트 전용면적별 전세가격지수
- 월간 아파트 전용면적별(구) 매매가격지수
- 월간 아파트 전용면적별(구) 전세가격지수
- 단독 전용면적별 매매가격지수
- 단독 전용면적별 전세가격지수
- 연립 전용면적별 매매가격지수
- 연립 전용면적별 전세가격지수
- 주택종합 전용면적별 매매가격지수
- 주택종합 전용면적별 전세가격지수


```python
params = {
    "월간주간구분코드": "01",
    "매물종별구분": "98",
    "면적별코드": "02",
    "매매전세코드": "02",
    "기간": 1,
}

df = api.get_price_index_by_area(**params)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>월간주간구분</th>
      <th>매물종별구분</th>
      <th>면적별코드</th>
      <th>매매전세코드</th>
      <th>지역코드</th>
      <th>지역명</th>
      <th>날짜</th>
      <th>대형</th>
      <th>중형</th>
      <th>소형</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>294</th>
      <td>월간</td>
      <td>주택종합</td>
      <td>전용면적별</td>
      <td>전세</td>
      <td>4A0000</td>
      <td>기타지방</td>
      <td>2022-08-01</td>
      <td>101.174377</td>
      <td>101.727268</td>
      <td>102.974528</td>
    </tr>
    <tr>
      <th>295</th>
      <td>월간</td>
      <td>주택종합</td>
      <td>전용면적별</td>
      <td>전세</td>
      <td>4A0000</td>
      <td>기타지방</td>
      <td>2022-09-01</td>
      <td>101.119346</td>
      <td>101.663716</td>
      <td>103.074701</td>
    </tr>
    <tr>
      <th>296</th>
      <td>월간</td>
      <td>주택종합</td>
      <td>전용면적별</td>
      <td>전세</td>
      <td>4A0000</td>
      <td>기타지방</td>
      <td>2022-10-01</td>
      <td>100.969166</td>
      <td>101.484971</td>
      <td>103.072944</td>
    </tr>
    <tr>
      <th>297</th>
      <td>월간</td>
      <td>주택종합</td>
      <td>전용면적별</td>
      <td>전세</td>
      <td>4A0000</td>
      <td>기타지방</td>
      <td>2022-11-01</td>
      <td>100.743825</td>
      <td>101.092271</td>
      <td>102.477187</td>
    </tr>
    <tr>
      <th>298</th>
      <td>월간</td>
      <td>주택종합</td>
      <td>전용면적별</td>
      <td>전세</td>
      <td>4A0000</td>
      <td>기타지방</td>
      <td>2022-12-01</td>
      <td>100.461516</td>
      <td>100.749903</td>
      <td>101.713803</td>
    </tr>
  </tbody>
</table>
</div>



## 평균가격

- 아파트 매매평균가격
- 아파트 전세평균가격
- 단독 매매평균가격
- 단독 전세평균가격
- 연립 매매평균가격
- 연립 전세평균가격
- 주택종합 매매평균가격
- 주택종합 전세평균가격


```python
params = {
    "매물종별구분": "98",
    "매매전세코드": "02",
    "기간": 1,
}

df = api.get_average_price(**params)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>매물종별구분</th>
      <th>매매전세코드</th>
      <th>지역코드</th>
      <th>지역명</th>
      <th>날짜</th>
      <th>평균가격</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>307</th>
      <td>주택종합</td>
      <td>전세</td>
      <td>4500000000</td>
      <td>전북</td>
      <td>2022-12-01</td>
      <td>14278.121229</td>
    </tr>
    <tr>
      <th>308</th>
      <td>주택종합</td>
      <td>전세</td>
      <td>4600000000</td>
      <td>전남</td>
      <td>2022-12-01</td>
      <td>12319.907262</td>
    </tr>
    <tr>
      <th>309</th>
      <td>주택종합</td>
      <td>전세</td>
      <td>4700000000</td>
      <td>경북</td>
      <td>2022-12-01</td>
      <td>14227.938099</td>
    </tr>
    <tr>
      <th>310</th>
      <td>주택종합</td>
      <td>전세</td>
      <td>4800000000</td>
      <td>경남</td>
      <td>2022-12-01</td>
      <td>17297.151272</td>
    </tr>
    <tr>
      <th>311</th>
      <td>주택종합</td>
      <td>전세</td>
      <td>5000000000</td>
      <td>제주특별자치도</td>
      <td>2022-12-01</td>
      <td>19614.095751</td>
    </tr>
  </tbody>
</table>
</div>



## ㎡당 평균가격

- 아파트 ㎡당 매매평균가격
- 아파트 ㎡당 전세평균가격
- 단독 ㎡당 매매평균가격
- 단독 ㎡당 전세평균가격
- 연립 ㎡당 매매평균가격
- 연립 ㎡당 전세평균가격
- 주택종합 ㎡당 매매평균가격
- 주택종합 ㎡당 전세평균가격


```python
params = {
    "매물종별구분": "98",
    "매매전세코드": "02",
    "기간": 1,
}

df = api.get_average_price_per_squaremeter(**params)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>매물종별구분</th>
      <th>매매전세코드</th>
      <th>지역코드</th>
      <th>지역명</th>
      <th>날짜</th>
      <th>㎡당 평균가격</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>307</th>
      <td>주택종합</td>
      <td>전세</td>
      <td>4500000000</td>
      <td>전북</td>
      <td>2022-12-01</td>
      <td>166.325558</td>
    </tr>
    <tr>
      <th>308</th>
      <td>주택종합</td>
      <td>전세</td>
      <td>4600000000</td>
      <td>전남</td>
      <td>2022-12-01</td>
      <td>152.765673</td>
    </tr>
    <tr>
      <th>309</th>
      <td>주택종합</td>
      <td>전세</td>
      <td>4700000000</td>
      <td>경북</td>
      <td>2022-12-01</td>
      <td>169.046494</td>
    </tr>
    <tr>
      <th>310</th>
      <td>주택종합</td>
      <td>전세</td>
      <td>4800000000</td>
      <td>경남</td>
      <td>2022-12-01</td>
      <td>208.752911</td>
    </tr>
    <tr>
      <th>311</th>
      <td>주택종합</td>
      <td>전세</td>
      <td>5000000000</td>
      <td>제주</td>
      <td>2022-12-01</td>
      <td>189.594216</td>
    </tr>
  </tbody>
</table>
</div>



## 5분위 평균가격

- 아파트 5분위 매매평균가격
- 아파트 5분위 전세평균가격
- 주택종합 5분위 매매평균가격
- 주택종합 5분위 전세평균가격
- 아파트 ㎡당 5분위 매매평균가격
- 아파트 ㎡당 5분위 전세평균가격


```python
params = {
    "메뉴코드": "03",
    "매매전세코드": "02",
    "기간": 1,
}

df = api.get_average_price_by_quintile(**params)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구분</th>
      <th>매매전세코드</th>
      <th>지역코드</th>
      <th>지역명</th>
      <th>날짜</th>
      <th>5분위</th>
      <th>4분위</th>
      <th>3분위</th>
      <th>2분위</th>
      <th>1분위</th>
      <th>5분위배율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>164</th>
      <td>아파트 아파트 ㎡당 평균가격</td>
      <td>전세</td>
      <td>2800000000</td>
      <td>인천광역시</td>
      <td>2022-12-01</td>
      <td>491.403509</td>
      <td>386.471590</td>
      <td>344.264384</td>
      <td>303.610043</td>
      <td>215.612663</td>
      <td>2.279103</td>
    </tr>
    <tr>
      <th>165</th>
      <td>아파트 아파트 ㎡당 평균가격</td>
      <td>전세</td>
      <td>2900000000</td>
      <td>광주광역시</td>
      <td>2022-12-01</td>
      <td>402.463105</td>
      <td>310.735175</td>
      <td>253.624288</td>
      <td>206.210244</td>
      <td>150.805656</td>
      <td>2.668753</td>
    </tr>
    <tr>
      <th>166</th>
      <td>아파트 아파트 ㎡당 평균가격</td>
      <td>전세</td>
      <td>3000000000</td>
      <td>대전광역시</td>
      <td>2022-12-01</td>
      <td>443.503048</td>
      <td>360.930948</td>
      <td>315.748221</td>
      <td>267.492853</td>
      <td>179.190220</td>
      <td>2.475040</td>
    </tr>
    <tr>
      <th>167</th>
      <td>아파트 아파트 ㎡당 평균가격</td>
      <td>전세</td>
      <td>3100000000</td>
      <td>울산광역시</td>
      <td>2022-12-01</td>
      <td>449.334068</td>
      <td>353.766742</td>
      <td>292.955087</td>
      <td>212.044246</td>
      <td>141.421487</td>
      <td>3.177269</td>
    </tr>
    <tr>
      <th>168</th>
      <td>아파트 아파트 ㎡당 평균가격</td>
      <td>전세</td>
      <td>4100000000</td>
      <td>경기도</td>
      <td>2022-12-01</td>
      <td>674.547431</td>
      <td>496.251276</td>
      <td>421.876596</td>
      <td>354.425615</td>
      <td>253.803434</td>
      <td>2.657755</td>
    </tr>
  </tbody>
</table>
</div>



## 면적별 평균가격

- 아파트 전용면적별 매매평균가격
- 아파트 전용면적별 전세평균가격
- 아파트 전용면적별(구) 매매평균가격
- 아파트 전용면적별(구) 전세평균가격


```python
params = {
    "매매전세코드": "01",
    "면적별코드": "01",
    "기간": 1,
}

df = api.get_average_price_by_area(**params)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>매매전세코드</th>
      <th>면적별코드</th>
      <th>지역코드</th>
      <th>지역명</th>
      <th>날짜</th>
      <th>대형</th>
      <th>중대형</th>
      <th>중형</th>
      <th>중소형</th>
      <th>소형</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>307</th>
      <td>매매</td>
      <td>전용면적별(구)</td>
      <td>5000000000</td>
      <td>제주특별자치도</td>
      <td>2022-08-01</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>308</th>
      <td>매매</td>
      <td>전용면적별(구)</td>
      <td>5000000000</td>
      <td>제주특별자치도</td>
      <td>2022-09-01</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>309</th>
      <td>매매</td>
      <td>전용면적별(구)</td>
      <td>5000000000</td>
      <td>제주특별자치도</td>
      <td>2022-10-01</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>310</th>
      <td>매매</td>
      <td>전용면적별(구)</td>
      <td>5000000000</td>
      <td>제주특별자치도</td>
      <td>2022-11-01</td>
      <td>92332.644648</td>
      <td>82108.058292</td>
      <td>53114.571203</td>
      <td>33068.779514</td>
      <td>32441.575685</td>
    </tr>
    <tr>
      <th>311</th>
      <td>매매</td>
      <td>전용면적별(구)</td>
      <td>5000000000</td>
      <td>제주특별자치도</td>
      <td>2022-12-01</td>
      <td>91952.479358</td>
      <td>81926.410356</td>
      <td>52536.604788</td>
      <td>32807.007917</td>
      <td>31969.414118</td>
    </tr>
  </tbody>
</table>
</div>



## 중위가격

- 아파트 매매중위가격
- 아파트 전세중위가격
- 단독 매매중위가격
- 단독 전세중위가격
- 연립 매매중위가격
- 연립 전세중위가격
- 주택종합 매매중위가격
- 주택종합 전세중위가격


```python
params = {
    "매물종별구분": "01",
    "매매전세코드": "02",
    "기간": 1,
}

df = api.get_median_price(**params)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>매물종별구분</th>
      <th>매매전세코드</th>
      <th>지역코드</th>
      <th>지역명</th>
      <th>날짜</th>
      <th>중위가격</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>281</th>
      <td>아파트</td>
      <td>전세</td>
      <td>4400000000</td>
      <td>충청남도</td>
      <td>2022-12-01</td>
      <td>17250.0</td>
    </tr>
    <tr>
      <th>282</th>
      <td>아파트</td>
      <td>전세</td>
      <td>4500000000</td>
      <td>전라북도</td>
      <td>2022-12-01</td>
      <td>13750.0</td>
    </tr>
    <tr>
      <th>283</th>
      <td>아파트</td>
      <td>전세</td>
      <td>4600000000</td>
      <td>전라남도</td>
      <td>2022-12-01</td>
      <td>13000.0</td>
    </tr>
    <tr>
      <th>284</th>
      <td>아파트</td>
      <td>전세</td>
      <td>4700000000</td>
      <td>경상북도</td>
      <td>2022-12-01</td>
      <td>14500.0</td>
    </tr>
    <tr>
      <th>285</th>
      <td>아파트</td>
      <td>전세</td>
      <td>4800000000</td>
      <td>경상남도</td>
      <td>2022-12-01</td>
      <td>17500.0</td>
    </tr>
  </tbody>
</table>
</div>



## 소득연계

- PIR
- J-PIR


```python
params = {
    "메뉴코드": "02",
}

df = api.get_pir(**params)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구분</th>
      <th>지역코드</th>
      <th>지역명</th>
      <th>주택분위</th>
      <th>소득분위</th>
      <th>날짜</th>
      <th>PIR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8295</th>
      <td>J-PIR</td>
      <td>1100000000</td>
      <td>서울특별시</td>
      <td>3</td>
      <td>1</td>
      <td>202209</td>
      <td>25.850212</td>
    </tr>
    <tr>
      <th>8296</th>
      <td>J-PIR</td>
      <td>0000000000</td>
      <td>전국</td>
      <td>2</td>
      <td>1</td>
      <td>202209</td>
      <td>8.545496</td>
    </tr>
    <tr>
      <th>8297</th>
      <td>J-PIR</td>
      <td>1100000000</td>
      <td>서울특별시</td>
      <td>2</td>
      <td>1</td>
      <td>202209</td>
      <td>20.340611</td>
    </tr>
    <tr>
      <th>8298</th>
      <td>J-PIR</td>
      <td>0000000000</td>
      <td>전국</td>
      <td>1</td>
      <td>1</td>
      <td>202209</td>
      <td>4.295563</td>
    </tr>
    <tr>
      <th>8299</th>
      <td>J-PIR</td>
      <td>1100000000</td>
      <td>서울특별시</td>
      <td>1</td>
      <td>1</td>
      <td>202209</td>
      <td>11.646335</td>
    </tr>
  </tbody>
</table>
</div>



- 주택구매력지수



```python
params = {}

df = api.get_hai(**params)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역코드</th>
      <th>지역명</th>
      <th>날짜</th>
      <th>종합</th>
      <th>아파트</th>
      <th>단독</th>
      <th>연립</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1323</th>
      <td>4A0000</td>
      <td>기타지방</td>
      <td>2022-05-01</td>
      <td>224.305503</td>
      <td>209.899887</td>
      <td>242.425435</td>
      <td>472.918121</td>
    </tr>
    <tr>
      <th>1324</th>
      <td>4A0000</td>
      <td>기타지방</td>
      <td>2022-06-01</td>
      <td>221.198848</td>
      <td>206.861945</td>
      <td>239.488800</td>
      <td>467.126847</td>
    </tr>
    <tr>
      <th>1325</th>
      <td>4A0000</td>
      <td>기타지방</td>
      <td>2022-07-01</td>
      <td>217.481631</td>
      <td>203.061371</td>
      <td>235.803848</td>
      <td>459.470863</td>
    </tr>
    <tr>
      <th>1326</th>
      <td>4A0000</td>
      <td>기타지방</td>
      <td>2022-08-01</td>
      <td>213.914760</td>
      <td>199.443407</td>
      <td>231.976797</td>
      <td>452.013740</td>
    </tr>
    <tr>
      <th>1327</th>
      <td>4A0000</td>
      <td>기타지방</td>
      <td>2022-09-01</td>
      <td>205.390114</td>
      <td>192.133267</td>
      <td>221.238582</td>
      <td>425.540526</td>
    </tr>
  </tbody>
</table>
</div>



- (비노출) 중위가구월소득금액


```python
df = api.get_median_household_monthly_income()
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>주택담보대출금리</th>
      <th>중위가구월소득금액</th>
      <th>날짜</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>161</th>
      <td>3.90</td>
      <td>5267166</td>
      <td>2022-05-01</td>
    </tr>
    <tr>
      <th>162</th>
      <td>4.04</td>
      <td>5267166</td>
      <td>2022-06-01</td>
    </tr>
    <tr>
      <th>163</th>
      <td>4.16</td>
      <td>5240314</td>
      <td>2022-07-01</td>
    </tr>
    <tr>
      <th>164</th>
      <td>4.35</td>
      <td>5240314</td>
      <td>2022-08-01</td>
    </tr>
    <tr>
      <th>165</th>
      <td>4.79</td>
      <td>5240314</td>
      <td>2022-09-01</td>
    </tr>
  </tbody>
</table>
</div>



- KB주택구입잠재력지수



```python
df = api.get_kb_housing_purchase_potential_index()
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역코드</th>
      <th>지역명</th>
      <th>날짜</th>
      <th>잠재력지수</th>
      <th>가구별월소득금액</th>
      <th>연간지출가능주거비용</th>
      <th>구입가능주택가격</th>
      <th>구입가능아파트재고량</th>
      <th>총아파트재고량</th>
      <th>주택담보대출금리</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>154</th>
      <td>4100000000</td>
      <td>경기도</td>
      <td>2022-06-01</td>
      <td>26.046051</td>
      <td>531.096145</td>
      <td>2103.140734</td>
      <td>41013.335036</td>
      <td>68.6035</td>
      <td>263.3931</td>
      <td>3.95</td>
    </tr>
    <tr>
      <th>155</th>
      <td>2800000000</td>
      <td>인천광역시</td>
      <td>2022-06-01</td>
      <td>38.398347</td>
      <td>486.684354</td>
      <td>1927.270040</td>
      <td>37583.681683</td>
      <td>21.9877</td>
      <td>57.2621</td>
      <td>3.95</td>
    </tr>
    <tr>
      <th>156</th>
      <td>1100000000</td>
      <td>서울특별시</td>
      <td>2022-09-01</td>
      <td>2.454326</td>
      <td>571.271954</td>
      <td>2262.236936</td>
      <td>42294.773917</td>
      <td>3.4422</td>
      <td>140.2503</td>
      <td>4.43</td>
    </tr>
    <tr>
      <th>157</th>
      <td>4100000000</td>
      <td>경기도</td>
      <td>2022-09-01</td>
      <td>24.190945</td>
      <td>528.388618</td>
      <td>2092.418927</td>
      <td>39119.857008</td>
      <td>63.7070</td>
      <td>263.3506</td>
      <td>4.43</td>
    </tr>
    <tr>
      <th>158</th>
      <td>2800000000</td>
      <td>인천광역시</td>
      <td>2022-09-01</td>
      <td>35.409012</td>
      <td>484.203238</td>
      <td>1917.444822</td>
      <td>35848.541747</td>
      <td>20.2678</td>
      <td>57.2391</td>
      <td>4.43</td>
    </tr>
  </tbody>
</table>
</div>



- KB아파트주택담보대출 PIR


```python
df = api.get_apartment_mortgage_loan_pir()
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역코드</th>
      <th>지역명</th>
      <th>날짜</th>
      <th>KB아파트PIR</th>
      <th>주택가격</th>
      <th>가구소득</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>172</th>
      <td>4100000000</td>
      <td>경기도</td>
      <td>2022-06-01</td>
      <td>10.818947</td>
      <td>47000.0</td>
      <td>4344.0</td>
    </tr>
    <tr>
      <th>173</th>
      <td>2800000000</td>
      <td>인천광역시</td>
      <td>2022-06-01</td>
      <td>10.844437</td>
      <td>42000.0</td>
      <td>3873.0</td>
    </tr>
    <tr>
      <th>174</th>
      <td>1100000000</td>
      <td>서울특별시</td>
      <td>2022-09-01</td>
      <td>14.537210</td>
      <td>82875.0</td>
      <td>5701.0</td>
    </tr>
    <tr>
      <th>175</th>
      <td>4100000000</td>
      <td>경기도</td>
      <td>2022-09-01</td>
      <td>10.301471</td>
      <td>47000.0</td>
      <td>4562.0</td>
    </tr>
    <tr>
      <th>176</th>
      <td>2800000000</td>
      <td>인천광역시</td>
      <td>2022-09-01</td>
      <td>9.110603</td>
      <td>37500.0</td>
      <td>4116.0</td>
    </tr>
  </tbody>
</table>
</div>



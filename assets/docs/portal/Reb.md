# 한국부동산원 부동산 종합 정보 사용 가이드

[공공데이터포털](https://www.data.go.kr)에서 제공하는 오픈 API 서비스를 이용하려면 인증키가 필요합니다. 인증키를 얻기 위해서는 [공공데이터포털](https://www.data.go.kr)에 회원가입을 하고 원하는 오픈 API 서비스를 신청해야 합니다. 공공데이터포털에서 API를 신청하면 일반적으로 1~2시간 이내에 호출이 가능합니다. 그러나 일부 API의 경우 인증 절차가 24시간 이상 소요될 수 있습니다.

## 한국부동산원 부동산 종합 정보 조회 서비스

- [한국부동산원 오픈 API 서비스 신청 목록](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=&detailKeyword=&publicDataPk=&recmSe=&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=%ED%95%9C%EA%B5%AD%EB%B6%80%EB%8F%99%EC%82%B0%EC%9B%90&orgFilter=%ED%95%9C%EA%B5%AD%EB%B6%80%EB%8F%99%EC%82%B0%EC%9B%90&org=%ED%95%9C%EA%B5%AD%EB%B6%80%EB%8F%99%EC%82%B0%EC%9B%90&orgSearch=&currentPage=1&perPage=40&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode=)


## 서비스 목록

* [청약홈 분양정보 조회 서비스](#청약홈-분양정보-조회-서비스)
* [청약홈 청약접수 경쟁률 조회 서비스](#청약홈-청약접수-경쟁률-조회-서비스)
* [청약홈 청약 신청·당첨자 정보 조회 서비스](#청약홈-청약-신청당첨자-정보-조회-서비스)
* [공동주택 단지 식별정보 조회 서비스](#공동주택-단지-식별정보-조회-서비스)
* [공동주택 실거래가격지수 통계 조회 서비스](#공동주택-실거래가격지수-통계-조회-서비스)
* [전국주택가격동향조사 통계 조회 서비스](#전국주택가격동향조사-통계-조회-서비스)
* [주간아파트동향 조회 서비스](#주간아파트동향-조회-서비스)
* [오피스텔 가격동향조사 통계 조회 서비스](#오피스텔-가격동향조사-통계-조회-서비스)
* [상업용부동산 임대동향 조사 통계 조회 서비스](#상업용부동산-임대동향-조사-통계-조회-서비스)
* [월세가격동향조사 통계 조회 서비스](#월세가격동향조사-통계-조회-서비스)
* [부동산 거래 현황 통계 조회 서비스](#부동산-거래-현황-통계-조회-서비스)
* [전국 지가변동률 조사 통계 조회 서비스](#전국-지가변동률-조사-통계-조회-서비스)
* [매입자 연령대별 부동산거래 조회 서비스](#매입자-연령대별-부동산거래-조회-서비스)
* [녹색건축 인증현황 조회 서비스](#녹색건축-인증현황-조회-서비스)


<div align="center">

</div>

```python
# 한국부동산원 부동산 종합 정보 조회 클래스 임포트하기
from PublicDataReader import Reb

# 공공 데이터 포털 오픈 API 서비스 인증키 입력하기
service_key = "공공 데이터 포털에서 발급받은 서비스 키"

# 데이터 조회 API 인스턴스 정의하기
api = Reb(service_key)
```

## 청약홈 분양정보 조회 서비스

- [오픈 API 신청 페이지](https://www.data.go.kr/data/15098547/openapi.do)


```python
service_name = "분양정보"

category_list = list(api.meta_dict[service_name].keys())
it = iter(category_list)
print(f"{service_name} 카테고리 목록")
print(", ".join(category_list))
```

    분양정보 카테고리 목록
    아파트, 오피스텔, 아파트잔여, 아파트주택형별, 오피스텔주택형별, 아파트잔여주택형별
    


```python
category_name = next(it)
print(f"카테고리명: {category_name}")

df = api.get_data(
    service_name, 
    category_name,
    verbose=True,
    )
df.tail(1)
```

    카테고리명: 아파트
    total_count: 1488, match_count: 1488, cumulative_count: 1488
    




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>BSNS_MBY_NM</th>
      <th>CNSTRCT_ENTRPS_NM</th>
      <th>CNTRCT_CNCLS_BGNDE</th>
      <th>CNTRCT_CNCLS_ENDDE</th>
      <th>GNRL_RNK1_CRSPAREA_RCEPT_PD</th>
      <th>GNRL_RNK1_ETC_AREA_RCPTDE_PD</th>
      <th>GNRL_RNK1_ETC_GG_RCPTDE_PD</th>
      <th>GNRL_RNK2_CRSPAREA_RCEPT_PD</th>
      <th>GNRL_RNK2_ETC_AREA_RCPTDE_PD</th>
      <th>GNRL_RNK2_ETC_GG_RCPTDE_PD</th>
      <th>...</th>
      <th>RCEPT_ENDDE</th>
      <th>RCRIT_PBLANC_DE</th>
      <th>RENT_SECD</th>
      <th>RENT_SECD_NM</th>
      <th>SPECLT_RDN_EARTH_AT</th>
      <th>SPSPLY_RCEPT_BGNDE</th>
      <th>SPSPLY_RCEPT_ENDDE</th>
      <th>SUBSCRPT_AREA_CODE</th>
      <th>SUBSCRPT_AREA_CODE_NM</th>
      <th>TOT_SUPLY_HSHLDCO</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1487</th>
      <td>한국토지주택공사 광주전남지역본부</td>
      <td>None</td>
      <td>2022-09-19</td>
      <td>2022-09-22</td>
      <td>2022-05-23</td>
      <td>2022-05-23</td>
      <td>None</td>
      <td>2022-05-24</td>
      <td>2022-05-24</td>
      <td>None</td>
      <td>...</td>
      <td>2022-05-24</td>
      <td>2022-05-16</td>
      <td>0</td>
      <td>분양주택</td>
      <td>N</td>
      <td>None</td>
      <td>None</td>
      <td>500</td>
      <td>광주</td>
      <td>58</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 41 columns</p>
</div>



## 청약홈 청약접수 경쟁률 조회 서비스

- [오픈 API 신청 페이지](https://www.data.go.kr/data/15098905/openapi.do)

```python
service_name = "청약경쟁률"

category_list = list(api.meta_dict[service_name].keys())
it = iter(category_list)
print(f"{service_name} 카테고리 목록")
print(", ".join(category_list))
```

    청약경쟁률 카테고리 목록
    아파트, 오피스텔, 임대, 취소후재공급, 잔여
    


```python
category_name = next(it)
print(f"카테고리명: {category_name}")

df = api.get_data(
    service_name, 
    category_name,
    verbose=True,
    )
df.tail(1)
```

    카테고리명: 아파트
    total_count: 30042, match_count: 30042, cumulative_count: 10000
    total_count: 30042, match_count: 30042, cumulative_count: 20000
    total_count: 30042, match_count: 30042, cumulative_count: 30000
    total_count: 30042, match_count: 30042, cumulative_count: 30042
    




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AVRG_SCORE</th>
      <th>CMPET_RATE</th>
      <th>HOUSE_MANAGE_NO</th>
      <th>HOUSE_TY</th>
      <th>LWET_SCORE</th>
      <th>MODEL_NO</th>
      <th>PBLANC_NO</th>
      <th>REQ_CNT</th>
      <th>RESIDE_SECD</th>
      <th>RESIDE_SENM</th>
      <th>SUBSCRPT_RANK_CODE</th>
      <th>SUPLY_HSHLDCO</th>
      <th>TOP_SCORE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>30041</th>
      <td>50.0</td>
      <td>28.00</td>
      <td>2022000129</td>
      <td>039.9690A</td>
      <td>48.0</td>
      <td>01</td>
      <td>2022000129</td>
      <td>112</td>
      <td>01</td>
      <td>해당지역</td>
      <td>1</td>
      <td>4</td>
      <td>51.0</td>
    </tr>
  </tbody>
</table>
</div>



## 청약홈 청약 신청·당첨자 정보 조회 서비스

- [오픈 API 신청 페이지](https://www.data.go.kr/data/15110812/openapi.do)


```python
service_name = "청약당첨정보"

category_list = list(api.meta_dict[service_name].keys())
it = iter(category_list)
print(f"{service_name} 카테고리 목록")
print(", ".join(category_list))
```

    청약당첨정보 카테고리 목록
    지역별신청자, 연령별신청자, 지역별당첨자, 연령별당첨자, 지역별경쟁률, 지역별가점제당첨자
    


```python
category_name = next(it)
print(f"카테고리명: {category_name}")

df = api.get_data(
    service_name, 
    category_name,
    verbose=True,
    )
df.tail(1)
```

    카테고리명: 지역별신청자
    total_count: 432, match_count: 432, cumulative_count: 432
    




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AGE_30</th>
      <th>AGE_40</th>
      <th>AGE_50</th>
      <th>AGE_60</th>
      <th>STAT_DE</th>
      <th>SUBSCRPT_AREA_CODE</th>
      <th>SUBSCRPT_AREA_CODE_NM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>431</th>
      <td>7</td>
      <td>5</td>
      <td>2</td>
      <td>3</td>
      <td>202211</td>
      <td>700</td>
      <td>대구</td>
    </tr>
  </tbody>
</table>
</div>



## 공동주택 단지 식별정보 조회 서비스

- [오픈 API 신청 페이지](https://www.data.go.kr/data/15106817/openapi.do)

```python
service_name = "공동주택단지정보"

category_list = list(api.meta_dict[service_name].keys())
it = iter(category_list)
print(f"{service_name} 카테고리 목록")
print(", ".join(category_list))
```

    공동주택단지정보 카테고리 목록
    기본, 동, 단지명
    


```python
category_name = next(it)
print(f"카테고리명: {category_name}")

df = api.get_data(
    service_name, 
    category_name,
    verbose=True,
    )
df.tail(1)
```

    카테고리명: 기본
    total_count: 44064, match_count: 44064, cumulative_count: 10000
    total_count: 44064, match_count: 44064, cumulative_count: 20000
    total_count: 44064, match_count: 44064, cumulative_count: 30000
    total_count: 44064, match_count: 44064, cumulative_count: 40000
    total_count: 44064, match_count: 44064, cumulative_count: 44064
    




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ADRES</th>
      <th>COMPLEX_GB_CD</th>
      <th>COMPLEX_NM1</th>
      <th>COMPLEX_NM2</th>
      <th>COMPLEX_NM3</th>
      <th>COMPLEX_PK</th>
      <th>DONG_CNT</th>
      <th>PNU</th>
      <th>UNIT_CNT</th>
      <th>USEAPR_DT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>44063</th>
      <td>경기도 고양일산동구 중산동 1573</td>
      <td>1</td>
      <td>중산마을6(태영)</td>
      <td>중산마을</td>
      <td>중산마을</td>
      <td>41285100007899</td>
      <td>6</td>
      <td>4128510200115730000</td>
      <td>413</td>
      <td>19950428</td>
    </tr>
  </tbody>
</table>
</div>



## 공동주택 실거래가격지수 통계 조회 서비스

- [오픈 API 신청 페이지](https://www.data.go.kr/data/15099308/openapi.do)

```python
service_name = "공동주택실거래가격지수"

category_list = list(api.meta_dict[service_name].keys())
it = iter(category_list)
print(f"{service_name} 카테고리 목록")
print(", ".join(category_list))
```

    공동주택실거래가격지수 카테고리 목록
    지역별, 규모별
    


```python
category_name = next(it)
print(f"카테고리명: {category_name}")

df = api.get_data(
    service_name, 
    category_name,
    verbose=True,
    )
df.tail(1)
```

    카테고리명: 지역별
    total_count: 18892, match_count: 12306, cumulative_count: 10000
    total_count: 18892, match_count: 12306, cumulative_count: 12306
    




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>APT_TYPE</th>
      <th>CONTRACT_TYPE</th>
      <th>INDICES</th>
      <th>LEVEL_NO</th>
      <th>REGION_CD</th>
      <th>REGION_NM</th>
      <th>RESEARCH_DATE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12305</th>
      <td>1</td>
      <td>1</td>
      <td>99.012758</td>
      <td>0</td>
      <td>A2001</td>
      <td>지방</td>
      <td>201707</td>
    </tr>
  </tbody>
</table>
</div>



## 전국주택가격동향조사 통계 조회 서비스

- [오픈 API 신청 페이지](https://www.data.go.kr/data/15099307/openapi.do)

```python
service_name = "주택"

category_list = list(api.meta_dict[service_name].keys())
it = iter(category_list)
print(f"{service_name} 카테고리 목록")
print(", ".join(category_list))
```

    주택 카테고리 목록
    지역별, 5분위배율, 전세가격비율, 계절조정, 연령별, 규모별, 매매수급, 매매거래, 전세수급, 전세가격, 가격별
    


```python
category_name = next(it)
print(f"카테고리명: {category_name}")

df = api.get_data(
    service_name, 
    category_name,
    verbose=True,
    )
df.tail(1)
```

    카테고리명: 지역별
    total_count: 496912, match_count: 496912, cumulative_count: 10000
    total_count: 496912, match_count: 496912, cumulative_count: 20000
    total_count: 496912, match_count: 496912, cumulative_count: 30000
    total_count: 496912, match_count: 496912, cumulative_count: 40000
    total_count: 496912, match_count: 496912, cumulative_count: 50000
    total_count: 496912, match_count: 496912, cumulative_count: 60000
    total_count: 496912, match_count: 496912, cumulative_count: 70000
    total_count: 496912, match_count: 496912, cumulative_count: 80000
    total_count: 496912, match_count: 496912, cumulative_count: 90000
    total_count: 496912, match_count: 496912, cumulative_count: 100000
    total_count: 496912, match_count: 496912, cumulative_count: 110000
    total_count: 496912, match_count: 496912, cumulative_count: 120000
    total_count: 496912, match_count: 496912, cumulative_count: 130000
    total_count: 496912, match_count: 496912, cumulative_count: 140000
    total_count: 496912, match_count: 496912, cumulative_count: 150000
    total_count: 496912, match_count: 496912, cumulative_count: 160000
    total_count: 496912, match_count: 496912, cumulative_count: 170000
    total_count: 496912, match_count: 496912, cumulative_count: 180000
    total_count: 496912, match_count: 496912, cumulative_count: 190000
    total_count: 496912, match_count: 496912, cumulative_count: 200000
    total_count: 496912, match_count: 496912, cumulative_count: 210000
    total_count: 496912, match_count: 496912, cumulative_count: 220000
    total_count: 496912, match_count: 496912, cumulative_count: 230000
    total_count: 496912, match_count: 496912, cumulative_count: 240000
    total_count: 496912, match_count: 496912, cumulative_count: 250000
    total_count: 496912, match_count: 496912, cumulative_count: 260000
    total_count: 496912, match_count: 496912, cumulative_count: 270000
    total_count: 496912, match_count: 496912, cumulative_count: 280000
    total_count: 496912, match_count: 496912, cumulative_count: 290000
    total_count: 496912, match_count: 496912, cumulative_count: 300000
    total_count: 496912, match_count: 496912, cumulative_count: 310000
    total_count: 496912, match_count: 496912, cumulative_count: 320000
    total_count: 496912, match_count: 496912, cumulative_count: 330000
    total_count: 496912, match_count: 496912, cumulative_count: 340000
    total_count: 496912, match_count: 496912, cumulative_count: 350000
    total_count: 496912, match_count: 496912, cumulative_count: 360000
    total_count: 496912, match_count: 496912, cumulative_count: 370000
    total_count: 496912, match_count: 496912, cumulative_count: 380000
    total_count: 496912, match_count: 496912, cumulative_count: 390000
    total_count: 496912, match_count: 496912, cumulative_count: 400000
    total_count: 496912, match_count: 496912, cumulative_count: 410000
    total_count: 496912, match_count: 496912, cumulative_count: 420000
    total_count: 496912, match_count: 496912, cumulative_count: 430000
    total_count: 496912, match_count: 496912, cumulative_count: 440000
    total_count: 496912, match_count: 496912, cumulative_count: 450000
    total_count: 496912, match_count: 496912, cumulative_count: 460000
    total_count: 496912, match_count: 496912, cumulative_count: 470000
    total_count: 496912, match_count: 496912, cumulative_count: 480000
    total_count: 496912, match_count: 496912, cumulative_count: 490000
    total_count: 496912, match_count: 496912, cumulative_count: 496912
    




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>APT_TYPE</th>
      <th>LEVEL_NO</th>
      <th>PRICE</th>
      <th>PRICE_GBN</th>
      <th>REGION_CD</th>
      <th>REGION_NM</th>
      <th>RESEARCH_DATE</th>
      <th>TR_GBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>496911</th>
      <td>1</td>
      <td>2</td>
      <td>2974.718909</td>
      <td>MU</td>
      <td>26410</td>
      <td>금정구</td>
      <td>202212</td>
      <td>D</td>
    </tr>
  </tbody>
</table>
</div>



## 주간아파트동향 조회 서비스

- [오픈 API 신청 페이지](https://www.data.go.kr/data/15099305/openapi.do)

```python
service_name = "주간아파트"

category_list = list(api.meta_dict[service_name].keys())
it = iter(category_list)
print(f"{service_name} 카테고리 목록")
print(", ".join(category_list))
```

    주간아파트 카테고리 목록
    연령별거래유형별, 규모별거래유형별, 전세수급, 매매수급, 지역별거래유형별
    


```python
category_name = next(it)
print(f"카테고리명: {category_name}")

df = api.get_data(
    service_name, 
    category_name,
    verbose=True,
    )
df.tail(1)
```

    카테고리명: 연령별거래유형별
    total_count: 228370, match_count: 228370, cumulative_count: 10000
    total_count: 228370, match_count: 228370, cumulative_count: 20000
    total_count: 228370, match_count: 228370, cumulative_count: 30000
    total_count: 228370, match_count: 228370, cumulative_count: 40000
    total_count: 228370, match_count: 228370, cumulative_count: 50000
    total_count: 228370, match_count: 228370, cumulative_count: 60000
    total_count: 228370, match_count: 228370, cumulative_count: 70000
    total_count: 228370, match_count: 228370, cumulative_count: 80000
    total_count: 228370, match_count: 228370, cumulative_count: 90000
    total_count: 228370, match_count: 228370, cumulative_count: 100000
    total_count: 228370, match_count: 228370, cumulative_count: 110000
    total_count: 228370, match_count: 228370, cumulative_count: 120000
    total_count: 228370, match_count: 228370, cumulative_count: 130000
    total_count: 228370, match_count: 228370, cumulative_count: 140000
    total_count: 228370, match_count: 228370, cumulative_count: 150000
    total_count: 228370, match_count: 228370, cumulative_count: 160000
    total_count: 228370, match_count: 228370, cumulative_count: 170000
    total_count: 228370, match_count: 228370, cumulative_count: 180000
    total_count: 228370, match_count: 228370, cumulative_count: 190000
    total_count: 228370, match_count: 228370, cumulative_count: 200000
    total_count: 228370, match_count: 228370, cumulative_count: 210000
    total_count: 228370, match_count: 228370, cumulative_count: 220000
    total_count: 228370, match_count: 228370, cumulative_count: 228370
    




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AGE_GBN</th>
      <th>INDICES</th>
      <th>LEVEL_NO</th>
      <th>REGION_CD</th>
      <th>REGION_NM</th>
      <th>RESEARCH_DATE</th>
      <th>TR_GBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>228369</th>
      <td>15</td>
      <td>102.893041</td>
      <td>0</td>
      <td>43000</td>
      <td>충북</td>
      <td>20120507</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>



## 오피스텔 가격동향조사 통계 조회 서비스

- [오픈 API 신청 페이지](https://www.data.go.kr/data/15099816/openapi.do)

```python
service_name = "오피스텔"

category_list = list(api.meta_dict[service_name].keys())
it = iter(category_list)
print(f"{service_name} 카테고리 목록")
print(", ".join(category_list))
```

    오피스텔 카테고리 목록
    지역별가격지수, 규모별가격지수, 지역별가격, 규모별가격, 지역별전세가격비율, 규모별전세가격비율, 지역별월세보증금비율, 규모별월세보증금비율
    


```python
category_name = next(it)
print(f"카테고리명: {category_name}")

df = api.get_data(
    service_name, 
    category_name,
    verbose=True,
    )
df.tail(1)
```

    카테고리명: 지역별가격지수
    total_count: 3060, match_count: 3060, cumulative_count: 3060
    




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>INDICES</th>
      <th>LEVEL_NO</th>
      <th>REGION_CD</th>
      <th>REGION_NM</th>
      <th>RESEARCH_DATE</th>
      <th>TR_GBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3059</th>
      <td>99.880429</td>
      <td>0</td>
      <td>A2001</td>
      <td>지방</td>
      <td>201801</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>



## 상업용부동산 임대동향 조사 통계 조회 서비스

- [오픈 API 신청 페이지](https://www.data.go.kr/data/15099345/openapi.do)

```python
service_name = "상업용임대"

category_list = list(api.meta_dict[service_name].keys())
it = iter(category_list)
print(f"{service_name} 카테고리 목록")
print(", ".join(category_list))
```

    상업용임대 카테고리 목록
    지역별전환율, 지역별임대가격지수, 지역별분기소득수익률, 지역별분기자본수익률, 지역별분기투자수익률, 지역별기타수입구성비, 순영업소득, 지역별영업경비구성비, 지역별임대수입구성비, 지역별임대료, 층별임대료, 층별효용비율, 지역별공실률, 지역별연간소득수익률, 지역별연간자본수익률, 지역별연간투자수익률
    


```python
category_name = next(it)
print(f"카테고리명: {category_name}")

df = api.get_data(
    service_name, 
    category_name,
    verbose=True,
    )
df.tail(1)
```

    카테고리명: 지역별전환율
    total_count: 23659, match_count: 23659, cumulative_count: 10000
    total_count: 23659, match_count: 23659, cumulative_count: 20000
    total_count: 23659, match_count: 23659, cumulative_count: 23659
    




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>BULD_GBN</th>
      <th>CONV_RATE</th>
      <th>LEVEL_NO_OUT</th>
      <th>METRO_NM</th>
      <th>REGION_CD</th>
      <th>REGION_NM</th>
      <th>RESEARCH_DATE</th>
      <th>SECTION_NM</th>
      <th>SIDO_NM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>23658</th>
      <td>3</td>
      <td>5.9</td>
      <td>3</td>
      <td>None</td>
      <td>4800N245</td>
      <td>창원의창구청</td>
      <td>202202</td>
      <td>창원의창구청</td>
      <td>경남</td>
    </tr>
  </tbody>
</table>
</div>



## 월세가격동향조사 통계 조회 서비스

- [오픈 API 신청 페이지](https://www.data.go.kr/data/15099310/openapi.do)

```python
service_name = "월세가격"

category_list = list(api.meta_dict[service_name].keys())
it = iter(category_list)
print(f"{service_name} 카테고리 목록")
print(", ".join(category_list))
```

    월세가격 카테고리 목록
    지역별전월세전환율, 규모별전월세전환율, 규모별월세가격지수, 지역별수급동향, 지역별거래동향, 지역별주택유형별월세가격지수
    


```python
category_name = next(it)
print(f"카테고리명: {category_name}")

df = api.get_data(
    service_name, 
    category_name,
    verbose=True,
    )
df.tail(1)
```

    카테고리명: 지역별전월세전환율
    total_count: 37466, match_count: 37466, cumulative_count: 10000
    total_count: 37466, match_count: 37466, cumulative_count: 20000
    total_count: 37466, match_count: 37466, cumulative_count: 30000
    total_count: 37466, match_count: 37466, cumulative_count: 37466
    




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>APT_TYPE</th>
      <th>LEVEL_NO</th>
      <th>RATE</th>
      <th>REGION_CD</th>
      <th>REGION_NM</th>
      <th>RESEARCH_DATE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>37465</th>
      <td>35</td>
      <td>0</td>
      <td>10.690207</td>
      <td>43000</td>
      <td>충북</td>
      <td>202206</td>
    </tr>
  </tbody>
</table>
</div>



## 부동산 거래 현황 통계 조회 서비스

- [오픈 API 신청 페이지](https://www.data.go.kr/data/15099361/openapi.do)

```python
service_name = "부동산거래"

category_list = list(api.meta_dict[service_name].keys())
it = iter(category_list)
print(f"{service_name} 카테고리 목록")
print(", ".join(category_list))
```

    부동산거래 카테고리 목록
    거래면적, 거주지별거래면적, 거래건수, 거주지별거래건수, 건물유형별거래면적, 거래주체별거래건수, 외국인거래면적, 신탁거래면적, 외국인거래건수, 신탁거래건수, 지목별거래면적, 지목별거래건수, 토지거래허가처리별거래면적, 토지거래허가처리별거래건수, 거래원인별거래면적, 거래원인별거래건수, 거래규모별거래면적, 거래규모별거래건수, 용도지역별거래면적, 용도지역별거래건수, 건물유형별거래건수, 거래주체별거래면적, 연도별거래면적, 연도별거래건수, 연도별거주지별거래면적, 연도별거주지별거래건수, 연도별건물유형별거래면적, 연도별건물유형별거래건수, 연도별거래주체별거래면적, 연도별거래주체별거래건수, 연도별외국인거래면적, 연도별외국인거래건수, 연도별신탁거래면적, 연도별신탁거래건수, 연도별지목별거래면적, 연도별지목별거래건수, 연도별토지거래허가처리별거래면적, 연도별토지거래허가처리별거래건수, 연도별거래원인별거래면적, 연도별거래원인별거래건수, 연도별거래규모별거래면적, 연도별거래규모별거래건수, 연도별용도지역별거래면적, 연도별용도지역별거래건수
    


```python
category_name = next(it)
print(f"카테고리명: {category_name}")

df = api.get_data(
    service_name, 
    category_name,
    verbose=True,
    )
df.tail(1)
```

    카테고리명: 거래면적
    total_count: 407067, match_count: 407067, cumulative_count: 10000
    total_count: 407067, match_count: 407067, cumulative_count: 20000
    total_count: 407067, match_count: 407067, cumulative_count: 30000
    total_count: 407067, match_count: 407067, cumulative_count: 40000
    total_count: 407067, match_count: 407067, cumulative_count: 50000
    total_count: 407067, match_count: 407067, cumulative_count: 60000
    total_count: 407067, match_count: 407067, cumulative_count: 70000
    total_count: 407067, match_count: 407067, cumulative_count: 80000
    total_count: 407067, match_count: 407067, cumulative_count: 90000
    total_count: 407067, match_count: 407067, cumulative_count: 100000
    total_count: 407067, match_count: 407067, cumulative_count: 110000
    total_count: 407067, match_count: 407067, cumulative_count: 120000
    total_count: 407067, match_count: 407067, cumulative_count: 130000
    total_count: 407067, match_count: 407067, cumulative_count: 140000
    total_count: 407067, match_count: 407067, cumulative_count: 150000
    total_count: 407067, match_count: 407067, cumulative_count: 160000
    total_count: 407067, match_count: 407067, cumulative_count: 170000
    total_count: 407067, match_count: 407067, cumulative_count: 180000
    total_count: 407067, match_count: 407067, cumulative_count: 190000
    total_count: 407067, match_count: 407067, cumulative_count: 200000
    total_count: 407067, match_count: 407067, cumulative_count: 210000
    total_count: 407067, match_count: 407067, cumulative_count: 220000
    total_count: 407067, match_count: 407067, cumulative_count: 230000
    total_count: 407067, match_count: 407067, cumulative_count: 240000
    total_count: 407067, match_count: 407067, cumulative_count: 250000
    total_count: 407067, match_count: 407067, cumulative_count: 260000
    total_count: 407067, match_count: 407067, cumulative_count: 270000
    total_count: 407067, match_count: 407067, cumulative_count: 280000
    total_count: 407067, match_count: 407067, cumulative_count: 290000
    total_count: 407067, match_count: 407067, cumulative_count: 300000
    total_count: 407067, match_count: 407067, cumulative_count: 310000
    total_count: 407067, match_count: 407067, cumulative_count: 320000
    total_count: 407067, match_count: 407067, cumulative_count: 330000
    total_count: 407067, match_count: 407067, cumulative_count: 340000
    total_count: 407067, match_count: 407067, cumulative_count: 350000
    total_count: 407067, match_count: 407067, cumulative_count: 360000
    total_count: 407067, match_count: 407067, cumulative_count: 370000
    total_count: 407067, match_count: 407067, cumulative_count: 380000
    total_count: 407067, match_count: 407067, cumulative_count: 390000
    total_count: 407067, match_count: 407067, cumulative_count: 400000
    total_count: 407067, match_count: 407067, cumulative_count: 407067
    




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ALL_AREA</th>
      <th>DEAL_OBJ</th>
      <th>LEVEL_NO</th>
      <th>REGION_CD</th>
      <th>REGION_NM</th>
      <th>RESEARCH_DATE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>407066</th>
      <td>54877.513296</td>
      <td>01</td>
      <td>1</td>
      <td>28200</td>
      <td>남동구</td>
      <td>202210</td>
    </tr>
  </tbody>
</table>
</div>



## 전국 지가변동률 조사 통계 조회 서비스

- [오픈 API 신청 페이지](https://www.data.go.kr/data/15098962/openapi.do)

```python
service_name = "지가변동률"

category_list = list(api.meta_dict[service_name].keys())
it = iter(category_list)
print(f"{service_name} 카테고리 목록")
print(", ".join(category_list))
```

    지가변동률 카테고리 목록
    연도별지역별, 이용상황별, 월별지역별, 용도지역별, 보조지수
    


```python
category_name = next(it)
print(f"카테고리명: {category_name}")

df = api.get_data(
    service_name, 
    category_name,
    verbose=True,
    )
df.tail(1)
```

    카테고리명: 연도별지역별
    total_count: 8664, match_count: 8664, cumulative_count: 8664
    




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>INDICES_MEAN</th>
      <th>LEVEL_NO</th>
      <th>REGION_CD</th>
      <th>REGION_NM</th>
      <th>RESEARCH_YEAR</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8663</th>
      <td>73.324325</td>
      <td>1</td>
      <td>29140</td>
      <td>서구</td>
      <td>2013</td>
    </tr>
  </tbody>
</table>
</div>



## 매입자 연령대별 부동산거래 조회 서비스 

- [오픈 API 신청 페이지](https://www.data.go.kr/data/15099309/openapi.do)

```python
service_name = "연령대별부동산거래"

category_list = list(api.meta_dict[service_name].keys())
it = iter(category_list)
print(f"{service_name} 카테고리 목록")
print(", ".join(category_list))
```

    연령대별부동산거래 카테고리 목록
    거래면적, 거래건수
    


```python
category_name = next(it)
print(f"카테고리명: {category_name}")

df = api.get_data(
    service_name, 
    category_name,
    verbose=True,
    )
df.tail(1)
```

    카테고리명: 거래면적
    total_count: 26194, match_count: 26194, cumulative_count: 10000
    total_count: 26194, match_count: 26194, cumulative_count: 20000
    total_count: 26194, match_count: 26194, cumulative_count: 26194
    




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AGE01_AREA</th>
      <th>AGE02_AREA</th>
      <th>AGE03_AREA</th>
      <th>AGE04_AREA</th>
      <th>AGE05_AREA</th>
      <th>AGE06_AREA</th>
      <th>AGE07_AREA</th>
      <th>ALL_AREA</th>
      <th>DEAL_OBJ</th>
      <th>REGION_CD</th>
      <th>REGION_NM</th>
      <th>RESEARCH_DATE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>26193</th>
      <td>194.3929</td>
      <td>1436.5566</td>
      <td>855.4802</td>
      <td>781.2606</td>
      <td>116.41</td>
      <td>134.896</td>
      <td>0.0</td>
      <td>3518.9963</td>
      <td>07</td>
      <td>41273</td>
      <td>단원구</td>
      <td>202207</td>
    </tr>
  </tbody>
</table>
</div>



## 녹색건축 인증현황 조회 서비스

- [오픈 API 신청 페이지](https://www.data.go.kr/data/15099344/openapi.do)

```python
service_name = "녹색건축인증현황"

category_list = list(api.meta_dict[service_name].keys())
it = iter(category_list)
print(f"{service_name} 카테고리 목록")
print(", ".join(category_list))
```

    녹색건축인증현황 카테고리 목록
    녹색건축
    


```python
category_name = next(it)
print(f"카테고리명: {category_name}")

df = api.get_data(
    service_name, 
    category_name,
    verbose=True,
    )
df.tail(1)
```

    카테고리명: 녹색건축
    total_count: 3364, match_count: 3364, cumulative_count: 3364
    




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ADDR</th>
      <th>BUILDING_NM</th>
      <th>CERTIFY_DATE</th>
      <th>CERTIFY_GRADE</th>
      <th>CERTIFY_GUBUN</th>
      <th>CERTIFY_NUM</th>
      <th>CERTIFY_STD</th>
      <th>CERTIFY_SUBJECT_GROUP</th>
      <th>REGION_NM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3363</th>
      <td>경기도 안산시 상록구 각골로 75(본오동)</td>
      <td>안산 본오2동 공공복합청사</td>
      <td>2022/08/25</td>
      <td>일반(그린4등급)</td>
      <td>예비인증</td>
      <td>G-SEED-P-2022-0962-5</td>
      <td>녹색</td>
      <td>업무용건축물,일반건축물</td>
      <td>경기도</td>
    </tr>
  </tbody>
</table>
</div>



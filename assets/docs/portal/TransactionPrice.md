# 국토교통부 부동산 실거래가 사용 가이드

[공공데이터포털](https://www.data.go.kr)에서 제공하는 오픈 API 서비스를 이용하려면 인증키가 필요합니다. 인증키를 얻기 위해서는 [공공데이터포털](https://www.data.go.kr)에 회원가입을 하고 원하는 오픈 API 서비스를 신청해야 합니다. 공공데이터포털에서 API를 신청하면 일반적으로 1~2시간 이내에 호출이 가능합니다. 그러나 일부 API의 경우 인증 절차가 24시간 이상 소요될 수 있습니다.

## 국토교통부 실거래가 정보 조회 서비스

<div align="center">

| **서비스명**                          | **부동산 유형** | **거래 유형** |
| ------------------------------------- | ------------ | ------------ |
| [아파트매매 실거래 상세 자료 조회](https://www.data.go.kr/data/15057511/openapi.do)      | 아파트       | 매매         |
| [아파트 전월세 자료 조회](https://www.data.go.kr/data/15058017/openapi.do)               | 아파트       | 전월세       |
| [아파트 분양권전매 신고 자료 조회](https://www.data.go.kr/data/15056782/openapi.do)      | 분양입주권   | 매매         |
| [오피스텔 매매 신고 조회](https://www.data.go.kr/data/15058452/openapi.do)               | 오피스텔     | 매매         |
| [오피스텔 전월세 신고 조회](https://www.data.go.kr/data/15059249/openapi.do)             | 오피스텔     | 전월세       |
| [연립다세대 매매 실거래자료 조회](https://www.data.go.kr/data/15058038/openapi.do)       | 연립다세대   | 매매         |
| [연립다세대 전월세 실거래자료 조회](https://www.data.go.kr/data/15058016/openapi.do)     | 연립다세대   | 전월세       |
| [단독/다가구 매매 실거래 조회](https://www.data.go.kr/data/15058022/openapi.do)          | 단독다가구   | 매매         |
| [단독/다가구 전월세 자료 조회](https://www.data.go.kr/data/15058352/openapi.do)          | 단독다가구   | 전월세       |
| [토지 매매 신고 조회](https://www.data.go.kr/data/15056649/openapi.do)                   | 토지         | 매매         |
| [상업업무용 부동산 매매 신고 자료 조회](https://www.data.go.kr/data/15057267/openapi.do) | 상업업무용   | 매매         |
| [공장 및 창고 등 부동산 매매 신고 자료 조회](https://www.data.go.kr/data/15100574/openapi.do) | 공장창고등   | 매매         |

</div>


## 입력 명세

* [아파트매매 실거래 상세 자료 조회 서비스](#아파트매매-실거래-상세-자료-조회-서비스)
* [아파트 전월세 자료 조회 서비스](#아파트-전월세-자료-조회-서비스)
* [아파트 분양권전매 신고 자료 조회 서비스](#아파트-분양권전매-신고-자료-조회-서비스)
* [오피스텔 매매 신고 조회 서비스](#오피스텔-매매-신고-조회-서비스)
* [오피스텔 전월세 신고 조회 서비스](#오피스텔-전월세-신고-조회-서비스)
* [연립다세대 매매 실거래자료 조회 서비스](#연립다세대-매매-실거래자료-조회-서비스)
* [연립다세대 전월세 실거래자료 조회 서비스](#연립다세대-전월세-실거래자료-조회-서비스)
* [단독/다가구 매매 실거래 조회 서비스](#단독다가구-매매-실거래-조회-서비스)
* [단독/다가구 전월세 자료 조회 서비스](#단독다가구-전월세-자료-조회-서비스)
* [토지 매매 신고 조회 서비스](#토지-매매-신고-조회-서비스)
* [상업업무용 부동산 매매 신고 자료 조회 서비스](#상업업무용-부동산-매매-신고-자료-조회-서비스)
* [공장 및 창고 등 부동산 매매 신고 자료 조회 서비스](#공장-및-창고-등-부동산-매매-신고-자료-조회-서비스)

<div align="center">

| 이름             | 설명                                                                                                                               | 데이터 타입   | 샘플 데이터   | 항목구분    |
|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------|:--------------|:--------------|:------------|
| property_type    | 부동산 유형<br>(아파트, 오피스텔, 단독다가구, 연립다세대, 토지, 분양입주권, 공장창고등)                                            | String        | 아파트        | 필수        |
| trade_type       | 거래 유형<br>(매매, 전월세)                                                                                                        | String        | 매매          | 필수        |
| sigungu_code     | 시군구의 5자리 지역코드<br>(서울 서초구: 11650, 경기 성남 분당구: 41135)                                                           | String        | 11650         | 필수        |
| year_month       | 조회 년월 (단일 월 조회 시 필수)<br>(2023년 1월: 202301)<br>※ start_year_month와 end_year_month 모두 입력 시 기간 내 조회가 실행됨 | String        | 202301        | 조건부 필수 |
| start_year_month | 조회 시작 년월 (기간 내 조회 시 필수)<br>(2022년 1월 202201)                                                                       | String        | 202201        | 조건부 필수 |
| end_year_month   | 조회 종료 년월 (기간 내 조회 시 필수)<br>(2022년 12월: 202212)                                                                     | String        | 202212        | 조건부 필수 |
| verbose          | 데이터 조회 진행 상황 메시지 출력 여부<br>(출력: True, 미출력: False)<br>※ 기본값: False                                           | Boolean       | True          | 선택        |

</div>


## 아파트매매 실거래 상세 자료 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

<br>


```python
from PublicDataReader import TransactionPrice

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = TransactionPrice(service_key)

# 단일 월 조회
df = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11650",
    year_month="202212",
)

# 기간 내 조회
df = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="11650",
    start_year_month="202201",
    end_year_month="202212",
)

df.tail()
```


<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역코드</th>
      <th>도로명</th>
      <th>법정동</th>
      <th>지번</th>
      <th>아파트</th>
      <th>건축년도</th>
      <th>층</th>
      <th>전용면적</th>
      <th>년</th>
      <th>월</th>
      <th>...</th>
      <th>법정동본번코드</th>
      <th>법정동부번코드</th>
      <th>법정동시군구코드</th>
      <th>법정동읍면동코드</th>
      <th>법정동지번코드</th>
      <th>일련번호</th>
      <th>거래유형</th>
      <th>중개사소재지</th>
      <th>해제사유발생일</th>
      <th>해제여부</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>674</th>
      <td>11650</td>
      <td>남부순환로317길</td>
      <td>서초동</td>
      <td>1465-7</td>
      <td>서초코아</td>
      <td>2003</td>
      <td>5</td>
      <td>70.13</td>
      <td>2022</td>
      <td>12</td>
      <td>...</td>
      <td>1465</td>
      <td>0007</td>
      <td>11650</td>
      <td>10800</td>
      <td>1</td>
      <td>11650-555</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>675</th>
      <td>11650</td>
      <td>NaN</td>
      <td>서초동</td>
      <td>1335</td>
      <td>서초그랑자이</td>
      <td>2021</td>
      <td>21</td>
      <td>84.51</td>
      <td>2022</td>
      <td>12</td>
      <td>...</td>
      <td>1335</td>
      <td>0000</td>
      <td>11650</td>
      <td>10800</td>
      <td>1</td>
      <td>11650-4969</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>676</th>
      <td>11650</td>
      <td>효령로45길</td>
      <td>서초동</td>
      <td>1527-13</td>
      <td>로얄파크에이</td>
      <td>2005</td>
      <td>4</td>
      <td>146.56</td>
      <td>2022</td>
      <td>12</td>
      <td>...</td>
      <td>1527</td>
      <td>0013</td>
      <td>11650</td>
      <td>10800</td>
      <td>1</td>
      <td>11650-773</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>677</th>
      <td>11650</td>
      <td>서초대로65길</td>
      <td>서초동</td>
      <td>1682</td>
      <td>서초래미안</td>
      <td>2003</td>
      <td>12</td>
      <td>84.97</td>
      <td>2022</td>
      <td>12</td>
      <td>...</td>
      <td>1682</td>
      <td>0000</td>
      <td>11650</td>
      <td>10800</td>
      <td>1</td>
      <td>11650-523</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>678</th>
      <td>11650</td>
      <td>서운로</td>
      <td>서초동</td>
      <td>1312-3</td>
      <td>롯데캐슬클래식</td>
      <td>2006</td>
      <td>23</td>
      <td>84.98</td>
      <td>2022</td>
      <td>12</td>
      <td>...</td>
      <td>1312</td>
      <td>0003</td>
      <td>11650</td>
      <td>10800</td>
      <td>1</td>
      <td>11650-3300</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 28 columns</p>
</div>


## 아파트 전월세 자료 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import TransactionPrice

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = TransactionPrice(service_key)

# 단일 월 조회
df = api.get_data(
    property_type="아파트",
    trade_type="전월세",
    sigungu_code="11650",
    year_month="202212",
)

# 기간 내 조회
df = api.get_data(
    property_type="아파트",
    trade_type="전월세",
    sigungu_code="11650",
    start_year_month="202201",
    end_year_month="202212",
)

df.tail()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역코드</th>
      <th>법정동</th>
      <th>지번</th>
      <th>아파트</th>
      <th>건축년도</th>
      <th>층</th>
      <th>전용면적</th>
      <th>년</th>
      <th>월</th>
      <th>일</th>
      <th>보증금액</th>
      <th>월세금액</th>
      <th>계약구분</th>
      <th>계약기간</th>
      <th>갱신요구권사용</th>
      <th>종전계약보증금</th>
      <th>종전계약월세</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13859</th>
      <td>11650</td>
      <td>신원동</td>
      <td>NaN</td>
      <td>힐스테이트 서초 젠트리스</td>
      <td>2014</td>
      <td>3</td>
      <td>84.95</td>
      <td>2022</td>
      <td>12</td>
      <td>24</td>
      <td>70000</td>
      <td>0</td>
      <td>갱신</td>
      <td>22.12~24.12</td>
      <td>None</td>
      <td>35000</td>
      <td>100</td>
    </tr>
    <tr>
      <th>13860</th>
      <td>11650</td>
      <td>신원동</td>
      <td>690</td>
      <td>서초포레스타5단지</td>
      <td>2014</td>
      <td>16</td>
      <td>84.40</td>
      <td>2022</td>
      <td>12</td>
      <td>26</td>
      <td>90000</td>
      <td>0</td>
      <td>신규</td>
      <td>23.02~25.02</td>
      <td>None</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>13861</th>
      <td>11650</td>
      <td>신원동</td>
      <td>NaN</td>
      <td>서초 선포레</td>
      <td>2015</td>
      <td>2</td>
      <td>29.26</td>
      <td>2022</td>
      <td>12</td>
      <td>29</td>
      <td>10493</td>
      <td>12</td>
      <td>신규</td>
      <td>None</td>
      <td>None</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>13862</th>
      <td>11650</td>
      <td>신원동</td>
      <td>615</td>
      <td>서초포레스타7단지</td>
      <td>2013</td>
      <td>7</td>
      <td>59.94</td>
      <td>2022</td>
      <td>12</td>
      <td>31</td>
      <td>10000</td>
      <td>210</td>
      <td>신규</td>
      <td>23.01~25.01</td>
      <td>None</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>13863</th>
      <td>11650</td>
      <td>신원동</td>
      <td>NaN</td>
      <td>힐스테이트 서초 젠트리스</td>
      <td>2014</td>
      <td>7</td>
      <td>84.95</td>
      <td>2022</td>
      <td>12</td>
      <td>31</td>
      <td>30000</td>
      <td>190</td>
      <td>신규</td>
      <td>23.03~25.03</td>
      <td>None</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
    </tr>
  </tbody>
</table>
</div>


## 아파트 분양권전매 신고 자료 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import TransactionPrice

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = TransactionPrice(service_key)

# 단일 월 조회
df = api.get_data(
    property_type="분양입주권",
    trade_type="매매",
    sigungu_code="11650",
    year_month="202212",
)

# 기간 내 조회
df = api.get_data(
    property_type="분양입주권",
    trade_type="매매",
    sigungu_code="11650",
    start_year_month="202201",
    end_year_month="202212",
)

df.tail()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역코드</th>
      <th>시군구</th>
      <th>법정동</th>
      <th>지번</th>
      <th>단지</th>
      <th>층</th>
      <th>전용면적</th>
      <th>구분</th>
      <th>년</th>
      <th>월</th>
      <th>일</th>
      <th>거래금액</th>
      <th>거래유형</th>
      <th>중개사소재지</th>
      <th>해제사유발생일</th>
      <th>해제여부</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11650</td>
      <td>서초구</td>
      <td>반포동</td>
      <td>1-1</td>
      <td>래미안 원베일리</td>
      <td>18</td>
      <td>84.9800</td>
      <td>입</td>
      <td>2022</td>
      <td>3</td>
      <td>2</td>
      <td>387407</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11650</td>
      <td>서초구</td>
      <td>잠원동</td>
      <td>27-2</td>
      <td>멀버리힐스</td>
      <td>13</td>
      <td>30.7260</td>
      <td>NaN</td>
      <td>2022</td>
      <td>9</td>
      <td>23</td>
      <td>86500</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11650</td>
      <td>서초구</td>
      <td>잠원동</td>
      <td>27-2</td>
      <td>멀버리힐스</td>
      <td>12</td>
      <td>36.5219</td>
      <td>NaN</td>
      <td>2022</td>
      <td>10</td>
      <td>6</td>
      <td>85500</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11650</td>
      <td>서초구</td>
      <td>반포동</td>
      <td>1-1</td>
      <td>래미안 원베일리</td>
      <td>9</td>
      <td>84.9500</td>
      <td>입</td>
      <td>2022</td>
      <td>11</td>
      <td>23</td>
      <td>300340</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11650</td>
      <td>서초구</td>
      <td>양재동</td>
      <td>11-11</td>
      <td>강남월드메르디앙프레스티지</td>
      <td>6</td>
      <td>43.2800</td>
      <td>NaN</td>
      <td>2022</td>
      <td>12</td>
      <td>19</td>
      <td>118790</td>
      <td>직거래</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>


## 오피스텔 매매 신고 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import TransactionPrice

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = TransactionPrice(service_key)

# 단일 월 조회
df = api.get_data(
    property_type="오피스텔",
    trade_type="매매",
    sigungu_code="11650",
    year_month="202212",
)

# 기간 내 조회
df = api.get_data(
    property_type="오피스텔",
    trade_type="매매",
    sigungu_code="11650",
    start_year_month="202201",
    end_year_month="202212",
)

df.tail()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역코드</th>
      <th>시군구</th>
      <th>법정동</th>
      <th>지번</th>
      <th>단지</th>
      <th>건축년도</th>
      <th>층</th>
      <th>전용면적</th>
      <th>년</th>
      <th>월</th>
      <th>일</th>
      <th>거래금액</th>
      <th>거래유형</th>
      <th>중개사소재지</th>
      <th>해제사유발생일</th>
      <th>해제여부</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>776</th>
      <td>11650</td>
      <td>서초구</td>
      <td>서초동</td>
      <td>1446-11</td>
      <td>현대슈퍼빌</td>
      <td>2003</td>
      <td>14</td>
      <td>37.07</td>
      <td>2022</td>
      <td>12</td>
      <td>21</td>
      <td>44000</td>
      <td>중개거래</td>
      <td>서울 마포구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>777</th>
      <td>11650</td>
      <td>서초구</td>
      <td>서초동</td>
      <td>1445-13</td>
      <td>서초쌍용플래티넘</td>
      <td>2006</td>
      <td>5</td>
      <td>56.92</td>
      <td>2022</td>
      <td>12</td>
      <td>26</td>
      <td>52000</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>778</th>
      <td>11650</td>
      <td>서초구</td>
      <td>서초동</td>
      <td>1600-7</td>
      <td>동양라디안루키</td>
      <td>2004</td>
      <td>12</td>
      <td>20.50</td>
      <td>2022</td>
      <td>12</td>
      <td>26</td>
      <td>11000</td>
      <td>직거래</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>779</th>
      <td>11650</td>
      <td>서초구</td>
      <td>서초동</td>
      <td>1337-21</td>
      <td>현대썬앤빌 서초</td>
      <td>2015</td>
      <td>15</td>
      <td>19.44</td>
      <td>2022</td>
      <td>12</td>
      <td>27</td>
      <td>19000</td>
      <td>직거래</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>780</th>
      <td>11650</td>
      <td>서초구</td>
      <td>신원동</td>
      <td>609</td>
      <td>프라임시티</td>
      <td>2015</td>
      <td>3</td>
      <td>33.22</td>
      <td>2022</td>
      <td>12</td>
      <td>10</td>
      <td>21000</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>


## 오피스텔 전월세 신고 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import TransactionPrice

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = TransactionPrice(service_key)

# 단일 월 조회
df = api.get_data(
    property_type="오피스텔",
    trade_type="전월세",
    sigungu_code="11650",
    year_month="202212",
)

# 기간 내 조회
df = api.get_data(
    property_type="오피스텔",
    trade_type="전월세",
    sigungu_code="11650",
    start_year_month="202201",
    end_year_month="202212",
)

df.tail()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역코드</th>
      <th>시군구</th>
      <th>법정동</th>
      <th>지번</th>
      <th>단지</th>
      <th>건축년도</th>
      <th>층</th>
      <th>전용면적</th>
      <th>년</th>
      <th>월</th>
      <th>일</th>
      <th>보증금</th>
      <th>월세</th>
      <th>계약구분</th>
      <th>계약기간</th>
      <th>갱신요구권사용</th>
      <th>종전계약보증금</th>
      <th>종전계약월세</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1895</th>
      <td>11650</td>
      <td>서초구</td>
      <td>신원동</td>
      <td>661</td>
      <td>서초포레지움</td>
      <td>2018</td>
      <td>2</td>
      <td>27.34</td>
      <td>2022</td>
      <td>12</td>
      <td>15</td>
      <td>1000</td>
      <td>79</td>
      <td>신규</td>
      <td>23.01~24.01</td>
      <td>None</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>1896</th>
      <td>11650</td>
      <td>서초구</td>
      <td>신원동</td>
      <td>NaN</td>
      <td>자연누리 오피스텔</td>
      <td>2015</td>
      <td>3</td>
      <td>21.39</td>
      <td>2022</td>
      <td>12</td>
      <td>19</td>
      <td>1000</td>
      <td>70</td>
      <td>신규</td>
      <td>22.12~23.12</td>
      <td>None</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>1897</th>
      <td>11650</td>
      <td>서초구</td>
      <td>신원동</td>
      <td>NaN</td>
      <td>자연누리 오피스텔</td>
      <td>2015</td>
      <td>2</td>
      <td>21.39</td>
      <td>2022</td>
      <td>12</td>
      <td>23</td>
      <td>17500</td>
      <td>0</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>1898</th>
      <td>11650</td>
      <td>서초구</td>
      <td>신원동</td>
      <td>660</td>
      <td>심플리시티</td>
      <td>2018</td>
      <td>4</td>
      <td>28.63</td>
      <td>2022</td>
      <td>12</td>
      <td>27</td>
      <td>2000</td>
      <td>82</td>
      <td>갱신</td>
      <td>23.01~24.01</td>
      <td>None</td>
      <td>2000</td>
      <td>81</td>
    </tr>
    <tr>
      <th>1899</th>
      <td>11650</td>
      <td>서초구</td>
      <td>신원동</td>
      <td>659</td>
      <td>해피트리앤</td>
      <td>2015</td>
      <td>3</td>
      <td>21.24</td>
      <td>2022</td>
      <td>12</td>
      <td>31</td>
      <td>1000</td>
      <td>63</td>
      <td>갱신</td>
      <td>23.01~24.01</td>
      <td>None</td>
      <td>1000</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>


## 연립다세대 매매 실거래자료 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import TransactionPrice

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = TransactionPrice(service_key)

# 단일 월 조회
df = api.get_data(
    property_type="연립다세대",
    trade_type="매매",
    sigungu_code="11650",
    year_month="202212",
)

# 기간 내 조회
df = api.get_data(
    property_type="연립다세대",
    trade_type="매매",
    sigungu_code="11650",
    start_year_month="202201",
    end_year_month="202212",
)

df.tail()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역코드</th>
      <th>법정동</th>
      <th>지번</th>
      <th>연립다세대</th>
      <th>건축년도</th>
      <th>층</th>
      <th>대지권면적</th>
      <th>전용면적</th>
      <th>년</th>
      <th>월</th>
      <th>일</th>
      <th>거래금액</th>
      <th>거래유형</th>
      <th>중개사소재지</th>
      <th>해제사유발생일</th>
      <th>해제여부</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>760</th>
      <td>11650</td>
      <td>서초동</td>
      <td>1619-8</td>
      <td>(1619-8)</td>
      <td>2015</td>
      <td>3</td>
      <td>27.85</td>
      <td>48.15</td>
      <td>2022</td>
      <td>12</td>
      <td>19</td>
      <td>34000</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>761</th>
      <td>11650</td>
      <td>서초동</td>
      <td>1619-8</td>
      <td>(1619-8)</td>
      <td>2015</td>
      <td>2</td>
      <td>27.50</td>
      <td>47.55</td>
      <td>2022</td>
      <td>12</td>
      <td>19</td>
      <td>33500</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>762</th>
      <td>11650</td>
      <td>서초동</td>
      <td>1619-8</td>
      <td>(1619-8)</td>
      <td>2015</td>
      <td>2</td>
      <td>27.85</td>
      <td>48.15</td>
      <td>2022</td>
      <td>12</td>
      <td>19</td>
      <td>34000</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>763</th>
      <td>11650</td>
      <td>서초동</td>
      <td>1619-8</td>
      <td>(1619-8)</td>
      <td>2015</td>
      <td>3</td>
      <td>27.50</td>
      <td>47.55</td>
      <td>2022</td>
      <td>12</td>
      <td>19</td>
      <td>33500</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>764</th>
      <td>11650</td>
      <td>서초동</td>
      <td>1564-15</td>
      <td>서화빌</td>
      <td>2016</td>
      <td>2</td>
      <td>18.67</td>
      <td>26.23</td>
      <td>2022</td>
      <td>12</td>
      <td>22</td>
      <td>30500</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>


## 연립다세대 전월세 실거래자료 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import TransactionPrice

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = TransactionPrice(service_key)

# 단일 월 조회
df = api.get_data(
    property_type="연립다세대",
    trade_type="전월세",
    sigungu_code="11650",
    year_month="202212",
)

# 기간 내 조회
df = api.get_data(
    property_type="연립다세대",
    trade_type="전월세",
    sigungu_code="11650",
    start_year_month="202201",
    end_year_month="202212",
)

df.tail()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역코드</th>
      <th>법정동</th>
      <th>지번</th>
      <th>연립다세대</th>
      <th>건축년도</th>
      <th>층</th>
      <th>전용면적</th>
      <th>년</th>
      <th>월</th>
      <th>일</th>
      <th>보증금액</th>
      <th>월세금액</th>
      <th>계약구분</th>
      <th>계약기간</th>
      <th>갱신요구권사용</th>
      <th>종전계약보증금</th>
      <th>종전계약월세</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6773</th>
      <td>11650</td>
      <td>서초동</td>
      <td>1360-28</td>
      <td>(1360-28)</td>
      <td>1998</td>
      <td>2</td>
      <td>76.45</td>
      <td>2022</td>
      <td>12</td>
      <td>29</td>
      <td>35000</td>
      <td>0</td>
      <td>신규</td>
      <td>23.02~25.02</td>
      <td>None</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>6774</th>
      <td>11650</td>
      <td>서초동</td>
      <td>1432-2</td>
      <td>미소빌</td>
      <td>2002</td>
      <td>3</td>
      <td>24.82</td>
      <td>2022</td>
      <td>12</td>
      <td>29</td>
      <td>1000</td>
      <td>63</td>
      <td>신규</td>
      <td>23.01~24.04</td>
      <td>None</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>6775</th>
      <td>11650</td>
      <td>서초동</td>
      <td>1628-9</td>
      <td>서초동1628-9공동주택(이상화)</td>
      <td>2017</td>
      <td>3</td>
      <td>29.66</td>
      <td>2022</td>
      <td>12</td>
      <td>30</td>
      <td>2000</td>
      <td>110</td>
      <td>갱신</td>
      <td>23.01~24.01</td>
      <td>None</td>
      <td>20000</td>
      <td>23</td>
    </tr>
    <tr>
      <th>6776</th>
      <td>11650</td>
      <td>서초동</td>
      <td>1508-13</td>
      <td>PineVill</td>
      <td>2003</td>
      <td>3</td>
      <td>71.83</td>
      <td>2022</td>
      <td>12</td>
      <td>31</td>
      <td>40000</td>
      <td>0</td>
      <td>갱신</td>
      <td>23.03~25.03</td>
      <td>None</td>
      <td>37000</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>6777</th>
      <td>11650</td>
      <td>신원동</td>
      <td>192-47</td>
      <td>(192-47)</td>
      <td>2018</td>
      <td>2</td>
      <td>59.70</td>
      <td>2022</td>
      <td>12</td>
      <td>4</td>
      <td>42998</td>
      <td>0</td>
      <td>갱신</td>
      <td>23.01~25.01</td>
      <td>사용</td>
      <td>40950</td>
      <td>&lt;NA&gt;</td>
    </tr>
  </tbody>
</table>
</div>


## 단독/다가구 매매 실거래 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import TransactionPrice

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = TransactionPrice(service_key)

# 단일 월 조회
df = api.get_data(
    property_type="단독다가구",
    trade_type="매매",
    sigungu_code="11650",
    year_month="202212",
)

# 기간 내 조회
df = api.get_data(
    property_type="단독다가구",
    trade_type="매매",
    sigungu_code="11650",
    start_year_month="202201",
    end_year_month="202212",
)

df.tail()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역코드</th>
      <th>법정동</th>
      <th>지번</th>
      <th>주택유형</th>
      <th>건축년도</th>
      <th>대지면적</th>
      <th>연면적</th>
      <th>년</th>
      <th>월</th>
      <th>일</th>
      <th>거래금액</th>
      <th>거래유형</th>
      <th>중개사소재지</th>
      <th>해제사유발생일</th>
      <th>해제여부</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>126</th>
      <td>11650</td>
      <td>양재동</td>
      <td>*</td>
      <td>단독</td>
      <td>1988</td>
      <td>335.3</td>
      <td>819.07</td>
      <td>2022</td>
      <td>11</td>
      <td>10</td>
      <td>640000</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>127</th>
      <td>11650</td>
      <td>서초동</td>
      <td>1***</td>
      <td>다가구</td>
      <td>1995</td>
      <td>166.9</td>
      <td>352.61</td>
      <td>2022</td>
      <td>11</td>
      <td>30</td>
      <td>340000</td>
      <td>중개거래</td>
      <td>서울 강남구</td>
      <td>22.12.19</td>
      <td>O</td>
    </tr>
    <tr>
      <th>128</th>
      <td>11650</td>
      <td>방배동</td>
      <td>5**</td>
      <td>단독</td>
      <td>1989</td>
      <td>172.0</td>
      <td>245.88</td>
      <td>2022</td>
      <td>12</td>
      <td>19</td>
      <td>220000</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>129</th>
      <td>11650</td>
      <td>서초동</td>
      <td>1***</td>
      <td>단독</td>
      <td>1990</td>
      <td>614.8</td>
      <td>323.94</td>
      <td>2022</td>
      <td>12</td>
      <td>5</td>
      <td>780000</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>130</th>
      <td>11650</td>
      <td>서초동</td>
      <td>1***</td>
      <td>다가구</td>
      <td>1995</td>
      <td>166.9</td>
      <td>352.61</td>
      <td>2022</td>
      <td>12</td>
      <td>19</td>
      <td>340000</td>
      <td>중개거래</td>
      <td>서울 강남구</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>


## 단독/다가구 전월세 자료 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import TransactionPrice

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = TransactionPrice(service_key)

# 단일 월 조회
df = api.get_data(
    property_type="단독다가구",
    trade_type="전월세",
    sigungu_code="11650",
    year_month="202212",
)

# 기간 내 조회
df = api.get_data(
    property_type="단독다가구",
    trade_type="전월세",
    sigungu_code="11650",
    start_year_month="202201",
    end_year_month="202212",
)

df.tail()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역코드</th>
      <th>법정동</th>
      <th>건축년도</th>
      <th>계약면적</th>
      <th>년</th>
      <th>월</th>
      <th>일</th>
      <th>보증금액</th>
      <th>월세금액</th>
      <th>계약구분</th>
      <th>계약기간</th>
      <th>갱신요구권사용</th>
      <th>종전계약보증금</th>
      <th>종전계약월세</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4649</th>
      <td>11650</td>
      <td>신원동</td>
      <td>1980</td>
      <td>164.23</td>
      <td>2022</td>
      <td>12</td>
      <td>8</td>
      <td>70000</td>
      <td>55</td>
      <td>신규</td>
      <td>23.01~25.01</td>
      <td>None</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>4650</th>
      <td>11650</td>
      <td>신원동</td>
      <td>&lt;NA&gt;</td>
      <td>40.00</td>
      <td>2022</td>
      <td>12</td>
      <td>10</td>
      <td>12000</td>
      <td>0</td>
      <td>신규</td>
      <td>23.01~24.01</td>
      <td>None</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>4651</th>
      <td>11650</td>
      <td>신원동</td>
      <td>2008</td>
      <td>109.65</td>
      <td>2022</td>
      <td>12</td>
      <td>11</td>
      <td>20000</td>
      <td>130</td>
      <td>갱신</td>
      <td>22.12~23.12</td>
      <td>사용</td>
      <td>20000</td>
      <td>120</td>
    </tr>
    <tr>
      <th>4652</th>
      <td>11650</td>
      <td>신원동</td>
      <td>2015</td>
      <td>101.68</td>
      <td>2022</td>
      <td>12</td>
      <td>15</td>
      <td>10000</td>
      <td>200</td>
      <td>신규</td>
      <td>23.02~25.02</td>
      <td>None</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
    </tr>
    <tr>
      <th>4653</th>
      <td>11650</td>
      <td>신원동</td>
      <td>2018</td>
      <td>49.93</td>
      <td>2022</td>
      <td>12</td>
      <td>20</td>
      <td>28000</td>
      <td>0</td>
      <td>신규</td>
      <td>23.02~25.02</td>
      <td>None</td>
      <td>&lt;NA&gt;</td>
      <td>&lt;NA&gt;</td>
    </tr>
  </tbody>
</table>
</div>


## 토지 매매 신고 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import TransactionPrice

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = TransactionPrice(service_key)

# 단일 월 조회
df = api.get_data(
    property_type="토지",
    trade_type="매매",
    sigungu_code="11650",
    year_month="202212",
)

# 기간 내 조회
df = api.get_data(
    property_type="토지",
    trade_type="매매",
    sigungu_code="11650",
    start_year_month="202201",
    end_year_month="202212",
)

df.tail()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역코드</th>
      <th>시군구</th>
      <th>법정동</th>
      <th>지번</th>
      <th>용도지역</th>
      <th>지목</th>
      <th>거래면적</th>
      <th>거래금액</th>
      <th>구분</th>
      <th>년</th>
      <th>월</th>
      <th>일</th>
      <th>거래유형</th>
      <th>중개사소재지</th>
      <th>해제사유발생일</th>
      <th>해제여부</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>237</th>
      <td>11650</td>
      <td>서초구</td>
      <td>서초동</td>
      <td>1***</td>
      <td>일반상업지역</td>
      <td>대</td>
      <td>610.02</td>
      <td>4623893</td>
      <td>지분</td>
      <td>2022</td>
      <td>12</td>
      <td>27</td>
      <td>직거래</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>238</th>
      <td>11650</td>
      <td>서초구</td>
      <td>내곡동</td>
      <td>*</td>
      <td>개발제한구역</td>
      <td>답</td>
      <td>29.50</td>
      <td>3000</td>
      <td>지분</td>
      <td>2022</td>
      <td>12</td>
      <td>25</td>
      <td>직거래</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>239</th>
      <td>11650</td>
      <td>서초구</td>
      <td>염곡동</td>
      <td>2**</td>
      <td>개발제한구역</td>
      <td>전</td>
      <td>1304.00</td>
      <td>162348</td>
      <td>NaN</td>
      <td>2022</td>
      <td>12</td>
      <td>30</td>
      <td>직거래</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>240</th>
      <td>11650</td>
      <td>서초구</td>
      <td>신원동</td>
      <td>2**</td>
      <td>준주거지역</td>
      <td>전</td>
      <td>4090.10</td>
      <td>1105221</td>
      <td>NaN</td>
      <td>2022</td>
      <td>12</td>
      <td>1</td>
      <td>직거래</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>241</th>
      <td>11650</td>
      <td>서초구</td>
      <td>신원동</td>
      <td>1**</td>
      <td>개발제한구역</td>
      <td>임야</td>
      <td>7920.00</td>
      <td>133452</td>
      <td>NaN</td>
      <td>2022</td>
      <td>12</td>
      <td>1</td>
      <td>직거래</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>


## 상업업무용 부동산 매매 신고 자료 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import TransactionPrice

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = TransactionPrice(service_key)

# 단일 월 조회
df = api.get_data(
    property_type="상업업무용",
    trade_type="매매",
    sigungu_code="11650",
    year_month="202212",
)

# 기간 내 조회
df = api.get_data(
    property_type="상업업무용",
    trade_type="매매",
    sigungu_code="11650",
    start_year_month="202201",
    end_year_month="202212",
)

df.tail()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역코드</th>
      <th>시군구</th>
      <th>법정동</th>
      <th>지번</th>
      <th>유형</th>
      <th>용도지역</th>
      <th>건물주용도</th>
      <th>건축년도</th>
      <th>층</th>
      <th>대지면적</th>
      <th>건물면적</th>
      <th>구분</th>
      <th>년</th>
      <th>월</th>
      <th>일</th>
      <th>거래금액</th>
      <th>거래유형</th>
      <th>중개사소재지</th>
      <th>해제사유발생일</th>
      <th>해제여부</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>765</th>
      <td>11650</td>
      <td>서초구</td>
      <td>서초동</td>
      <td>1***</td>
      <td>집합</td>
      <td>제3종일반주거</td>
      <td>제2종근린생활</td>
      <td>1979</td>
      <td>&lt;NA&gt;</td>
      <td>NaN</td>
      <td>22.60</td>
      <td>NaN</td>
      <td>2022</td>
      <td>12</td>
      <td>15</td>
      <td>25000</td>
      <td>직거래</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>766</th>
      <td>11650</td>
      <td>서초구</td>
      <td>서초동</td>
      <td>1***</td>
      <td>집합</td>
      <td>일반상업</td>
      <td>업무</td>
      <td>2005</td>
      <td>&lt;NA&gt;</td>
      <td>NaN</td>
      <td>10.15</td>
      <td>NaN</td>
      <td>2022</td>
      <td>12</td>
      <td>15</td>
      <td>4500</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>767</th>
      <td>11650</td>
      <td>서초구</td>
      <td>서초동</td>
      <td>1***</td>
      <td>집합</td>
      <td>일반상업</td>
      <td>업무</td>
      <td>2005</td>
      <td>&lt;NA&gt;</td>
      <td>NaN</td>
      <td>10.15</td>
      <td>NaN</td>
      <td>2022</td>
      <td>12</td>
      <td>15</td>
      <td>4000</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>768</th>
      <td>11650</td>
      <td>서초구</td>
      <td>서초동</td>
      <td>1***</td>
      <td>집합</td>
      <td>제2종일반주거</td>
      <td>제2종근린생활</td>
      <td>2015</td>
      <td>1</td>
      <td>NaN</td>
      <td>29.34</td>
      <td>NaN</td>
      <td>2022</td>
      <td>12</td>
      <td>19</td>
      <td>18000</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>769</th>
      <td>11650</td>
      <td>서초구</td>
      <td>서초동</td>
      <td>1***</td>
      <td>일반</td>
      <td>제3종일반주거</td>
      <td>제2종근린생활</td>
      <td>2003</td>
      <td>&lt;NA&gt;</td>
      <td>376.2</td>
      <td>973.98</td>
      <td>NaN</td>
      <td>2022</td>
      <td>12</td>
      <td>26</td>
      <td>740000</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>


## 공장 및 창고 등 부동산 매매 신고 자료 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import TransactionPrice

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = TransactionPrice(service_key)

# 단일 월 조회
df = api.get_data(
    property_type="공장창고등",
    trade_type="매매",
    sigungu_code="11650",
    year_month="202212",
)

# 기간 내 조회
df = api.get_data(
    property_type="공장창고등",
    trade_type="매매",
    sigungu_code="11650",
    start_year_month="202201",
    end_year_month="202212",
)

df.tail()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역코드</th>
      <th>시군구</th>
      <th>법정동</th>
      <th>지번</th>
      <th>유형</th>
      <th>용도지역</th>
      <th>건물주용도</th>
      <th>건축년도</th>
      <th>층</th>
      <th>대지면적</th>
      <th>건물면적</th>
      <th>구분</th>
      <th>년</th>
      <th>월</th>
      <th>일</th>
      <th>거래금액</th>
      <th>거래유형</th>
      <th>중개사소재지</th>
      <th>해제사유발생일</th>
      <th>해제여부</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>11650</td>
      <td>서초구</td>
      <td>양재동</td>
      <td>2**</td>
      <td>집합</td>
      <td>일반상업</td>
      <td>자동차 관련시설</td>
      <td>&lt;NA&gt;</td>
      <td>5</td>
      <td>NaN</td>
      <td>45.20</td>
      <td>NaN</td>
      <td>2022</td>
      <td>7</td>
      <td>5</td>
      <td>18500</td>
      <td>중개거래</td>
      <td>서울 서초구</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11650</td>
      <td>서초구</td>
      <td>양재동</td>
      <td>2**</td>
      <td>집합</td>
      <td>일반상업</td>
      <td>자동차 관련시설</td>
      <td>2003</td>
      <td>3</td>
      <td>NaN</td>
      <td>47.80</td>
      <td>NaN</td>
      <td>2022</td>
      <td>9</td>
      <td>1</td>
      <td>75500</td>
      <td>직거래</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11650</td>
      <td>서초구</td>
      <td>양재동</td>
      <td>2**</td>
      <td>집합</td>
      <td>일반상업</td>
      <td>자동차 관련시설</td>
      <td>2003</td>
      <td>&lt;NA&gt;</td>
      <td>NaN</td>
      <td>66.98</td>
      <td>지분</td>
      <td>2022</td>
      <td>9</td>
      <td>1</td>
      <td>21500</td>
      <td>직거래</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11650</td>
      <td>서초구</td>
      <td>양재동</td>
      <td>2**</td>
      <td>집합</td>
      <td>일반상업</td>
      <td>자동차 관련시설</td>
      <td>2003</td>
      <td>&lt;NA&gt;</td>
      <td>NaN</td>
      <td>66.98</td>
      <td>지분</td>
      <td>2022</td>
      <td>9</td>
      <td>1</td>
      <td>21500</td>
      <td>직거래</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11650</td>
      <td>서초구</td>
      <td>양재동</td>
      <td>2**</td>
      <td>집합</td>
      <td>일반상업</td>
      <td>자동차 관련시설</td>
      <td>2003</td>
      <td>&lt;NA&gt;</td>
      <td>NaN</td>
      <td>66.75</td>
      <td>지분</td>
      <td>2022</td>
      <td>9</td>
      <td>1</td>
      <td>21500</td>
      <td>직거래</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>

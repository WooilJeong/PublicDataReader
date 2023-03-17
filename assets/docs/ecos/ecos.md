# ECOS 한국은행 경제통계 서비스 사용 가이드

[한국은행 Open API 서비스](https://ecos.bok.or.kr/api//)에서 제공하는 오픈 API 서비스를 이용하려면 인증키가 필요합니다. 인증키를 얻기 위해서는 [한국은행 Open API 서비스](https://ecos.bok.or.kr/api/)에 회원가입해야 합니다. 가입과 동시에 인증키가 자동으로 부여되며 일반적으로 1일 이내에 API 호출이 가능합니다.

## API 목록

- [서비스 통계 목록](#서비스-통계-목록)
- [통계용어사전](#통계용어사전)
- [통계 세부항목 목록](#통계-세부항목-목록)
- [통계 조회 조건 설정](#통계-조회-조건-설정)
- [100대 통계지표](#100대-통계지표)
- [통계메타유](#통계메타db)


## 서비스 통계 목록

### 입력 명세

<div align="center">

| 항목명     | 설명                            | 샘플데이터   | 항목구분   |
|:-----------|:--------------------------------|:-------------|:-----------|
| 통계표코드 | 통계표코드                      | 102Y004      | 선택       |
| translate  | 국문 컬럼명 여부 (기본값: True) | True         | 선택       |

</div>


### 출력 명세

<div align="center">

| 항목명     | 설명                            | 샘플데이터   | 항목구분   |
|:-----------|:--------------------------------|:-------------|:-----------|
| 통계표코드 | 통계표코드                      | 102Y004      | 선택       |
| translate  | 국문 컬럼명 여부 (기본값: True) | True         | 선택       |

</div>

### 예제

```python
from PublicDataReader import Ecos
# service_key = "API 인증키"
api = Ecos(service_key)
df = api.get_statistic_table_list()
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>상위통계표코드</th>
      <th>통계표코드</th>
      <th>통계명</th>
      <th>시점</th>
      <th>검색가능여부</th>
      <th>출처</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>*</td>
      <td>0000000001</td>
      <td>1. 통화/금융</td>
      <td>None</td>
      <td>N</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0000000001</td>
      <td>0000000002</td>
      <td>1.1. 통화/유동성</td>
      <td>None</td>
      <td>N</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0000000002</td>
      <td>0000000003</td>
      <td>1.1.1. 본원통화</td>
      <td>None</td>
      <td>N</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0000000003</td>
      <td>0000000004</td>
      <td>1.1.1.1. 본원통화 구성내역</td>
      <td>None</td>
      <td>N</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0000000004</td>
      <td>102Y004</td>
      <td>1.1.1.1.1. 본원통화 구성내역(평잔, 계절조정계열)</td>
      <td>M</td>
      <td>Y</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>






## 통계표용어

### 입력 명세

<div align="center">

| 항목명    | 설명                            | 샘플데이터     | 항목구분   |
|:----------|:--------------------------------|:---------------|:-----------|
| 용어      | 용어                            | 소비자동향지수 | 필수       |
| translate | 국문 컬럼명 여부 (기본값: True) | True           | 선택       |

</div>


### 출력 명세

<div align="center">

| 항목명    | 설명                            | 샘플데이터     | 항목구분   |
|:----------|:--------------------------------|:---------------|:-----------|
| 용어      | 용어                            | 소비자동향지수 | 필수       |
| translate | 국문 컬럼명 여부 (기본값: True) | True           | 선택       |

</div>

### 예제


```python
from PublicDataReader import Ecos
# service_key = "API 인증키"
api = Ecos(service_key)
df = api.get_statistic_word(용어="소비자동향지수")
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>용어</th>
      <th>용어설명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>소비자동향지수</td>
      <td>소비자들이 느끼는 경기, 소비지출계획, 생활형편 등 경제에 대한 전반적인 인식을 조...</td>
    </tr>
  </tbody>
</table>
</div>




## 통계 세부항목 목록

### 입력 명세

<div align="center">

| 항목명     | 설명                            | 샘플데이터   | 항목구분   |
|:-----------|:--------------------------------|:-------------|:-----------|
| 통계표코드 | 통계표코드                      | 601Y002      | 필수       |
| translate  | 국문 컬럼명 여부 (기본값: True) | True         | 선택       |

</div>


### 출력 명세

<div align="center">

| 항목명     | 설명                            | 샘플데이터   | 항목구분   |
|:-----------|:--------------------------------|:-------------|:-----------|
| 통계표코드 | 통계표코드                      | 601Y002      | 필수       |
| translate  | 국문 컬럼명 여부 (기본값: True) | True         | 선택       |

</div>

### 예제



```python
from PublicDataReader import Ecos
# service_key = "API 인증키"
api = Ecos(service_key)
df = api.get_statistic_item_list(통계표코드="601Y002")
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>통계표코드</th>
      <th>통계명</th>
      <th>항목그룹코드</th>
      <th>항목그룹명</th>
      <th>통계항목코드</th>
      <th>통계항목명</th>
      <th>상위통계항목코드</th>
      <th>상위통계항목명</th>
      <th>시점</th>
      <th>수록시작일자</th>
      <th>수록종료일자</th>
      <th>자료수</th>
      <th>단위</th>
      <th>가중치</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>601Y002</td>
      <td>7.5.2. 지역별 소비유형별 개인 신용카드</td>
      <td>Group1</td>
      <td>지역코드</td>
      <td>A</td>
      <td>서울</td>
      <td>None</td>
      <td>None</td>
      <td>M</td>
      <td>200912</td>
      <td>202212</td>
      <td>12874</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>601Y002</td>
      <td>7.5.2. 지역별 소비유형별 개인 신용카드</td>
      <td>Group1</td>
      <td>지역코드</td>
      <td>B</td>
      <td>부산</td>
      <td>None</td>
      <td>None</td>
      <td>M</td>
      <td>200912</td>
      <td>202212</td>
      <td>12874</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>601Y002</td>
      <td>7.5.2. 지역별 소비유형별 개인 신용카드</td>
      <td>Group1</td>
      <td>지역코드</td>
      <td>C</td>
      <td>대구</td>
      <td>None</td>
      <td>None</td>
      <td>M</td>
      <td>200912</td>
      <td>202212</td>
      <td>12874</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>601Y002</td>
      <td>7.5.2. 지역별 소비유형별 개인 신용카드</td>
      <td>Group1</td>
      <td>지역코드</td>
      <td>D</td>
      <td>인천</td>
      <td>None</td>
      <td>None</td>
      <td>M</td>
      <td>200912</td>
      <td>202212</td>
      <td>12874</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>601Y002</td>
      <td>7.5.2. 지역별 소비유형별 개인 신용카드</td>
      <td>Group1</td>
      <td>지역코드</td>
      <td>E</td>
      <td>광주</td>
      <td>None</td>
      <td>None</td>
      <td>M</td>
      <td>200912</td>
      <td>202212</td>
      <td>12874</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>




## 통계 조회 조건 설정

### 입력 명세

<div align="center">

| 항목명        | 설명                                                                       | 샘플데이터   | 항목구분   |
|:--------------|:---------------------------------------------------------------------------|:-------------|:-----------|
| 통계표코드    | 통계표코드                                                                 | 200Y001      | 필수       |
| 주기          | 주기(년:A, 반년:S, 분기:Q, 월:M, 반월:SM, 일: D)                           | A            | 필수       |
| 검색시작일자  | 검색시작일자(주기에 맞는 형식으로 입력: 2015, 2015Q1, 201501, 20150101 등) | 2015         | 필수       |
| 검색종료일자  | 검색종료일자(주기에 맞는 형식으로 입력: 2021, 2021Q1, 202101, 20210101 등) | 2021         | 필수       |
| 통계항목코드1 | 통계항목코드1                                                              | 10101        | 선택       |
| 통계항목코드2 | 통계항목코드2                                                              | nan          | 선택       |
| 통계항목코드3 | 통계항목코드3                                                              | nan          | 선택       |
| 통계항목코드4 | 통계항목코드4                                                              | nan          | 선택       |
| translate     | 국문 컬럼명 여부 (기본값: True)                                            | True         | 선택       |

</div>


### 출력 명세

<div align="center">

| 항목명        | 설명                                                                       | 샘플데이터   | 항목구분   |
|:--------------|:---------------------------------------------------------------------------|:-------------|:-----------|
| 통계표코드    | 통계표코드                                                                 | 200Y001      | 필수       |
| 주기          | 주기(년:A, 반년:S, 분기:Q, 월:M, 반월:SM, 일: D)                           | A            | 필수       |
| 검색시작일자  | 검색시작일자(주기에 맞는 형식으로 입력: 2015, 2015Q1, 201501, 20150101 등) | 2015         | 필수       |
| 검색종료일자  | 검색종료일자(주기에 맞는 형식으로 입력: 2021, 2021Q1, 202101, 20210101 등) | 2021         | 필수       |
| 통계항목코드1 | 통계항목코드1                                                              | 10101        | 선택       |
| 통계항목코드2 | 통계항목코드2                                                              | nan          | 선택       |
| 통계항목코드3 | 통계항목코드3                                                              | nan          | 선택       |
| 통계항목코드4 | 통계항목코드4                                                              | nan          | 선택       |
| translate     | 국문 컬럼명 여부 (기본값: True)                                            | True         | 선택       |

</div>

### 예제


```python
from PublicDataReader import Ecos
# service_key = "API 인증키"
api = Ecos(service_key)
df = api.get_statistic_search(통계표코드="200Y001", 주기="A", 검색시작일자="2015", 검색종료일자="2021")
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>통계표코드</th>
      <th>통계명</th>
      <th>통계항목코드1</th>
      <th>통계항목명1</th>
      <th>통계항목코드2</th>
      <th>통계항목명2</th>
      <th>통계항목코드3</th>
      <th>통계항목명3</th>
      <th>통계항목코드4</th>
      <th>통계항목명4</th>
      <th>단위</th>
      <th>시점</th>
      <th>값</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>200Y001</td>
      <td>2.1.1.1. 주요지표(연간지표)</td>
      <td>3010101</td>
      <td>민간</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>%</td>
      <td>2015</td>
      <td>2.2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>200Y001</td>
      <td>2.1.1.1. 주요지표(연간지표)</td>
      <td>7010106</td>
      <td>가계</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>%</td>
      <td>2015</td>
      <td>55.8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>200Y001</td>
      <td>2.1.1.1. 주요지표(연간지표)</td>
      <td>7010107</td>
      <td>기업</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>%</td>
      <td>2015</td>
      <td>22.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>200Y001</td>
      <td>2.1.1.1. 주요지표(연간지표)</td>
      <td>7010108</td>
      <td>정부</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>%</td>
      <td>2015</td>
      <td>21.7</td>
    </tr>
    <tr>
      <th>4</th>
      <td>200Y001</td>
      <td>2.1.1.1. 주요지표(연간지표)</td>
      <td>70105</td>
      <td>총조정처분가능소득의분배</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>2015</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>




## 100대 통계지표

### 입력 명세

<div align="center">

| 항목명    | 설명                            | 샘플데이터   | 항목구분   |
|:----------|:--------------------------------|:-------------|:-----------|
| translate | 국문 컬럼명 여부 (기본값: True) | True         | 선택       |

</div>


### 출력 명세

<div align="center">

| 항목명    | 설명                            | 샘플데이터   | 항목구분   |
|:----------|:--------------------------------|:-------------|:-----------|
| translate | 국문 컬럼명 여부 (기본값: True) | True         | 선택       |

</div>

### 예제



```python
from PublicDataReader import Ecos
# service_key = "API 인증키"
api = Ecos(service_key)
df = api.get_key_statistic_list()
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>통계그룹명</th>
      <th>통계명</th>
      <th>값</th>
      <th>시점</th>
      <th>단위</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>시장금리</td>
      <td>한국은행 기준금리</td>
      <td>3.5</td>
      <td>20230315</td>
      <td>%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>시장금리</td>
      <td>콜금리(익일물)</td>
      <td>3.439</td>
      <td>20230316</td>
      <td>%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>시장금리</td>
      <td>KORIBOR(3개월)</td>
      <td>3.56</td>
      <td>20230317</td>
      <td>%</td>
    </tr>
    <tr>
      <th>3</th>
      <td>시장금리</td>
      <td>CD수익률(91일)</td>
      <td>3.62</td>
      <td>20230317</td>
      <td>%</td>
    </tr>
    <tr>
      <th>4</th>
      <td>시장금리</td>
      <td>통안증권수익률(364일)</td>
      <td>3.429</td>
      <td>20230317</td>
      <td>%</td>
    </tr>
  </tbody>
</table>
</div>




## 통계메타유

### 입력 명세

<div align="center">

| 항목명    | 설명                            | 샘플데이터   | 항목구분   |
|:----------|:--------------------------------|:-------------|:-----------|
| 데이터명  | 데이터명                        | 경제심리지수 | 필수       |
| translate | 국문 컬럼명 여부 (기본값: True) | True         | 선택       |

</div>


### 출력 명세

<div align="center">

| 항목명    | 설명                            | 샘플데이터   | 항목구분   |
|:----------|:--------------------------------|:-------------|:-----------|
| 데이터명  | 데이터명                        | 경제심리지수 | 필수       |
| translate | 국문 컬럼명 여부 (기본값: True) | True         | 선택       |

</div>

### 예제



```python
from PublicDataReader import Ecos
# service_key = "API 인증키"
api = Ecos(service_key)
df = api.get_statistic_meta(데이터명="경제심리지수")
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>레벨</th>
      <th>상위통계항목코드</th>
      <th>통계항목코드</th>
      <th>통계항목명</th>
      <th>메타데이터</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0000000001</td>
      <td>0000000098</td>
      <td>무응답률</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>0000000001</td>
      <td>0000000099</td>
      <td>MSE</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>None</td>
      <td>0000000100</td>
      <td>예산 인력 교육 홍보</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0000000001</td>
      <td>0000000101</td>
      <td>관련 예산</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>0000000001</td>
      <td>0000000102</td>
      <td>인력</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>
# 국토교통부 토지임야정보 사용 가이드

[공공데이터포털](https://www.data.go.kr)에서 제공하는 오픈 API 서비스를 이용하려면 인증키가 필요합니다. 인증키를 얻기 위해서는 [공공데이터포털](https://www.data.go.kr)에 회원가입을 하고 원하는 오픈 API 서비스를 신청해야 합니다. 공공데이터포털에서 API를 신청하면 일반적으로 1~2시간 이내에 호출이 가능합니다. 그러나 일부 API의 경우 인증 절차가 24시간 이상 소요될 수 있습니다.


## 국토교통부 토지임야정보 서비스

- [토지임야정보 조회 서비스 신청 페이지](https://www.data.go.kr/data/15057917/openapi.do)


## 토지임야목록 조회 서비스

### 입력 명세

<div align="center">

| 항목명         | 설명                                                                                                                              | 데이터 타입   | 샘플 데이터   | 항목구분   |
|:-------------|:----------------------------------------------------------------------------------------------------------------------------------|:--------------|:--------------|:-----------|
| pnu_code    | PNU코드: 각 필지를 서로 구별하기 위하여 필지마다 붙이는 고유한 번호                                                                            | String        | 540           | 필수       |
| translate    | 컬럼명 한글 표시 여부<br>(한글 표시: True, 영문 표시: False)<br>※ 기본값: True                                                    | Boolean       | True          | 선택       |
| verbose      | 데이터 조회 진행 상황 메시지 출력 여부<br>(출력: True, 미출력: False)<br>※ 기본값: False                                          | Boolean       | False         | 선택       |
| wait_time    | API 추가 요청 시 대기 시간(초)<br>(30초: 30)<br>※ 기본값: 30                                                                      | Integer       | 30            | 선택       |

</div>

### 출력 명세

<div align="center">

| 항목명(국문)     | 항목명(영문)        | 항목설명                              | 샘플데이터         |
| :----------- | :-------------- | :--------------------------------- | :------------- |
| 고유번호        | pnu            | 각 필지를 서로 구별하기 위하여 필지마다 붙이는 고유한 번호 | 1.11101E+18   |
| 법정동명        | ldCodeNm       | 토지가 소재한 소재지의 행정구역코드(법정동코드) 10자리   | 서울특별시 종로구 청운동 |
| 법정동코드       | ldCode         | 토지가 소재한 소재지의 행정구역 명칭(법정동명)        | 1111010100    |
| 지번          | mnnmSlno       | 필지에 부여하여 지적공부에 등록한 번호             | 126-25        |
| 대장구분코드      | regstrSeCode   | 토지가 위치한 토지의 대장 구분 (토지(임야)대장구분)코드  | 1             |
| 대장구분명       | regstrSeCodeNm | 코드 정보                             | 토지대장          |
| 지목코드        | lndcgrCode     | 토지의 주된 용도에 따라 토지의 종류를 구분한 지목코드    | 8             |
| 지목명         | lndcgrCodeNm   | 코드 정보                             | 대             |
| 면적(㎡)       | lndpclAr       | 지적공부에 등록한 필지의 수평면상 넓이(㎡)          | 376.9         |
| 소유구분코드      | posesnSeCode   | 국토를 토지 소유권 취득 주체에 따라 구분한 코드       | 6             |
| 소유구분명       | posesnSeCodeNm | 코드 정보                             | 법인            |
| 소유(공유)인수(명) | cnrsPsnCo      | 토지를 공동 소유하고있는 사람수(명)              | 2             |
| 축척구분코드      | ladFrtlSc      | 토지(임야)대장에 등록된 지적도(임야도)의 축척구분 코드   | 6             |
| 축척구분명       | ladFrtlScNm    | 코드 정보                             | 0.458333333   |
| 데이터기준일자     | lastUpdtDt     | 데이터 작성 기준일자                       | 2015-11-12    |

</div>

```python
from PublicDataReader import LandForestLedger

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = LandForestLedger(service_key)

df = api.get_data(
    pnu_code="4113511000105420000", 
)
df.head()
```


<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>고유번호</th>
      <th>법정동명</th>
      <th>법정동코드</th>
      <th>지번</th>
      <th>대장구분코드</th>
      <th>대장구분명</th>
      <th>지목코드</th>
      <th>지목명</th>
      <th>면적(㎡)</th>
      <th>소유구분코드</th>
      <th>소유구분명</th>
      <th>소유(공유)인수(명)</th>
      <th>축척구분코드</th>
      <th>축척구분명</th>
      <th>데이터기준일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4113511000105420000</td>
      <td>경기도 성남시 분당구 백현동</td>
      <td>4113511000</td>
      <td>542-0</td>
      <td>1</td>
      <td>토지대장</td>
      <td>08</td>
      <td>대</td>
      <td>65893.5</td>
      <td>01</td>
      <td>개인</td>
      <td>0</td>
      <td>00</td>
      <td>수치</td>
      <td>2022-06-07</td>
    </tr>
  </tbody>
</table>
</div>


## (참고) 건축물대장에서 PNU코드 목록 조회

- 법정동코드 목록 확인

```python
import PublicDataReader as pdr
code_bdong = pdr.code_bdong()
code_bdong.loc[
    (code_bdong['시도명']=='서울특별시') &
    (code_bdong['말소일자']=='') &
    (code_bdong['시군구명']=='서초구')
]
```


<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>시도코드</th>
      <th>시도명</th>
      <th>시군구코드</th>
      <th>시군구명</th>
      <th>법정동코드</th>
      <th>읍면동명</th>
      <th>동리명</th>
      <th>생성일자</th>
      <th>말소일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>975</th>
      <td>11</td>
      <td>서울특별시</td>
      <td>11650</td>
      <td>서초구</td>
      <td>1165000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>19880423</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>977</th>
      <td>11</td>
      <td>서울특별시</td>
      <td>11650</td>
      <td>서초구</td>
      <td>1165010100</td>
      <td>방배동</td>
      <td>NaN</td>
      <td>19890427</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>978</th>
      <td>11</td>
      <td>서울특별시</td>
      <td>11650</td>
      <td>서초구</td>
      <td>1165010200</td>
      <td>양재동</td>
      <td>NaN</td>
      <td>19920701</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>979</th>
      <td>11</td>
      <td>서울특별시</td>
      <td>11650</td>
      <td>서초구</td>
      <td>1165010300</td>
      <td>우면동</td>
      <td>NaN</td>
      <td>19920701</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>980</th>
      <td>11</td>
      <td>서울특별시</td>
      <td>11650</td>
      <td>서초구</td>
      <td>1165010400</td>
      <td>원지동</td>
      <td>NaN</td>
      <td>19920701</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>982</th>
      <td>11</td>
      <td>서울특별시</td>
      <td>11650</td>
      <td>서초구</td>
      <td>1165010600</td>
      <td>잠원동</td>
      <td>NaN</td>
      <td>19880423</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>983</th>
      <td>11</td>
      <td>서울특별시</td>
      <td>11650</td>
      <td>서초구</td>
      <td>1165010700</td>
      <td>반포동</td>
      <td>NaN</td>
      <td>19880423</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>984</th>
      <td>11</td>
      <td>서울특별시</td>
      <td>11650</td>
      <td>서초구</td>
      <td>1165010800</td>
      <td>서초동</td>
      <td>NaN</td>
      <td>19880423</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>985</th>
      <td>11</td>
      <td>서울특별시</td>
      <td>11650</td>
      <td>서초구</td>
      <td>1165010900</td>
      <td>내곡동</td>
      <td>NaN</td>
      <td>19880423</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>986</th>
      <td>11</td>
      <td>서울특별시</td>
      <td>11650</td>
      <td>서초구</td>
      <td>1165011000</td>
      <td>염곡동</td>
      <td>NaN</td>
      <td>19880423</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>987</th>
      <td>11</td>
      <td>서울특별시</td>
      <td>11650</td>
      <td>서초구</td>
      <td>1165011100</td>
      <td>신원동</td>
      <td>NaN</td>
      <td>19880423</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




- 건축물대장 조회 후 PNU코드 생성

```python
from PublicDataReader import BuildingLedger
bl = BuildingLedger(service_key)
buildings = bl.get_data("총괄표제부", sigungu_code="11650", bdong_code="10300")
transform_dict = {
    "0": "1",
    "1": "2",
    "2": "3",
}
buildings['필지구분코드'] = buildings['대지구분코드'].replace(transform_dict)
buildings['PNU'] = buildings['시군구코드'] + buildings['법정동코드'] + buildings['필지구분코드'] + buildings['번'].str.zfill(4) + buildings['지'].str.zfill(4)
buildings['필지구분코드'].value_counts()
```

    1    27
    2     1
    Name: 필지구분코드, dtype: int64


- 필지구분코드로 PNU코드 list_iterator 객체 생성

```python
it = iter(list(buildings.loc[buildings['필지구분코드']=='2']['PNU']))
```

- 토지임야정보 조회

```python
pnu_code = next(it)
print(pnu_code)
api.get_data(pnu_code=pnu_code)
```


    1165010300200360000
    




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>고유번호</th>
      <th>법정동명</th>
      <th>법정동코드</th>
      <th>지번</th>
      <th>대장구분코드</th>
      <th>대장구분명</th>
      <th>지목코드</th>
      <th>지목명</th>
      <th>면적(㎡)</th>
      <th>소유구분코드</th>
      <th>소유구분명</th>
      <th>소유(공유)인수(명)</th>
      <th>축척구분코드</th>
      <th>축척구분명</th>
      <th>데이터기준일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1165010300200360000</td>
      <td>서울특별시 서초구 우면동</td>
      <td>1165010300</td>
      <td>36-0</td>
      <td>2</td>
      <td>임야대장</td>
      <td>05</td>
      <td>임야</td>
      <td>14777</td>
      <td>02</td>
      <td>국유지</td>
      <td>0</td>
      <td>30</td>
      <td>1:3000</td>
      <td>2022-06-07</td>
    </tr>
  </tbody>
</table>
</div>

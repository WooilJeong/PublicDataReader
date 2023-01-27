# 국토교통부 토지소유정보 사용 가이드

[공공데이터포털](https://www.data.go.kr)에서 제공하는 오픈 API 서비스를 이용하려면 인증키가 필요합니다. 인증키를 얻기 위해서는 [공공데이터포털](https://www.data.go.kr)에 회원가입을 하고 원하는 오픈 API 서비스를 신청해야 합니다. 공공데이터포털에서 API를 신청하면 일반적으로 1~2시간 이내에 호출이 가능합니다. 그러나 일부 API의 경우 인증 절차가 24시간 이상 소요될 수 있습니다.


## 국토교통부 토지소유정보 서비스

- [토지소유정보 조회 서비스 신청 페이지](https://www.data.go.kr/data/15058047/openapi.do)


## 토지소유정보 조회 서비스

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

| 항목명(국문)   | 항목명(영문)               | 항목설명                                                  | 샘플데이터               |
| :--------- | :--------------------- | :----------------------------------------------------- | :------------------- |
| 고유번호      | pnu                   | 각 필지를 서로 구별하기 위하여 필지마다 붙이는 고유한 번호                     | 1165010800113320000 |
| 법정동코드     | ldCode                | 토지가 소재한 행정구역코드(법정동코드) 10자리                            | 1165010800          |
| 법정동명      | ldCodeNm              | 토지가 소재한 소재지의 행정구역 명칭(법정동명)                            | 서울특별시 서초구 서초동       |
| 대장구분코드    | regstrSeCode          | 토지가 위치한 토지의 대장 구분 (토지(임야)대장구분)코드                      | 1                   |
| 대장구분명     | regstrSeCodeNm        | 토지가 위치한 토지의 대장 구분 (토지(임야)대장구분)                        | 토지대장                |
| 지번        | mnnmSlno              | 필지에 부여하여 지적공부에 등록한 번호                                 | 1332-11             |
| 집합건물일련번호  | agbldgSn              | 집합건물일련번호                                              | 5091                |
| 건물동명      | buldDongNm            | 건물동명                                                  | 202                 |
| 건물층명      | buldFloorNm           | 건물층명                                                  | 17                  |
| 건물호명      | buldHoNm              | 건물호명                                                  | 1702                |
| 건물실명      | buldRoomNm            | 건물실명                                                  | 5                   |
| 공유인일련번호   | cnrsPsnSn             | 공유인일련번호                                               | 1                   |
| 기준연월      | stdrYm                | 기준연월                                                  | 42583               |
| 지목코드      | lndcgrCode            | 토지의 주된 용도에 따라 토지의 종류를 구분한 지목코드                        | 8                   |
| 지목        | lndcgrCodeNm          | 토지의 주된 용도에 따라 토지의 종류를 구분한 지목코드의 코드정보                  | 대                   |
| 토지면적(㎡)   | ndpclAr               | 지적공부에 등록한 필지의 수평면상 넓이(㎡)                              | 122                 |
| 공시지가(원/㎡) | pblntfPclnd           | 대한민국의 건설교통부가 토지의 가격을 조사, 감정을 해 공시함. 개별토지에한 공시 가격(원/㎡) | 1544000             |
| 소유구분코드    | posesnSeCode          | 국토를 토지 소유권 취득 주체에 따라 구분한 코드                           | 4                   |
| 소유구분      | posesnSeCodeNm        | 국토를 토지 소유권 취득 주체에 따라 구분                               | 시, 도유지              |
| 거주지구분코드   | resdncSeCode          | 거주지구분코드                                               | ZZ                  |
| 거주지구분     | resdncSeCodeNm        | 거주지구분                                                 | 구분없음                |
| 국가기관구분코드  | nationInsttSeCode     | 국가기관구분코드                                              | 2                   |
| 국가기관구분    | nationInsttSeCodeNm   | 국가기관구분                                                | 지자체                 |
| 소유권변동원인코드 | ownshipChgCauseCode   | 소유권변동원인코드                                             | 5                   |
| 소유권변동원인   | ownshipChgCauseCodeNm | 소유권변동원인                                               | 성명(명칭)변경            |
| 소유권변동일자   | ownshipChgDe          | 소유권변동일자                                               | 34080               |
| 공유인수      | cnrsPsnCo             | 공유인수                                                  | 0                   |
| 데이터기준일자   | lastUpdtDt            | 데이터 작성 기준일자                                           | 42597               |

</div>

```python
from PublicDataReader import LandOwnership

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = LandOwnership(service_key)

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
      <th>법정동코드</th>
      <th>법정동명</th>
      <th>대장구분코드</th>
      <th>대장구분명</th>
      <th>지번</th>
      <th>집합건물일련번호</th>
      <th>건물동명</th>
      <th>건물층명</th>
      <th>건물호명</th>
      <th>...</th>
      <th>거주지구분코드</th>
      <th>거주지구분</th>
      <th>국가기관구분코드</th>
      <th>국가기관구분</th>
      <th>소유권변동원인코드</th>
      <th>소유권변동원인</th>
      <th>소유권변동일자</th>
      <th>공유인수</th>
      <th>데이터기준일자</th>
      <th>lndpclAr</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4113511000105420000</td>
      <td>4113511000</td>
      <td>경기도 성남시 분당구 백현동</td>
      <td>1</td>
      <td>토지대장</td>
      <td>542</td>
      <td>0017</td>
      <td>101</td>
      <td>1</td>
      <td>101</td>
      <td>...</td>
      <td>02</td>
      <td>시도내</td>
      <td>ZZ</td>
      <td>구분없음</td>
      <td>03</td>
      <td>소유권이전</td>
      <td>2011-11-02</td>
      <td>1</td>
      <td>2023-01-14</td>
      <td>34.04</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4113511000105420000</td>
      <td>4113511000</td>
      <td>경기도 성남시 분당구 백현동</td>
      <td>1</td>
      <td>토지대장</td>
      <td>542</td>
      <td>0017</td>
      <td>101</td>
      <td>1</td>
      <td>101</td>
      <td>...</td>
      <td>03</td>
      <td>읍면동내</td>
      <td>ZZ</td>
      <td>구분없음</td>
      <td>03</td>
      <td>소유권이전</td>
      <td>2011-11-02</td>
      <td>1</td>
      <td>2023-01-14</td>
      <td>34.04</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4113511000105420000</td>
      <td>4113511000</td>
      <td>경기도 성남시 분당구 백현동</td>
      <td>1</td>
      <td>토지대장</td>
      <td>542</td>
      <td>0017</td>
      <td>101</td>
      <td>1</td>
      <td>103</td>
      <td>...</td>
      <td>46</td>
      <td>관외(전남)</td>
      <td>ZZ</td>
      <td>구분없음</td>
      <td>03</td>
      <td>소유권이전</td>
      <td>2011-11-17</td>
      <td>1</td>
      <td>2023-01-14</td>
      <td>34.04</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4113511000105420000</td>
      <td>4113511000</td>
      <td>경기도 성남시 분당구 백현동</td>
      <td>1</td>
      <td>토지대장</td>
      <td>542</td>
      <td>0017</td>
      <td>101</td>
      <td>1</td>
      <td>103</td>
      <td>...</td>
      <td>46</td>
      <td>관외(전남)</td>
      <td>ZZ</td>
      <td>구분없음</td>
      <td>03</td>
      <td>소유권이전</td>
      <td>2011-11-17</td>
      <td>1</td>
      <td>2023-01-14</td>
      <td>34.04</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4113511000105420000</td>
      <td>4113511000</td>
      <td>경기도 성남시 분당구 백현동</td>
      <td>1</td>
      <td>토지대장</td>
      <td>542</td>
      <td>0017</td>
      <td>101</td>
      <td>10</td>
      <td>1001</td>
      <td>...</td>
      <td>03</td>
      <td>읍면동내</td>
      <td>ZZ</td>
      <td>구분없음</td>
      <td>03</td>
      <td>소유권이전</td>
      <td>2011-10-27</td>
      <td>1</td>
      <td>2023-01-14</td>
      <td>34.04</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 29 columns</p>
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

- 토지소유정보 조회

```python
pnu_code = next(it)
print(pnu_code)
df = api.get_data("1165010300200360000")
df.head()
```


    1165010300200360000
    

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>고유번호</th>
      <th>법정동코드</th>
      <th>법정동명</th>
      <th>대장구분코드</th>
      <th>대장구분명</th>
      <th>지번</th>
      <th>집합건물일련번호</th>
      <th>건물동명</th>
      <th>건물층명</th>
      <th>건물호명</th>
      <th>...</th>
      <th>거주지구분코드</th>
      <th>거주지구분</th>
      <th>국가기관구분코드</th>
      <th>국가기관구분</th>
      <th>소유권변동원인코드</th>
      <th>소유권변동원인</th>
      <th>소유권변동일자</th>
      <th>공유인수</th>
      <th>데이터기준일자</th>
      <th>lndpclAr</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1165010300200360000</td>
      <td>1165010300</td>
      <td>서울특별시 서초구 우면동</td>
      <td>2</td>
      <td>임야대장</td>
      <td>36</td>
      <td>0000</td>
      <td>0000</td>
      <td>0000</td>
      <td>0000</td>
      <td>...</td>
      <td>ZZ</td>
      <td>구분없음</td>
      <td>01</td>
      <td>중앙부처</td>
      <td>03</td>
      <td>소유권이전</td>
      <td>1964-04-01</td>
      <td>0</td>
      <td>2023-01-14</td>
      <td>14777</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 29 columns</p>
</div>






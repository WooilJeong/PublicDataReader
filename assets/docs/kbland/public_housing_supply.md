# 공공통계 주택공급 사용 가이드

- [KB부동산 데이터허브](https://data.kbland.kr/)


## 주택공급 데이터 목록

* [아파트 분양물량](#아파트-분양물량)
* [아파트 입주물량](#아파트-입주물량)
* [아파트 단지(분양)](#아파트-단지-분양)
* [아파트 단지(입주)](#아파트-단지-입주)
* [주택공급실적](#주택공급실적)
* [청약통장가입현황](#아파트-분양물량)


## 참고

- PublicDataReader의 code_bdong() 메서드로 지역코드(시도코드)를 조회 가능

</div>

```python
import PublicDataReader as pdr
code = pdr.code_bdong()
code.head()
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
      <th>0</th>
      <td>11</td>
      <td>서울특별시</td>
      <td>11000</td>
      <td></td>
      <td>1100000000</td>
      <td></td>
      <td></td>
      <td>19880423</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>11</td>
      <td>서울특별시</td>
      <td>11110</td>
      <td>종로구</td>
      <td>1111000000</td>
      <td></td>
      <td></td>
      <td>19880423</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>11</td>
      <td>서울특별시</td>
      <td>11110</td>
      <td>종로구</td>
      <td>1111010100</td>
      <td>청운동</td>
      <td></td>
      <td>19880423</td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td>11</td>
      <td>서울특별시</td>
      <td>11110</td>
      <td>종로구</td>
      <td>1111010200</td>
      <td>신교동</td>
      <td></td>
      <td>19880423</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td>11</td>
      <td>서울특별시</td>
      <td>11110</td>
      <td>종로구</td>
      <td>1111010300</td>
      <td>궁정동</td>
      <td></td>
      <td>19880423</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>



## 아파트 분양물량

* [맨 위로](#공공통계-주택공급-사용-가이드)

### 입력 명세

<div align="center">
</div>

### 출력 명세

<div align="center">
</div>

### 샘플 코드

- 상세비중구분: 0: 총세대수, 1: 유형별 세대수
- 기간구분: 0: 월별, 1: 년별, 2: 반기별
- 법정동코드: 법정동코드 10자리

```python
from PublicDataReader import Kbland
api = Kbland()
params = {
    "상세비중구분": 0,
    "기간구분": 0,
    "법정동코드": 법정동코드,
}

api = Kbland()
df = api.아파트_분양물량(**params)
```


## 아파트 입주물량

### 입력 명세

<div align="center">
</div>

### 출력 명세

<div align="center">
</div>

### 샘플 코드

- 기간구분: 0: 월별, 1: 년별, 2: 반기별
- 법정동코드: 법정동코드 10자리

```python
from PublicDataReader import Kbland
api = Kbland()
params = {
    "기간구분": 0,
    "법정동코드": 법정동코드,
}

api = Kbland()
df = api.아파트_입주물량(**params)
```

## 아파트 단지 분양

### 입력 명세

<div align="center">
</div>

### 출력 명세

<div align="center">
</div>

### 샘플 코드

- 임대포함여부: 0: 제외, 1: 포함
- 정렬구분: 1: 청약임박순, 2: 분양일정순, 3: 분양가순, 4: 세대수순
- 정렬순서: 0: 오름차순, 1: 내림차순
- 조회시작년월: e.g. 202401
- 조회종료년월: e.g. 202407
- 법정동코드: 법정동코드 10자리

```python
from PublicDataReader import Kbland
api = Kbland()
params = {
    "법정동코드": 법정동코드,
    "임대포함여부": "1",
    "정렬구분": "3",
    "정렬순서": "1",
    "조회시작년월": "201401",
    "조회종료년월": "202612",   
}

api = Kbland()
df = api.아파트_단지_분양(**params)
```

## 아파트 단지 입주

### 입력 명세

<div align="center">
</div>

### 출력 명세

<div align="center">
</div>

### 샘플 코드

- 임대포함여부: 0: 제외, 1: 포함
- 정렬구분: 1: 입주일순, 2: 세대수순
- 정렬순서: 0: 오름차순, 1: 내림차순
- 조회시작년월: e.g. 202401
- 조회종료년월: e.g. 202407
- 법정동코드: 법정동코드 10자리

```python
from PublicDataReader import Kbland
api = Kbland()
params = {
    "법정동코드": 법정동코드,
    "임대포함여부": "1",
    "정렬구분": "2",
    "정렬순서": "1",
    "조회시작년월": "202401",
    "조회종료년월": "202612",   
}

api = Kbland()
df = api.아파트_단지_입주(**params)
```

## 주택공급실적

### 입력 명세

<div align="center">
</div>

### 출력 명세

<div align="center">
</div>

### 샘플 코드

- dtailDataSelct: 1: 전체, 2: 공급단계별, 3: 주택유형별
- 공급단계별 조회인 경우
  - splyStge: 01: 인허가 02: 착공 03: 분양 04: 준공
- 주택유형별 조회인 경우
  - husePtrn: 1: 아파트 2: 비아파트
- 법정동코드: 법정동코드 10자리

```python
from PublicDataReader import Kbland
api = Kbland()
params = {
    "법정동코드": 법정동코드,
    "dtailDataSelct": "1",
}

api = Kbland()
df = api.주택공급실적(**params)
```

## 청약통장가입현황

### 입력 명세

<div align="center">
</div>

### 출력 명세

<div align="center">
</div>

### 샘플 코드

- scipClsfiDstic: 00: 전체, 01: 주택청약종합저축, 03: 청약부금, 04: 청약예금
- 법정동코드: 법정동코드 10자리

```python
from PublicDataReader import Kbland
api = Kbland()
params = {
    "법정동코드": 법정동코드,
    "scipClsfiDstic": "00",
}

api = Kbland()
df = api.청약통장가입현황(**params)
```

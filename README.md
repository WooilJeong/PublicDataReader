# PublicDataReader
Open Source Public Data Reader

## Overview
Current Version : 0.0.9

**History**  

```
- v0.0.9 (2020-02-04)
AptDetailReader 메서드 수정 - numOfRows
인증키 에러 문구 추가 - OpenAPI 인증키가 잘못 초기화 된 경우 경고 문구 출력
```

## Installation
```bash
pip install PublicDataReader
```

## Usage
### 국토교통부 실거래가 정보 - 아파트매매 실거래자료

```python
import PublicDataReader as pdr

serviceKey = "<<YOUR API SERVICE KEY>>"
Apt = pdr.AptTransactionReader(serviceKey)

# 특정 월 데이터 조회
df_code = Apt.CodeFinder("백현동")                           # 지역코드 : 41135
df = Apt.DataReader("41135", "201911")                     # 지역코드(LAWD_CD), 계약월(DEAL_YMD)

# 특정 기간 데이터 조회
df_sum = Apt.DataCollector("41135", "2019-01", "2019-11")  # 지역코드, 시작 월, 종료 월

# 동 별 데이터 집계 (중앙값, 평균값, 최솟값, 최댓값, 표준편차, 거래량)
df_agg = Apt.Agg(df)
df_sum_agg = Apt.Agg(df_sum)
```

## Requirements
python >= 3.7.4

## Contact
email : wooil@kakao.com

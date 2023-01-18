# 서울시 교통 관련 데이터 사용 가이드

<div align="center">


| **서비스명**                                        | **카테고리명**     |
| ---------------------------------------------------- | ------------------ |
| [서울시 지하철호선별 역별 승하차 인원 정보](http://data.seoul.go.kr/dataList/OA-12914/S/1/datasetView.do)            | 지하철승하차       |
| [서울시 버스노선별 정류장별 승하차 인원 정보](http://data.seoul.go.kr/dataList/OA-12912/S/1/datasetView.do)          | 버스승하차         |

</div>

## 서울 열린데이터 광장 교통 관련 정보 조회 서비스

```python
# 1. 라이브러리 임포트 및 버전 확인하기
import PublicDataReader as pdr
print(pdr.__version__)

# 2. 서울 열린데이터 광장 OpenAPI 서비스 인증키 입력하기
serviceKey = "서울 열린데이터 광장에서 발급받은 서비스 키"

# 3. 데이터 조회 세션 정의하기
# debug: True이면 모든 메시지 출력, False이면 오류 메시지만 출력 (기본값: False)
tp = pdr.Transportation(serviceKey, debug=True)

# 4. 서울시 지하철호선별 역별 승하차 인원 정보
category = "지하철승하차"
date = "20211001"

df = tp.read_data(category=category, date=date)

# 5. 서울시 버스노선별 정류장별 승하차 인원 정보
category = "버스승하차"
date = "20211001"

df = tp.read_data(category=category, date=date)
```
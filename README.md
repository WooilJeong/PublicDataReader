# PublicDataReader
Open Source Public Data Reader

## Overview
Current Version : 0.0.4

## Installation

```
pip install PublicDataReader
```

## Usage
### 국토교통부 실거래가 정보 - 아파트매매 실거래자료
https://www.data.go.kr/dataset/3050988/openapi.do

```python
import PublicDataReader as pdr

serviceKey = "<<YOUR API SERVICE KEY>>"
Apt = pdr.AptTransaction(serviceKey)

Apt.CodeFinder("백현동")            # 지역코드 : 41135
Apt.DataReader("41135", "201911") # 지역코드(LAWD_CD), 계약월(DEAL_YMD)
```

## Requirements

## Contact
email : wooil@kakao.com

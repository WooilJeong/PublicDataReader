<div align="center">

<img src="https://github.com/WooilJeong/PublicDataReader/blob/main/assets/img/logo.png?raw=true" width="500" />

<b>공공 데이터 조회를 위한 오픈소스 파이썬 라이브러리</b><br>
<b>🚀`pip install PublicDataReader --upgrade`</b>

[![Pypi 패키지 버전](https://img.shields.io/pypi/v/publicdatareader.svg)](https://pypi.org/project/publicdatareader/)
[![License](https://img.shields.io/pypi/l/ansicolortags.svg)](https://img.shields.io/pypi/l/ansicolortags.svg)
[![Python](https://img.shields.io/badge/Official-Docs-tomato)](https://wooiljeong.github.io/PublicDataReader/)
[![Downloads](https://static.pepy.tech/badge/publicdatareader)](https://pepy.tech/project/publicdatareader)  
[![오픈채팅](https://img.shields.io/badge/오픈채팅-사용자모임-yellow?logo=KakaoTalk)](https://open.kakao.com/o/gbt2Pl2d)

<br>

<div align="left">

## PublicDataReader

PublicDataReader는 공공 데이터를 자동으로 조회할 수 있는 파이썬 라이브러리입니다. 이 라이브러리로 공공데이터포털과 국가통계포털(KOSIS)과 같이 오픈 API 서비스로 제공하는 공공 데이터를 쉽게 조회할 수 있습니다. 인증키가 필요한 공공 데이터는 인증키를 사용하여 조회할 수 있고, 인증키가 필요하지 않은 데이터는 별도의 인증 절차 없이 조회할 수 있습니다. PublicDataReader를 이용하면 일반적인 공공 데이터 조회 과정에서 필요한 API 명세 찾기, 요청 작성, 반환된 데이터 정리 과정을 자동으로 처리할 수 있고, 웹에 공개된 데이터를 조회할 때도 데이터 수집과 가공 과정을 자동화할 수 있습니다. 이를 통해 코드 작성이 간결해지고 공공 데이터 조회 작업이 편리해집니다.


<br>

## 설치방법

1. 운영체제(OS)에 따라 아래 중 하나를 선택합니다.

- Windows: CMD(명령 프롬프트) 실행
- Mac: Terminal(터미널) 실행

2. 아래 Shell 명령어를 입력 후 실행합니다.

```bash
pip install PublicDataReader --upgrade
```

<br>

## 사용 가이드

<div align="center">

| 사용 가이드 목록                                                                                                                | 플랫폼명                                                      | 인증키 필요 |
| :------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------: | :---------: |
| [국토교통부 부동산 실거래가 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/TransactionPrice.md) | [공공데이터포털](https://www.data.go.kr/)                        | ✔️         |
| [국토교통부 건축물대장정보 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/BuildingLedger.md)    | [공공데이터포털](https://www.data.go.kr/)                        | ✔️         |
| [국토교통부 건축인허가정보 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/BuildingLicense.md)    | [공공데이터포털](https://www.data.go.kr/)                        | ✔️         |
| [국토교통부 주택인허가정보 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/HousingLicense.md)    | [공공데이터포털](https://www.data.go.kr/)                        | ✔️         |
| [국토교통부 토지임야정보 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/LandForestLedger.md)   | [공공데이터포털](https://www.data.go.kr/)                        | ✔️         |
| [국토교통부 토지소유정보 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/LandOwnership.md)   | [공공데이터포털](https://www.data.go.kr/)                        | ✔️         |
| [소상공인시장진흥공단 상가(상권)정보 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/SmallShop.md)   | [공공데이터포털](https://www.data.go.kr/)                        | ✔️         |
| [한국자산관리공사 공매물건 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/Kamco.md)             | [공공데이터포털](https://www.data.go.kr/)                        | ✔️         |
| [국세청 사업자등록정보 진위확인 및 상태조회 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/Nts.md)     | [공공데이터포털](https://www.data.go.kr/)                        | ✔️         |
| [한국부동산원 부동산 종합 정보 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/Reb.md)            | [공공데이터포털](https://www.data.go.kr/)                        | ✔️         |
| [KOSIS 통계정보 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/kosis/Kosis.md)                 | [국가통계포털(KOSIS)](https://kosis.kr/openapi/index/index.jsp) | ✔️         |
| [ECOS 한국은행 경제통계 서비스 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/ecos/ecos.md)                 | [한국은행 경제통계시스템(ECOS)](https://ecos.bok.or.kr/api/) | ✔️         |
| [서울시 교통 관련 데이터 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/seoul/Transportation.md)     | [서울 열린데이터 광장](https://data.seoul.go.kr/)                  | ✔️         |
| [국가공간정보 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/vworld/VworldData.md)               | [공간정보 오픈플랫폼(V-Word)](https://www.vworld.kr/v4po_main.do)  | ✔️         |
| [KB통계 주택가격동향조사 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/kbland/Kbland.md)            | [KB부동산](https://data.kbland.kr/)                          | ➖         |
| [FRED(Federal Reserve Economic Data) 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/fred/fred.md)            | [FRED(Federal Reserve Economic Data)](https://fred.stlouisfed.org/docs/api/fred/)                          | ✔️         |

</div>

<br>


## 튜토리얼

- 공공데이터포털
  - [부동산 실거래가 조회하기](https://wooiljeong.github.io/python/public_data_reader_01/)
  - [건축물대장 데이터 조회하기](https://wooiljeong.github.io/python/public_data_reader_03/)
  - [건축인허가 데이터 조회하기](https://wooiljeong.github.io/python/pdr-building-license/)
  - [주택인허가 데이터 조회하기](https://wooiljeong.github.io/python/pdr-housing-license/)
  - [토지대장 및 임야대장 조회하기](https://wooiljeong.github.io/python/pdr-land-forest-ledger/)
  - [토지소유정보 조회하기](https://wooiljeong.github.io/python/pdr-land-ownership/)
  - [상가업소 데이터 조회하기](https://wooiljeong.github.io/python/public_data_reader_02/)
  - [한국자산관리공사 캠코 공매물건 조회하기](https://wooiljeong.github.io/python/pdr-kamco/)
  - [사업자등록정보 진위확인 및 상태조회하기](https://wooiljeong.github.io/python/pdr-nts/)

- 국가통계포털(KOSIS)
  - [Python으로 KOSIS 데이터 조회하기](https://wooiljeong.github.io/python/pdr-kosis/)
  - [주민등록인구 데이터 조회하기](https://wooiljeong.github.io/python/pdr-kosis-ex1/)
  - [미분양주택현황 데이터 조회하기](https://wooiljeong.github.io/python/pdr-kosis-ex2/)

- 한국은행(ECOS)
  - [ECOS 한국은행 경제통계 조회하기](https://wooiljeong.github.io/python/pdr-ecos/)

- KB부동산
  - [KB부동산 주택가격동향조사 데이터 조회하기](https://wooiljeong.github.io/python/pdr-kbland/)

- 기타
  - [법정동코드와 행정동코드 조회하기](https://wooiljeong.github.io/python/pdr-code/)


## 참고

- **Google Colab 실습**  
  - [Colab 부동산 실거래가 조회 실습](https://colab.research.google.com/drive/12SGCX4dwQfOwK-nIlG8jUOGSG80xE_o1?pli=1)
  - [Colab 건축물대장 정보 조회 실습](https://colab.research.google.com/drive/1g_vwaqrhyZ_HAifxrKd_AFR_8U29elGW)
  - [Colab 소상공인 상가업소 정보 조회 실습](https://colab.research.google.com/drive/1wQZcJZfwfl_5y_NK5vbz__95gRt0xwrb)

- **공식문서**
  - [Documents](https://wooiljeong.github.io/PublicDataReader/)

- **문의**  
  - **이메일**: wooil@kakao.com  
  - **카카오톡 오픈채팅방**: [PublicDataReader 사용자 모임](https://open.kakao.com/o/gbt2Pl2d)  

<br>

## 기여자


<a href="https://github.com/wooiljeong/PublicDataReader/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=wooiljeong/PublicDataReader" />
</a>

<br>



<div align=center>

<!-- [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FWooilJeong%2FPublicDataReader&count_bg=%2379C83D&title_bg=%23555555&icon=github.svg&icon_color=%23FFFFFF&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) -->

</div>
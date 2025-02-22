<div align="center">

<img src="https://github.com/WooilJeong/PublicDataReader/blob/main/assets/img/logo.png?raw=true" width="500" />

<b>공공 데이터 조회를 위한 오픈소스 파이썬 라이브러리</b><br>
<b>🚀`pip install PublicDataReader --upgrade`</b>

[![Pypi 패키지 버전](https://img.shields.io/pypi/v/publicdatareader.svg)](https://pypi.org/project/publicdatareader/)
[![License](https://img.shields.io/pypi/l/ansicolortags.svg)](https://img.shields.io/pypi/l/ansicolortags.svg)
[![pandas](https://img.shields.io/badge/pandas-2.2.3-blue)](https://pypi.org/project/pandas/)
[![requests](https://img.shields.io/badge/requests-2.32.3-green)](https://pypi.org/project/requests/)
[![xmltodict](https://img.shields.io/badge/xmltodict-0.14.2-orange)](https://pypi.org/project/xmltodict/)
[![beautifulsoup4](https://img.shields.io/badge/beautifulsoup4-4.13.3-purple)](https://pypi.org/project/beautifulsoup4/)
[![Downloads](https://static.pepy.tech/badge/publicdatareader)](https://pepy.tech/project/publicdatareader)  
[![오픈채팅](https://img.shields.io/badge/오픈채팅-PublicDataReader_사용자모임-yellow?logo=KakaoTalk)](https://open.kakao.com/o/gbt2Pl2d)


<br>

<div align="left">

## PublicDataReader

PublicDataReader는 공공 데이터를 자동으로 조회할 수 있는 파이썬 라이브러리입니다. 이 라이브러리로 공공데이터포털과 국가통계포털(KOSIS)과 같이 오픈 API 서비스로 제공하는 공공 데이터를 쉽게 조회할 수 있습니다. 인증키가 필요한 공공 데이터는 인증키를 사용하여 조회할 수 있고, 인증키가 필요하지 않은 데이터는 별도의 인증 절차 없이 조회할 수 있습니다. PublicDataReader를 이용하면 일반적인 공공 데이터 조회 과정에서 필요한 API 명세 찾기, 요청 작성, 반환된 데이터 정리 과정을 자동으로 처리할 수 있고, 웹에 공개된 데이터를 조회할 때도 데이터 수집과 가공 과정을 자동화할 수 있습니다. 이를 통해 코드 작성이 간결해지고 공공 데이터 조회 작업이 편리해집니다.


<br>

## 설치 방법

1. 운영체제(OS)에 따라 아래 중 하나를 선택합니다.

- Windows: CMD(명령 프롬프트) 실행
- Mac: Terminal(터미널) 실행

2. 아래 Shell 명령어를 입력 후 실행합니다.

```bash
pip install PublicDataReader --upgrade
```

<br>

## 사용 방법

아래는 PublicDataReader 사용법을 자세히 설명한 가이드 문서들입니다. 이 문서들을 통해 라이브러리가 어떤 오픈 API 서비스를 지원하는지 알아볼 수 있습니다. 데이터를 조회할 때 필요한 정보와 함께, 코드 예시도 제공되어 있어 실제 사용에 바로 활용할 수 있습니다.

<div align="center">

| 사용 가이드 목록                                                                                                                | 플랫폼명                                                      | 인증키 |
| :------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------- | :--------- |
| [FRED(Federal Reserve Economic Data) 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/fred/fred.md)            | [FRED(Federal Reserve Economic Data)](https://fred.stlouisfed.org/docs/api/fred/)                          | 필요         |
| [국토교통부 부동산 실거래가 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/TransactionPrice.md) | [공공데이터포털](https://www.data.go.kr/)                        | 필요         |
| [국토교통부 건축물대장정보 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/BuildingLedger.md)    | [공공데이터포털](https://www.data.go.kr/)                        | 필요         |
| [국토교통부 건축인허가정보 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/BuildingLicense.md)    | [공공데이터포털](https://www.data.go.kr/)                        | 필요         |
| [국토교통부 주택인허가정보 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/HousingLicense.md)    | [공공데이터포털](https://www.data.go.kr/)                        | 필요         |
| [국토교통부 토지임야정보 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/LandForestLedger.md)   | [공공데이터포털](https://www.data.go.kr/)                        | 필요         |
| [국토교통부 토지소유정보 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/LandOwnership.md)   | [공공데이터포털](https://www.data.go.kr/)                        | 필요         |
| [소상공인시장진흥공단 상가(상권)정보 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/SmallShop.md)   | [공공데이터포털](https://www.data.go.kr/)                        | 필요         |
| [한국자산관리공사 공매물건 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/Kamco.md)             | [공공데이터포털](https://www.data.go.kr/)                        | 필요         |
| [국세청 사업자등록정보 진위확인 및 상태조회 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/Nts.md)     | [공공데이터포털](https://www.data.go.kr/)                        | 필요         |
| [한국부동산원 부동산 종합 정보 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal/Reb.md)            | [공공데이터포털](https://www.data.go.kr/)                        | 필요         |
| [KOSIS 통계정보 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/kosis/Kosis.md)                 | [국가통계포털(KOSIS)](https://kosis.kr/openapi/index/index.jsp) | 필요         |
| [ECOS 한국은행 경제통계 서비스 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/ecos/ecos.md)                 | [한국은행 경제통계시스템(ECOS)](https://ecos.bok.or.kr/api/) | 필요         |
| [서울시 교통 관련 데이터 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/seoul/Transportation.md)     | [서울 열린데이터 광장](https://data.seoul.go.kr/)                  | 필요         |
| [국가공간정보 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/vworld/VworldData.md)               | [공간정보 오픈플랫폼(V-Word)](https://www.vworld.kr/v4po_main.do)  | 필요         |
| [KB통계 주택가격동향조사 사용 가이드](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/kbland/Kbland.md)            | [KB부동산](https://data.kbland.kr/)                          | 불필요         |

</div>

<br>


## 활용 사례 모음

아래는 PublicDataReader 활용 사례 모음입니다. 이들 사례를 통해, 실제 사용자들이 어떻게 이 라이브러리를 다양하고 창의적인 방식으로 활용하고 있는지 알아볼 수 있습니다. PublicDataReader를 사용한 재미있는 프로젝트가 있다면 자유롭게 PR을 보내주세요.

<div align="center">


| 제목                                              | 출처       |
|:-------------------------------------------------|:----------|
| [공공데이터를 활용한 우리 동네 아파트 실거래가 분석](https://www.youtube.com/watch?v=31EX6TLao5g&t=852s) | [나도코딩 유튜브 채널](https://www.youtube.com/@nadocoding) |
| [Python 국세청홈택스 사업자등록상태 조회 방법](https://blog.naver.com/devradio/223419187567) | [심심한세상](https://blog.naver.com/devradio) |
| [[부동산 데이터 수집] KOSIS 시군구별 미분양 현황 및 준공후 미분양 데이터 조회(파이썬)](https://growing-datascientist.tistory.com/136) | [레디코의 인사이트창고](https://growing-datascientist.tistory.com/) |
| [[부동산 데이터 수집] KOSIS 시군구별 주택 건설 착공 실적(파이썬)](https://growing-datascientist.tistory.com/137) | [레디코의 인사이트창고](https://growing-datascientist.tistory.com/) |
| [[부동산 데이터 수집] 국가통계포털/부동산원 아파트 전세가율 상하락요인 확인(파이썬)](https://growing-datascientist.tistory.com/138) | [레디코의 인사이트창고](https://growing-datascientist.tistory.com/) |
| [[부동산 데이터 수집] 국가통계포털 지역별 전월세전환율(파이썬 API) 금리와의 관계](https://growing-datascientist.tistory.com/139) | [레디코의 인사이트창고](https://growing-datascientist.tistory.com/) |
| [파이썬으로 부동산 매매가 조회기 만들기 - 1. 만들기 시작하기, API 키 발급받기](https://drop-by-drop-fills-the-tub.tistory.com/65) | [밑빠진 독에 티끌붓기](https://drop-by-drop-fills-the-tub.tistory.com/) |
| [파이썬으로 부동산 매매가 조회기 만들기 - 2. 지역 구분별 코드 먼저 준비하기](https://drop-by-drop-fills-the-tub.tistory.com/66) | [밑빠진 독에 티끌붓기](https://drop-by-drop-fills-the-tub.tistory.com/) |
| [파이썬으로 부동산 매매가 조회기 만들기 - 3. 지역별 코드 컨버터 만들기](https://drop-by-drop-fills-the-tub.tistory.com/67) | [밑빠진 독에 티끌붓기](https://drop-by-drop-fills-the-tub.tistory.com/) |
| [파이썬으로 부동산 매매가 조회기 만들기 - 5. 서울 이외의 지역 매매가를 조회하는 메소드 만들기](https://drop-by-drop-fills-the-tub.tistory.com/69) | [밑빠진 독에 티끌붓기](https://drop-by-drop-fills-the-tub.tistory.com/) |
| [파이썬으로 부동산 매매가 조회기 만들기 - 6. 조건 필터와 엑셀로 내보내기 만들어보기](https://drop-by-drop-fills-the-tub.tistory.com/70) | [밑빠진 독에 티끌붓기](https://drop-by-drop-fills-the-tub.tistory.com/) |
| [ECOS api와 PublicDataReader 사용해 경제 데이터 가져오기](https://blog.naver.com/won19600/223361269999) | [경의선통학중](https://blog.naver.com/won19600) |
| [KOSPI 지수와 장단기 금리차 간 상관계수 분석하기](https://blog.naver.com/won19600/223369431187) | [경의선통학중](https://blog.naver.com/won19600) |
| [Python으로 부동산 자료 크롤링(1)_아파트단지별 매물 조회](https://blog.naver.com/neo_in_matrix/223080501154) | [이것 저것 닥치는 대로](https://blog.naver.com/neo_in_matrix) |
| [Python으로 부동산 자료 크롤링(2)_아파트단지별 정보 조회](https://blog.naver.com/neo_in_matrix/223082116325) | [이것 저것 닥치는 대로](https://blog.naver.com/neo_in_matrix) |
| [Python으로 부동산 자료 크롤링(3)_법정동내 아파트단지 고유 코드 조회](https://blog.naver.com/neo_in_matrix/223082171378) | [이것 저것 닥치는 대로](https://blog.naver.com/neo_in_matrix) |
| [Python으로 부동산 자료 크롤링(4)_공공데이터 & PublicDataReader 모듈을 이용한 아파트 실거래가 조회](https://blog.naver.com/neo_in_matrix/223082470340) | [이것 저것 닥치는 대로](https://blog.naver.com/neo_in_matrix) |
| [Python으로 부동산 자료 크롤링(5)_법정동코드 Requests로 얻기](https://blog.naver.com/neo_in_matrix/223086804052) | [이것 저것 닥치는 대로](https://blog.naver.com/neo_in_matrix) |
| [용인 수지 아파트 실거래가 조회하기(feat. PublicDataReader)](https://blog.naver.com/yhhoegwan/223085305300) | [영희회관](https://blog.naver.com/yhhoegwan) |
| [[Python] PublicDataReader 라이브러리를 사용한 FRED 데이터 수집](https://unfinishedgod.netlify.app/2023/07/26/python-publicdatareader-fred/) | [미완성의신](https://unfinishedgod.netlify.app/) |
| [Django_자산관리 Web Program Project_01](https://akym00.tistory.com/2) | [Asset_Web_Program](https://akym00.tistory.com/) |
| [Django_자산관리 W_P_Project_02..[아파트 시세 조회]](https://akym00.tistory.com/3) | [Asset_Web_Program](https://akym00.tistory.com/) |
| [[Python Data Analytics] OpenAPI를 활용한 데이터 호출&적재](https://data-is-power.tistory.com/217) | [데이터로 보는 세상](https://data-is-power.tistory.com/) |
| [부동산 실거래가 조회하기](https://wooiljeong.github.io/python/public_data_reader_01/) | [정우일 블로그](https://wooiljeong.github.io) |
| [건축물대장 데이터 조회하기](https://wooiljeong.github.io/python/public_data_reader_03/) | [정우일 블로그](https://wooiljeong.github.io) |
| [건축인허가 데이터 조회하기](https://wooiljeong.github.io/python/pdr-building-license/) | [정우일 블로그](https://wooiljeong.github.io) |
| [주택인허가 데이터 조회하기](https://wooiljeong.github.io/python/pdr-housing-license/) | [정우일 블로그](https://wooiljeong.github.io) |
| [토지대장 및 임야대장 조회하기](https://wooiljeong.github.io/python/pdr-land-forest-ledger/) | [정우일 블로그](https://wooiljeong.github.io) |
| [토지소유정보 조회하기](https://wooiljeong.github.io/python/pdr-land-ownership/) | [정우일 블로그](https://wooiljeong.github.io) |
| [상가업소 데이터 조회하기](https://wooiljeong.github.io/python/public_data_reader_02/) | [정우일 블로그](https://wooiljeong.github.io) |
| [한국자산관리공사 캠코 공매물건 조회하기](https://wooiljeong.github.io/python/pdr-kamco/) | [정우일 블로그](https://wooiljeong.github.io) |
| [사업자등록정보 진위확인 및 상태조회하기](https://wooiljeong.github.io/python/pdr-nts/) | [정우일 블로그](https://wooiljeong.github.io) |
| [Python으로 KOSIS 데이터 조회하기](https://wooiljeong.github.io/python/pdr-kosis/) | [정우일 블로그](https://wooiljeong.github.io) |
| [주민등록인구 데이터 조회하기](https://wooiljeong.github.io/python/pdr-kosis-ex1/) | [정우일 블로그](https://wooiljeong.github.io) |
| [미분양주택현황 데이터 조회하기](https://wooiljeong.github.io/python/pdr-kosis-ex2/) | [정우일 블로그](https://wooiljeong.github.io) |
| [ECOS 한국은행 경제통계 조회하기](https://wooiljeong.github.io/python/pdr-ecos/) | [정우일 블로그](https://wooiljeong.github.io) |
| [KB부동산 주택가격동향조사 데이터 조회하기](https://wooiljeong.github.io/python/pdr-kbland/) | [정우일 블로그](https://wooiljeong.github.io) |
| [법정동코드와 행정동코드 조회하기](https://wooiljeong.github.io/python/pdr-code/) | [정우일 블로그](https://wooiljeong.github.io) |

</div>


<br>

## 구글 코랩(Google Colab)

- [Colab 부동산 실거래가 조회 실습](https://colab.research.google.com/drive/12SGCX4dwQfOwK-nIlG8jUOGSG80xE_o1?pli=1)
- [Colab 건축물대장 정보 조회 실습](https://colab.research.google.com/drive/1g_vwaqrhyZ_HAifxrKd_AFR_8U29elGW)
- [Colab 소상공인 상가업소 정보 조회 실습](https://colab.research.google.com/drive/1wQZcJZfwfl_5y_NK5vbz__95gRt0xwrb)

<br>

## 사용 관련 문의

- **카카오톡 오픈채팅방**: [![오픈채팅](https://img.shields.io/badge/오픈채팅-PublicDataReader_사용자모임-yellow?logo=KakaoTalk)](https://open.kakao.com/o/gbt2Pl2d)
- **이메일**: wooil@kakao.com

<br>

## 기여자

[![PublicDataReader contributors](https://contrib.rocks/image?repo=wooiljeong/PublicDataReader)](https://github.com/wooiljeong/PublicDataReader/graphs/contributors)

<br>


<div align=center>

<!-- [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FWooilJeong%2FPublicDataReader&count_bg=%2379C83D&title_bg=%23555555&icon=github.svg&icon_color=%23FFFFFF&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) -->

</div>

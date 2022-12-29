<div align="center">

![PNG](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/img/logo_v1.png?raw=true)

<b>공공 데이터 조회를 위한 오픈소스 파이썬 라이브러리</b><br>
<b>🚀`pip install PublicDataReader --upgrade`</b>

[![Pypi 패키지 버전](https://img.shields.io/pypi/v/publicdatareader.svg)](https://pypi.org/project/publicdatareader/)
[![License](https://img.shields.io/pypi/l/ansicolortags.svg)](https://img.shields.io/pypi/l/ansicolortags.svg)
[![Python](https://img.shields.io/badge/Official-Docs-tomato)](https://wooiljeong.github.io/PublicDataReader/)  
[![오픈채팅](https://img.shields.io/badge/오픈채팅-사용자모임-yellow?logo=KakaoTalk)](https://open.kakao.com/o/gbt2Pl2d)

<br>

<div align="left">

## PublicDataReader

PublicDataReader는 공공 데이터를 자동으로 조회할 수 있는 파이썬 라이브러리입니다. 공공데이터포털이나 국가통계포털과 같이 Open API 서비스로 제공하는 데이터의 경우 인증키를 사용하여 간편하게 공공 데이터를 조회할 수 있습니다. 이와 달리 Open API 서비스로 제공하지 않고 웹에 공개되는 데이터의 경우 별도의 인증키 없이 더 쉽게 데이터를 조회할 수 있습니다. 일반적인 공공 데이터 조회 과정에서는 API 명세를 찾고, 적절한 형식으로 요청을 작성하고, 반환된 데이터를 정리하는 과정이 필요합니다. 또한, 웹에 공개된 데이터를 조회하는 과정에서 역시 데이터를 원하는 형식에 맞게 수집하고 가공하는 과정이 필요합니다. PublicDataReader는 이러한 과정을 자동화해주기 때문에 코드 작성이 간결해집니다.

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

### 플랫폼 별 상세 사용 방법

- [공공데이터포털 데이터 조회 방법 예시](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/portal.md)
  - 국토교통부 실거래가 정보 조회 서비스
  - 국토교통부 건축물대장정보 서비스
  - 소상공인 상가업소 정보 조회 서비스
  - 한국자산관리공사 공매물건 조회 서비스
  - 국세청 사업자등록정보 진위확인 및 상태조회 서비스
- [KOSIS 국가통계포털 데이터 조회 방법 예시](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/kosis.md)
  - KOSIS 통계 자료 조회 방법
- [서울 열린데이터광장 데이터 조회 방법 예시](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/seoul.md)
  - 서울시 지하철호선별 역별 승하차 인원 정보
  - 서울시 버스노선별 정류장별 승하차 인원 정보
- [Vworld 데이터 조회 방법 예시](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/vworld.md)
  - Vworld Data API를 이용한 공간정보 조회 방법
- [KB부동산 데이터허브 조회 방법 예시](https://github.com/WooilJeong/PublicDataReader/blob/main/assets/docs/kbland.md) - **인증키 필요 없음**
  - 주택가격동향조사 데이터 조회 방법


<br>


## 튜토리얼

- 공공데이터포털
  - [부동산 실거래가 조회하기](https://wooiljeong.github.io/python/public_data_reader_01/)
  - [건축물대장 데이터 조회하기](https://wooiljeong.github.io/python/public_data_reader_03/)
  - [상가업소 데이터 조회하기](https://wooiljeong.github.io/python/public_data_reader_02/)
  - [한국자산관리공사 캠코 공매물건 조회하기](https://wooiljeong.github.io/python/pdr-kamco/)
  - [사업자등록정보 진위확인 및 상태조회하기](https://wooiljeong.github.io/python/pdr-nts/)

- KOSIS
  - [Python으로 KOSIS 데이터 조회하기](https://wooiljeong.github.io/python/pdr-kosis/)
  - [주민등록인구 데이터 조회하기](https://wooiljeong.github.io/python/pdr-kosis-ex1/)
  - [미분양주택현황 데이터 조회하기](https://wooiljeong.github.io/python/pdr-kosis-ex2/)

- KB부동산
  - [KB부동산 주택가격동향조사 데이터 조회하기](https://wooiljeong.github.io/python/pdr-kbland/)


## 참고


- 이용 가능한 Open API 플랫폼 웹 사이트
  - [KOSIS 국가통계포털](https://kosis.kr/index/index.do)
  - [공공데이터포털](https://www.data.go.kr/)
  - [서울 열린데이터광장](https://data.seoul.go.kr/)
  - [브이월드(Vworld) 공간정보 오픈플랫폼](https://www.vworld.kr/dev/v4api.do)


- **실습코드**  
  - [Colab에서 PublicDataReader 실행하기](https://colab.research.google.com/drive/1fgT0D_tP-JyglobtDFfYQ6wQXfWWujIV?usp=sharing)  

- **공식문서**
  - [Docs](https://wooiljeong.github.io/PublicDataReader/)

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

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FWooilJeong%2FPublicDataReader&count_bg=%2379C83D&title_bg=%23555555&icon=github.svg&icon_color=%23FFFFFF&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</div>
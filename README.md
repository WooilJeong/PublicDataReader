# PublicDataReader

<div align="center">

![PNG](./assets/img/logo_v1.png)

<b>공공 데이터 조회를 위한 오픈소스 로우코드 파이썬 라이브러리</b><br>
<b>🚀`pip install PublicDataReader --upgrade`</b>

[![Pypi 패키지 버전](https://img.shields.io/pypi/v/publicdatareader.svg)](https://pypi.org/project/publicdatareader/)
[![License](https://img.shields.io/pypi/l/ansicolortags.svg)](https://img.shields.io/pypi/l/ansicolortags.svg)
[![Python](https://img.shields.io/badge/Official-Docs-tomato)](https://wooiljeong.github.io/PublicDataReader/)  
[![오픈채팅](https://img.shields.io/badge/오픈채팅-Q&A-yellow?logo=KakaoTalk)](https://open.kakao.com/o/gbt2Pl2d)

<br>

<div align="left">

## PublicDataReader

**PublicDataReader**는 **Open API를 통해 공공 데이터를 조회하는 과정을 자동화하는 오픈소스 로우코드 파이썬 라이브러리**입니다. 즉시 분석에 활용할 수 있는 형태로 데이터를 조회할 수 있어 생산성 향상에 도움을 주는 도구입니다. 공공 데이터 제공처 마다 서로 다른 API 명세를 확인하는 작업, 명세에 따라 적합한 형식으로 데이터를 요청하는 코드를 작성하는 작업 그리고 반환된 데이터를 분석 가능한 형태로 가공하는 작업 등의 번거로운 작업들을 단 몇 줄의 코드로 자동화할 수 있습니다. 발급받은 Open API 서비스 인증키와 PublicDataReader 라이브러리만으로 원하는 데이터를 쉽게 조회할 수 있습니다.

<br>

## 이용 가능한 Open API 플랫폼

- [KOSIS 국가통계포털](https://kosis.kr/index/index.do)
- [공공데이터포털](https://www.data.go.kr/)
- [서울 열린데이터광장](https://data.seoul.go.kr/)

<br>

## 설치 방법

- Windows: CMD(명령 프롬프트)를 열어 아래 Shell 명령어를 입력
- Mac: Terminal(터미널)을 열어 아래 Shell 명령어를 입력

```bash
pip install PublicDataReader --upgrade
```

PublicDataReader를 정상적으로 실행하기 위해서는 pandas, requests, beautifulsoup4 라이브러리가 설치되어 있어야 합니다. 설치되어 있지 않은 경우 아래와 같이 설치합니다.

```bash
pip install pandas requests beautifulsoup4
```

<br>

## 사용 방법

### 라이브러리 임포트

```python
import PublicDataReader as pdr
```

### 데이터 제공처 별 조회 방법

- [KOSIS 국가통계포털 데이터 조회 방법 예시](./assets/docs/kosis.md)
- [공공데이터포털 데이터 조회 방법 예시](./assets/docs/portal.md)
- [서울 열린데이터광장 데이터 조회 방법 예시](./assets/docs/seoul.md)


<br>

## 참고

- **튜토리얼**  
  - [(블로그) KOSIS 데이터 조회하기](https://wooiljeong.github.io/python/pdr-kosis/)
  - [(블로그) 부동산 실거래가 조회하기](https://wooiljeong.github.io/python/public_data_reader_01/)
  - [(블로그) 건축물대장 데이터 조회하기](https://wooiljeong.github.io/python/public_data_reader_03/)
  - [(블로그) 상가업소 데이터 조회하기](https://wooiljeong.github.io/python/public_data_reader_02/)

- **실습코드**  
  - [Colab에서 PublicDataReader 실행하기](https://colab.research.google.com/drive/1fgT0D_tP-JyglobtDFfYQ6wQXfWWujIV?usp=sharing)  

- **공식문서**
  - [Docs](https://wooiljeong.github.io/PublicDataReader/)

- **문의**  
  - **이메일**: wooil@kakao.com  
  - **카카오톡 오픈채팅방**: [(Python) PublicDataReader Q&A](https://open.kakao.com/o/gbt2Pl2d)  

<br>

## 기여자

<a href="https://github.com/wooiljeong/publicdatareader/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=wooiljeong/publicdatareader" />
</a>

<br>



<div align=center>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FWooilJeong%2FPublicDataReader&count_bg=%2379C83D&title_bg=%23555555&icon=github.svg&icon_color=%23FFFFFF&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</div>
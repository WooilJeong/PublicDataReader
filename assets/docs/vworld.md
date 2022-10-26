## Vworld 데이터 API


```python
import PublicDataReader as pdr
print(pdr.__version__)

# Vworld API 인증키
apiKey = "사용자 인증키"

# Vworld Data API 인스턴스 생성
api = pdr.VworldData(apiKey)
```

    1.0.3
    
<br>

## 데이터 API 서비스 목록 확인
- [데이터 API 레퍼런스](https://www.vworld.kr/dev/v4dv_2ddataguide2_s001.do)


```python
# 서비스 목록
code = pdr.get_vworld_data_api_info_by_dataframe()
code.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>서비스명</th>
      <th>서비스ID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>연속지적도</td>
      <td>LP_PA_CBND_BUBUN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>도시지역</td>
      <td>LT_C_UQ111</td>
    </tr>
    <tr>
      <th>2</th>
      <td>관리지역</td>
      <td>LT_C_UQ112</td>
    </tr>
    <tr>
      <th>3</th>
      <td>농림지역</td>
      <td>LT_C_UQ113</td>
    </tr>
    <tr>
      <th>4</th>
      <td>자연환경보전지역</td>
      <td>LT_C_UQ114</td>
    </tr>
  </tbody>
</table>
</div>


    
<br>

## (예시) 연속지적도 조회

`get_data()`를 이용하면 관심 지번에 대한 연속지적도 정보를 [GeoJSON](https://ko.wikipedia.org/wiki/GeoJSON)으로 표현된 딕셔너리 타입 데이터로 가져올 수 있다. 참고로 GeoJSON은 위치정보를 갖는 점을 기반으로 체계적으로 지형을 표현하기 위해 설계된 개방형 공개 표준 형식이다. PNU코드가 '41135110001'로 시작하는 모든 지번에 대한 연속지적도를 조회하려면 다음과 같이 코드를 작성한다. [PNU코드](http://www.gisdeveloper.co.kr/?p=1562)는 개별 필지에 대한 고유한 코드값으로 지번을 일련번호로 표현한 것이라고 이해하면 된다. PNU코드는 시도 코드, 시군구 코드, 산지 구분 코드, 본번 그리고 부번으로 구성되어 있다.


```python
# 파라미터
params = {
    "serviceName": "연속지적도",
    "attrFilter": "pnu:like:41135110001",
}

# 데이터 요청
geo = api.get_data(**params)

print(f"""
- 결과 타입: {type(geo)}
- 키 종류: {geo.keys()}
""")
```

    
    - 결과 타입: <class 'dict'>
    - 키 종류: dict_keys(['type', 'features'])
    
    
    
<br>

## (예시) 시군구 다각형 정보 조회

시군구 코드 5자리를 아래와 같이 입력하면, 해당 시군구에 해당하는 다각형 정보를 GeoJSON으로 표현된 딕셔너리 타입 데이터를 조회할 수 있다.


```python
# 파라미터
params = {
    "serviceName": "시군구",
    "attrFilter": "sig_cd:=:41135",
}

# 데이터 요청
geo2 = api.get_data(**params)

print(f"""
- 결과 타입: {type(geo2)}
- 키 종류: {geo2.keys()}
""")
```

    
    - 결과 타입: <class 'dict'>
    - 키 종류: dict_keys(['type', 'features'])
    
    
    
<br>

## (활용) 연속지적도 시각화


```python
import folium

lat, lon = 37.3925, 127.112

# Map
m = folium.Map(location=[lat, lon], 
               zoom_start=14)

# 시군구 다각형
folium.GeoJson(
               data=geo2,
               name="시군구",
                style_function=lambda x: {
                    "fillColor": "#0000ff",
                    "color": "#0000ff",
                    "weight": 1,
                    "fillOpacity": 0.5,
                },
                tooltip=folium.features.GeoJsonTooltip(
                    fields=["full_nm"],
                    aliases=["주소"],
                    localize=True,
                    sticky=False,
                    labels=True,
                    style="",
                    toLocaleString=True,
                ),
               ).add_to(m)

# 연속지적도
folium.GeoJson(
               data=geo,
               name="연속지적도",
                style_function=lambda x: {
                    "fillColor": "#ffff00",
                    "color": "#ffff00",
                    "weight": 1,
                    "fillOpacity": 0.5,
                },
                tooltip=folium.features.GeoJsonTooltip(
                    fields=["addr"],
                    aliases=["주소"],
                    localize=True,
                    sticky=False,
                    labels=True,
                    style="",
                    toLocaleString=True,
                ),
               ).add_to(m)

# 레이어 컨트롤
folium.LayerControl().add_to(m)
m
```


<iframe
  src="/assets/html/sample_vworld.html"
  style="width:100%; height:500px;"
></iframe>

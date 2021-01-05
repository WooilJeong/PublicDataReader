import PublicDataReader as pdr
from config import OpenAPI

if __name__ == "__main__":
    
    # 서울 열린데이터 광장 Open API 서비스키
    serviceKey = OpenAPI.seoul
    # 소상공인 상가업소 정보 조회 인스턴스 생성
    seoul = pdr.SubwayInfo(serviceKey)

    # 데이터 조회
    start_index = 1
    end_index = 1000
    use_dt = 20210101
    df = seoul.CardSubwayStatsNew(start_index, end_index, use_dt)

    print(df.head(20))

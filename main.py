import PublicDataReader as pdr
from config import OpenAPI

if __name__ == "__main__":

    # 공공데이터포털 Open API 서비스키
    serviceKey = OpenAPI.semas
    # 소상공인 상가업소 정보 조회 인스턴스 생성
    semas = pdr.StoreInfo(serviceKey)

    # 01 지정 상권조회
    print("=" * 40)
    print("01 지정 상권조회")
    print("=" * 40)
    key = 1
    df = semas.storeZoneOne(key=key)
    print(df.head())

    # 02 반경내 상권조회
    print("=" * 40)
    print("02 반경내 상권조회")
    print("=" * 40)
    radius = 500
    cx = 127.03641615737838
    cy = 37.50059843782878
    df = semas.storeZoneInRadius(radius=radius, cx=cx, cy=cy)
    print(df.head())

    # 03 사각형내 상권조회
    print("=" * 40)
    print("03 사각형내 상권조회")
    print("=" * 40)
    minx = 127.0327683531071
    miny = 37.495967935149146
    maxx = 127.04268179746694
    maxy = 37.502402894207286
    df = semas.storeZoneInRectangle(minx=minx, miny=miny, maxx=maxx, maxy=maxy)
    print(df.head())

    # 04 행정구역 단위 상권조회
    print("=" * 40)
    print("04 행정구역 단위 상권조회")
    print("=" * 40)
    divId = "adongCd"
    key = "1168058000"
    df = semas.storeZoneInAdmi(divId=divId, key=key)
    print(df.head())

    # 05 단일 상가업소 조회
    print("=" * 40)
    print("05 단일 상가업소 조회")
    print("=" * 40)
    key = "19911027"
    df = semas.storeOne(key=key)
    print(df.head())

    # 06. 건물단위 상가업소 조회
    print("=" * 40)
    print("06. 건물단위 상가업소 조회")
    print("=" * 40)
    key = "1168011000104940000004966"
    pageNo = "1"
    df = semas.storeListInBuilding(key=key, pageNo=1)
    print(df.head())

    # 07. 지번단위 상가업소 조회
    print("=" * 40)
    print("07. 지번단위 상가업소 조회")
    print("=" * 40)
    key = "1168010600209380024"
    pageNo = "1"
    indsLclsCd = "Q"
    indsMclsCd = "Q12"
    indsSclsCd = "Q12A01"
    df = semas.storeListInPnu(key=key, indsLclsCd_=indsLclsCd, pageNo=1)
    print(df.head())

    # 08. 행정동 단위 상가업소 조회
    print("=" * 40)
    print("08. 행정동 단위 상가업소 조회")
    print("=" * 40)
    divId = "adongCd"
    key = "1168064000"
    indsLclsCd = "Q"
    pageNo = 1

    df = semas.storeListInDong(divId=divId, key=key, indsLclsCd_=indsLclsCd, pageNo=pageNo)
    print(df.head())

    # 09 상권내 상가업소 조회
    print("=" * 40)
    print("09 상권내 상가업소 조회")
    print("=" * 40)
    key = "1819"
    pageNo = "1"
    indsLclsCd = "Q"

    df = semas.storeListInArea(key=key, pageNo=pageNo, indsLclsCd_=indsLclsCd)
    print(df.head())

    # 10. 반경내 상가업소 조회
    print("=" * 40)
    print("10. 반경내 상가업소 조회")
    print("=" * 40)
    radius = "500"
    cx = 127.03641615737838
    cy = 37.50059843782878
    indsLclsCd = "Q"
    pageNo = "1"

    df = semas.storeListInRadius(radius=radius, cx=cx, cy=cy, indsLclsCd_=indsLclsCd, pageNo=pageNo)
    print(df.head())

    # 11. 사각형내 상가업소 조회
    print("=" * 40)
    print("11. 사각형내 상가업소 조회")
    print("=" * 40)
    minx = 127.0327683531071
    miny = 37.495967935149146
    maxx = 127.04268179746694
    maxy = 37.502402894207286
    indsLclsCd = "Q"
    pageNo = 1

    df = semas.storeListInRectangle(
        minx=minx, miny=miny, maxx=maxx, maxy=maxy, indsLclsCd_=indsLclsCd, pageNo=1
    )
    print(df.head())

    # 12. 다각형내 상가업소 조회
    print("=" * 40)
    print("12. 다각형내 상가업소 조회")
    print("=" * 40)
    key = "POLYGON((127.02355609555755 37.504264372557095, 127.02496157306963 37.50590702991155, 127.0270858825753 37.50486867039889, 127.02628121988377 37.503489842823114))"
    pageNo = 1
    indsLclsCd = "Q"

    df = semas.storeListInPolygon(key, indsLclsCd_=indsLclsCd, pageNo=pageNo)
    print(df.head())

    # 13. 업종별 상가업소 조회
    print("=" * 40)
    print("13. 업종별 상가업소 조회")
    print("=" * 40)
    divId = "indsLclsCd"
    key = "Q"
    pageNo = 1

    df = semas.storeListInUpjong(divId=divId, key=key, pageNo=pageNo)
    print(df.head())

    # 14. 수정일자기준 상가업소 조회
    print("=" * 40)
    print("14. 수정일자기준 상가업소 조회")
    print("=" * 40)
    key = "20200101"
    indsLclsCd = "Q"
    pageNo = "1"

    df = semas.storeListByDate(key=key, pageNo=pageNo)
    print(df.head())

    # 21. 상권정보 업종 대분류 조회
    print("=" * 40)
    print("21. 상권정보 업종 대분류 조회")
    print("=" * 40)
    df = semas.largeUpjongList()
    print(df.head())

    # 22. 상권정보 업종 중분류 조회
    print("=" * 40)
    print("22. 상권정보 업종 중분류 조회")
    print("=" * 40)
    indsLclsCd = "Q"
    df = semas.middleUpjongList(indsLclsCd_=indsLclsCd)
    print(df.head())

    # 23. 상권정보 업종 소분류 조회
    print("=" * 40)
    print("23. 상권정보 업종 소분류 조회")
    print("=" * 40)
    indsLclsCd = "Q"
    indsMclsCd = "Q01"
    df = semas.smallUpjongList(indsLclsCd_=indsLclsCd)
    print(df.head())

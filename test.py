import PublicDataReader as pdr
from config import OpenAPI

if __name__ == "__main__":
    
    # 공공 데이터 포털 Open API 서비스키
    serviceKey = OpenAPI.molit
    molit = pdr.Building(serviceKey)
    
    # Operation 01
    # sigunguCd = 11680
    # bjdongCd = 10300
    # platGbCd = 0
    # bun = '0012'
    # ji = '0000'

    # df = molit.getBrBasisOulnInfo(sigunguCd, bjdongCd, platGbCd, bun, ji)
    # print(df.head(1))


    # # Operation 02
    # sigunguCd = 11680
    # bjdongCd = 10300
    # platGbCd = 0
    # bun = '0012'
    # ji = '0000'

    # df = molit.getBrRecapTitleInfo(sigunguCd, bjdongCd, platGbCd, bun, ji)
    # print(df.head(1))


    # # Operation 03
    # sigunguCd = 11680
    # bjdongCd = 10300
    # platGbCd = 0
    # bun = '0012'
    # ji = '0000'

    # df = molit.getBrTitleInfo(sigunguCd, bjdongCd, platGbCd, bun, ji)
    # print(df.head(1))


    # # Operation 04
    # sigunguCd = 11680
    # bjdongCd = 10300
    # platGbCd = 0
    # bun = '0012'
    # ji = '0000'

    # df = molit.getBrFlrOulnInfo(sigunguCd, bjdongCd, platGbCd, bun, ji)
    # print(df.head(1))

    # # Operation 05
    # sigunguCd = 11680
    # bjdongCd = 10300
    # platGbCd = 0
    # bun = '0012'
    # ji = '0005'

    # df = molit.getBrAtchJibunInfo(sigunguCd, bjdongCd, platGbCd, bun, ji)
    # print(df.head(1))


    # Operation 06
    sigunguCd = 11680
    bjdongCd = 10300
    platGbCd = 0
    bun = '0012'
    ji = '0000'
    dongNm = ''
    hoNm = ''

    df = molit.getBrExposPubuseAreaInfo(sigunguCd, bjdongCd, platGbCd, bun, ji)
    print(df.head(1))

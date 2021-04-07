import PublicDataReader as pdr
from config import OpenAPI

if __name__ == "__main__":

    # 공공 데이터 포털 Open API 서비스키
    serviceKey = OpenAPI.molit
    molit = pdr.Building(serviceKey)

    # # Operation 01
    # print(">>> Operation 01")

    # sigunguCd = "11680"
    # bjdongCd = "10300"
    # platGbCd = "0"
    # bun = "0012"
    # ji = "0000"
    # startDate = "202001"
    # endDate = "202012"

    # df = molit.getBrBasisOulnInfo(sigunguCd, bjdongCd, platGbCd, bun, ji, startDate, endDate)
    # print(df.head(2))

    # # Operation 02
    # print(">>> Operation 02")

    # sigunguCd = "11680"
    # bjdongCd = "10300"
    # platGbCd = "0"
    # bun = "0012"
    # ji = "0000"
    # startDate = "202001"
    # endDate = "202012"

    # df = molit.getBrRecapTitleInfo(sigunguCd, bjdongCd, platGbCd, bun, ji, startDate, endDate)
    # print(df.head(1))

    # # Operation 03
    # print(">>> Operation 03")

    # sigunguCd = "11680"
    # bjdongCd = "10300"
    # platGbCd = "0"
    # bun = "0012"
    # ji = "0000"
    # startDate = "202001"
    # endDate = "202012"

    # df = molit.getBrTitleInfo(sigunguCd, bjdongCd, platGbCd, bun, ji, startDate, endDate)
    # print(df.head(1))

    # # Operation 04
    # print(">>> Operation 04")

    # sigunguCd = "11680"
    # bjdongCd = "10300"
    # platGbCd = "0"
    # bun = "0012"
    # ji = "0000"
    # startDate = "202001"
    # endDate = "202012"

    # df = molit.getBrFlrOulnInfo(sigunguCd, bjdongCd, platGbCd, bun, ji, startDate, endDate)
    # print(df.head(1))

    # # Operation 05
    # print(">>> Operation 05")

    # sigunguCd = "11680"
    # bjdongCd = "10300"
    # platGbCd = "0"
    # bun = "0012"
    # ji = "0005"
    # startDate = ""
    # endDate = ""

    # df = molit.getBrAtchJibunInfo(sigunguCd, bjdongCd, platGbCd, bun, ji, startDate, endDate)
    # print(df.head(2))

    # # Operation 06
    # print(">>> Operation 06")

    # sigunguCd = "11680"
    # bjdongCd = "10300"
    # platGbCd = "0"
    # bun = "0012"
    # ji = "0000"
    # startDate = "202001"
    # endDate = "202012"
    # dongNm = ""
    # hoNm = ""

    # df = molit.getBrExposPubuseAreaInfo(
    #     sigunguCd, bjdongCd, platGbCd, bun, ji, startDate, endDate, dongNm, hoNm
    # )
    # print(df.head(1))

    # # Operation 07
    # print(">>> Operation 07")

    # sigunguCd = "11680"
    # bjdongCd = "10300"
    # platGbCd = "0"
    # bun = "0012"
    # ji = "0000"
    # startDate = "202001"
    # endDate = "202012"

    # df = molit.getBrWclfInfo(sigunguCd, bjdongCd, platGbCd, bun, ji, startDate, endDate)
    # print(df.head(1))

    # # Operation 08
    # print(">>> Operation 08")

    # sigunguCd = "11680"
    # bjdongCd = "10300"
    # platGbCd = "0"
    # bun = "0012"
    # ji = "0000"
    # startDate = "202001"
    # endDate = "202012"

    # df = molit.getBrHsprcInfo(sigunguCd, bjdongCd, platGbCd, bun, ji, startDate, endDate)
    # print(df.head(2))

    # # Operation 09
    # print(">>> Operation 09")

    # sigunguCd = "11680"
    # bjdongCd = "10300"
    # platGbCd = "0"
    # bun = "0012"
    # ji = "0000"
    # startDate = "202001"
    # endDate = "202012"

    # df = molit.getBrExposInfo(sigunguCd, bjdongCd, platGbCd, bun, ji, startDate, endDate)
    # print(df.head(2))

    # # Operation 10
    # print(">>> Operation 10")

    # sigunguCd = "11680"
    # bjdongCd = "10300"
    # platGbCd = "0"
    # bun = "0012"
    # ji = "0000"
    # startDate = "202001"
    # endDate = "202012"

    # df = molit.getBrJijiguInfo(sigunguCd, bjdongCd, platGbCd, bun, ji, startDate, endDate)
    # print(df.head(2))


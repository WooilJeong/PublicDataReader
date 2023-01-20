"""
한국부동산원 오픈 API
https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=&detailKeyword=&publicDataPk=&recmSe=&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=%ED%95%9C%EA%B5%AD%EB%B6%80%EB%8F%99%EC%82%B0%EC%9B%90&orgFilter=%ED%95%9C%EA%B5%AD%EB%B6%80%EB%8F%99%EC%82%B0%EC%9B%90&org=%ED%95%9C%EA%B5%AD%EB%B6%80%EB%8F%99%EC%82%B0%EC%9B%90&orgSearch=&currentPage=1&perPage=40&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode=
"""

import time
import requests
import pandas as pd

requests.packages.urllib3.disable_warnings()


class Reb:
    """
    한국부동산원(REB) 오픈 API 클래스

    Parameters
    ----------
    service_key : str
        API 서비스 키
    """

    def __init__(self, service_key):
        # 서비스 키 설정
        self.service_key = service_key
        # 메타데이터 조회
        self.meta_dict = self.get_meta_dict()

    def get_data(self,
                 service_name,
                 category_name,
                 verbose=False,
                 wait_time=0.1,
                 **kwargs):
        """
        데이터 조회

        Parameters
        ----------
        service_name : str
            서비스명
        category_name : str
            카테고리명
        verbose : bool
            진행상황 출력 여부 - 기본값 False
        wait_time : float
            API 요청 대기 시간(초) - 기본값 0.1초
        **kwargs : dict
            API 파라미터

        Returns
        -------
        df : pandas.DataFrame
            조회 결과
        """
        # 파라미터 설정
        try:
            url = self.meta_dict[service_name.replace(
                " ", "")][category_name.replace(" ", "")]["url"]
        except Exception as e:
            print(e)
            return None

        params = {
            "serviceKey": requests.utils.unquote(self.service_key),
            "page": 1,
            "perPage": 10000,
            "returnType": "json",
        }
        params.update(kwargs)

        if service_name == "공동주택실거래가격지수" and category_name == "지역별":
            params['cond[SIZE_GBN::EQ]'] = "0"
        if service_name == "월세가격" and category_name == "지역별수급동향":
            params['cond[TREND_GBN::EQ]'] = "ST"
        if service_name == "월세가격" and category_name == "지역별거래동향":
            params['cond[TREND_GBN::EQ]'] = "DT"

        # 빈 데이터프레임 생성
        df = pd.DataFrame()

        # 데이터 조회
        try:
            res = requests.get(url, params=params, verify=False)
            res_json = res.json()
        except Exception as e:
            print(e)
            return None

        # 데이터프레임 생성
        try:
            df = pd.concat([df, pd.DataFrame(res_json["data"])],
                           axis=0, ignore_index=True)
        except Exception as e:
            print(e)
            return None

        # 페이지네이션
        total_count = res_json["totalCount"]
        match_count = res_json["matchCount"]
        current_count = res_json["currentCount"]
        cumulative_count = res_json["currentCount"]
        while True:
            time.sleep(wait_time)
            if verbose:
                print(
                    f"total_count: {total_count}, match_count: {match_count}, cumulative_count: {cumulative_count}")
            if cumulative_count < match_count:
                params["page"] += 1
                res = requests.get(url, params=params, verify=False)
                res_json = res.json()
                if len(res_json["data"]) == 0:
                    print(res.url)
                    break
                df = pd.concat([df, pd.DataFrame(res_json["data"])],
                               axis=0, ignore_index=True)
                current_count = res_json["currentCount"]
                cumulative_count += current_count
            else:
                break

        return df

    def get_meta_dict(self):
        """
        메타데이터 조회

        Returns
        -------
        meta_dict : dict
            메타데이터
        """
        return {

            "분양정보": {
                "아파트": {
                    "url": "https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancDetail",
                    "columns": "",
                },
                "오피스텔": {
                    "url": "https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getUrbtyOfctlLttotPblancDetail",
                    "columns": "",
                },
                "아파트잔여": {
                    "url": "https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getRemndrLttotPblancDetail",
                    "columns": "",
                },
                "아파트주택형별": {
                    "url": "https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getAPTLttotPblancMdl",
                    "columns": "",
                },
                "오피스텔주택형별": {
                    "url": "https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getUrbtyOfctlLttotPblancMdl",
                    "columns": "",
                },
                "아파트잔여주택형별": {
                    "url": "https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getRemndrLttotPblancMdl",
                    "columns": "",
                },
            },

            "청약경쟁률": {
                "아파트": {
                    "url": "https://api.odcloud.kr/api/ApplyhomeInfoCmpetRtSvc/v1/getAPTLttotPblancCmpet",
                    "columns": "",
                },
                "오피스텔": {
                    "url": "https://api.odcloud.kr/api/ApplyhomeInfoCmpetRtSvc/v1/getUrbtyOfctlLttotPblancCmpet",
                    "columns": "",
                },
                "임대": {
                    "url": "https://api.odcloud.kr/api/ApplyhomeInfoCmpetRtSvc/v1/getPblPvtRentLttotPblancCmpet",
                    "columns": "",
                },
                "취소후재공급": {
                    "url": "https://api.odcloud.kr/api/ApplyhomeInfoCmpetRtSvc/v1/getCancResplLttotPblancCmpet",
                    "columns": "",
                },
                "잔여": {
                    "url": "https://api.odcloud.kr/api/ApplyhomeInfoCmpetRtSvc/v1/getRemndrLttotPblancCmpet",
                    "columns": "",
                },
            },

            "청약당첨정보": {
                "지역별신청자": {
                    "url": "https://api.odcloud.kr/api/ApplyhomeStatSvc/v1/getAPTReqstAreaStat",
                    "columns": "",
                },
                "연령별신청자": {
                    "url": "https://api.odcloud.kr/api/ApplyhomeStatSvc/v1/getAPTReqstAgeStat",
                    "columns": "",
                },
                "지역별당첨자": {
                    "url": "https://api.odcloud.kr/api/ApplyhomeStatSvc/v1/getAPTPrzwnerAreaStat",
                    "columns": "",
                },
                "연령별당첨자": {
                    "url": "https://api.odcloud.kr/api/ApplyhomeStatSvc/v1/getAPTPrzwnerAgeStat",
                    "columns": "",
                },
                "지역별경쟁률": {
                    "url": "https://api.odcloud.kr/api/ApplyhomeStatSvc/v1/getAPTCmpetrtAreaStat",
                    "columns": "",
                },
                "지역별가점제당첨자": {
                    "url": "https://api.odcloud.kr/api/ApplyhomeStatSvc/v1/getAPTApsPrzwnerStat",
                    "columns": "",
                },
            },

            "공동주택단지정보": {
                "기본": {
                    "url": "https://api.odcloud.kr/api/AptIdInfoSvc/v1/getAptInfo",
                    "columns": "",
                },
                "동": {
                    "url": "https://api.odcloud.kr/api/AptIdInfoSvc/v1/getDongInfo",
                    "columns": "",
                },
                "단지명": {
                    "url": "https://api.odcloud.kr/api/AptIdInfoSvc/v1/getHistInfo",
                    "columns": "",
                },
            },

            "공동주택실거래가격지수": {
                "지역별": {
                    "url": "https://api.odcloud.kr/api/RealTradingPriceIndexSvc/v1/getAptRealTradingPriceIndex",
                    "columns": "",
                },
                "규모별": {
                    "url": "https://api.odcloud.kr/api/RealTradingPriceIndexSvc/v1/getAptRealTradingPriceIndexSize",
                    "columns": "",
                },
            },

            "주택": {
                "지역별": {
                    "url": "https://api.odcloud.kr/api/HousePriceTrendSvc/v1/getHousePrice",
                    "columns": "",
                },
                "5분위배율": {
                    "url": "https://api.odcloud.kr/api/HousePriceTrendSvc/v1/getHousePercentilePrice",
                    "columns": "",
                },
                "전세가격비율": {
                    "url": "https://api.odcloud.kr/api/HousePriceTrendSvc/v1/getHouseSaleDepositRate",
                    "columns": "",
                },
                "계절조정": {
                    "url": "https://api.odcloud.kr/api/HousePriceTrendSvc/v1/getHousePriceIndexSeason",
                    "columns": "",
                },
                "연령별": {
                    "url": "https://api.odcloud.kr/api/HousePriceTrendSvc/v1/getHousePriceIndexAge",
                    "columns": "",
                },
                "규모별": {
                    "url": "https://api.odcloud.kr/api/HousePriceTrendSvc/v1/getHousePriceIndexSize",
                    "columns": "",
                },
                "매매수급": {
                    "url": "https://api.odcloud.kr/api/HousePriceTrendSvc/v1/getHouseDemandSupplyTrend",
                    "columns": "",
                },
                "매매거래": {
                    "url": "https://api.odcloud.kr/api/HousePriceTrendSvc/v1/getHouseTradingTrend",
                    "columns": "",
                },
                "전세수급": {
                    "url": "https://api.odcloud.kr/api/HousePriceTrendSvc/v1/getJeonseSndTrend",
                    "columns": "",
                },
                "전세가격": {
                    "url": "https://api.odcloud.kr/api/HousePriceTrendSvc/v1/getJeonseTradingTrend",
                    "columns": "",
                },
                "가격별": {
                    "url": "https://api.odcloud.kr/api/HousePriceTrendSvc/v1/getHousePriceIndex",
                    "columns": "",
                },
            },

            "주간아파트": {
                "연령별거래유형별": {
                    "url": "https://api.odcloud.kr/api/WeeklyAptTrendSvc/v1/getAptTradingPriceIndexAge",
                    "columns": "",
                },
                "규모별거래유형별": {
                    "url": "https://api.odcloud.kr/api/WeeklyAptTrendSvc/v1/getAptTradingPriceIndexSize",
                    "columns": "",
                },
                "전세수급": {
                    "url": "https://api.odcloud.kr/api/WeeklyAptTrendSvc/v1/getAptRentalMarketTrend",
                    "columns": "",
                },
                "매매수급": {
                    "url": "https://api.odcloud.kr/api/WeeklyAptTrendSvc/v1/getAptTradingMarketTrend",
                    "columns": "",
                },
                "지역별거래유형별": {
                    "url": "https://api.odcloud.kr/api/WeeklyAptTrendSvc/v1/getAptTradingPriceIndex",
                    "columns": "",
                },
            },

            "오피스텔": {
                "지역별가격지수": {
                    "url": "https://api.odcloud.kr/api/OfstPriceTrendSvc/v1/getOfstPriceIndex",
                    "columns": "",
                },
                "규모별가격지수": {
                    "url": "https://api.odcloud.kr/api/OfstPriceTrendSvc/v1/getOfstPriceIndexSize",
                    "columns": "",
                },
                "지역별가격": {
                    "url": "https://api.odcloud.kr/api/OfstPriceTrendSvc/v1/getOfstPrice",
                    "columns": "",
                },
                "규모별가격": {
                    "url": "https://api.odcloud.kr/api/OfstPriceTrendSvc/v1/getOfstPriceSize",
                    "columns": "",
                },
                "지역별전세가격비율": {
                    "url": "https://api.odcloud.kr/api/OfstPriceTrendSvc/v1/getSalePriceJeonsePriceRate",
                    "columns": "",
                },
                "규모별전세가격비율": {
                    "url": "https://api.odcloud.kr/api/OfstPriceTrendSvc/v1/getSalePriceJeonsePriceRateSize",
                    "columns": "",
                },
                "지역별월세보증금비율": {
                    "url": "https://api.odcloud.kr/api/OfstPriceTrendSvc/v1/getJeonsePriceRentDepositRate",
                    "columns": "",
                },
                "규모별월세보증금비율": {
                    "url": "https://api.odcloud.kr/api/OfstPriceTrendSvc/v1/getJeonsePriceRentDepositRateSize",
                    "columns": "",
                },

            },

            "상업용임대": {
                "지역별전환율": {
                    "url": "https://api.odcloud.kr/api/CommercialRealEstateLeaseTrendSvc/v1/getConvertRate",
                    "columns": "",
                },
                "지역별임대가격지수": {
                    "url": "https://api.odcloud.kr/api/CommercialRealEstateLeaseTrendSvc/v1/getLeasePriceIndex",
                    "columns": "",
                },
                "지역별분기소득수익률": {
                    "url": "https://api.odcloud.kr/api/CommercialRealEstateLeaseTrendSvc/v1/getIncomRateOfReturnQuarter",
                    "columns": "",
                },
                "지역별분기자본수익률": {
                    "url": "https://api.odcloud.kr/api/CommercialRealEstateLeaseTrendSvc/v1/getCapitalRateOfReturnQuarter",
                    "columns": "",
                },
                "지역별분기투자수익률": {
                    "url": "https://api.odcloud.kr/api/CommercialRealEstateLeaseTrendSvc/v1/getInvestRateOfReturnQuarter",
                    "columns": "",
                },
                "지역별기타수입구성비": {
                    "url": "https://api.odcloud.kr/api/CommercialRealEstateLeaseTrendSvc/v1/getEtcIncomeRatioOfGrossIncome",
                    "columns": "",
                },
                "순영업소득": {
                    "url": "https://api.odcloud.kr/api/CommercialRealEstateLeaseTrendSvc/v1/getNetOperationIncome",
                    "columns": "",
                },
                "지역별영업경비구성비": {
                    "url": "https://api.odcloud.kr/api/CommercialRealEstateLeaseTrendSvc/v1/getOperationExpensesRatioOfGrossIncome",
                    "columns": "",
                },
                "지역별임대수입구성비": {
                    "url": "https://api.odcloud.kr/api/CommercialRealEstateLeaseTrendSvc/v1/getRentIncomeRatioOfGrossIncome",
                    "columns": "",
                },
                "지역별임대료": {
                    "url": "https://api.odcloud.kr/api/CommercialRealEstateLeaseTrendSvc/v1/getLeasePrice",
                    "columns": "",
                },
                "층별임대료": {
                    "url": "https://api.odcloud.kr/api/CommercialRealEstateLeaseTrendSvc/v1/getPerFloorLeasePrice",
                    "columns": "",
                },
                "층별효용비율": {
                    "url": "https://api.odcloud.kr/api/CommercialRealEstateLeaseTrendSvc/v1/getPerFloorUtilityRatio",
                    "columns": "",
                },
                "지역별공실률": {
                    "url": "https://api.odcloud.kr/api/CommercialRealEstateLeaseTrendSvc/v1/getVacantRate",
                    "columns": "",
                },
                "지역별연간소득수익률": {
                    "url": "https://api.odcloud.kr/api/CommercialRealEstateLeaseTrendSvc/v1/getIncomRateOfReturnYear",
                    "columns": "",
                },
                "지역별연간자본수익률": {
                    "url": "https://api.odcloud.kr/api/CommercialRealEstateLeaseTrendSvc/v1/getCapitalRateOfReturnYear",
                    "columns": "",
                },
                "지역별연간투자수익률": {
                    "url": "https://api.odcloud.kr/api/CommercialRealEstateLeaseTrendSvc/v1/getInvestRateOfReturnYear",
                    "columns": "",
                },

            },

            "월세가격": {
                "지역별전월세전환율": {
                    "url": "https://api.odcloud.kr/api/RentPriceTrendSvc/v1/getJeonseRentChangeRate",
                    "columns": "",
                },
                "규모별전월세전환율": {
                    "url": "https://api.odcloud.kr/api/RentPriceTrendSvc/v1/getJeonseRentChangeRateSize",
                    "columns": "",
                },
                "규모별월세가격지수": {
                    "url": "https://api.odcloud.kr/api/RentPriceTrendSvc/v1/getRentPriceIndexSize",
                    "columns": "",
                },
                "지역별수급동향": {
                    "url": "https://api.odcloud.kr/api/RentPriceTrendSvc/v1/getRentDemandSupplyTrend",
                    "columns": "",
                },
                "지역별거래동향": {
                    "url": "https://api.odcloud.kr/api/RentPriceTrendSvc/v1/getRentTradingTrend",
                    "columns": "",
                },
                "지역별주택유형별월세가격지수": {
                    "url": "https://api.odcloud.kr/api/RentPriceTrendSvc/v1/getRentPriceIndex",
                    "columns": "",
                },

            },

            "부동산거래": {
                "거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingArea",
                    "columns": "",
                },
                "거주지별거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaResidence",
                    "columns": "",
                },
                "거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCount",
                    "columns": "",
                },
                "거주지별거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountResidence",
                    "columns": "",
                },
                "건물유형별거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaBuildType",
                    "columns": "",
                },
                "거래주체별거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountDealer",
                    "columns": "",
                },
                "외국인거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaForeigner",
                    "columns": "",
                },
                "신탁거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaTrust",
                    "columns": "",
                },
                "외국인거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountForeigner",
                    "columns": "",
                },
                "신탁거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountTrust",
                    "columns": "",
                },
                "지목별거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaJiMok",
                    "columns": "",
                },
                "지목별거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountJiMok",
                    "columns": "",
                },
                "토지거래허가처리별거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaPermission",
                    "columns": "",
                },
                "토지거래허가처리별거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountPermission",
                    "columns": "",
                },
                "거래원인별거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaReason",
                    "columns": "",
                },
                "거래원인별거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountReason",
                    "columns": "",
                },
                "거래규모별거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaSize",
                    "columns": "",
                },
                "거래규모별거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountSize",
                    "columns": "",
                },
                "용도지역별거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaUseDistrict",
                    "columns": "",
                },
                "용도지역별거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountUseDistrict",
                    "columns": "",
                },
                "건물유형별거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountBuildType",
                    "columns": "",
                },
                "거래주체별거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaDealer",
                    "columns": "",
                },
                "연도별거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaYear",
                    "columns": "",
                },
                "연도별거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountYear",
                    "columns": "",
                },
                "연도별거주지별거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaResidenceYear",
                    "columns": "",
                },
                "연도별거주지별거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountResidenceYear",
                    "columns": "",
                },
                "연도별건물유형별거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaBuildTypeYear",
                    "columns": "",
                },
                "연도별건물유형별거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountBuildTypeYear",
                    "columns": "",
                },
                "연도별거래주체별거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaDealerYear",
                    "columns": "",
                },
                "연도별거래주체별거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountDealerYear",
                    "columns": "",
                },
                "연도별외국인거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaForeignerYear",
                    "columns": "",
                },
                "연도별외국인거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountForeignerYear",
                    "columns": "",
                },
                "연도별신탁거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaTrustYear",
                    "columns": "",
                },
                "연도별신탁거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountTrustYear",
                    "columns": "",
                },
                "연도별지목별거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaJiMokYear",
                    "columns": "",
                },
                "연도별지목별거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountJiMokYear",
                    "columns": "",
                },
                "연도별토지거래허가처리별거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaPermissionYear",
                    "columns": "",
                },
                "연도별토지거래허가처리별거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountPermissionYear",
                    "columns": "",
                },
                "연도별거래원인별거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaReasonYear",
                    "columns": "",
                },
                "연도별거래원인별거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountReasonYear",
                    "columns": "",
                },
                "연도별거래규모별거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaSizeYear",
                    "columns": "",
                },
                "연도별거래규모별거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountSizeYear",
                    "columns": "",
                },
                "연도별용도지역별거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingAreaUseDistrictYear",
                    "columns": "",
                },
                "연도별용도지역별거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingSvc/v1/getRealEstateTradingCountUseDistrictYear",
                    "columns": "",
                },

            },

            "지가변동률": {
                "연도별지역별": {
                    "url": "https://api.odcloud.kr/api/LfrPriceSvc/v1/getLfrPriceRateYear",
                    "columns": "",
                },
                "이용상황별": {
                    "url": "https://api.odcloud.kr/api/LfrPriceSvc/v1/getLfrPriceRateUtilization",
                    "columns": "",
                },
                "월별지역별": {
                    "url": "https://api.odcloud.kr/api/LfrPriceSvc/v1/getLfrPriceRate",
                    "columns": "",
                },
                "용도지역별": {
                    "url": "https://api.odcloud.kr/api/LfrPriceSvc/v1/getLfrPriceRateUseDistrict",
                    "columns": "",
                },
                "연도별지역별": {
                    "url": "https://api.odcloud.kr/api/LfrPriceSvc/v1/getLfrPriceIndexYear",
                    "columns": "",
                },
                "월별지역별": {
                    "url": "https://api.odcloud.kr/api/LfrPriceSvc/v1/getLfrPriceIndex",
                    "columns": "",
                },
                "용도지역별": {
                    "url": "https://api.odcloud.kr/api/LfrPriceSvc/v1/getLfrPriceIndexUseDistrict",
                    "columns": "",
                },
                "이용상황별": {
                    "url": "https://api.odcloud.kr/api/LfrPriceSvc/v1/getLfrPriceIndexUtilization",
                    "columns": "",
                },
                "보조지수": {
                    "url": "https://api.odcloud.kr/api/LfrPriceSvc/v1/getLfrHelpIndex",
                    "columns": "",
                },
            },

            "연령대별부동산거래": {
                "거래면적": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingBuyerAge/v1/getRealEstateTradingAreaAge",
                    "columns": "",
                },
                "거래건수": {
                    "url": "https://api.odcloud.kr/api/RealEstateTradingBuyerAge/v1/getRealEstateTradingCountAge",
                    "columns": "",
                },
            },

            "녹색건축인증현황": {
                "녹색건축": {
                    "url": "https://api.odcloud.kr/api/GreenBuildCertifySvc/v1/getGreenBuildCertify",
                    "columns": "",
                },
            },
        }

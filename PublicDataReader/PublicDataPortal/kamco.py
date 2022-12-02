import pandas as pd
import datetime
import requests
import xmltodict


class Kamco:
    """
    KAMCO Open API 클래스
    """

    def __init__(self, serviceKey):
        
        # 전역 변수
        self.serviceKey = serviceKey
        self.numOfRows = 99999
        self.page = 1
        self.endpoint = "http://openapi.onbid.co.kr/openapi/services"

        # 서비스, 기능 딕셔너리
        self.meta_dict = {
            
            "온비드코드": {
                "서비스": "OnbidCodeInfoInquireSvc",
                "기능": {
                    "용도상위코드": "getOnbidTopCodeInfo",
                    "용도중간코드": "getOnbidMiddleCodeInfo",
                    "용도하위코드": "getOnbidBottomCodeInfo",
                    "시도": "getOnbidAddr1Info",
                    "시군구": "getOnbidAddr2Info",
                    "읍면동": "getOnbidAddr3Info",
                    "상세주소": "getOnbidDtlAddrInfo",
                }
            },
            
            "캠코공매물건": {
                "서비스": "KamcoPblsalThingInquireSvc",
                "기능": {
                    "물건목록": "getKamcoPbctCltrList",
                    "공고목록": "getKamcoPlnmPbctList",
                    "일정": "getKamcoPbctSchedule",
                    "공고기본정보": "getKamcoPlnmPbctBasicInfoDetail",
                    "공고공매일정": "getKamcoPlnmPbctBidDateInfoDetail",
                    "공고첨부파일": "getKamcoPlnmPbctFileInfoDetail",
                }
            },

            "이용기관공매물건": {
                "서비스": "UtlinsttPblsalThingInquireSvc",
                "기능": {
                    "공고목록": "getPublicSaleAnnouncement",
                    "물건목록": "getPublicSaleObject",
                    "통합공고목록": "getPublicSaleList",
                    "매각공고목록": "getPublicSaleAnnouncementList",
                    "임대공고목록": "getPublicLeaseAnnouncementList",
                    "마감임박공고목록": "getPublicDeadlineAnnouncementList",
                }
            },

            
            "정부재산정보공개": {
                "서비스": "GovernmentPropertyInfoSvc",
                "기능": {
                    "정부재산정보공개정보목록": "getGovernmentProperty",
                    "정부재산정보공개정보상세": "getGovernmentPropertyDetail",
                    "캠코관리재산정보공개목록정보": "getKamcoProperty",
                    "캠코관리재산정보공개정보상세": "getKamcoPropertyDetail",
                }
            },
            
            
            "물건정보": {
                "서비스": "ThingInfoInquireSvc",
                "기능": {
                    "통합용도별물건목록": "getUnifyUsageCltr",
                    "통합새로운물건목록": "getUnifyNewCltrList",
                    "통합마감임박물건목록": "getUnifyDeadlineCltrList",
                    "통합수의계약가능물건목록": "getUnifyPrivateContractCltrList",
                    "통합50%체감물건목록": "getUnifyDegression50PerCltrList",
                    "통합클릭탑20물건목록": "getUnifyClickTop20CltrList",
                    "통합관심탑20물건목록": "getUnifyInterestTop20CltrList",
                    "통합용도별물건기본정보상세": "getUnifyUsageCltrBasicInfoDetail",
                    "통합용도별물건감정평가서정보상세": "getUnifyUsageCltrEstimationInfoDetail",
                    "통합용도별물건임대차정보상세": "getUnifyUsageCltrRentalInfoDetail",
                    "통합용도별물건권리종류정보상세": "getUnifyUsageCltrRegisteredInfoDetail",
                    "통합용도별물건공매일정상세": "getUnifyUsageCltrBidDateInfoDetail",
                    "통합용도별물건입찰이력상세": "getUnifyUsageCltrBidHistoryInfoDetail",
                    "통합용도별물건주주정보상세": "getUnifyUsageCltrStockholderInfoDetail",
                    "통합용도별물건법인현황정보상세": "getUnifyUsageCltrCorporatebodyInfoDetail",
                }
            },

        }

    def get_data(self, service, function, **kwargs):
        
        try:
            service = service.replace(" ","")
            function = function.replace(" ","")
            _service = self.meta_dict[service]['서비스']
            _function = self.meta_dict[service]['기능'][function]
            url = f"{self.endpoint}/{_service}/{_function}"
        except:
            print("서비스 및 기능 설정 오류")
            return None

        # 기본 파라미터
        params = {
            "serviceKey": self.serviceKey,
            "numOfRows": self.numOfRows,
            "page": self.page,
        }
        params.update(kwargs)

        # 요청
        try:
            response = requests.get(url, params=params)
        except:
            print("API 요청 오류")
            return None
        
        try:
            data = xmltodict.parse(response.text)
        except:
            print("XML-Dictionary 변환 오류")
            return None
        
        try:
            body = data['response']['body']
        except:
            print(data.get("response").get("header").get("resultMsg"))
            return None

        # 데이터프레임으로 변환
        try:
            
            # 바디에 items 키 값이 존재하는 경우
            if body.get("items") is not None:
                
                if body['items'].get("bidDateInfoItem"):
                    if type(body['items'].get("bidDateInfoItem")) == dict:
                        df = pd.DataFrame([body['items']['bidDateInfoItem']])
                    else:
                        df = pd.DataFrame(body['items']['bidDateInfoItem'])
                
                elif body['items'].get("estimationInfo"):
                    if type(body['items'].get("estimationInfo")) == dict:
                        df = pd.DataFrame([body['items']['estimationInfo']])
                    else:
                        df = pd.DataFrame(body['items']['estimationInfo'])
     
                elif body['items'].get("registered"):
                    if type(body['items'].get("registered")) == dict:
                        df = pd.DataFrame([body['items']['registered']])
                    else:
                        df = pd.DataFrame(body['items']['registered'])
                
                elif body['items'].get("bidInfo"):
                    if type(body['items'].get("bidInfo")) == dict:
                        df = pd.DataFrame([body['items']['bidInfo']])
                    else:
                        df = pd.DataFrame(body['items']['bidInfo'])
                
                elif body['items'].get("bidHistoryInfo"):
                    if type(body['items'].get("bidHistoryInfo")) == dict:
                        df = pd.DataFrame([body['items']['bidHistoryInfo']])
                    else:
                        df = pd.DataFrame(body['items']['bidHistoryInfo'])

                elif body['items'].get("stockholderInfo"):
                    if type(body['items'].get("stockholderInfo")) == dict:
                        df = pd.DataFrame([body['items']['stockholderInfo']])
                    else:
                        df = pd.DataFrame(body['items']['stockholderInfo'])

                elif body['items'].get("corporatebodyInfo"):
                    if type(body['items'].get("corporatebodyInfo")) == dict:
                        df = pd.DataFrame([body['items']['corporatebodyInfo']])
                    else:
                        df = pd.DataFrame(body['items']['corporatebodyInfo'])
            
                elif body['items'].get("rentalInfo"):
                    if type(body['items'].get("rentalInfo")) == dict:
                        df = pd.DataFrame([body['items']['rentalInfo']])
                    else:
                        df = pd.DataFrame(body['items']['rentalInfo'])
            
                else:
                    if type(body['items']['item'])==dict:
                        df = pd.DataFrame([body['items']['item']])
                    else:
                        df = pd.DataFrame(body['items']['item'])
            
            # 바디에 items 키 값이 존재하지 않는 경우
            else:
                
                # items 대신 item 키 값이 존재하는 경우
                if body.get("item"):
                    df = pd.DataFrame([body['item']])
                
                # items와 item 모두 키 값이 존재하지 않는 경우
                else:
                    print("데이터가 없습니다.")
                    return None
        except:
            print("데이터 프레임 생성 오류")
            return body

        return df
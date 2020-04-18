# 아파트매매 실거래자료 조회 서비스
from PublicDataReader.PublicDataPortal.AptTrade import AptTradeReader
# 아파트매매 실거래 상세 자료 조회 서비스
from PublicDataReader.PublicDataPortal.AptTradeDetail import AptTradeDetailReader
# 아파트 전월세 자료 조회 서비스
from PublicDataReader.PublicDataPortal.AptRent import AptRentReader
# 아파트 분양권 전매 신고 자료 조회 서비스
from PublicDataReader.PublicDataPortal.AptOwnership import AptOwnershipReader

AptTradeReader = AptTradeReader
AptTradeDetailReader = AptTradeDetailReader
AptRentReader = AptRentReader
AptOwnership = AptOwnershipReader


from PublicDataReader.PublicDataPortal.Air import AirStation, AirDataRT, AirData

AirStation = AirStation
AirDataRT = AirDataRT
AirData = AirData

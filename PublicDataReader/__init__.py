from .data import AptTradeReader, AptTradeDetailReader, AptRentReader, AptOwnershipReader, AirStation, AirDataRT, AirData

version = "0.1.0"
__version__ = f"""
>>> PublicDataReader Version : {version}

- Author : Wooil Jeong
- E-mail : wooil@kakao.com
- Github : https://github.com/WooilJeong/PublicDataReader
- Blog : https://wooiljeong.github.io
"""

# __version__ = 'PublicDataReader Version : 0.1.0'
__all__=['__version__', 'AptTradeReader', 'AptTradeDetailReader', 'AptRentReader', 'AptOwnershipReader', 'AirStation', 'AirDataRT', 'AirData']

import json
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs

df = pd.DataFrame()
i = 1
while True:

    print(f"page: {str(i)}")

    url = f"https://www.vworld.kr/dev/v4dv_2ddataguide2_s001.do"
    data = {"pageIndex": i}
    res = requests.post(url, data, verify=False)
    soup = bs(res.text, "html5lib")
    title_tags = soup.select(
        "#container > div.page.clearfix > div.content > div > table > thead > tr > th")
    data_tags = soup.select(
        '#container > div.page.clearfix > div.content > div > table > tbody > tr > td')
    page_tags = soup.select(
        "#container > div.page.clearfix > div.content > div:nth-child(11) > div.news_info.clearfix > div")
    end_page = int(page_tags[0].text.split("/")[1].split("page")[0].strip())
    columns = list(map(lambda x: x.text, title_tags))
    values = list(map(lambda x: x.text, data_tags))
    df_sub = pd.DataFrame(
        np.array(values).reshape(-1, len(columns)), columns=columns)
    df = pd.concat([df, df_sub], axis=0, ignore_index=True)
    i += 1
    if i == end_page+1:
        break
df = df.set_index("서비스명")

code = json.loads(df.to_json(force_ascii=False))['서비스ID']

with open("../PublicDataReader/raw/code_vworld.json", "w") as f:
    f.write(json.dumps(code))
    f.close()

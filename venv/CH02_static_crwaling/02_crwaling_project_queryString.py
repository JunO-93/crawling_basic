'''
환율 가져오기 -- 쿼리스트링

✔ 접속하지 않아도 URL을 찾아낼 수 있는 방법

* 쿼리스트링 : 웹 요청시에 보내는 추가 인자 값

1. 미국 : https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_USDKRW
2. 유럽 : https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_EURKRW
>>> marketindexCd에 통화코드 값이 들어간다.
'''

import re
import requests as req

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=감자"
res = req.get(url)
print(res.text)


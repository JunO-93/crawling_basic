'''
requests : http 통신을 편하게
beautifulsoup : html 통신을 편하게

- html 문자열 파싱
- html 노드 인식 및 편리한 기능들
- parent, children, contents, descendants, sibling
- string, strings, stripped_strings, get_text()
- prettyify
- html attribute

'''

from bs4 import BeautifulSoup as BS
import requests as req


url ="https://finance.naver.com/marketindex/exchangeList.naver"
res = req.get(url)
soup = BS(res.text,"html.parser")

# 타이틀 태그를 가져옴
# print(soup.title)
# # 타이틀 내용을 가져옴
# print(soup.title.string)


# 통화명 추출
tds = soup.find_all("td")

names = []
for td in tds:
    if len(td.find_all("a")) ==0:
        continue
    print(td.getText(strip=True)) #strip 옵션 공백, 엔터를 제거한다.
    # print(td.string)
    # # 스트링스 사용
    # for s in td.strings:
    #     print(s)
    # for s in td.stripped_strings:
    #     print(s)

    names.append(td.getText(strip=True))

# 매매 기준율 가져오기
prices = []
for td in tds:
    # 어떤 td는 class라는게 없을 수도 있으므로 방어코드 작성이 필요하다.
    if "class" in td.attrs:
        # class가 sale 인 값이 있으면 가격리스트에 추가
        if "sale" in td.attrs["class"]:
            prices.append(td.getText(strip=True))

print(names)
print(prices)

print(len(names))
print(len(prices))



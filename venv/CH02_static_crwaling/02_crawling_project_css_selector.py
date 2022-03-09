from bs4 import BeautifulSoup as BS
import requests as req


url ="https://finance.naver.com/marketindex/exchangeList.naver"
res = req.get(url)
soup = BS(res.text,"html.parser")
'''
CSS 셀렉터로 파싱이 유리한 이유
    * 프로그래머들이 자기가 보고 쓰기 편한 이름으로 설정해 놓으므로 이해가 쉽다.
    * 사람이 읽기 좋고, 이해하기 편한 이름, Human readable 
    * 동적 크롤링에서도 사용 됨.
    
CSS select 2가지 클래스 가지고 있을 경우

    * document.querySelector("div.main_content.main_content_new")
    * 클래스의 순서는 중요하지 않다. 
    * attribute = 속성 
    
CSS selector - attribute 예시
    ✔ *= : 포함
    ✔ ^= : ~으로 시작
    ✔ $= : ~으로 끝남
    
일반 한정자
    * 좀 더 세밀하게 select 하고 싶을 때 ( 사실 대부분의 경우)
    
    ✔ 한정자 예시
        - *  : 모든 노드들
        - div, p : div 와 p 노드들
        - div p : div 안에 있는 p 노드들
        - div > p : div 바로 안에 있는 p 노드들
        - div ~ p : p 옆(앞)에 있는 div 노드들
        - div + p : div 옆(뒤)에 있는 p 노드들 

고급 한정자 
    - :enabled >> 활성화된 상태
    - :checked >> 체크 된 상태
    - :disabled >> 비활성화 된 상태
    - :empty >> 값이 비어 있는 상태
    - :first-child >> 첫번쨰 잣기
    - :last-child >> 마지막 자식
    - :first-of-type >> 해당타입의 첫번쨰 노드
    - :last-of-type >> 해당타입의 마지막 노드
    - hover >> 마우스가 올라간 상태
    - :not >> 다음조건이 거짓일 경우
    - :nth-child >> n번째 자식
    - :nth-of-type >> n번째 타입
    
    

'''

names=[]
for td in soup.select("td.tit"):
    names.append(td.get_text(strip=True))

price=[]
for td in soup.select("td.sale"):
    price.append(td.get_text(strip=True))

print(names)
print(price)


# 고급 한정자 예제

#mutli line stringS
html = """

"""

soup = BS(html, "html.parser")

div = soup.select("div")
print(div[0].get_text(strip=True))

#enabled
# arr = soup.select("input:enabled")
# print(arr)

#checked
# arr = soup.select("input:checked")
# print(arr)

#disabled
# el = soup.select("inpt:disabled")
# print(el)

#empty
# arr = soup.select("label+input:empty")
# print(arr)

# firstchild
# arr = soup.select("b:first-child")
# print(arr)

# lastchild
# arr = soup.select("table tbody tr:last-child")
# print(arr)

#first-of-type
arr = soup.select("table tbody td:first-of-type")
print(arr)
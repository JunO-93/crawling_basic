'''
# 프로젝트 진행하며 배우게되는 내용
    - requests 활용한 기초적인 파싱
    - find(), split() 등을 활용한 기초적인 문자열 파싱
    - 정규식(regx)을 활용한 패턴검색
    - 쿼리스트링에 대한 이해
    - beautifulsoup을 활용한 편리한 html 파싱
    - css selector를 활용한 손쉬운 파싱
'''

import requests as req
import re

res = req.get("https://finance.naver.com/marketindex/?tabSel=exchange#tab_section")

html = res.text

# split으로 앞과 뒤를 지정하여 값을 가져오기
pos = html.split('<span class="value">')[1].split('</span>')[0]
print(pos)

# 정규식을 통하여 가져오기
s = '이 영화는 F등급 입니다.'
print(re.findall(r'영화는 (.)등급 입니다.',s))
# print(re.findall(r'<span class="value">([0-9],[0-9][0-9][0-9]\.[0-9][0-9])|([0-9][0-9][0-9]\.[0-9][0-9])',s))

# <span class="blind">미국 USD</span>
# <span class="value">1,217.50</span>
url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = req.get(url)
body = res.text

print("=================================================================")
# match ,search, findall
# 이 중에 findall 사용
# 정규 표현식을 미리 세팅할 수 있다.
'''
r = re.compile(r"미국 USD.*value\">(.*)</span>")
captures = r.findall(body)
print(captures)
'''
#
# 이렇게 하면 출력 : [] 아무것도 안나옴.
# 이유는 . 은 개행문자 즉, \n \t 같은 건 인식 못한다. 추가로 세팅해야한다.

# regex 수정
# *? 아무문자나 0개를 가져오는데 그중에서 가장 좁은 범위를 가져와라
# 환율 값만 가져오기
'''
r = re.compile(r"미국 USD.*?value\">(.*?)</", re.DOTALL)
captures = r.findall(body)
print(captures)
'''

# regex 수정 2
'''
환율 데이터 크롤링 후, 환율 계산기 생성
'''
r = re.compile(r"h_lst\">.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL)

captures = r.findall(body)
print(captures)


print("=========")
print("===환율===")
print("=========",end="\n\n")

for c in captures:
    print(f"{c[0]} : {c[1]}")

dollar = captures[0][1].replace(",","")
input_won = input("환율을 계산하고 싶은 금액 (원): ")
cvt_money = float(input_won) / float(dollar)

print(f"$ {cvt_money} 입니다.")

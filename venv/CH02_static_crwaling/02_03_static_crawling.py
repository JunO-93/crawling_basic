import requests



"""
Requests 주요함수

# GET : 요청, 값 가져오는 역할
# POST : 생성, 액션
# PUT : 수정, 덮어씌우기
# DELETE : 삭제

# PUT / HTTP/1.1
# Host: www.naver.com
"""

res = requests.get("https://www.naver.com/")
print(res.text)

# 내 IP 확인

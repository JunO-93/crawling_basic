import requests as req

# https://api.ipify.org/ 자신의 아이피를 알려주는 사이트

res = req.get("https://api.ipify.org/")
print(res.request.headers)
print(res.elapsed)

print(res.text)
# 바이트 값을 가지고 있다. 이미지나 동영상이 텍스트로 표현될 수 없으므로 해당 자료형을 가지고 올 때 사용할 수 있다.
print(res.raw)

# 정적 웹크롤링 이론
```buildoutcfg
* 크롤링 기초 : 웹 크롤러(web crawler)는 조직적, 자동화된 방법으로 월드 와이드 웹을 탐색하는 컴퓨터 프로그램이다. - 위키피디아 -
    ✔ 역사 : 검색을 위해 크롤링이 만들어 졌다. 홈페이지글들의 글을 구글이 모두 자기 서버로 가져와 검색엔진으로 조회할 수 있게 만들었다.
    ✔ 활용처 : 
        (1). 사이트에서 원하는 데이터 추출하기
        (2). 업무 자동화하기
        (3). 알림 받기
        
    - 인터넷과 웹( World wide web )                 
    - 웹서버와 디비
        ✔ CRUD
        DB --> 서버 --> 사용자
           <--     <--
    - http와 소켓
        ✔ HTTP : 
        Request Line , 
        Request-Line = Method Request-URI SP HTTP-Version CRLF (3개의 컴포넌트로 이루어져 있음)
            SP : 공백
            CRLF : 줄바꿈 후 한글자 띄우기
            ex) POST /upload HTTP/1.1  -> 리퀘스트 라인
        0개 이상의 헤더, 
        빈라인, 
        바디
            요청을 보낼 때, 같이 보내는 본문 이라고 생각하면 된다.
            
        의 구조로 이루어져 있다.
        
        ✔ HTTP METHOD
        GET : 데이터를 받기만 하겠다.
        HEAD : 헤더만 가져올 때 사용
        POST : 데이터를 요청을 주고 받기까지 하겠다.
        PUT : POST로 만들어진 것에 대해서 수정을 한다.
        DELETE : 삭제
        OPTIONS :  이것을 찌를 수 있는지?
        
        ✔ HTTP Example Login (계좌)
        1. 
        --> GET /money HTTP/1.1 #HTTP 1.1 에다가 GET /money를 요청 ( 로그인하지 않은 상태 )
                         
        ==> HTTP/1.1 400 Unauthorized ( 비 인증 상태 )
         
            - HTTP 버전이 선행되고 에러코드( status code )에 대한 추가정보가 주어진다.
            - status code 400 : 미인증 상태
                #Status code 
                100-199 : 정보전달용
                200-299 : 성공
                300-399 : 리다이렉트 ( 바로가기 연결 )
                400-499 : 클라이언트 에러 ( 요청에 있어서 실패 시, 클라이언트의 문제일 때) 
                500-599 : 서버에러 ( 요청에 있어서 실패 시, 서버의 문제일 때 )
                
        2. 로그인 시도 
        --> POST /login HTTP/1.1 
            User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
            
            id=apple&password=banana
            
        ==> HTTP/1.1 200 OK
            Set-Cookie: JSessionId=abcd1234 #쿠키를 셋한다
            
        3. 계좌잔고 재요청
        --> GET /money HTTP/1.1
            Cookie: JsessionId=abcd1234 #로그인에서 나온 쿠키
            
        ==> HTTP/1.1 200 OK
            money=15000
            
        ✔ Web Socket
        HTTP : 핑 퐁 --> 항상 request, response는 짝을 이룬다
        Socket : 자유롭다 ( 채팅같은 것 )
                                 
    - 브라우저
        ✔ 크롬, 인터넷 익스플로러, 파이어폭스, 엣지, 웨일, 사파리 등
        ✔ 브라우저의 필요성
            - 편의성
            - 보안
            - 스크립트 실행(동적 기능)        
    - 웹앱과 api
        ✔ 웹앱? 
            - 페이스북 기준으로 항상 로딩이 되어있는 곳과, 피드가 떠있는곳은 ( 켰을때 로딩이 시작되는 곳 ) --> 대부분 웹앱이 가지고 있는 특징이다.
            - UI로 그려내는것과 데이터를 분리되어 있는 것
            - 크롤링에선 UI를 크롤링하진 않는다.
            - 웹 앱은 골격만 로딩, 내용은 채우지 않음, 골격 로딩 후 내용을 요청 --> 이것이 API
        ✔ API 재사용성이 뛰어남, 서버 사이드 렌더링 ( 서버가 부분적으로 담당하므로써 디버깅도 편해졌다 )
    - 크롤링 주의사항
        ✔ 네티켓
            - https://www.robotstxt.org/robotstxt.html --> 하나의 규격과 관련된 robots.txt 사이트
    
* 정적 크롤링
    - requests
    - xml, html, json, jsonp, binary
    - regex
    - beautifulsoup
    - css    
    
* 동적 크롤링
    - browser
    - selenium

```
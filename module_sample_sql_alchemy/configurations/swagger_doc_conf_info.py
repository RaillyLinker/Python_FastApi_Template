# [Swagger 문서 설정 작성 파일]
# (Swagger 문서 타이틀)
swagger_doc_title = "SAMPLE-SQL-ALCHEMY"

# (Swagger 문서 버전)
swagger_doc_version = "1.0.0"

# (Swagger 문서 연락처)
swagger_doc_contact = {
    "name": "Railly Linker",
    "url": "https://railly-linker.tistory.com",
    "email": "raillylinker@gmail.com",
}

# (Swagger 문서 라이센스)
swagger_doc_license_info = {
    "name": "MIT",
    "url": "https://opensource.org/licenses/MIT",
}

# (Swagger 문서 공지)
swagger_doc_description = """
**[읽어주세요]**

**(공지)**
- 오류 제보, 요청 사항 환영 합니다.

**(일반 규칙)**
- 본 프로젝트가 제공하는 API 중 응답 반환값이 있는 API 의 경우, 반환값인 Response Body 는 항상 Nullable 입니다.

  해당 API 가 정상적으로 동작을 하였다면 Http Status Code 200 과 더불어 Swagger 에 게시된 해당 API 의 Response Body 의 형태와 같은 결과값을 반드시 반환할 것이지만,

  만약 데이터를 반환하기 위해 필요한 데이터가 반환 불가능한 상태(데이터베이스 조회시 원하는 데이터가 없는 상태 등)라면 Response Body 는 Null 이 될 것입니다.

- 서버에 입력하고 서버에서 반환하는 DATE_TIME 변수의 타임존은 항상 UTC 를 기준으로 합니다.

**(인증/인가 관련 규칙)**
- API 항목의 제목 문장의 마지막에 붙는 "<>" 는 해당 API 사용을 위한 권한을 의미합니다.

  예를들어 권한이 필요 없으면 표시 하지 않고, 로그인이 필요한 경우 <>, 

  특정 권한이 필요한 경우 <'ADMIN' or ('DEVELOPER' and 'MANAGER')> 와 같은 형식으로 표시됩니다.

  참고로 위의 예시의 경우는 ADMIN 권한이 있거나, 혹은 DEVELOPER 와 MANAGER 권한을 같이 가지고 있는 경우에만 동작할 것이라는 의미입니다.
- 토큰 인증 방식을 사용하는 api 에서 로그인이 필요한 API 요청시엔 네트워크 요청 Header 에 "Authorization" 이란 키로 

  로그인 API 에서 반환된 토큰 타입과 토큰 String 을 붙여서 보내주면 됩니다.

  예를들어 로그인시 토큰 타입이 "Bearer", 토큰 String 이 "abcd1234" 로 반환되었다면,

{"Header" : {"Authorization" : "Bearer abcd1234"}}

  위와 같은 형식으로, 토큰 타입 뒤에 한칸을 띄우고 토큰 String 을 합쳐서 헤더에 Authorization 이란 이름으로 보내면 됩니다.
- <> 가 붙지 않은(로그인이 필요치 않은) API 에도 Authorization Request Header 를 보내줘도 무방합니다.

  로그인 제한이 붙지 않은 API 에서 인증/인가 코드를 입력한 경우, 

  액세스 토큰 형식이 잘못 되었건, 만료되었건 상관없이 API 로직이 정상 실행됩니다.
- 토큰 인증 api 에서 사용하는 RefreshToken 은 AccessToken 발급(Login, Reissue api 사용)시마다 재발행됩니다.

  AccessToken 보다 더 길게 설정된 RefreshToken 의 만료시간 동안 토큰 재발급을 전혀 하지 않아 RefreshToken 마저 만료된 경우, 

  만료된 RefreshToken 으로 토큰 재발급 API 를 사용시 만료 에러가 떨어지는데, 이때는 클라이언트 측에서 멤버에게 재로그인을 요청해야합니다.
- 클라이언트 사이드에서 JWT 인증을 처리할 때는, 

  1. 로그인으로 JWT 정보를 로컬에 저장

  2. API Header 에 JWT Access Token 을 포함하여 요청을 보내기

  3. 만약 API 에서 401 status 가 반환된다면 JWT Access Token 과 Refresh Token 으로 reissue API 를 사용하여 새로운 JWT 를 받아오기

  4. Reissue 시 정상적으로 토큰이 갱신되었다면 새 정보를 로컬에 저장하고 401 이 반환되었던 API 를 다시 새로운 JWT Access Token 으로 호출하기

  5. Reissue 시 토큰을 받지 못했다면 로컬에서 기존 JWT 정보를 삭제하고 로그아웃 처리하기

  위와 같은 절차로 처리하시면 됩니다.

**(Dummy API)**
  - 프로젝트 개발 진행 시작 시점에 백엔드 개발자는 API 를 하나씩 구현하는 것이 아니라 인터페이스를 먼저 공개할 것입니다.

    이 인터페이스는 스웨거 문서에 표시되며, 요청시 데이터를 반환하지만, 해당 데이터는 하드코딩으로 심어둔 상수값(더미 데이터)일 뿐입니다.

    이렇듯, 아직 완성되지 않은 인터페이스와 더미 데이터를 먼저 공개하는 이유는,

    서버의 API 설계가 완료되어야만 클라이언트에서 API 요청 로직을 개발할 수 있기 때문에,

    최대한 빠르게 인터페이스를 공개하여 해당 API 를 클라이언트 개발에 사용할 수 있도록 하여, 전체 프로젝트 개발기간을 단축하는 것이 목적이며,

    백엔드 개발자의 입장에서는 놓칠 수 있는 부분에 대한 프론트 엔드 개발자의 수정 요청을, 

    API 구현 전의 시점에 얻을 수 있기에 상호간 이득을 얻을 수 있는 방법이기 때문입니다.
  - 더미 API 에 대한 스웨거 문서 내 표시 방법에 대해 설명하겠습니다.

    Controller 안에 속한 각 API 목록이 있습니다.

    그리고 각 API 목록별로 표시된 메소드, 주소의 오른쪽에는 N1, N2 와 같이 API 고유번호와 그 설명이 적혀있습니다.

    해당 설명의 가장 우측에 (설계중), 혹은 (더미) 라는 상태 태그를 붙일 것입니다.

    만약 (설계중) 이라고 붙은 API 는 할당된 API 고유 번호를 제외하고는 변경될 가능성이 존재하기 때문에 프론트 엔드 개발에서 무시하셔도 되며,

    이를 참고하여 원하는 인터페이스에 대한 의견을 내주시면 됩니다.

    (더미) 라고 붙은 API 의 경우는 추후 구현이 완료될 것이며, 상의없이 인터페이스를 변경할 일은 없기 때문에 프론트 엔드 개발에 사용하셔도 됩니다.

    구현까지 완료된 API 는 상태 태그를 제거할 것입니다.
"""

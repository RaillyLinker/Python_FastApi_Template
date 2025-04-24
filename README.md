# Python FastAPI Template

## 프로젝트 설명

- 본 프로젝트는 FastAPI 의 템플릿 프로젝트입니다.<br>
  <br>
  MSA 의 마이크로 서비스 단위, 모듈 단위, 기능 단위 구현이 되어 있는 프로젝트로,<br><br>
  자동 로깅 처리, JWT 인증/인가 처리, 설정 상수값 응집 처리, API 문서 생성 방법, 데이터베이스 연동 방법, 서버 분산 및 Kafka 연동 방식 등...<br>
  <br>
  구조적으로 명확히 분리하였으며, 클린 코드를 지향하였으므로,<br>
  실제 프로젝트에 적용할 기술에 대한 테스트 코드 작성, 및 이식이 용이 합니다.<br>
  <br>
  실제 상황에 사용될 기능들을 재활용 가능하게 구분하였으므로,<br>
  추후 어떤 프레임워크를 습득하더라도 이를 기반으로 빠른 습득이 가능합니다.<br><br>
  (ex : 별도 백엔드 프레임워크 습득시 본 프로젝트에서 지원하는 기능과 구조를 카피 하는 방식으로 구현하면 실용적인 코드 개발 능력 습득이 가능하며, 실무에 작성 코드 바로 적용 가능.)

  <br>
- 자세한 설명은 블로그 글로 대체합니다.
  https://railly-linker.tistory.com/entry/Python-FastAPI-%EA%B0%9C%EB%B0%9C-%EB%B0%A9%EB%B2%95-%EC%A0%95%EB%A6%AC

![화면 캡처 2025-04-20 185004](https://github.com/user-attachments/assets/01f7511f-2270-4c7b-82fd-41b1df822d33)

- 각 모듈별 가상 환경은 다르게 설정하고,<br>
  environment.yaml 로 관리하기<br>

  > 출력<br>
  > conda env export > conda_environment.yaml<br>
  > 입력 <br>
  > conda env create --file conda_environment.yaml

- 배포시 모듈 실행은, 프로젝트 루트 경로에서,

  > python module_sample_api/main.py --profile dev

  이런식으로

- 모듈 정보
  - 모듈 템플릿 (8080)
  - API 테스트 샘플 (12006)
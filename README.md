# Python FastAPI Template

## 프로젝트 설명

- 본 프로젝트는 FastAPI 의 템플릿 프로젝트입니다.<br>
  자세한 설명은 블로그 글로 대체합니다.
  https://railly-linker.tistory.com/entry/Python-FastAPI-%EA%B0%9C%EB%B0%9C-%EB%B0%A9%EB%B2%95-%EC%A0%95%EB%A6%AC

![화면 캡처 2025-04-20 185004](https://github.com/user-attachments/assets/01f7511f-2270-4c7b-82fd-41b1df822d33)

- 각 모듈별 가상 환경은 다르게 설정하고,<br>
  environment.yaml 로 관리하기<br>

> 출력<br>
> conda env export > environment.yaml<br>
> 입력 <br>
> conda env create --file environment.yaml

- 배포시 모듈 실행은, 프로젝트 루트 경로에서,
> python module_sample_api/main.py --profile dev

이런식으로
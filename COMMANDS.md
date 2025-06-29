# 데이터 파이프라인

| 명령어                                                 | 설명                        |
| ------------------------------------------------------ | --------------------------- |
| `poetry poe run-digital-data-etl`                      | 데이터 수집 ETL 실행        |
| `poetry poe run-velog-data-etl`                        | Velog 데이터 수집           |
| `poetry poe run-feature-engineering-pipeline`          | 피처 엔지니어링 실행        |
| `poetry poe run-generate-instruct-datasets-pipeline`   | 인스트럭션 데이터셋 생성    |
| `poetry poe run-generate-preference-datasets-pipeline` | 선호도 데이터셋 생성        |
| `poetry poe run-end-to-end-data-pipeline`              | 위 모든 과정을 한 번에 실행 |

# 유틸리티 파이프라인

| 명령어                                            | 설명                          |
| ------------------------------------------------- | ----------------------------- |
| `poetry poe run-export-data-warehouse-to-json`    | 데이터 웨어하우스 → JSON 추출 |
| `poetry poe run-import-data-warehouse-from-json`  | JSON → 데이터 웨어하우스 적재 |
| `poetry poe run-export-artifact-to-json-pipeline` | ZenML 아티팩트 JSON 추출      |

# 학습 및 평가 파이프라인

| 명령어                               | 설명                 |
| ------------------------------------ | -------------------- |
| `poetry poe run-training-pipeline`   | 학습 파이프라인 실행 |
| `poetry poe run-evaluation-pipeline` | 평가 파이프라인 실행 |

# 추론 관련 명령어

| 명령어                                 | 설명                    |
| -------------------------------------- | ----------------------- |
| `poetry poe call-rag-retrieval-module` | RAG 모듈 테스트 호출    |
| `poetry poe run-inference-ml-service`  | 추론 REST API 서버 실행 |
| `poetry poe call-inference-ml-service` | 추론 API 호출 테스트    |

# 인프라 (서버 실행 등)

| 명령어                                                                 | 설명                               |
| ---------------------------------------------------------------------- | ---------------------------------- |
| `poetry poe local-infrastructure-up` / `...down`                       | 로컬 Docker · ZenML 환경 시작/종료 |
| `poetry poe set-local-stack`                                           | ZenML 로컬 스택 설정               |
| `poetry poe set-aws-stack`                                             | ZenML AWS 스택 설정                |
| `poetry poe set-asynchronous-runs`                                     | 비동기 실행 설정                   |
| `poetry poe create-sagemaker-role` / `create-sagemaker-execution-role` | SageMaker IAM 역할 생성            |
| `poetry poe deploy-inference-endpoint`                                 | SageMaker 추론 엔드포인트 배포     |
| `poetry poe test-sagemaker-endpoint` / `delete-inference-endpoint`     | 엔드포인트 테스트/삭제             |
| `poetry poe build-docker-image`                                        | Docker 이미지 빌드                 |
| `poetry poe run-docker-end-to-end-data-pipeline`                       | Docker에서 데이터 파이프라인 실행  |

# QA & Testing

| 명령어                                   | 설명                         |
| ---------------------------------------- | ---------------------------- |
| `poetry poe lint-check` / `lint-fix`     | 코드 린트 검사 / 자동 수정   |
| `poetry poe format-check` / `format-fix` | 코드 포매팅 검사 / 자동 수정 |
| `poetry poe gitleaks-check`              | 비밀 키 노출 검사            |
| `poetry poe test`                        | PyTest 실행                  |

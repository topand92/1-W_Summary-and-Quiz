# Summary-and-Quiz
- 한국어 텍스트 요약 및 퀴즈 생성 AI (2학년 복학 전 겨울학기 프로젝트)

- 협업용 워크스페이스는 노션에 메인으로 구성했습니다.
  - 링크: [Workspace](https://sj92.notion.site/summary-and-quiz)

- 프로젝트를 진행하면서 관련 정보를 수집한 깃허브 위키입니다.
  - 링크: [Wiki](https://github.com/topand92/Summary-and-Quiz/wiki)

- 파인튜닝을 테스트한 모델은 용량 문제로 허깅 페이스에 대신 업로드 했습니다.
  - 링크: [Hugging Face](https://huggingface.co/sgjeong/Private_Fine-tuning_Test)

- 이슈 관리 테스트
  - 링크: [Test](https://github.com/topand92/Summary-and-Quiz/issues)

## 파일 정리

### main.ipynb
- 완성 파일
### README.md
- 현재 README 파일

### notebook_study
파인튜닝 실습을 위해 테스트한 코드들
- 0_download_model.ipynb
  - 파인튜닝 실습에 사용한 모델을 다운로드
- 1_model_test.ipynb
  - 로컬에 설치된 모델의 사용법을 테스트
- 2_download_dataset.ipynb
  - 파인튜닝 실습에 사용한 데이터셋을 다운로드
- 3_eda.ipynb
  - 로컬에 설치된 데이터셋 EDA
- 4_train.ipynb
  - 파인튜닝 실습
- 5_visualization.ipynb
  - 데이터 시각화
- 6_evaluate.ipynb
  - 요약 모델 평가

### notebook_draft
main 파일 구현을 위해 테스트한 코드들
- download_llama.py
  - 라마 한국어 모델 다운로드
- openai.ipynb
  - OpenAI API Key와 랭체인 테스트
- v1.ipynb
  - 모델 활용 1안
- v2.ipynb
  - 모델 활용 2안
- test.ipynb
  - main 파일의 초안

# 성적 CSV 검증기

## ① 무엇을 하나요 (What · 현재 상태)

성적 CSV에서 0~100의 정수 점수를 읽고, 보관한 이름·점수와 제외한 행의 번호·내용·이유를 각각 돌려줍니다. 같은 이름은 모두 보관합니다. 평균·학점 계산은 아직 하지 않습니다.

## ② 왜 만들었나요 (Why)

점수가 하나 비어 있어도 나머지 학생의 점수는 읽을 수 있어야 합니다. 제외한 행의 번호와 이유를 남기면 원본에서 어느 줄을 확인해야 할지 바로 알 수 있습니다.

## ③ 어떻게 쓰나요 (How)

저장소 폴더에서 다음 명령을 실행합니다.

```
python --version
python -m pip install --user -U pytest~=7.0 pytest-cov
python load_scores.py scores.csv
```

예상 결과는 보관 5개, 제외 5개입니다.

## ④ 어떻게 테스트하나요

아래에서 사용하는 터미널에 맞는 줄을 먼저 실행합니다. 오래된 pytest 플러그인이 자동으로 로드되는 것을 막는 설정입니다.

- 명령 프롬프트(CMD) `set PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`
- PowerShell `$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD = "1"`
- Bash `export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`

```
python -m pytest test_load_scores.py -q
```

실제 결과는 `12 passed`입니다. 기본 11개에 `weird.csv` 보강 테스트 1개를 더했습니다.

`test_bug_A.py`와 `test_bug_B.py`는 AI 실험에서 받은 첫 응답입니다. 아래처럼 각각 실행하면 `find_max`가 마지막 원소를 검사하지 않는 버그가 드러납니다. A는 3개 통과·2개 실패, B는 3개 통과·1개 실패였습니다.

```
python -m pytest test_bug_A.py -q
python -m pytest test_bug_B.py -q
```

## ⑤ 파일 구성

| 파일 | 하는 일 |
| --- | --- |
| load_scores.py | CSV를 읽어 `(kept, skipped)`를 반환 |
| scores.csv · empty.csv · weird.csv | 일반 입력, 헤더만 있는 입력, 잘못된 값이 섞인 입력 |
| test_load_scores.py | 기본 테스트와 빈 이름 보강 테스트 |
| bug3_logic.py · test_bug_A.py · test_bug_B.py | 배포된 버그 코드와 A·B 실험 응답 |
| prompts.txt | 배포된 AI 실험 요청문 |

## ⑥ 만든 사람과 AI 사용

- 만든 사람 : 송채민
- 사용한 AI 도구·모델 : Copilot Chat
- AI에게 도움받은 부분 : 기본 테스트 구성과 A·B 비교 실험용 테스트 코드 초안 작성
- 확인한 부분 : Python 3.14에서 기본 테스트를 실행해 12개가 통과했고, A·B 테스트는 각각 실행해 실패한 항목을 비교했다.

## 라이선스

MIT License (LICENSE 파일 참고)

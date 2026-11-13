# 자격증 소개 | AICE Associate은(는) 어떤 자격증인가

## 한 줄로 설명하면

KT가 개발하고 한국경제신문과 함께 주관하는 **AI 활용 능력 시험**이다. Associate 등급은 Python으로 데이터를 전처리하고 머신러닝·딥러닝 모델을 직접 만드는 **실습형 시험**이다.

:::tip 이런 사람에게 맞다
- AI·데이터 분야 취업을 준비하는 학생
- 파이썬을 배우고 있어 실력을 증명할 목표가 필요한 학생
- 객관식보다 직접 해 보는 시험이 맞는 학생
:::

## 시험 한눈에

| 항목 | 내용 |
|---|---|
| 주관 | KT · 한국경제신문 (aice.study) |
| 방식 | 온라인 실습형 (Jupyter 환경) |
| 문항 | 14문항 / 90분 |
| 합격 | 80점 이상 |
| 유효 기간 | 3년 |

## 따면 어디에 쓰나

- AI·데이터 직무 서류에서 **실제로 모델을 만들 줄 안다**는 증명
- 빅데이터분석기사 실기와 내용이 많이 겹친다

## 난이도와 준비 기간

- 문항 흐름이 정해져 있어 **연습한 만큼 점수가 나온다**
- 파이썬 기초가 없으면 시작이 어렵다
- 파이썬 기초가 있으면 3~4주

## 함께 보면 좋은 자격증 · 추천 순서

- 함께 → **빅데이터분석기사**, **ADsP**
- AI 활용 쪽 → **AI-POT**
- 상위 → AICE Professional

:::exam 준비할 때 알아 둘 것
- 파이썬 → 데이터 분석 → 머신러닝 순서로 공부하면 시험 범위와 그대로 맞는다
- 시험 환경을 미리 써 보는 것이 중요하다 (공식 사이트 체험 환경)
:::

## 더 자세한 정보는 여기서 확인

- **AICE 공식 사이트** (aice.study): 시험 일정, 응시료, 등급별 출제 범위, 샘플 문항, 체험 환경

시험 일정·응시료·출제 기준은 해마다 바뀔 수 있다. **응시 전에 위 공식 사이트에서 최신 공고를 꼭 확인**하자.

## 자주 묻는 질문

- **Q. 코딩 처음인데 가능해요?** 파이썬 기초부터 배우면 가능하다. 시험 자체는 정형화되어 있다.
- **Q. 국가자격인가요?** 국가자격은 아니고 기업 주관 민간 시험이다.

# 시작하기 | 시험 구성과 공부 순서

## AICE Associate는 어떤 시험인가

AICE(AI Certificate for Everyone)는 **KT가 개발하고 한국경제신문과 함께 주관**하는 AI 활용 능력 시험이다. Associate는 그중 실무 입문 등급으로, **Python으로 데이터를 다루고 머신러닝·딥러닝 모델을 직접 만드는 실습형 시험**이다. 객관식 이론 시험이 아니다.

| 구분 | 내용 |
|---|---|
| 주관 | KT · 한국경제신문 (aice.study) |
| 등급 체계 | Future(초·중) · Basic · **Associate** · Professional |
| 방식 | 온라인 실습형. 웹 브라우저의 **Jupyter 환경**에서 코드 작성 |
| 문항 | **14문항 / 90분** |
| 합격 | 100점 만점 **80점 이상** |
| 응시료 | 80,000원 |
| 자격 유효 | 3년 |
| 사용 언어 | Python (pandas, numpy, matplotlib, seaborn, scikit-learn, TensorFlow/Keras) |
| 오픈북 | 인터넷 검색 불가. 시험 환경 내 도움말 사용 가능 |

| 문항 흐름 (예) | 내용 |
|---|---|
| 1~3 | 라이브러리 임포트, 데이터 불러오기, 시각화로 데이터 확인 |
| 4~8 | 결측치·이상치 처리, 불필요한 열 삭제, 원-핫 인코딩, 데이터 분할, 스케일링 |
| 9~11 | 머신러닝 모델(의사결정나무, 랜덤 포레스트, XGBoost 등) 학습 |
| 12~13 | 딥러닝 모델(Keras Sequential) 설계·학습 |
| 14 | 모델 성능 평가 (MAE, 정확도 등) |

:::warn 접수 전에 꼭 다시 확인할 것
2026년 11월 기준이다. 응시료와 문항 구성은 AICE 공식 사이트(aice.study) 공고를 확인하자. 공식 사이트에 **샘플 문항과 체험 환경**이 있으니 반드시 한 번 풀어 보고 들어가자. 문제는 "변수명 `df`로 저장하세요", "`X_train`, `X_test` …으로 분할하세요"처럼 **지정한 변수명**을 쓰라고 한다. 변수명이 다르면 채점이 안 된다.
:::

## 공부 순서

1. **1주** — Python 기초 문법과 pandas 데이터 다루기
2. **2주** — 시각화(matplotlib, seaborn)와 전처리
3. **3주** — scikit-learn 머신러닝 흐름
4. **4주** — Keras 딥러닝
5. **5주** — 마지막 장의 모의 문제를 **처음부터 끝까지 손으로 쳐서** 90분 안에 끝내기

# 데이터 다루기 | Python과 pandas 기본

## 라이브러리 불러오기

시험 첫 문항은 대부분 라이브러리 임포트다. 관례적인 별칭을 그대로 쓴다.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

## 데이터 불러오기와 확인

```python
df = pd.read_csv("data.csv")             # CSV
df = pd.read_json("data.json")           # JSON
df = pd.read_excel("data.xlsx")          # 엑셀

df.head()          # 앞 5행
df.tail(3)         # 뒤 3행
df.info()          # 열, 자료형, 결측 아닌 개수
df.describe()      # 수치형 기초 통계
df.shape           # (행 수, 열 수)
df.columns         # 열 이름
df.dtypes          # 열별 자료형
df["col"].value_counts()    # 범주별 개수
df["col"].unique()          # 고유값
df["col"].nunique()         # 고유값 개수
```

## 선택과 필터링

```python
df["age"]                     # 열 하나 → Series
df[["age", "sex"]]            # 여러 열 → DataFrame
df.loc[0:4, ["age", "sex"]]   # 라벨 기준 (끝 포함)
df.iloc[0:5, 0:2]             # 위치 기준 (끝 제외)
df[df["age"] >= 30]
df[(df["age"] >= 30) & (df["sex"] == "M")]
df[df["city"].isin(["서울", "부산"])]
df.query("age >= 30 and sex == 'M'")
```

## 정렬, 그룹, 병합

```python
df.sort_values("price", ascending=False)
df.groupby("city")["price"].mean()
df.groupby(["city", "type"]).agg({"price": "mean", "id": "count"})
pd.merge(df1, df2, on="id", how="left")      # inner, left, right, outer
pd.concat([df1, df2], axis=0)                # 위아래로 붙이기
df.pivot_table(index="city", columns="type", values="price", aggfunc="mean")
```

:::quiz
Q. DataFrame의 열 이름, 자료형, 결측이 아닌 값의 개수를 한 번에 확인하는 메서드는?
1) df.describe()
2) df.info()
3) df.head()
4) df.shape
> 정답 2 | info()다.

Q. df.iloc[0:3]이 반환하는 행의 개수는?
1) 2
2) 3
3) 4
4) 0
> 정답 2 | iloc은 끝 위치를 포함하지 않으므로 0, 1, 2 세 행이다.

Q. 'city' 열의 범주별 개수를 세는 코드는?
1) df["city"].count()
2) df["city"].value_counts()
3) df["city"].unique()
4) df.groupby("city")
> 정답 2 | value_counts()다.
:::

# 데이터 다루기 | 시각화로 데이터 이해하기

## 자주 나오는 그래프

```python
# 범주별 개수
sns.countplot(data=df, x="churn")
plt.show()

# 분포
sns.histplot(data=df, x="age", bins=30, kde=True)
sns.kdeplot(data=df, x="age", hue="churn")

# 이상치 확인
sns.boxplot(data=df, x="type", y="price")

# 두 수치형 변수 관계
sns.scatterplot(data=df, x="area", y="price", hue="type")
sns.jointplot(data=df, x="area", y="price")

# 범주별 평균
sns.barplot(data=df, x="city", y="price")

# 상관관계 히트맵 (수치형만)
corr = df.select_dtypes("number").corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.show()

# 여러 변수 한 번에
sns.pairplot(df[["age", "price", "area"]])
```

:::exam 시각화 문항이 묻는 것
그래프를 그린 다음 "**가장 상관관계가 높은 변수**를 답안 변수에 저장하라", "**이상치가 있는 열**은?" 같은 해석 질문이 함께 나온다. 히트맵에서는 대각선(자기 자신과 상관 1)을 빼고 타깃과의 상관계수 절댓값이 가장 큰 열을 찾는다.

```python
corr["price"].drop("price").abs().idxmax()
```
:::

:::quiz
Q. 수치형 변수 간 상관계수를 색으로 표현하는 그래프 함수는?
1) sns.countplot
2) sns.heatmap
3) sns.histplot
4) sns.boxplot
> 정답 2 | df.corr() 결과를 heatmap으로 그린다.

Q. 범주형 타깃 변수의 클래스별 데이터 개수를 막대로 보는 함수는?
1) sns.countplot
2) sns.scatterplot
3) sns.kdeplot
4) sns.jointplot
> 정답 1 | countplot이다.
:::

# 데이터 다루기 | 전처리

## 결측치

```python
df.isnull().sum()                        # 열별 결측 개수
df.isna().sum().sum()                    # 전체 결측 개수

df = df.dropna()                         # 결측이 있는 행 모두 삭제
df = df.dropna(subset=["income"])        # 특정 열 기준
df = df.drop(columns=["memo"])           # 결측이 너무 많은 열 삭제

df["age"] = df["age"].fillna(df["age"].mean())
df["city"] = df["city"].fillna(df["city"].mode()[0])   # 최빈값
df["price"] = df["price"].fillna(method="ffill")        # 앞 값으로
```

## 자료형 변환과 값 바꾸기

```python
df["TotalCharge"] = pd.to_numeric(df["TotalCharge"], errors="coerce")  # 숫자 아닌 값 → NaN
df["date"] = pd.to_datetime(df["date"])
df["sex"] = df["sex"].replace({"M": 0, "F": 1})
df["churn"] = df["churn"].map({"Yes": 1, "No": 0})
df = df[df["price"] > 0]                                 # 이상한 값 제거
df["age"] = df["age"].astype(int)
```

## 이상치

```python
q1 = df["price"].quantile(0.25)
q3 = df["price"].quantile(0.75)
iqr = q3 - q1
df = df[(df["price"] >= q1 - 1.5 * iqr) & (df["price"] <= q3 + 1.5 * iqr)]
```

## 범주형 인코딩

```python
# 원-핫 인코딩 (시험에서 가장 자주 나옴)
cat_cols = df.select_dtypes("object").columns
df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

# 레이블 인코딩
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df["grade"] = le.fit_transform(df["grade"])
```

:::tip drop_first=True
범주가 k개면 k−1개 더미만 있어도 정보가 다 담긴다. 선형 모델에서 다중공선성을 줄이려고 쓴다. 문제에서 지정하면 그대로 따른다.
:::

## 데이터 분할과 스케일링

```python
from sklearn.model_selection import train_test_split

X = df.drop("churn", axis=1)
y = df["churn"]
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

from sklearn.preprocessing import StandardScaler, MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)    # 학습 데이터로 fit
X_valid = scaler.transform(X_valid)        # 검증 데이터는 transform만
```

:::warn 스케일러는 학습 데이터로만 fit
검증·테스트 데이터까지 fit하면 **데이터 누수**가 생긴다. 시험에서도 "train에는 fit_transform, valid에는 transform"을 확인한다. 분할은 스케일링보다 **먼저** 한다.
:::

:::quiz
Q. 문자열이 섞인 열을 숫자로 바꾸면서 변환할 수 없는 값을 NaN으로 만드는 코드는?
1) df["a"].astype(float)
2) pd.to_numeric(df["a"], errors="coerce")
3) df["a"].replace("", 0)
4) df["a"].fillna(0)
> 정답 2 | errors="coerce"를 쓴다.

Q. 범주형 열을 0/1 더미 열로 바꾸는 pandas 함수는?
1) pd.get_dummies
2) pd.factorize
3) pd.cut
4) pd.melt
> 정답 1 | get_dummies다.

Q. 데이터를 학습 80%, 검증 20%로 나누는 train_test_split 인자는?
1) train_size=0.2
2) test_size=0.2
3) random_state=0.2
4) stratify=0.2
> 정답 2 | test_size=0.2다.

Q. 스케일링 순서로 옳은 것은?
1) 전체 데이터에 fit_transform 후 분할
2) 분할 후 train에 fit_transform, valid에 transform
3) 분할 후 valid에 fit_transform, train에 transform
4) 분할 후 둘 다 fit_transform
> 정답 2 | 데이터 누수를 막는다.

Q. 분류 문제에서 학습·검증 데이터의 클래스 비율을 같게 유지하려면 train_test_split에 어떤 인자를 주는가?
1) shuffle=False
2) stratify=y
3) random_state=42
4) test_size=0.3
> 정답 2 | stratify다.
:::

# 모델링 | 머신러닝 모델

## scikit-learn 공통 흐름

모든 모델이 **생성 → fit → predict → 평가** 같은 모양이다.

```python
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier

# 분류
dt = DecisionTreeClassifier(max_depth=5, random_state=42)
dt.fit(X_train, y_train)
pred = dt.predict(X_valid)

rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
rf.fit(X_train, y_train)

lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
proba = lr.predict_proba(X_valid)[:, 1]   # 양성 클래스 확률

# 회귀
reg = RandomForestRegressor(n_estimators=100, random_state=42)
reg.fit(X_train, y_train)
```

## 부스팅 모델

```python
from xgboost import XGBClassifier, XGBRegressor
from lightgbm import LGBMClassifier, LGBMRegressor

xgb = XGBClassifier(n_estimators=100, max_depth=5, learning_rate=0.1, random_state=42)
xgb.fit(X_train, y_train)

lgbm = LGBMRegressor(n_estimators=100, random_state=42)
lgbm.fit(X_train, y_train)
```

## 주요 하이퍼파라미터

| 모델 | 인자 | 의미 |
|---|---|---|
| 의사결정나무 | `max_depth` | 최대 깊이. 크면 과대적합 |
| | `min_samples_split`, `min_samples_leaf` | 분할·리프 최소 샘플 수 |
| 랜덤 포레스트 | `n_estimators` | 트리 개수 |
| | `max_features` | 분할마다 고려할 변수 수 |
| XGBoost / LightGBM | `learning_rate` | 학습률. 작으면 트리를 더 많이 |
| KNN | `n_neighbors` | 이웃 수 K |
| 공통 | `random_state` | 결과 재현용 난수 고정 |

## 평가

```python
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score,
                             confusion_matrix, classification_report, roc_auc_score,
                             mean_absolute_error, mean_squared_error, r2_score)

# 분류
accuracy_score(y_valid, pred)
confusion_matrix(y_valid, pred)
print(classification_report(y_valid, pred))
roc_auc_score(y_valid, proba)

# 회귀
mae = mean_absolute_error(y_valid, pred)
mse = mean_squared_error(y_valid, pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_valid, pred)
```

:::fig cm

## 하이퍼파라미터 탐색과 변수 중요도

```python
from sklearn.model_selection import GridSearchCV, cross_val_score

params = {"max_depth": [3, 5, 7], "n_estimators": [100, 200]}
gs = GridSearchCV(RandomForestClassifier(random_state=42), params, cv=5, scoring="accuracy")
gs.fit(X_train, y_train)
print(gs.best_params_, gs.best_score_)

scores = cross_val_score(rf, X_train, y_train, cv=5)
print(scores.mean())

imp = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)
print(imp.head())
```

:::quiz
Q. scikit-learn 모델을 학습시키는 메서드는?
1) train()
2) fit()
3) compile()
4) learn()
> 정답 2 | fit()이다. compile()은 Keras.

Q. 분류 모델에서 클래스별 확률을 반환하는 메서드는?
1) predict()
2) predict_proba()
3) score()
4) transform()
> 정답 2 | predict_proba()다.

Q. 랜덤 포레스트에서 트리 개수를 정하는 인자는?
1) max_depth
2) n_estimators
3) learning_rate
4) n_neighbors
> 정답 2 | n_estimators다.

Q. 회귀 모델의 평균 절대 오차를 계산하는 함수는?
1) mean_squared_error
2) mean_absolute_error
3) r2_score
4) accuracy_score
> 정답 2 | MAE다.

Q. 실제 양성 중 모델이 양성으로 맞힌 비율은?
1) 정확도
2) 정밀도
3) 재현율
4) 특이도
> 정답 3 | TP / (TP + FN).
:::

# 모델링 | 딥러닝 모델 (Keras)

## 기본 구조

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

model = Sequential([
    Dense(64, activation="relu", input_shape=(X_train.shape[1],)),
    Dropout(0.3),
    Dense(32, activation="relu"),
    Dropout(0.3),
    Dense(1, activation="sigmoid")        # 이진 분류
])
model.summary()
```

## 문제 유형별 마지막 층과 손실 함수

| 문제 | 마지막 층 | loss | metrics |
|---|---|---|---|
| **이진 분류** | `Dense(1, activation="sigmoid")` | `binary_crossentropy` | `accuracy` |
| **다중 분류 (정수 레이블)** | `Dense(클래스 수, activation="softmax")` | `sparse_categorical_crossentropy` | `accuracy` |
| **다중 분류 (원-핫 레이블)** | `Dense(클래스 수, activation="softmax")` | `categorical_crossentropy` | `accuracy` |
| **회귀** | `Dense(1)` (활성화 없음) | `mse` | `mae` |

:::exam 가장 자주 틀리는 조합
레이블이 0, 1, 2처럼 **정수**인데 `categorical_crossentropy`를 쓰면 오류가 난다. 정수면 `sparse_`가 붙은 것. 원-핫으로 바꾸려면 `tf.keras.utils.to_categorical(y)`.
:::

## 컴파일과 학습

```python
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

es = EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True)
mc = ModelCheckpoint("best_model.h5", monitor="val_loss", save_best_only=True)

history = model.fit(X_train, y_train,
                    validation_data=(X_valid, y_valid),
                    epochs=50, batch_size=32,
                    callbacks=[es, mc], verbose=1)
```

| 용어 | 의미 |
|---|---|
| epoch | 전체 학습 데이터를 한 번 다 보는 것 |
| batch_size | 가중치를 한 번 갱신할 때 쓰는 샘플 수 |
| EarlyStopping | 검증 손실이 `patience`번 연속 나아지지 않으면 중단 |
| ModelCheckpoint | 가장 좋은 모델을 파일로 저장 |
| Dropout(0.3) | 학습 때 뉴런 30%를 무작위로 끔 (과대적합 방지) |

## 학습 곡선과 평가

```python
plt.plot(history.history["loss"], label="loss")
plt.plot(history.history["val_loss"], label="val_loss")
plt.xlabel("epoch"); plt.legend(); plt.show()

loss, acc = model.evaluate(X_valid, y_valid)
pred = (model.predict(X_valid) > 0.5).astype(int)     # 이진 분류 확률 → 클래스
pred_multi = np.argmax(model.predict(X_valid), axis=1) # 다중 분류
```

:::tip 학습 곡선 읽기
train loss는 계속 줄어드는데 **val loss가 다시 올라가기 시작하면 과대적합**이다. 그 지점에서 멈추게 하는 것이 EarlyStopping이다.
:::

:::quiz
Q. 3개 클래스 다중 분류 모델의 출력층으로 알맞은 것은?
1) Dense(1, activation="sigmoid")
2) Dense(3, activation="softmax")
3) Dense(3, activation="relu")
4) Dense(1)
> 정답 2 | 클래스 수만큼, softmax.

Q. 레이블이 0, 1, 2 정수일 때 쓰는 손실 함수는?
1) binary_crossentropy
2) categorical_crossentropy
3) sparse_categorical_crossentropy
4) mse
> 정답 3 | 정수 레이블이면 sparse를 쓴다.

Q. 집값을 예측하는 회귀 모델의 출력층과 손실 함수 조합은?
1) Dense(1, activation="sigmoid") / binary_crossentropy
2) Dense(1) / mse
3) Dense(10, activation="softmax") / mse
4) Dense(1, activation="relu") / accuracy
> 정답 2 | 회귀는 활성화 없는 Dense(1)과 mse.

Q. 검증 손실이 개선되지 않을 때 학습을 멈추게 하는 콜백은?
1) ModelCheckpoint
2) EarlyStopping
3) Dropout
4) TensorBoard
> 정답 2 | EarlyStopping이다.

Q. 학습 데이터 1,000개, batch_size 100이면 1 epoch 동안 가중치는 몇 번 갱신되는가?
1) 1
2) 10
3) 100
4) 1,000
> 정답 2 | 1000 / 100 = 10번.
:::

# 마무리 | 실전 모의 문제 (14문항)

## 상황

통신사 고객 데이터 `churn.csv`로 **고객 이탈 여부(`Churn`: Yes/No)**를 예측한다. 실제 시험처럼 각 문항의 지시대로 코드를 작성해 보자. 아래 해설 코드는 한 흐름으로 이어진다.

:::ex 문항과 답안 코드
**1.** pandas를 `pd`, numpy를 `np`, seaborn을 `sns`로 임포트하세요.
```python
import pandas as pd, numpy as np, seaborn as sns, matplotlib.pyplot as plt
```
**2.** `churn.csv`를 읽어 `df`에 저장하세요.
```python
df = pd.read_csv("churn.csv")
```
**3.** `Churn` 열의 클래스별 개수를 countplot으로 그리세요.
```python
sns.countplot(data=df, x="Churn"); plt.show()
```
**4.** 불필요한 `customerID` 열을 삭제하세요.
```python
df = df.drop("customerID", axis=1)
```
**5.** `TotalCharges` 열을 숫자형으로 바꾸고, 결측치가 있는 행을 삭제하세요.
```python
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna()
```
**6.** `Churn`의 Yes를 1, No를 0으로 바꾸세요.
```python
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
```
**7.** 수치형 열의 상관관계 히트맵을 그리고, `Churn`과 상관계수 절댓값이 가장 큰 열 이름을 `answer7`에 저장하세요.
```python
corr = df.select_dtypes("number").corr()
sns.heatmap(corr, annot=True); plt.show()
answer7 = corr["Churn"].drop("Churn").abs().idxmax()
```
**8.** object 타입 열을 모두 원-핫 인코딩해 `df`에 저장하세요 (`drop_first=True`).
```python
df = pd.get_dummies(df, columns=df.select_dtypes("object").columns, drop_first=True)
```
**9.** `Churn`을 y, 나머지를 X로 하여 8:2로 나누고 `X_train, X_valid, y_train, y_valid`에 저장하세요 (`random_state=42`, `stratify=y`).
```python
from sklearn.model_selection import train_test_split
X = df.drop("Churn", axis=1); y = df["Churn"]
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
```
**10.** MinMaxScaler로 X_train은 fit_transform, X_valid는 transform하세요.
```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train); X_valid = scaler.transform(X_valid)
```
**11.** `max_depth=5`인 의사결정나무를 `dt`로 학습시키세요.
```python
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(max_depth=5, random_state=42).fit(X_train, y_train)
```
**12.** `n_estimators=100`인 랜덤 포레스트를 `rf`로 학습시키세요.
```python
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100, random_state=42).fit(X_train, y_train)
```
**13.** 은닉층 2개(64, 32, relu)와 Dropout(0.2)을 가진 이진 분류 딥러닝 모델을 만들어 30 epoch, batch_size 32로 학습하고 기록을 `history`에 저장하세요.
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
model = Sequential([Dense(64, activation="relu", input_shape=(X_train.shape[1],)), Dropout(0.2),
                    Dense(32, activation="relu"), Dropout(0.2), Dense(1, activation="sigmoid")])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
history = model.fit(X_train, y_train, validation_data=(X_valid, y_valid), epochs=30, batch_size=32)
```
**14.** 랜덤 포레스트로 X_valid를 예측해 정확도를 `acc`에 저장하세요.
```python
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_valid, rf.predict(X_valid))
print(acc)
```
:::

## 회귀형 변형

같은 흐름에서 타깃이 연속형(예: 배달 시간, 집값)이면 바뀌는 것만 정리한다.

| 단계 | 분류 | 회귀 |
|---|---|---|
| 분할 | `stratify=y` | stratify 없음 |
| 모델 | `...Classifier` | `...Regressor` |
| 딥러닝 출력 | `Dense(1, activation="sigmoid")` | `Dense(1)` |
| 손실 | `binary_crossentropy` | `mse` |
| 평가 | `accuracy_score` | `mean_absolute_error`, `mean_squared_error` |

:::quiz
Q. 다음 중 데이터 누수가 발생하는 코드는?
1) scaler.fit(X_train)
2) scaler.fit(pd.concat([X_train, X_valid]))
3) scaler.transform(X_valid)
4) train_test_split 후 스케일링
> 정답 2 | 검증 데이터 정보가 학습에 들어간다.

Q. df.drop("customerID", axis=1)에서 axis=1의 의미는?
1) 행 삭제
2) 열 삭제
3) 첫 번째 행 삭제
4) 결측 삭제
> 정답 2 | axis=1은 열 방향이다.

Q. Keras 이진 분류 모델의 predict 결과를 0/1 클래스로 바꾸는 코드는?
1) np.argmax(pred)
2) (pred > 0.5).astype(int)
3) pred.round(2)
4) pred.sum()
> 정답 2 | 시그모이드 확률을 0.5 기준으로 나눈다.

Q. 회귀 문제에서 train_test_split에 stratify를 쓰지 않는 이유는?
1) 타깃이 연속형이라 클래스 비율이 없기 때문
2) 속도가 느려서
3) random_state와 충돌해서
4) 회귀는 분할하지 않아서
> 정답 1 | stratify는 범주 비율을 맞추는 기능이다.
:::

:::tip 시험 직전 체크리스트
- 문제에서 지정한 **변수명** 그대로 쓰기 (df, X_train, answer7 …)
- `read_csv`, `info`, `isnull().sum()`, `value_counts`, `drop(axis=1)`
- `to_numeric(errors="coerce")`, `fillna`, `dropna`, `map`, `get_dummies(drop_first=True)`
- `train_test_split(test_size, random_state, stratify)`, 스케일러 fit은 train만
- 모델 생성 → `fit` → `predict` / `predict_proba`, 주요 하이퍼파라미터
- Keras: 출력층·손실 함수 조합 표, `compile(optimizer="adam")`, `EarlyStopping`, `validation_data`
- 평가: `accuracy_score`, `mean_absolute_error`, `np.sqrt(mse)`
:::

from pathlib import Path

import pandas as pd


데이터_폴더 = Path(__file__).resolve().parent


def 정제(df):
    df = df.copy()
    print("시작", len(df))

    # 점수가 비어 있는 행을 지운다.
    df = df.dropna(subset=["점수"])
    print("빈 칸 제거", len(df))

    # 모든 열이 같은 행은 첫 번째만 남긴다.
    df = df.drop_duplicates()
    print("중복 제거", len(df))

    # 반과 과목 이름의 앞뒤 공백을 지운다.
    df["반"] = df["반"].str.strip()
    df["과목"] = df["과목"].str.strip()

    # 점수가 0점 이상 100점 이하인 행만 남긴다.
    df = df[(df["점수"] >= 0) & (df["점수"] <= 100)]
    print("범위 밖 제거", len(df))
    return df


def 반별평균(df):
    통계 = df.groupby("반")["점수"].agg(["count", "mean", "median", "max"]).round(2)
    print(통계.rename(columns={"count": "개수", "mean": "평균", "median": "중앙값", "max": "최댓값"}))
    return 통계["mean"]


if __name__ == "__main__":
    df = 정제(pd.read_csv(데이터_폴더 / "scores_2026.csv"))
    print("반", sorted(df["반"].unique()))
    print("과목", sorted(df["과목"].unique()))

    # B. 필터링
    수학 = df[df["과목"] == "수학"]
    우수 = df[(df["반"] == "1반") & (df["점수"] >= 90)]
    print("수학 행 수", len(수학))
    print("1반 90점 이상 행 수", len(우수))

    # C. 반별과 과목별 평균
    print("\n반별 평균")
    print(df.groupby("반")["점수"].mean())
    print("\n과목과 반으로 묶은 평균")
    print(df.groupby(["과목", "반"])["점수"].mean())
    print("\n과목과 반으로 묶은 개수")
    print(df.groupby(["과목", "반"])["점수"].count())

    # D. 반별 통계와 검증
    print("\n반별 통계")
    평균 = 반별평균(df)
    print("1반 평균", 평균["1반"])
    print("그룹 합계 / 전체 합계", df.groupby("반")["점수"].sum().sum(), df["점수"].sum())
    print("그룹 개수 / 전체 개수", df.groupby("반")["점수"].count().sum(), len(df))
    수학_1반 = df[(df["반"] == "1반") & (df["과목"] == "수학")]["점수"]
    print("1반 수학 점수", 수학_1반.tolist())
    print("1반 수학 평균", 수학_1반.mean())

    print("\nmini.csv 검산")
    미니 = 정제(pd.read_csv(데이터_폴더 / "mini.csv"))
    print(반별평균(미니))

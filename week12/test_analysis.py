import pandas as pd

from analysis import 데이터_폴더, 반별평균, 정제


본 = 정제(pd.read_csv(데이터_폴더 / "scores_2026.csv"))
미니 = 정제(pd.read_csv(데이터_폴더 / "mini.csv"))


def test_정제하면_100행이_남는다():
    assert len(본) == 100


def test_반은_두_종류만_남는다():
    assert sorted(본["반"].unique()) == ["1반", "2반"]


def test_그룹합이_전체합과_같다():
    assert 본.groupby("반")["점수"].sum().sum() == 본["점수"].sum()


def test_손계산과_일치한다():
    assert 반별평균(미니)["1반"] == 80.0

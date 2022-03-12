"""Baseline model that returns the most common answer for a given length."""

import pandas as pd


train = pd.read_csv("./train.csv", index_col="index")
counts = train.groupby(["length", "answer"]).year.count().rename("count")
count_dict = counts.reset_index(level=1).sort_values(by="count", ascending=False).groupby(
    "length"
).answer.apply(lambda x: list(x)[:50]).to_dict()

test = pd.read_csv("./nyt.csv", index_col="index")
test.loc[:, "answer"] = test.length.apply(
    lambda x: " ".join(count_dict[x])
)
test["answer"].to_csv("sample_output.csv")

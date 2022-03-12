# Clue Retrieval

For the majority of March, we will be working on clue retrieval. That is, given
a `clue`, we want to generate the corresponding `fill` (answer).

To do this, we have several datasets to train and evaluate.

- `nyt.csv` is a test set of clues sampled from only NYT clues from 2021 and 2022
- `train.csv` contains a random set of clues from the clue database (test set excluded)
- `dev.csv` contains a separate set of clues from the clue database (test set excluded)

Your approach will be evaluated based on whether the correct fill appears in
your top-k predictions

## Output format

You should output a CSV file with the following format:
```
index,answer
0,ANANSWER ANSWER2 ANSWER3 ...
1,ANOTHER ANOTHER2 ANOTHER3 ....
...
```
where each row contains a list of answers to the clue with the corresponding
index in `nyt.csv`. You can have _up to_ 50 answers for each clue, ordered by
best to worst. Answers should be separated by a space.

## Some notes about the datasets

1. There may be leakage between the different splits. This is ok because we are
   treating it as an pseudo-info-retrieval task.
2. DO NOT use `nyt.csv` to do any training or model / hyperparameter tuning.
3. There are lots of cultural references in crosswords. Be aware of this (and
   how they might evolve through time) as you construct your solution.

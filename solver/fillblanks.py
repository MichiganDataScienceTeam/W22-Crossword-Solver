"""
Fills in crossword with valid answers.
Does not consider clues.
"""
from argparse import ArgumentParser
from collections import defaultdict
from copy import deepcopy
import puz


def print_grid(puzzle):
    for row in range(puzzle.height):
        cell = row * puzzle.width
        # Substitute p.solution for p.fill to print the answers
        print(" ".join(puzzle.fill[cell : cell + puzzle.width]))


def sort_by_length(wordlist):
    words = defaultdict(list)
    for word in wordlist:
        words[len(word)].append(word)
    return words


def get_constraints(puzzle):
    """Return tuple (unary, binary, clues) of unary and binary constraints.

    clues is a dict mapping clue_id -> {clue, clue_id, across: T/F}
    unary is a dict mapping clue_id -> length
    binary is a dict mapping clue_id -> [(clue_id, index), ...]

    To explain the binary constraints, consider clue with id 7 in 010222.puz:
        Clue with id 7 points to [(0, 2), (1, 2), (2, 2), (3, 2), (4, 0)] in
        the binary constraints dict.

        This means the first character of clue 7 intersects with the 3rd
        character of clue 0, the second char intersects with the 3rd char of
        clue 1, so on until the last char of clue 7 intersects with the first
        char of clue 4.
    """
    clues = dict()
    clue_to_idx = defaultdict(list)
    clue_ind = 0
    unary = dict()
    numbering = puzzle.clue_numbering()

    for clue in numbering.down:
        clues[clue_ind] = {"clue": clue, "clue_ind": clue_ind, "across": False}
        unary[clue_ind] = clue["len"]
        clue_to_idx[clue_ind] = [
            clue["cell"] + i * numbering.width for i in range(clue["len"])
        ]
        clue_ind += 1

    for clue in numbering.across:
        clues[clue_ind] = {"clue": clue, "clue_ind": clue_ind, "across": True}
        unary[clue_ind] = clue["len"]
        clue_to_idx[clue_ind] = [clue["cell"] + i for i in range(clue["len"])]
        clue_ind += 1

    idx_to_clues = defaultdict(list)
    for clue, indices in clue_to_idx.items():
        for str_idx, idx in enumerate(indices):
            idx_to_clues[idx].append((clue, str_idx))

    binary = defaultdict(dict)
    for clue_id in clues:
        for current_idx, idx in enumerate(clue_to_idx[clue_id]):
            candidates = idx_to_clues[idx]
            crossing_clue, crossing_idx = (
                candidates[1] if candidates[0][0] == clue_id else candidates[0]
            )
            binary[clue_id][crossing_clue] = (current_idx, crossing_idx)

    return unary, binary, clues


def main(args):
    puzzle = puz.read(args.puzzle)
    constraints = get_constraints(puzzle)
    words = [
        "BOSS",
        "OTTER",
        "WHALE",
        "LETME",
        "READ",
        "BOWL",
        "OTHER",
        "STATE",
        "SELMA",
        "REED",
        "BREW",
        "ROSE",
        "JOUST",
        "LANE",
        "ODDS",
        "BROAD",
        "ROUND",
        "ESSES",
        "WET",
        "JLO",
        "SALAD",
        "AGITA",
        "GROOM",
        "GENZ",
        "YES",
        "SAGGY",
        "AGREE",
        "LIONS",
        "ATOZ",
        "DAM",
        "BITE",
        "CRUX",
        "CATCH",
        "QUOI",
        "ISNT",
        "BCC",
        "IRAQI",
        "TUTUS",
        "EXCON",
        "HIT",
        "TUSKS",
        "ONTOP",
        "ADORE",
        "SEVEN",
        "TREAT",
        "TOAST",
        "UNDER",
        "STOVE",
        "KOREA",
        "SPENT",
        "SQUID",
        "PURSE",
        "LOGAN",
        "ATEIN",
        "TEDDY",
        "SPLAT",
        "QUOTE",
        "URGED",
        "ISAID",
        "DENNY",
        "HIT",
        "SUNUP",
        "ALGEBRA",
        "GOGREEN",
        "EMITTED",
        "ONION",
        "GAP",
        "HUGGING",
        "INERTIA",
        "TUBETOP",
        "SLOMO",
        "PREEN",
        "AGE",
        "AND",
        "CLUB",
        "HATER",
        "AZURE",
        "TIRED",
        "ONTO",
        "CHAT",
        "LAZIO",
        "UTURN",
        "BERET",
        "REDO",
        "WISEASS",
        "ICEDTEA",
        "PANTLEG",
        "ERE",
        "ESE",
        "RUGRATS",
        "SAYSO",
        "LET",
        "WIPER",
        "ICARUS",
        "SENEGAL",
        "EDT",
        "ATLEAST",
        "SEESTO",
        "SAGES",
        "RYE",
    ]
    wordlist = sort_by_length(words)
    # TODO: fill in the blanks!


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("puzzle")
    main(parser.parse_args())

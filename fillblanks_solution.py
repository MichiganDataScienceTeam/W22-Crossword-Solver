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
        # print(clue)
        clues[clue_ind] = {"clue": clue, "clue_ind": clue_ind, "across": False}
        unary[clue_ind] = clue["len"]
        clue_to_idx[clue_ind] = [
            clue["cell"] + i * numbering.width for i in range(clue["len"])
        ]
        clue_ind += 1

    for clue in numbering.across:
        # print(clue)
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


def check(solution, binary):
    for clue in solution:
        if len(solution[clue]) > 0:
            for crossing in binary[clue]:
                crossing_fill = solution[crossing]
                if len(crossing_fill) == 0:
                    continue
                x_ind, y_ind = binary[clue][crossing]
                if solution[clue][x_ind] != crossing_fill[y_ind]:
                    return False
            # for i, char in enumerate(solution[clue]):
            #     fill_id, fill_index = binary[clue][i]
            #     crossing_fill = solution[fill_id]
            #     if len(crossing_fill) == 0:
            #         continue
            #     if char != crossing_fill[fill_index]:
            #         return False
    return True


def ac3(constraints, wordlist):
    def satisfies(dx, dy, x, y):
        x_ind, y_ind = binary[x][y]
        return dx[x_ind] == dy[y_ind]

    def arc_reduce(x, y):
        change = False
        for dx in domain[x].copy():
            satisfied = False
            for dy in domain[y]:
                if satisfies(dx, dy, x, y):
                    satisfied = True
            if not satisfied:
                domain[x].remove(dx)
                change = True
        return change

    unary, binary, clues = constraints
    domain = dict()
    for x in clues:
        domain[x] = set(wordlist[unary[x]])
    worklist = [(x, y) for x in binary for y in binary[x] if y < x]
    while len(worklist) > 0:
        x, y = worklist.pop()
        if arc_reduce(x, y):
            if len(domain[x]) == 0:
                return False
            worklist += [(x, z) for x in binary for z in binary[x] if z != y]
    return domain


def solve(solution, constraints, wordlist):
    unary, binary, clues = constraints
    for i in unary:
        if len(solution[i]) != 0:
            continue
        length = unary[i]
        candidates = wordlist[length]
        for candidate in candidates:
            solution[i] = candidate
            if check(solution, binary):
                if solve(deepcopy(solution), constraints, wordlist):
                    return True
        solution[i] = ""
        return False
    return True


def main(args):
    puzzle = puz.read(args.puzzle)
    
    constraints = get_constraints(puzzle)
    print(constraints[1])
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
    # print(wordlist)
    # solution = {k: "" for k in constraints[0]}
    # solve(solution, constraints, wordlist)

    print(ac3(constraints, wordlist))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("puzzle")
    main(parser.parse_args())

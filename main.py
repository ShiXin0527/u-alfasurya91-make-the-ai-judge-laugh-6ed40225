#!/usr/bin/env python3
"""make.fun bounty entry: Make the AI Judge Laugh.

One joke, one courtroom, one AI judge. The defense rests its case
on a single line — and the judge cannot keep a straight face.
"""

RULING = (
    "I told the AI judge a joke so dry it objected to itself — "
    "the judge laughed, overruled the objection, and dismissed the case. "
    "Court adjourned for giggles."
)


def rule():
    """Return the judge's one-line ruling."""
    return RULING


def main():
    print(rule())


if __name__ == "__main__":
    main()

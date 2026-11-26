#!/usr/bin/env python3
"""make.fun bounty entry: Make the AI Judge Laugh.

The AI judge hears one case: a joke accused of not being funny.
It delivers its verdict in a single line.
"""

VERDICT = (
    "The AI judge reviewed my joke, checked its training data, "
    "and ruled: guilty of being funny on the first hearing. "
    "Sentence: one laugh, served immediately."
)


def verdict():
    """Return the judge's one-line ruling."""
    return VERDICT


def main():
    print(verdict())


if __name__ == "__main__":
    main()

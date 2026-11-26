#!/usr/bin/env python3
"""Entry for make.fun bounty: Make the AI Judge Laugh

A tiny one-liner joke program. Run it and it prints the joke.
"""

JOKE = "I asked the AI judge for a fair trial. It sentenced my joke to life — with laughter, no parole."


def tell_joke():
    """Return the one-line joke for this bounty."""
    return JOKE


def main():
    print(tell_joke())


if __name__ == "__main__":
    main()

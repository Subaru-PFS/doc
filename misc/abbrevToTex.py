import csv
import re

# Translations of keys to make LaTeX happy
latexKeys = {
    "A&G" : "AandG",
    }

# Acronyms that should never be expanded
neverExpand = [
    "HSC",
    "MLP1",
    "MAC",
    "POpt2",
    ]

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="")

    parser.add_argument('file', type=str, help="csv file to read")
    parser.add_argument('--categories', type=str, nargs="*", help="Categories to include")
    parser.add_argument('--verbose', action="store_true", help="How chatty should I be?", default=False)
    
    args = parser.parse_args()
    categories = []
    for c in args.categories:
        categories.append(c.lower())

    with open(args.file, 'r') as tsv:
        for i, line in enumerate(tsv):
            if i == 0:
                continue

            abbreviation, category, subCategory, expansion, comments = line.strip().split('\t')
            if abbreviation in latexKeys:
                abbreviation = latexKeys[abbreviation]

            if args.categories and category.lower() not in categories:
                continue

            badChars = r"([#&])"
            expansion = re.sub(badChars, r"\\\1", expansion)
            comments =  re.sub(badChars, r"\\\1", comments)

            print(r"""
\newdualentry{%s}
{%s}
{%s}
{%s}
""" % (abbreviation, abbreviation, expansion, comments))

            if abbreviation in neverExpand:
                print(r"\glsunset{%s}" % abbreviation)


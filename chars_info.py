import sys
import unicodedata

# input_data = "нумсăӈ ёх"
try:
    input_data = sys.argv[1]
except IndexError:
    print("Error: put a string system argument after the script name")
    exit()

# data

categories = {
    "Lu": "Letter, uppercase",
    "Ll": "Letter, lowercase",
    "Lt": "Letter, titlecase",
    "Lm": "Letter, modifier",
    "Lo": "Letter, other",

    "Mn": "Mark, nonspacing",
    "Mc": "Mark, spacing combining",
    "Me": "Mark, enclosing",

    "Nd": "Number, decimal digit",
    "Nl": "Number, letter",
    "No": "Number, other",

    "Pc": "Punctuation, connector",
    "Pd": "Punctuation, dash",
    "Ps": "Punctuation, open",
    "Pe": "Punctuation, close",
    "Pi": "Punctuation, initial quote",
    "Pf": "Punctuation, final quote",
    "Po": "Punctuation, other",

    "Sm": "Symbol, math",
    "Sc": "Symbol, currency",
    "Sk": "Symbol, modifier",
    "So": "Symbol, other",
    
    "Zs": "Separator, space",
    "Zl": "Separator, line",
    "Zp": "Separator, paragraph",

    "Cc": "Other, control",
    "Cf": "Other, format",
    "Cs": "Other, surrogate",
    "Co": "Other, private use",
    "Cn": "Other, not assigned",
}

for i in input_data:
    print(i + "\t" + hex(ord(i)) + "\t" + unicodedata.bidirectional('\u0660') + "\t" + unicodedata.name(i)
    + "\t" + unicodedata.category(i) + " (" + categories[unicodedata.category(i)] + ")")
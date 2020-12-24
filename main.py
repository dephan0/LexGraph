import sys
from pathlib import Path
import argparse
from matplotlib import pyplot as plt
import re

pl_alph = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
en_alph = "abcdefghijklmnopqrstuvwxyz"
alphs = {
        "pl": pl_alph,
        "en": en_alph
    }

# Function used for checking if the filepath is correct
def filterFilePath(string_path):
    if( not Path(string_path).is_file() ):
        raise argparse.ArgumentTypeError("Ścieżka nie prowadzi do pliku")
    elif( not bool(re.match(r".+\.txt", string_path)) ):
            raise argparse.ArgumentTypeError("Plik \"{0}\" ma nieprawidłowe rozszerzenie (powinno być .txt)".format(string_path))
    return string_path

# ARGUMENT PARSER
parser = argparse.ArgumentParser(description="Stwórz wykres ilośći wystąpień liter/słów w tekście :)", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("mode",
                    choices=['w', 'l', 'fl'],
                    help="Tryb pracy programu:\n    w - zliczenie wszystkich słów (prawo Zipfa)\n    l - zliczenie wszystkich liter\n    fl - zliczenie pierwszych liter",
                    )

parser.add_argument("lang",
                    choices=['pl', 'en'],
                    help="Język alfabetu, z którego zliczane będą litery w tekście:\n    pl - język polski\n    en - język angielski")
parser.add_argument("path",
                    type=filterFilePath,
                    help="Ścieżka do pliku tekstowego (jeśli plik jest w tym samym folderze co program, to można podać tylko jego nazwę np.'pan_tadeusz.txt')")

parser.add_argument("-s", "--sort",
                    default=False,
                    action="store_true",
                    help="Posortuj dane (według ilości wystąpień litery lub słowa od lewej do prawej)")
parser.add_argument("-lim", "--limit",
                    default=40,
                    type=int,
                    help="Ustaw limit ilości słów na osi X")


args = parser.parse_args()

# Returns a dicitionary (named "data") with letters and their occurences in text
def allLetters(lang, string_path):
    # Dictionary, where each letter is a key and a corresponding value is the number of its occurences in the text
    # (dictionary is the fastest choice in python, as it uses hash tables to store and look up data)
    data = {char: 0 for char in alphs[lang]}

    with open(string_path, 'r') as file:
        for line in file:
            for char in line.lower():
                try:
                    data[char] += 1
                except:
                    continue

    #set appropriate plot labels
    plt.title("Częstotliwość wszystkich liter w {}".format(Path(string_path).name))
    plt.ylabel("Ilość wystąpień")
    plt.xlabel("Litery w wybranym alfabecie ({0})".format(lang))

    return data

# Returns a dicitionary (named "data") with letters and their occurences in text
def firstLetters(lang, string_path):
    data = {char: 0 for char in alphs[lang]}

    with open(string_path, 'r') as file:
        for line in file:
            for word in re.findall(r"\w+", line.lower()):
                try:
                    data[word[0]] += 1
                except:
                    continue
    #set appropriate plot labels
    plt.title("Częstotliwość pierwszych liter słów w {}".format(Path(string_path).name))
    plt.ylabel("Ilość wystąpień")
    plt.xlabel("Litery w wybranym alfabecie ({0})".format(lang))
    return data


def words(string_path):
    data = {}
    count = 0
    with open(string_path, 'r') as file:
        for line in file:
            for word in re.findall(r"\w+", line.lower()):
                try:
                    data[word] += 1
                    count += 1
                except:
                    # \w matches numbers so I have to account for that
                    if word.isalpha():
                        data[word] = 1
                        count +=1
    # set appropriate plot labels
    plt.title("Częstotliwość słów w {}".format(Path(string_path).name))
    plt.ylabel("Ilość wystąpień")
    plt.xlabel("Ranga słowa")
    # PLT.SCATTER i PLT.ANNOTATE żeby te takie małe punkty z podpisami były
    #https://stackoverflow.com/questions/14432557/matplotlib-scatter-plot-with-different-text-at-each-data-point

    return data

def graph(x, y, mode, limit):
    if(mode == "w"):
        ranks = [i for i in range(1, limit + 1)]
        plt.scatter(ranks, y[:limit])
        if(limit < 100):
            for i,word in enumerate(x[:limit]):
                plt.annotate(word, (ranks[i], y[i]))
    else:
        plt.bar(x, y)

    plt.show()

def main(args):
    mode = args.mode
    lang = args.lang
    string_path = args.path
    sort = args.sort
    limit = args.limit if mode == 'w' else len(alphs[lang])

    modes_functions = {
        'w': lambda: words(string_path),
        'l': lambda: allLetters(lang, string_path),
        'fl': lambda: firstLetters(lang, string_path)
    }
    # Get data from one of these three functions
    data = modes_functions[mode]()

    keys = data.keys()
    values = data.values()

    sorted_keys = sorted(keys, key=lambda elem: data[elem], reverse=True)
    sorted_values = sorted(values, reverse=True)

    if (sort):
        graph(list(sorted_keys), list(sorted_values), mode, limit)
    else:
        graph(keys, values, mode, limit)


if( __name__ == "__main__"):
    main(args)
    sys.exit(0)
from collections import Counter


def count_letter(str):
    dictionary = {}
    for key1, value in Counter(str).items():
        if key1.isalpha():
            dictionary[key1] = value

    print(sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[0][0])


count_letter("Python is an interpreted high-level programing language for general-purpose programing."
             "Python features a dynamic type system and automatic memory management."
             "Python interpreters are available for many operating systems.")
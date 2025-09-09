#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dictionary = {
        "I": 1,
        "II": 2,
        "III": 3,
        "IV": 4,
        "V": 5,
        "VI": 6,
        "VII": 7,
        "VIII": 8,
        "IX": 9,
        "X": 10,
        "XI": 11,
        "XII": 12,
        "XIII": 13,
        "XIV": 14,
        "XV": 15,
        "XVI": 16,
        "XVII": 17,
        "XVIII": 18,
        "XIX": 19,
        "XX": 20,
        "XXI": 21,
        "L": 50,
        "LXXXVII": 87,
        "LXXXIX": 89,
        "XCIX": 99,
        "C": 100,
        "CXXIV": 124,
        "D": 500,
        "DCCVII": 707,
        "M": 1000,
        "": 0
    }

    for key in roman_dictionary:
        if roman_string == key:
            return roman_dictionary[key]

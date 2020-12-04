# Copyright (c) 2020 DanTGL
# This code is licensed under The MIT License (see LICENSE for details)

import string

required_fields = { "byr": lambda x: (1920 <= int(x) <= 2002) == True,
                    "iyr": lambda x: (2010 <= int(x) <= 2020) == True,
                    "eyr": lambda x: (2020 <= int(x) <= 2030) == True,
                    "hgt": lambda x: (150 <= int(x[0:-2]) <= 193 if x[-2:] == "cm" else 59 <= int(x[0:-2]) <= 76) == True,
                    "hcl": lambda x: (x[0] == "#" and all(c in string.hexdigits for c in x[1:])) == True,
                    "ecl": lambda x: (x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}) == True,
                    "pid": lambda x: (len(x) == 9 and all(c in string.digits for c in x)) == True
                    }

inputs = list(passport.split() for passport in open("day4/input").read().split("\n\n"))


def result():
    total_valid = 0

    for passport in inputs:
        fields = {key: value for key, value in (field.split(":") for field in passport)}

        valid = True
        for required_field in required_fields.keys():
            try:
                if not (required_field in fields.keys() and required_fields[required_field](fields[required_field])):
                
                    valid = False
                    break
            except ValueError:
                valid = False
                break

        if valid:
            total_valid += 1

    return total_valid

        

print(result())
# Copyright (c) 2020 DanTGL
# This code is licensed under The MIT License (see LICENSE for details)

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

inputs = list(passport.split() for passport in open("day4/input").read().split("\n\n"))



def result():
    total_valid = 0

    for passport in inputs:
        fields = list(field.split(":")[0] for field in passport)

        valid = True
        for required_field in required_fields:

            if required_field not in fields:
                valid = False
                break
        if valid:
            total_valid += 1

    return total_valid

        

print(result())
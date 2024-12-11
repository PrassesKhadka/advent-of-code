from operator import mul
import os
import re

with open(os.path.join('input.txt')) as f:
    input=f.read().strip()

"""
Regex in Python -> 
?: -> non-capturing group 
() -> capturing group 
\( -> match literal '(' and denote it not being a part of regex sequence
\d -> matches a digit
\d+ -> matches one or more digit
+ -> one or more 
* -> null or more
? -> null or one
| -> OR
to get capturing groups -> .group()
re.findall(pattern,input)-> [(gr1,gr2,gr3,gr4), ...]
"""

def part2():
    pattern=r"(?:mul\((\d+),(\d+)\)|(don't\(\))|(do\(\)))"
    matches=re.findall(pattern,input)
    do=1
    sum=0
    for group in matches:
        # if do()
        if group[3]:
            do=1
        # if don't()
        if group[2]:
            do=0

        if not do or group[2] or group[3]:
            continue

        sum+=mul(int(group[0]),int(group[1]))
    return sum

def part1():
    pattern=r"(?:mul\((\d+),(\d+)\))"
    match=re.findall(pattern,input)
    sum=0

    for group in match:
        sum+=mul(int(group[0]),int(group[1]))
    
    return sum



if __name__ == "__main__":
    print(f"Output of part1: {part1()}")
    print(f"Output of part2: {part2()}")

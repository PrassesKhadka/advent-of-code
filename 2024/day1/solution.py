import os

col1=[]
col2=[]

def get_input(str:str):
    val1,val2=str.split()
    col1.append(int(val1))
    col2.append(int(val2))

with open(os.path.join('input.txt')) as f:
    value=list(map(get_input,f.readlines()))

def part1():
    output = sum([abs(val1 - val2) for val1, val2 in zip(sorted(col1), sorted(col2))])
    print(f"The final output is {output}")

def part2():
    output=sum([i * sum(1 for j in col2 if i == j) for i in col1])
    print(f"The similarity score is {output}")

if __name__ == "__main__":
    part1()
    part2()
import os

col1=[]
col2=[]

def get_input(str):
    val1,val2=str.split()
    col1.append(int(val1))
    col2.append(int(val2))

with open(os.path.join('input.txt')) as f:
    value=list(map(get_input,f.readlines()))

col1.sort()
col2.sort()

output=sum([val1-val2 if val1>val2  else val2-val1 for val1,val2 in zip(col1,col2)])
print(f"The final output is {output}")
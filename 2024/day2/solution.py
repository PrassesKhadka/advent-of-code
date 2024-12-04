import sys
import os

args=sys.argv

with open(os.path.join("input.txt")) as f:
    input=list(map(lambda x:list(map(int,x.split())),f.readlines()))

safe=[]
unsafe=[]

def check(arr):
    last=arr[0]
    flag = "inc" if arr[1]>arr[0] else "dec"
    diff=arr[1]-arr[0] if flag=="inc" else arr[0]-arr[1]
    
    if(diff==0 or diff>3): return False

    for index,num in enumerate(arr):
        if(index==0):continue

        if((flag=="inc" and num-last>0 and num-last<=3) or (flag=="dec" and last-num>0 and last-num<=3)):
            last=num
            continue
        else:
            return False
    return True

def filter(arr):
    if(check(arr)):
        safe.append(arr)
    else:
        unsafe.append(arr)

for i in input:
    filter(i)

print(f"{len(safe)} reports are safe.")

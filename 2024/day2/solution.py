import os

with open(os.path.join("input.txt")) as f:
    input=list(map(lambda x:list(map(int,x.split())),f.readlines()))

def check(arr):
    last=arr[0]
    inc = arr[1]>arr[0]

    for index,num in enumerate(arr):
        if index==0: continue
        if((inc and num-last>0 and num-last<=3) or (not inc and last-num>0 and last-num<=3)):
            last=num
            continue
        else:
            return index,False
    return -1,True

def part1():
    safe=[]
    unsafe=[]

    for arr in input:   
        _,isSafe=check(arr)
        (safe if isSafe else unsafe).append(arr)

    print(f"{len(safe)} reports are safe.")

def part2():
    safe=[]
    unsafe=[]

    for arr in input:
        index,isSafe=check(arr)

        if not isSafe: 
            arr.pop(index)
            _,isSafe=check(arr) 
        
        (safe if isSafe else unsafe).append(arr)
    
    print(f"{len(safe)} reports are safe.")

if __name__=="__main__":
    part2()

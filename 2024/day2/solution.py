import os

with open(os.path.join("input.txt")) as f:
    input=list(map(lambda x:list(map(int,x.split())),f.readlines()))

def check(arr):
    if len(arr) < 2:
        return True  

    last=arr[0]
    inc = arr[1]>arr[0]

    for index,num in enumerate(arr):
        if index==0: continue
        diff=num-last if inc else last-num

        if diff<1 or diff>3:
            return False

        last=num
    return True

def part1():
    safe=[]
    unsafe=[]

    for arr in input:   
        isSafe=check(arr)
        (safe if isSafe else unsafe).append(arr)

    print(f"{len(safe)} reports are safe.")

def check_by_remove_one_element(arr):
    for i in range(len(arr)):
        modified_arr=arr[:i]+arr[i+1:]
        is_safe=check(modified_arr)
        if is_safe:
            break
    
    if is_safe:
        return True
    else:
        return False

def part2():
    safe=[]
    unsafe=[]

    for arr in input:
        is_safe=check(arr)
        
        if not is_safe: 
            is_safe=check_by_remove_one_element(arr)
            
        (safe if is_safe else unsafe).append(arr)
    
    print(f"{len(safe)} reports are safe.")

if __name__=="__main__":
    part1()
    part2()

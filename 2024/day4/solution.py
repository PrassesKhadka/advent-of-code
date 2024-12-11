import os

with open(os.path.join('input.txt')) as f:
    input=[txt.strip() for txt in f.readlines()]
    
# [[(-1,-1),(-1,0),(-1,1)]]
# [[(0,-1),(0,0),(0,1)]]
# [[(1,-1),(1,0),(1,1)]]

# To find -> XMAS
def part1():
    count=0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if not input[i][j]=="X": continue
            # moving through all 8 direction 1 step
            for ii in [-1,0,1]:
                for jj in [-1,0,1]:
                    # in the original position i.e. middle then continue
                    if ii==0 and jj==0: continue
                    # index does not exist error if 3 step in all direction -> MAS -> so 3 (i.e index outside the matrix)
                    if not (0<=i+3*ii<len(input) and 0<=j+3*jj<len(input[i])): continue
                    if input[i+ii][j+jj]=="M" and input[i+2*ii][j+2*jj]=="A" and input[i+3*ii][j+3*jj]=="S":
                        count+=1
    return count

# To find -> two MAS in the shape of an X
# M.S
# .A.
# M.S
def part2():
    count=0
    # eliminate all edges
    for i in range(1,len(input)-1):
        for j in range(1,len(input[i])-1):
            if not input[i][j]=="A": continue

            diag1=input[i+1][j+1]+input[i-1][j-1]
            diag2=input[i-1][j+1]+input[i+1][j-1]

            flag =['MS','SM']
            if diag1 in flag and diag2 in flag:
                count+=1    

    return count

print(f"The result of part 1 is:{part1()}")                
print(f"The result of part 2 is:{part2()}")                






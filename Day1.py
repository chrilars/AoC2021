# Part 1 done elsewhere

f = open("day1input.txt", "r")
input = f.read().split("\n")
sum = 0

for i in range(3,len(input)-1):
    x = int(input[i-3]) + int(input[i-2]) + int(input[i-1])
    y = int(input[i-2]) + int(input[i-1]) + int(input[i])
    if(x < y):
        sum += 1

print(sum)

num = int(input("Enter the integer (0 to 100): "))
sum = 0

idx = 1
while idx <= num:
    sum += idx
    idx += 1

print(sum)
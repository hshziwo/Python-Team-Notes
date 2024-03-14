n = input()

value = int(n[0])
for i in range(1, len(n)) :
    if value * int(n[i]) > value + int(n[i]) :
        value *= int(n[i])
    else :
        value += + int(n[i])

print(value)
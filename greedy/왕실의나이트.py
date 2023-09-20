condition = input()
row = int(condition[1])
column = condition[0]

count = 0
for i in range(1,9) :
    for j in range(97,105) :
        if j + 2 == ord(column) or j - 2 == ord(column):
            if i + 1 == row or i - 1 == row :
                count += 1

        if j + 1 == ord(column) or j - 1 == ord(column):
            if i + 2 == row or i - 2 == row :
                count += 1
print(count)
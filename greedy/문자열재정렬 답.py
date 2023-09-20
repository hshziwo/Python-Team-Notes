data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else :
        value += int(x)

result.sort()

# 숫자값이 하나라도 있으면 0이 아니므로
if value != 0 :
    result.append(str(value))

print(''.join(result))
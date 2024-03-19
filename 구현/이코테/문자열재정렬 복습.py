import sys

input = lambda: sys.stdin.readline().rstrip()
text = input()

string_array = []
low_count = ord("A")
high_count = ord("Z")

number = 0
for string in text:
    # 알파벳인 경우 따지는 방법
    # if string.isalpha():
    if low_count <= ord(string) <= high_count:
        string_array.append(string)
    else:
        number += int(string)

string_array.sort()
if number == 0:
    number = ""
else:
    number = str(number)

result = "".join(string_array) + number
print(result)

# a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# # a.sort(reverse=True)
# # a = list(map(int, a))
# # a.sort()
# a.sort(reverse=True)
# print(a)

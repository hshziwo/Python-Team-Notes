key_value = {'L': -1, 'R': 1, 'U': -1, 'D': 1}

n = int(input())
plan = input().split()

ud = 1
lr = 1
for i in plan :
  if i == 'L' or i == 'R' :
    tmp = lr
  else :
    tmp = ud

  tmp = tmp + key_value[i]
  if tmp < 1 or tmp > n:
    pass
  else :
    if i == 'L' or i == 'R' :
      lr = tmp
    else :
      ud = tmp

print(ud, lr)
txt = input()
red_val = 0
for i in range(len(txt)) :
  a = int(txt[i])
  
  if i == 0 :
    red_val += a
    continue

  if red_val == 0 or a == 0 :
    red_val += a
  else :
    red_val *= a
print(red_val)
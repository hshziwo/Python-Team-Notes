txt = input()
result = int(txt[0])

for i in range(1,len(txt)) :
  a = int(txt[i])

  # 0뿐만 아니라 1도 곱하기보다는 더하기가 큼
  if result <= 1 or a <= 1 :
    result += a
  else :
    result *= a
    
print(result)
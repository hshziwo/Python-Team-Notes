txt = input()

txt_list = []
count_sum = 0
for i in txt :
    try :
        tmp = int(i)
        count_sum += tmp
    except:
        txt_list.append(i)

txt_list.sort()

print(''.join(txt_list) +str(count_sum))
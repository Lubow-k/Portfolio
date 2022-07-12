s = input()
p_1 = 0
p_2 = 0
p_3 = 0
d = [0]
f = 0
for c in s:   
    if c not in '(){}[]':
        continue       
    elif c == '(':
        p_1 += 1
        d.append(1)
    elif c == '[':
        p_2 += 1
        d.append(2)
    elif c == '{':
        p_3 += 1
        d.append(3)       
    elif c == ')' and d[-1] == 1:
        p_1 -= 1
        d = d[:-1]
    elif c == ']' and d[-1] == 2:
        p_2 -= 1
        d = d[:-1]
    elif c == '}' and d[-1] == 3:
        p_3 -= 1
        d = d[:-1]
    else:
        print('WRONG')  
        f = 1
        break
if f == 0:
    if p_1 == p_2 == p_3 == 0 and d == [0]:
        print('CORRECT')      
    else:
        print('WRONG')
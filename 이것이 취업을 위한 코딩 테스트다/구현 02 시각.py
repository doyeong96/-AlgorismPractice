n = int(input())
h = 0
m = 0
s = 0
cnt = 0
while 1:
    s += 1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h > n:
                break
    if '3' in str(s)+str(m)+str(h):
        cnt += 1
print(cnt)
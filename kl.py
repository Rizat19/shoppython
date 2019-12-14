from pyzt import inputs,inputi
while True:
    l=[]
    san=inputs('engiz:')
    hex_set = set('0xABCDEF123456789')
    engiz_set = set(san)
    if len(engiz_set - hex_set) == 0 and san != '':
        for i in san:
            l.append(i)
        l.remove(l[0])
        l.remove(l[0])
        print(l)
        for i in range(len(l)):
            if l[i]=='A':
                l[i]=10
            if l[i]=='B':
                l[i]=11
            if l[i]=='C':
                l[i]=12
            if l[i]=='D':
                l[i]=13
            if l[i]=='E':
                l[i]=14
            if l[i]=='F':
                l[i]=15
        for i in range(len(l)):
            l[i]=int(l[i])
        print(l)
        sum=0
        for i in range(len(l)):
            sum+=l[len(l)-i-1]*16**i
        print(sum)
        break
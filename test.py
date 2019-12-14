import pyzt
while True:
    print('1- 10>>2\n2- 2>>10\n3- 2>>8\n4- 8>>10\n5- 10>>8\n0- stop')
    tandau=pyzt.inputi('tandanyz:')
    if tandau==1:
        num=pyzt.inputi('Ондық сан:')
        l1=[]
        while True:
            c=num%2
            l1.append(c)
            b=num//2
            num=b
            if b==0:
                break
        print(num,'10-дық жүйеден 2-лік жүйеге:')
        for i in range(1,len(l1)+1):
            s=l1[-i]
            print(s,end='')
        print('\n')
    if tandau==2:
        byn_set=set('10')
        l2=[]
        a=1
        sum=0
        while True:
            san_2=input('Екілік сан:')
            san_set2=set(san_2)
            if len(san_set2-byn_set)==0 and san_2!='':
                for i in san_2:
                    l2.append(int(i))
                a1=len(l2)

                for it in l2:
                    sd=it*(2**(a1-a))
                    a1-=1
                    if a==-1:
                        break
                    sum+=sd
                print(san_2,'2-лік жүйеден 10-дық жүйеге:',sum,'\n')
                break
            else:
                print('Kaita engiz')
    if tandau==3:
        while True:
            san_set8 = set('01')
            inp = input('\n' + "2- лік жүйедегі сан енгіз:")
            inp_set = set(inp)
            l2 = []
            l88 = []
            if len(inp_set - san_set8) == 0 and inp != '':
                a = 1
                sum = 0
                for i in inp:
                    l2.append(int(i))
                a1 = len(l2)
                sum = 0
                for it in l2:
                    sd = it * (2 ** (a1 - a))
                    sum += sd
                    a1 -= 1
                    if a == -1:
                        break
                if sum == 0 or sum == 1 or sum == 2 or sum == 3 or sum == 4 or sum == 5 or sum == 6 or sum == 7:
                    print('2>>8', sum)
                else:
                    while True:
                        bytin = sum // 8
                        if sum < 8:
                            l88.append(sum)
                            print('2>>8: ')
                            for elem in range(len(l88)):
                                print(l88[-elem - 1], end='')
                            break
                        kaldyk = sum % 8
                        sum = bytin
                        l88.append(kaldyk)
                    break
            else:
                print('Kaita engiz')
    if tandau==4:
        san_set82 = set('01234567')
        while True:
            engiz = input(' сан енгіз:')
            engiz_set = set(engiz)
            if len(engiz_set - san_set82) == 0 and engiz != '':
                sum = 0
                for i in range(len(engiz)):
                    en = int(engiz[i])
                    res = en * (8 ** (len(engiz) - i - 1))
                    sum += res
                print(engiz,"8>>10: ", sum)
                break
            else:
                print('Kaita engiz!')
    if tandau==5:
        san_set5=set('0123456789')
        l8=[]
        while True:
            engiz5=input('10-дық жүйедегі сан енгіз:')
            engiz_set5=set(engiz5)
            if len(engiz_set5-san_set5)==0 and engiz5!='':
                en=int(engiz5)
                if en == 0 or en == 1 or en == 2 or en == 3 or en == 4 or en == 5 or en == 6 or en == 7:
                    print('10>>8: ', en)
                    break
                else:
                    while True:
                        butin=en//8
                        if en <= 7:
                            l8.append(en)
                            print('10>>8: ')
                            for i in range(len(l8)):
                                print(l8[-i-1],end='')
                            break
                        mod=en%8
                        en=butin
                        l8.append(mod)
                    break
            else:
                print('Kaita engiz!')
    if tandau==0:
        break




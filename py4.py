#
# import pyzt
# a=pyzt.inputs('plz input your name:')
# print(a.encode(encoding='utf-8'))

# a='ризат'
# a_e=a.encode(encoding='utf-8')
# print((a_e))

# with open('ri', 'r') as f:
#     line = f.read()
#     print(bytes(line, 'latin-1').decode('big5'))
#
# with open('ri', 'rb') as f:
#     line = f.read()
#     print(line.decode('big5'))

# s = "RZIAY"
# a=s.encode()
# print(a)
# a1=s.encode().decode("unicode-escape")
# print(a1.encode('latin1').decode())

#
# with open('stu','r') as d:
#     d1=d.read()
#     d2=d1.encode(encoding='utf-8')
#     print('encode: ',d2,end='')



# with open('ri','rb') as f:
#     q=f.read()
#     a=q.decode('unicode_escape').encode('latin1').decode()
#     sp=a.split("'")
#     print('\ndecode:',sp[1],end='')

with open('clients.txt', 'r') as client_vip:
    a = client_vip.read()
    print(a)
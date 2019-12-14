# import sys
# import re
# from pyzt import inputs
# surak=inputs("jureik:")
# #if surak=='yes' or surak=='y':
# if surak not in ['yes','Yes','Y','y']:
# #if re.search('yes',surak.lower()):
# # if re.search('yes',surak,re.IGNORECASE):
#     print('fuc',end='♥')
#     sys.exit('re')
# elif surak=='no' or surak=='n':
#     print(end='😭')
# else:
#     print(end='fuc#')
#
# import os
# # a=os.system('ls  -a')
# # print(a)
# # import subprocess
# # x=subprocess.check_output(['ls','-a'])
# # print(x)
# names=['Dar','Nur','Bek']
# def change():
#     names[0]='Dia'
#     print('ins:',names)
# change()
# print(names)

# sorak=input('jureik:')
# if sorak in ['yes','YES','y','Yes']:
#     print('hurrraaaa',end='❤')
# elif sorak=='no' or sorak=='n':
#     print('😢')
# else:
#     print('fuc#')

# import re
# #regular expression
# if re.search('yes',sorak.lower()):
#     print('wuuuuuu')

product_list=[
    ('Iphone 11 pro max',700000),
    ('Nike',15000),
    ('Azat coffe',750),
    ('Watch',150000),
    ('Surface',399000),
]
from pyzt import inputs,inputi

for index, item in enumerate(product_list):
    print(index, item)
# prod_index = inputi('Which product do you want to change : ')
# prod_item = product_list[prod_index]
new=[]
for i in product_list:
    new.append(list(i))

product_list1=[]

while True:
    prod_index = inputi('Which product do you want to change : ')
    if prod_index < len(product_list) and prod_index >= 0:
        prod_item = new[prod_index]
        change_price=inputi('Product price:')
        prod_item[1]=change_price
        surak = inputs("Want to change more? 'ok'- to continue , 'q'-for exists:")
        if surak == 'q':
            break
        else:
            pass
    else:
        print(f"Product {prod_index} does not exist! Dudo ")
for i in new:
    product_list1.append(tuple(i))
print(product_list1)







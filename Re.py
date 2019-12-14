from pyzt import inputi,inputs,inputf
#1
#names=("Azat",'Meru','Azat','Zhan','Dias')
# print(names.count('Azat'))
# print(names.index('Dias'))
# try:
#     print(names.index('Ri'))
# except:
#     pass
# finally:
#     print('ok')

#2
# l1=['tamak','taulet','taz','sabak']
# for each in enumerate(l1):
#     print(each)

product_list=[
    ('Iphone 11 pro max',700000),
    ('Nike',15000),
    ('Azat coffe',750),
    ('Watch',150000),
    ('Surface',399000),
]
shopping_list=[]
salary=inputi("Input your salary: ")
print(salary)
print(enumerate(product_list))
while True:
    for index,item in enumerate(product_list):
        print(index,item)
    choice=inputs("Input 'ok' to continue, 'q' for exist: ")
    if choice=='ok':
        user_choice = inputi('Which product do you want to buy: ')
        if user_choice<len(product_list) and user_choice>=0:
            p_item=product_list[user_choice]
            if p_item[1]<=salary:
                shopping_list.append(p_item)
                salary-=p_item[1]
                print(f"Added {p_item} into shopping cart, your current balance is {salary}")
            else:
                print(f"Sorry, only {salary} left on your credit. You can't buy")
        else:
            print(f"Product {user_choice} does not exist! Dudo ")
    elif choice=='q':
        print("-----------shopping list---------------")
        for p in shopping_list:
            print(p)
        print("Your current balance ",salary)
        exit()












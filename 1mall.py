from pyzt import inputi,inputs
# product_list=[
#     ('Iphone 11 pro max',700000),
#     ('Nike',15000),
#     ('Azat coffe',750),
#     ('Watch',150000),
#     ('Surface',399000),
# ]
import subprocess
def staff():
    product_list=[]
    global product_list
    while True:
        print('1-списокке жаңа тауар қосу, 2-бағаларын өзгерту,3-барлық тауарлaрды көру,0-шығу:')
        tandau = inputi('Таңдаңыз'.center(40,'-'))
        if tandau == 1:
            while True:
                product = inputs('Қандай продукты енгізгіңіз келеді? Атын енгізіңіз:')
                price = inputi('Продуктының бағасы:')
                product_list.append((product, price))
                with open('1mall.txt', 'w+') as fil:
                    for i, item in enumerate(product_list):
                        fil.write(str(i) + '\t' + str(item) + '\n')
                surak = inputs("Тізімге жаңа продукт енгізесіз бе? ok -жалғастыру үшін, q -тоқтату үшін :")
                if surak == 'q':
                    break
                elif surak == 'ok':
                    pass
                else:
                    print('Kaita engiz!')
        elif tandau == 2:
            product_list1 = []
            new = []
            for i in product_list:
                new.append(list(i))
            while True:
                surak = inputs("Өзгерту үшін-ok , тоқтау үшін -q: :")
                if surak == 'ok':
                    prod_index = inputi('Қай продуктыны өзгерткіңіз келeді?: ')
                    if prod_index < len(product_list) and prod_index >= 0:
                        prod_item = new[prod_index]
                        print(prod_item[0], end=' ')
                        change_price = inputi('Продуктың жаңа бағасы:')
                        prod_item[1] = change_price
                        for i in new:
                            product_list1.append(tuple(i))
                        product_list = product_list1
                        with open('1mall.txt','w+') as f:
                            for i, item in enumerate(product_list):
                                f.write(str(i) + '\t' + str(item) + '\n')
                    else:
                        print(f" {prod_index} -Өкінішке орай сіз қателестіңіз, бұндай продукт жоқ! ")
                elif surak == 'q':
                    break
                def change():
                    with open('1mall.txt', 'w+') as fil:
                        for i, item in enumerate(product_list):
                            fil.write(str(i) + '\t' + str(item) + '\n')
                change()

        elif tandau==3:
            with
    return product_list





while True:
    usr=inputs('plz input your login: ')
    pwds=inputs('plz input your password: ')
    if usr=='aistaff' and pwds=='staff':
        staff()
        break
    elif usr=='aimanager' and pwds=='manager':
        manager()
    elif usr=='x' and pwds=='y':
        client()
        break
    else:
        print('Invalid account!!!')


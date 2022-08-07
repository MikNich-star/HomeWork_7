
f = open('balans.txt', 'r')
x = int(f.read())
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print('БАЛАНС :', x)
    choice = input('Выберите пункт меню')
    if choice == '1':
        sum_balans = int(input('Введите сумму на которую хотите пополнить счет:'))
        x += sum_balans
        with open('balans.txt', 'w') as f:
            f.write(f'{x}')


    elif choice == '2':
        buy = int(input('Введите сумму покупки:'))
        if buy > x:
            print('На вашем балансе недостаточно средств')
        else:
            x -= buy
            with open('balans.txt', 'w') as f:
                f.write(f'{x}')
            name = input('Ведите название покупки:')
            with open('orders.txt', 'a') as f:
                f.write(f'{name} : {buy}\n')
    elif choice == '3':
        with open('orders.txt', 'r') as f:
            print(f.read())

    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')

import shutil
import os.path
import function as fun
while True:
    print('1.Создать папку')
    print('2.Удалить файл/папку')
    print('3.Копировать файл/папку')
    print('4.Просмотр содержимого рабочей директории')
    print('5.Просмотр папок')
    print('6.Просмотр файлов')
    print('7.Сохранить содержимое рабочей директории')
    print('8.Выход')
    choice = input('Выберите пункт меню')
    if choice == '1':
        os.mkdir(input(''))
    elif choice == '2':
        os.rmdir(input(''))
    elif choice == '3':
        shutil.copy(input(''), input(''))
    elif choice == '4':
        input(os.getcwd())
    elif choice == '5':
        input(os.listdir())
    elif choice == '6':
        print(fun.show_files())
    elif choice == '7':
        with open('listdir.txt', 'w') as f:
            f.write(f'files : {fun.show_files()}\n'
                    f'dirs : {fun.dir_list()}')
    elif choice == '8':
        break
    else:
        print('Неверный пункт меню')

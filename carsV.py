from objects import *

print('\t\t\t\t\tКаталог машин версия №3')

while True:
    print('-' * 117)
    print('Какую операцию вы хотите выполнить?')
    print('1)Добавить\n2)Список\n3)Поиск\n4)Очистить\n5)Завершить')

    qws = input()

    if qws == 'Добавить' or qws == 'добавить' or qws == '1':
        print('Чтобы добавить машину в список, введите её характеристики')
        car = AddCar()
        car.add_in_file('car catalog 3.1.txt')

    if qws == 'Список' or qws == 'список' or qws == '2':
        print('\t\t\t\t\tСписок всех машин')
        head = (f'|{"Марка":^20}|{"Модель":^20}|{"Номер":^10}|{"Двигатель л.с.":^14}|{"Цвет":^15}|'
                f'{"Фары":^5}|{"Двери":^7}|{"Скорость":^8}|{"Масса кг":^8}|')
        print(head)
        cars = ReadCar().list
        for i in range(len(cars)):
            print('-' * 117)
            print(f'|{cars[i][0]:^20}|{cars[i][1]:^20}|{cars[i][2]:^10}|{cars[i][3]:^14}|{cars[i][4]:^15}|'
                    f'{cars[i][5]:^5}|{cars[i][6]:^7}|{cars[i][7]:^8}|{cars[i][8]:^8}|')

    if qws == 'Поиск' or qws == 'поиск' or qws == '3':
        print('Введите марку, модель или номер автомобиля')

        head = (f'|{"Марка":^20}|{"Модель":^20}|{"Номер":^10}|{"Двигатель л.с.":^14}|{"Цвет":^15}|'
                f'{"Фары":^5}|{"Двери":^7}|{"Скорость":^8}|{"Масса кг":^8}|')

        art = input()
        print(head)
        read = ReadCar()
        read.search(art)

        status = read.status

        if status == 1:
            print('Что вы хотите сделать?')

            change = input('1)Изменить\n2)Удалить\n3)Ничего\n')
            if change == '1' or change == 'Изменить' or change == 'изменить':

                print('Что вы хотите изменить?')
                variant = input('1)Номер\n2)Цвет\n3)Состояние фар\n4)Состояние дверей\n5)Ничего\n')

                if variant == '1' or variant == 'Номер':
                    num = input('Номер: ')
                    read.change('car catalog 3.1.txt', art=num, index=art, what='num')

                if variant == '2' or variant == 'Цвет':
                    color = input('Цвет: ')
                    read.change('car catalog 3.1.txt', art=color, index=art, what='color')

                if variant == '3' or variant == 'Состояние фар':
                    light = input('Состояние фар: ')
                    read.change('car catalog 3.1.txt', art=light, index=art, what='light')

                if variant == '4' or variant == 'Состояние дверей':
                    doors = input('Состояниее дверей: ')
                    read.change('car catalog 3.1.txt', art=doors, index=art, what='doors')

            if change == '2' or change == 'Удалить' or change == 'удалить':
                delete = input('Точно хотите удалить машину из списка?\n')
                if delete in ['Yes', 'yes', 'Да', 'да']:
                    read.delete('car catalog 3.1.txt', what=art)

    if qws == 'Очистить' or qws == 'очистить' or qws == '4':
        delete = input('Вы точно хотите очистить список?\n')
        if delete == 'Да' or delete == 'да' or delete == 'Yes' or delete == 'yes':
            ReadCar().delete('car catalog 3.1.txt', 'all')

    if qws == 'Завершить' or qws == 'завершить' or qws == '5':
        print('Сеанс завершён')
        break
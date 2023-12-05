class AddCar:
    def __init__(self):
        self.mark = input('Марка:')
        self.mark = self.register(self.mark,what='mark')

        self.model = input('Модель:')
        self.model = self.register(self.model,what='model')

        print('Формат российского гос. номера А000АА000')
        self.num = input('Номер:')
        self.num = self.register(self.num, what='num')

        self.engine = input('Двигатель л.с.:')
        self.color = input('Цвет:')
        self.light = input('Состояние фар:')
        self.doors = input('Состояние дверей:')
        self.maxV = input('Максимальная скорость км/ч:')
        self.m = input('Масса кг:')

        self.check(self.light,self.doors,self.num)

    def add_in_file(self,file):
        with open(f'{file}', 'a', encoding='utf-8') as f:
            f.write(f'{self.mark} {self.model} {self.num} {self.engine} {self.color} '
                    f'{self.light} {self.doors} {self.maxV} {self.m}\n')

    def check(self,light, doors,num):  # Проверка верности введенных данных
        n = [i[2] for i in ReadCar().list]
        k = ['on', 'On', 'off', 'Off', 'вкл', 'Вкл', 'выкл', 'Выкл']
        d = ['open', 'Open', 'close', 'Close', 'открыто', 'Открыто', 'заперто', 'Заперто']

        if (light not in k) or (doors not in d) or (num in n):
            while num in n:
                num = input('\nВведеннный номер уже занят. Введите другой:\n')

            while light not in k:
                light = input('\nВведите состояние фар только вкл/выкл или on/off:\n')

            while doors not in d:
                doors = input('\nВведите состояние дверей только открыто/заперто или open/close:\n')

        self.light = light
        self.doors = doors
        self.num = num

        return self.light, self.doors, self.num

    def register(self,par,what):
        S = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        if (par[0] in s)and(what=='mark'or what=='model'):
            par = par.replace(par[0],S[s.index(par[0])],1)
            return par

        elif what=='num':
            for i in par:
                if i in s:
                    par = par.replace(i, S[s.index(i)], 1)

            return par

        else:
            return par


class ReadCar():
    def __init__(self):
        with open('car catalog 3.1.txt','r',encoding='utf-8') as f:
            self.list = []
            for i in f.readlines():
                self.mark,self.model,self.num,self.engine,self.color,self.light,self.doors,self.maxV,self.m = map(str,i.split())
                self.list += [[self.mark,self.model,self.num,self.engine,self.color,self.light,self.doors,self.maxV,self.m]]
            self.nums = [i[2] for i in self.list]

    def reg(self, par, what):
        S = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        if (par[0] in s) and (what == 'mark' or what == 'model'):
            par = par.replace(par[0], S[s.index(par[0])], 1)
            return par

        elif what == 'num':
            for i in par:
                if i in s:
                    par = par.replace(i, S[s.index(i)], 1)

            return par

        else:
            return par
    def search(self,art):
        cars = self.list
        marks = [i[0] for i in cars]
        models = [i[1] for i in cars]
        nums = [i[2] for i in cars]

        art = self.reg(art,'mark')
        NUM = self.reg(art,'num')

        if art in marks:
            for i in range(len(marks)):
                if marks[i]==art:
                    print('-' * 117)
                    print(f'|{cars[i][0]:^20}|{cars[i][1]:^20}|{cars[i][2]:^10}|{cars[i][3]:^14}|{cars[i][4]:^15}|'
                          f'{cars[i][5]:^5}|{cars[i][6]:^7}|{cars[i][7]:^8}|{cars[i][8]:^8}|')
                    self.status = 0

        elif art in models:
            for i in range(len(models)):
                if models[i]==art:
                    print('-' * 117)
                    print(f'|{cars[i][0]:^20}|{cars[i][1]:^20}|{cars[i][2]:^10}|{cars[i][3]:^14}|{cars[i][4]:^15}|'
                          f'{cars[i][5]:^5}|{cars[i][6]:^7}|{cars[i][7]:^8}|{cars[i][8]:^8}|')
                    self.status = 0

        elif NUM in nums:
            for i in range(len(nums)):
                if nums[i]==NUM:
                    print('-' * 117)
                    print(f'|{cars[i][0]:^20}|{cars[i][1]:^20}|{cars[i][2]:^10}|{cars[i][3]:^14}|{cars[i][4]:^15}|'
                          f'{cars[i][5]:^5}|{cars[i][6]:^7}|{cars[i][7]:^8}|{cars[i][8]:^8}|')
                    self.status = 1
                    break

        else:
            print('-' * 117)
            print('\t\t\t\t\tПо вашему запросу ничего не нашлось')
            self.status = 0

    def change(self,file,art,index,what):
        cars = self.list
        nums = [i[2] for i in cars]

        def wr(list):
            with open(f'{file}','w',encoding='utf-8') as f:
                for i in range(len(list)):
                    f.write(f'{list[i][0]} {list[i][1]} {list[i][2]} {list[i][3]} {list[i][4]} '
                          f'{list[i][5]} {list[i][6]} {list[i][7]} {list[i][8]}\n')

        if what=='num':
            n = [i[2] for i in cars]
            art = self.reg(art,'num')
            index = self.reg(index,'num')
            if (art in n):
                while art in n:
                    art = input('\nВведеннный номер уже занят. Введите другой:\n')

            for i in range(len(nums)):
                if nums[i]==index:
                    cars[i][2] = art
                    nums[i] = art

            wr(cars)

        if what=='color':
            index = self.reg(index, 'num')
            for i in range(len(nums)):
                if nums[i]==index:
                    cars[i][4] = art

            wr(cars)

        if what=='light':
            index = self.reg(index, 'num')
            k = ['on', 'On', 'off', 'Off', 'вкл', 'Вкл', 'выкл', 'Выкл']
            if (art not in k):
                while art not in k:
                    art = input('\nВведите состояние фар только вкл/выкл или on/off:\n')

            for i in range(len(nums)):
                if nums[i] == index:
                    cars[i][5] = art

            wr(cars)

        if what=='doors':
            index = self.reg(index, 'num')
            d = ['open', 'Open', 'close', 'Close', 'открыто', 'Открыто', 'заперто', 'Заперто']
            if (art not in d):
                while art not in d:
                    art = input('\nВведите состояние дверей только открыто/заперто или open/close:\n')

            for i in range(len(nums)):
                if nums[i] == index:
                    cars[i][6] = art

            wr(cars)

    def delete(self,file,what=None):
        if what=='all':
            with open(f'{file}','w',encoding='utf-8') as f:
                f.write('')

        else:
            with open(f'{file}','w',encoding='utf-8') as f:
                for i in self.list:
                    if what not in i:f.write(f'{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} '
                                             f'{i[5]} {i[6]} {i[7]} {i[8]}\n')

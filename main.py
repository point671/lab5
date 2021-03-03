import csv
import operator
import os.path

import path as path


class myCsvReader:

    def __init__(self, file_obj, NameTable):  # принимает объект файла csv
        self.File_obj = file_obj  # Присваивает новой переменной File_obj этот объект
        self.NameTable = NameTable

    def __iter__(self):
        self.cur_list = csv.DictReader(self.File_obj, delimiter=',')  # создание списка из объекта File_obj
        self.index = -1  # Счётчик
        self.ff = []
        '''заполнить список ff значениями из списка cur_list '''
        for line in self.cur_list:
            self.ff.append(line)
        self.File_obj.seek(0)  # смещает указатель в начало
        return self

    def __next__(self):
        if (self.index + 1) >= len(self.ff):  # Как только счётчик больше или равен длине листа ff
            raise StopIteration  # Прерываем итерацию
        self.index = self.index + 1  # Иначе прибовляем еденицу к счётчику
        return self.ff[self.index]  # Возращаем элемент листа ff с текущим значением счётчика

    def __getitem__(self, key):
        self.cur_list = csv.DictReader(self.File_obj, delimiter=',')
        self.listIndex = []
        for line in self.cur_list:
            self.listIndex.append(line)
        self.File_obj.seek(0)
        return self.listIndex[key]

    def __repr__(self):
        return f"Имя таблицы - ('{self.NameTable}')"

    '''Реализация __setattr__'''

    def __setattr__(self, name,
                    value):  # name :  Имя атрибута, которому присваивается значение. value : Значение, которое должно быть присвоено атрибуту.
        self.__dict__[name] = value

    def csv_dict_reader_number(self):
        reader = csv.DictReader(self.File_obj, delimiter=',')
        self.File_obj.seek(0)  # Создание словоря через DictReader(файл, разделитель)
        list1 = sorted(reader, key=operator.itemgetter("Number"))  # сортировка по ключу "Number"
        for line in list1:
            print(line["Number"], end=' '), print(line["FIO"], end=' '), print(line["Email"], end=' '), print(
                line["Group"])  # вывод по ключу

    def csv_dict_reader_string(self):
        reader = csv.DictReader(self.File_obj, delimiter=',')
        self.File_obj.seek(0)  # Создание словоря через DictReader(файл, разделитель)
        for line in reader:
            print(line["Number"], end=' '), print(line["FIO"], end=' '), print(line["Email"], end=' '), print(
                line["Group"])  # вывод по ключу

    def csv_dict_reader_criterion(self):
        print("Введите группу:")
        Crit = input()
        reader = csv.DictReader(self.File_obj, delimiter=',')
        self.File_obj.seek(0)
        for line in reader:  # проход по строкам
            if line["Group"] == Crit:  # Если поле группы равно введённой группе то выводим всю строку
                print(line["Number"], end=' '), print(line["FIO"], end=' '), print(line["Email"], end=' '), print(
                    line["Group"])

    def csv_dict_reader_stringITERATOR(self):
        reader = csv.DictReader(self.File_obj, delimiter=',')
        self.File_obj.seek(0)  # Создание словоря через DictReader(файл, разделитель)
        for line in reader:
            print(line["Number"], end=' '), print(line["FIO"], end=' '), print(line["Email"], end=' '), print(
                line["Group"])  # вывод по ключу

    '''генератор'''

    def generated_str(self, N):
        while N < 3:
            yield self.cur_list[N]
            N -= 1


class csv_dict_writer(myCsvReader):
    def csv_dict_writer(self):
        print("Введите данные:")
        print("Номер")
        Number = input()
        print("Имя")
        Name = input()
        print("Почта")
        Email = input()
        print("Группа")
        Group = input()
        fields = [Number, Name, Email, Group]  # Список из введённых данных, который будет добавлен в файл
        with open(r'data.csv', 'a',
                  newline='') as file:  # открытие(файла, добавление, без дополнительной пустой строки)
            writer = csv.writer(file)
            writer.writerow(fields)


if __name__ == "__main__":
    '''Открытие файла и передача в функции их объектов:'''

    with open("data.csv") as f_obj:

        reader = myCsvReader(f_obj, "Table")

        print(reader[3])
        """
        ыва
        '''Через обычный цикл'''
        for line in reader:
            print(line["Number"], end=' '), print(line["FIO"], end=' '), print(line["Email"], end=' '), print(
                line["Group"])
        """

        '''Через итератор'''
        print("По строкам через итератор")
        for i in reader:
            print(i)

        print(repr(reader))

        reader = 1  # Реализация __setattr__
        print(reader)

        s = myCsvReader.generated_str(myCsvReader,2)
        print(next(s))

        print("Слияние2")

        '''
        print("По строкам:")
        reader.csv_dict_reader_string()
        print("По номеру:")
        reader.csv_dict_reader_number()
        print("По критерию")
        reader.csv_dict_reader_criterion()
        print("==========Новая запись в файл===============")
        with open("data.csv") as f_obj:
            WriteReader = csv_dict_writer(f_obj)
        WriteReader.csv_dict_writer()
        
        with open("data.csv") as f_obj:
            strProhod = myCsvReader(f_obj)
        strProhod.csv_dict_reader_stringITERATOR()
'''

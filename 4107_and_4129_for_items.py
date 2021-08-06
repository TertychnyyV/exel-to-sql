print(f'Данный скрипт читает строчки из текстового файла и подставляет их в хранимую процедуру,\nна выходе файл с хранимками, '
      f'сделан для простоты заливки связей товаров с системой распознавания,\n'
      f'\n')
START_FILE_LOCATION = input(str(f'Формат пути d:\\1.txt \n'
                      f'Укажи путь до файла: '))
END_FILE_LOCATION = input(str(f'Формат пути d:\\1.sql \n'
                              f'Укажи куда сохранить и имя файла: '))
GET_ATTR = input(str('настройка\n' \
                    '0 - просталяем значения для атрибутов 4107(Код объекта в системе распознавания) и 4129(Код фотографии в системе распознавания)\n'
                    '1 - только для 4107(Код объекта в системе распознавания)\n'
                    '2 - только для 4129(Код фотографии в системе распознавания)\n'
                    'Введи число: '))
'''
открываем файл на чтение и запись по шаблону
'''
file = open(f'{START_FILE_LOCATION}', 'r')
complite_file = open(END_FILE_LOCATION, 'w')
for line in file:
    if GET_ATTR == '0':
        complite_file.write('exec ' +
                            f"DS_Set_ObjectsAttributes "
                            f"@DictId=1,"
                            f"@Id={line.strip()},"
                            f"@AttrID=4107,"
                            f"@RecordId=NULL,"
                            f"@AttrValueID=NULL,"
                            f"@AttrText=N'{line.strip()}',"
                            f"@ActiveFlag=1; \n")
        complite_file.write('exec ' +
                            f"DS_Set_ObjectsAttributes "
                            f"@DictId=1,"
                            f"@Id={line.strip()},"
                            f"@AttrID=4129,"
                            f"@RecordId=NULL,"
                            f"@AttrValueID=NULL,"
                            f"@AttrText=N'{line.strip()}',"
                            f"@ActiveFlag=1; \n")
    elif GET_ATTR == '1':
        complite_file.write('exec ' +
                            f"DS_Set_ObjectsAttributes "
                            f"@DictId=1,"
                            f"@Id={line.strip()},"
                            f"@AttrID=4107,"
                            f"@RecordId=NULL,"
                            f"@AttrValueID=NULL,"
                            f"@AttrText=N'{line.strip()}',"
                            f"@ActiveFlag=1; \n")
    elif GET_ATTR == '2':
        complite_file.write('exec ' +
                            f"DS_Set_ObjectsAttributes "
                            f"@DictId=1,"
                            f"@Id={line.strip()},"
                            f"@AttrID=4129,"
                            f"@RecordId=NULL,"
                            f"@AttrValueID=NULL,"
                            f"@AttrText=N'{line.strip()}',"
                            f"@ActiveFlag=1; \n")
    else: f'такое значение не предусмотренно, закрываюсь'
complite_file.close()

import openpyxl

'''
D - exID 3
E - Имя 4
F - Группа
'''
SQL_FILE_LOC = input('D:/SQL_exemple.sql - пример пути и имени\n'
                     'Укажи путь и имя сохраняемого файла: ')
EXID = 9000
COUNTER = 0
wb = openpyxl.load_workbook(input('C:/Users/tertychnyy/Desktop/forPythom/exemple.xlsx - пример пути\n'
                                  'Укажи где лежит файл: '))
sheet = wb.active
END_FILE = open(SQL_FILE_LOC, 'w')
END_FILE.write("use -- укажи БД;\n"
               "-- заводим товары конкурентов + делаем привязку их к системе распознавания, "
               "все товары конкурентов имеют префикс 9000 + поствикс от 1 до +N\n"
                "--begin tran\n"
               "exec DMP_Set_ItemGroups @Exid=N'Конкуренты', @Name=N'Конкуренты', @Activeflag=1;\n")

for row in sheet.rows:
    if str(row[4].value).lower() not in ['name', 'none']:
        COUNTER += 1
        formedExid = str(EXID)+str(COUNTER)
        END_FILE.write('exec DS_Set_Items '
                            '@iID=NULL,'
                            '@TargetDistId=NULL,'
                            '@merTypeID=NULL,'
                            '@ItID=-1,'
                            '@IgID=359,'
                            f"@Exid=N'{str(formedExid)}',"
                            f"@iName=N'{str(row[4].value)}',"
                            f"@iShortname=N'{str(row[4].value)}',"
                            '@activeFlag=1,'
                            '@weight=NULL,'
                            '@unit2=NULL,'
                            '@unit3=NULL,'
                            '@VAT=18,'
                            '@sort=0,'
                            '@OwnerDistId=NULL;\n')
        END_FILE.write('exec DS_Set_ObjectsAttributes '
                            f"@DictId=1,"
                            f"@Id={formedExid},"
                            f"@AttrID=4107,"
                            f"@RecordId=NULL,"
                            f"@AttrValueID=NULL,"
                            f"@AttrText=N'{str(row[3].value)}',"
                            f"@ActiveFlag=1;\n")

END_FILE.write("--select top(286) * from ds_items order by changedate desc;\n"
               "--select * from DS_IGROUPS where igName = 'Конкуренты';\n"
               "--rollback")
END_FILE.close()
wb.close()
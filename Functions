import csv

PATH_TO_FILE = './Corp Summary.csv'


def func1(list_data: list):
    departaments = list(set(elem['Департамент'] for elem in list_data))
    hierarchy=dict.fromkeys(departaments)
    #как сократить в comprehension
    for elem in departaments:
        otdel=set()
        for slov in list_data:
            if elem==slov['Департамент']:
                otdel.add(slov['Отдел'])
        hierarchy[elem]=otdel
    print("Иерархия")
    for key, value in hierarchy.items():
        print(key + ': ' + ', '.join(value))
    return

def func2(list_data: list):
    departaments = list(set(elem['Департамент'] for elem in list_data))
    column_headers = ['Название', 'Численность', '"Вилка" зарплат', 'Cредняя зарплата']
    consolidated_report = {key: [] for key in column_headers}
    consolidated_report['Название']=departaments
    
    chislennost=[]
    for elem in departaments:
        count = 0
        for slov in list_data:
            if elem==slov['Департамент']:
                count += 1
        chislennost.append(count)
    consolidated_report['Численность']=chislennost
    
    srednee=[]
    minimum=[]
    maximum=[]
    for elem in departaments:
        zarplata = []
        for slov in list_data:
            if elem==slov['Департамент']:
                zarplata.append(int(slov['Оклад']))
        srednee.append(sum(zarplata)/len(zarplata))  
        minimum.append(min(zarplata))
        maximum.append(max(zarplata))
    consolidated_report['Cредняя зарплата']=srednee
    vilka =[]
    for i in range(0,len(minimum)):
        a = (str(minimum[i]), str(maximum[i]))
        vilka.append('-'.join(a))
    consolidated_report['"Вилка" зарплат']=vilka
    #print(minimum)
    #print(maximum) 
    return consolidated_report

        
def func3(list_data: list):  
    result = func2(list_data)
    with open("consolidated_report.csv", 'w', encoding='utf-8') as file:
        file.write(";".join(result.keys()) + '\n')
        for tuple_element in zip(result['Название'],
                                         result['Численность'],
                                         result['"Вилка" зарплат'],
                                         result['Cредняя зарплата'],
                                         ):
            file.write(";".join(list(map(str, tuple_element))) + '\n')
    return
    
    

def main():
    with open('./Corp Summary.csv', 'r') as file_obj:
        reader = csv.DictReader(file_obj, delimiter=';')
        employees = [empl for empl in reader]
    #func1(employees)
    #func2(employees)
    #print(employees)
    command = 0
    while command != 4:
        print('Выберете одну из четырёх команд: \n \
        1 Вывести иерархию команд \n \
        2 Вывести сводный отчёт по департаментам\n \
        3 Сохранить сводный отчёт по департаментам в виде csv-файла\n \
        4 Выход из меню'
              )
        command = int(input())
        print()
        if command == 1:
            func1(employees)
        if command == 2:
            result = func2(employees)
            print("{:^17} | {:^17} | {:^17} | {:^17}".format(*result.keys()))
            for tuple_element in zip(result['Название'],
                                     result['Численность'],
                                     result['"Вилка" зарплат'],
                                     result['Cредняя зарплата'],
                                     ):
                print("{:^17} | {:^17} | {:^17} | {:^17}".format(*tuple_element))
        if command == 3:
            func3(employees)
            print('Done')
        if command == 4:
            return 1
if __name__ == '__main__':
    main()

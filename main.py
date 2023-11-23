expenses = {'Кредит':18800,
            'Курс':5000,
            'Мобильная связь':500,
            'Интернет':700,
            'ЖКХ':6000,
            'ИП':3500,
            'Дача':2000,
            'ЖКХ Каховка':2000,
            'Свадьба':10000,
            'Накопления': 40000}

def printExpenses(): #Функция печати всех расходов по позициям
    for i in expenses:
        print(i + ' - ' + str(expenses[i]))

def printHalfExpenses(): #Функция печати половины суммы расхода по каждой позиции
    tmp = 0
    for i in expenses:
        tmp += expenses[i] / 2
        print(i + ' - ' + str(expenses[i] / 2))
    print('Сумма всех расходов за половину месяца: ', tmp)

printHalfExpenses()
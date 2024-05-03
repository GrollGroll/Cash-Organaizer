import datetime

from models import Transaction, Wallet


filename = 'wallet.txt'
wallet = Wallet(filename)


def date_input() -> datetime.date:
    while True:
        date = input('Введите дату (ГГГГ-ММ-ДД): ')
        try:
            date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            return (date_obj)
        except ValueError:
            print('Дата введена некорректно! Повторите попытку.')


def category_input() -> str:
    while True:
        print('1. Доход')
        print('2. Расход')
        try:
            category_index = int(input('Выберите категорию (1/2): '))
            category = 'Доход' if category_index == 1 else 'Расход'
            print(f'Выбрана категория {category}')
            return category
        except ValueError:
            print('Категория не распознана. Пожалуйста, введите 1 или 2.')


def amount_input() -> float:
    while True:
        try:
            amount = float(input('Введите сумму: '))
            return (amount)
        except ValueError:
            print('Сумма введена некорректно! Повторите попытку.')


def create_transaction():
    date = date_input()
    category = category_input()
    amount = amount_input()
    description = input('Введите описание: ')
    transaction = Transaction(date, category, amount, description)
    return transaction


while True:
    print('\nВыберите действие:')
    print('1. Вывод баланса')
    print('2. Добавление записи')
    print('3. Редактирование записи')
    print('4. Поиск по записям')
    print('5. Выход')
    choice = input('Введите номер действия: ')

    # Вывод баланса
    if choice == '1':
        wallet.show_balance()

    # Добавление записи
    elif choice == '2':
        transaction = create_transaction()
        wallet.add_transaction(transaction)
        print('Запись добавлена успешно!')

    # Редактирование записи
    elif choice == '3':
        while True:
            try:
                index = int(input('Введите номер записи для редактирования: '))
                break
            except ValueError:
                print('Номер введен некорректно! Повторите попытку.')
        index -= 1
        if 0 <= index < wallet.count_transactions():
            new_transaction = create_transaction()
            wallet.edit_transaction(index, new_transaction)
            print('Запись отредактирована успешно!')
        else:
            print('Ошибка: запись не найдена.')

    # Поиск по записям
    elif choice == '4':
        print('Поиск транзакций.')
        date_filter = input('Требуется ли фильтр даты в поиске?'
                            ' Оставьте поле пустым, если нет. ')
        category_filter = input('Требуется ли фильтр категорий в поиске?'
                                ' Оставьте поле пустым, если нет. ')
        amount_filter = input('Требуется ли фильтр суммы в поиске?'
                              ' Оставьте поле пустым, если нет. ')
        date = date_input() if date_filter else None
        category = category_input() if category_filter else None
        amount = amount_input() if amount_filter else None
        results = wallet.search_transactions(date, category, amount)
        if results:
            print('Результаты поиска:')
            for result in results:
                print(f'Дата: {result.date}')
                print(f'Категория: {result.category}')
                print(f'Сумма: {result.amount}')
                print(f'Описание: {result.description}\n')
        else:
            print('Записей не найдено.')

    # Выход
    elif choice == '5':
        print('Удачных покупок!')
        break
    else:
        print('Ошибка: неверный ввод. Пожалуйста, введите число от 1 до 5.')

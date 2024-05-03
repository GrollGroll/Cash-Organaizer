import datetime
import os


class Transaction:
    def __init__(
        self,
        date: datetime.date,
        category: str,
        amount: float,
        description: str
    ) -> None:
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description


class Wallet:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def _load_transactions(self) -> list[Transaction]:
        transactions = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for i in range(0, len(lines), 5):
                    date_str = lines[i].strip()
                    date_format = 'Дата: %Y-%m-%d'
                    date = datetime.datetime.strptime(date_str, date_format).date()
                    category = lines[i+1].strip().split(': ')[1]
                    amount = float(lines[i+2].strip().split(': ')[1])
                    description = lines[i+3].strip().split(': ')[1]
                    transaction = Transaction(date, category, amount, description)
                    transactions.append(transaction)
        return transactions

    def _save_transactions(self, transactions: list[Transaction]) -> None:
        with open(self.filename, 'w') as file:
            for transaction in transactions:
                file.write(f'Дата: {transaction.date}\n')
                file.write(f'Категория: {transaction.category}\n')
                file.write(f'Сумма: {transaction.amount}\n')
                file.write(f'Описание: {transaction.description}\n')
                file.write('\n')

    def add_transaction(self, transaction: Transaction) -> None:
        with open(self.filename, 'a') as file:
            file.write(f'Дата: {transaction.date}\n')
            file.write(f'Категория: {transaction.category}\n')
            file.write(f'Сумма: {transaction.amount}\n')
            file.write(f'Описание: {transaction.description}\n')
            file.write('\n')

    def edit_transaction(self, index: int, new_transaction: Transaction) -> bool:
        transactions = self._load_transactions()
        transactions[index] = new_transaction
        self._save_transactions(transactions)
        return True

    def search_transactions(
        self,
        date: datetime.date | None = None,
        category: str | None = None,
        amount: float | None = None
    ) -> list[Transaction]:
        transactions = self._load_transactions()
        result = []
        for transaction in transactions:
            if (date is None or transaction.date == date) and \
                    (category is None or transaction.category == category) and \
                    (amount is None or transaction.amount == amount):
                result.append(transaction)
        return result

    def show_balance(self) -> None:
        transactions = self._load_transactions()
        incomes = sum(
            transaction.amount
            for transaction in transactions
            if transaction.category == 'Доход'
        )
        expenses = sum(
            transaction.amount
            for transaction in transactions
            if transaction.category == 'Расход'
        )
        balance = incomes - expenses
        print(f'Текущий баланс: {balance}')
        print(f'Доходы: {incomes}')
        print(f'Расходы: {expenses}')

    def count_transactions(self) -> int:
        transactions = self._load_transactions()
        return len(transactions)

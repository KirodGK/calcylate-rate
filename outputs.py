from prettytable import PrettyTable


def pretty_output(results: list[dict]):
    table = PrettyTable()

    # Определим порядок колонок
    columns = ['name', 'hours', 'department', 'rate', 'payout']
    table.field_names = columns
    table.align = 'l'

    # Преобразуем словари в списки значений
    for row in results:
        table.add_row([row.get(col, '') for col in columns])

    print(table)
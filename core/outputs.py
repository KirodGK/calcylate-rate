from prettytable import PrettyTable


def pretty_output(results: list[dict]):
    table = PrettyTable()
    columns = ['name', 'hours', 'department', 'rate', 'payout']
    table.field_names = columns
    table.align = 'l'
    for row in results:
        table.add_row([row.get(col, '') for col in columns])

    print(table)


def report(args, results, header):
    try:
        with open(f'{args.report}.csv', 'w', encoding='utf-8') as file:
            file.write(','.join(header) + '\n')
            for row in results:
                line = ('{department},{name},{hours},{rate},{payout}'
                        ).format(**row)
                file.write(line + '\n')
        print(f'Отчёт {args.report}.csv успешно сохранён.')
    except IOError:
        print('Ошибки при записи отсчёта в файл.')


def preview(results: list[dict], header: list[str]):
    maxLenHeaders = {}
    for col in header:
        values = [row.get(col) for row in results]
        if values:
            maxLenHeaders[col] = max(len(str(val)) for val in values + [col])

    formatHeaders = [formatColumn(newHeader, maxLenHeaders)
                     for newHeader in header]
    print('  '.join(formatHeaders))
    for row in results:
        print(formatRow(row, maxLenHeaders, header))


def formatColumn(header, maxLenHeader):
    lenHeader = len(str(header))
    getLen = maxLenHeader[header]
    if (lenHeader < getLen):
        header = header + ' ' * (getLen - lenHeader) 
    return header


def formatRow(row, maxLenHeader, header):
    line = ''
    for key in header:
        value = row.get(key, '')
        value_str = str(value)
        lenRow = len(value_str)
        getLen = maxLenHeader.get(key, lenRow)
        line += value_str + ' ' * (getLen - lenRow) + '  '
    return line.rstrip()

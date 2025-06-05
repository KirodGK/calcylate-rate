from typing import List, Dict, Any
from argparse import Namespace


def report(args: Namespace,
           results: List[Dict[str, Any]],
           header: List[str]) -> None:
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


def preview(results: List[Dict[str, Any]],
            header: List[str]) -> None:
    maxLenHeaders: Dict[str, int] = {}
    for col in header:
        values = [row.get(col) for row in results]
        if values:
            maxLenHeaders[col] = max(len(str(val)) for val in values + [col])

    formatHeaders = [formatColumn(newHeader,
                                  maxLenHeaders) for newHeader in header]
    print('  '.join(formatHeaders))
    for row in results:
        print(formatRow(row, maxLenHeaders, header))


def formatColumn(header: str, maxLenHeader: Dict[str, int]) -> str:
    lenHeader = len(header)
    getLen = maxLenHeader[header]
    if lenHeader < getLen:
        header += ' ' * (getLen - lenHeader)
    return header


def formatRow(row: Dict[str, Any],
              maxLenHeader: Dict[str, int],
              header: List[str]) -> str:
    line = ''
    for key in header:
        value = row.get(key, '')
        value_str = str(value)
        lenRow = len(value_str)
        getLen = maxLenHeader.get(key, lenRow)
        line += value_str + ' ' * (getLen - lenRow) + '  '
    return line.rstrip()
import argparse


def configure_argument_parser(available_modes):
    parser = argparse.ArgumentParser(description='Калькулятор зарплаты')
    parser.add_argument(
        'mode',
        choices=available_modes,
        help='Режимы работы'
    )
    parser.add_argument(
        'files',
        nargs='+',
        help='CSV-файлы с данными'
    )
    # parser.add_argument(
    #     '-c',
    #     '--clear-cache',
    #     action='store_true',
    #     help='Очистка кеша'
    # )
    # parser.add_argument(
    #     '-r',
    #     '--report',
    #     choices=('pretty', 'file'),
    #     help='Дополнительные способы вывода данных'
    # )
    parser.add_argument(
        '--report',
        default='Payout',
        help='Название отчёта'
    )
    return parser
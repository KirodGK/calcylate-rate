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
    parser.add_argument(
        '--report',
        help='Название отчёта'
    )
    return parser

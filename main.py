
from configs import configure_argument_parser
from core.count_salary import count_salary
from core.outputs import preview, report


MODE_TO_FUNCTION = {
    'calk': count_salary,
}


def main():
    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    try:
        args = arg_parser.parse_args()
    except SystemExit:
        print("Неверные аргументы. Используйте -h для помощи.")
        exit()
    args = arg_parser.parse_args()
    parser_mode = args.mode
    function = MODE_TO_FUNCTION.get(parser_mode)
    if function is not None:
        results = function(args.files)
        if not results:
            print('Нет данных')
            exit()
        header = ['department', 'name', 'hours', 'rate', 'payout']
        if args.report:
            report(args, results, header)
        else:
            print('Предварительный отчёт')
            preview(results, header)
            print(
                "Для сохранения отчёта повторите команду с ключом \"--report\""
                " и введите названием отчёта.\n"
                "Для дополнительной информации введите \"--h\""
            )


if __name__ == '__main__':
    main()

from core.parse_header import parse_header
from utils import counter
from core.outputs import pretty_output
from configs import configure_argument_parser


def calk(files):
    all_data = []
    for path in files:
        with open(path, 'r') as file:
            lines = file.read().split('\n')
            if not lines:
                continue
            header = parse_header(lines[0])
            data = counter(data=lines[1:], header=header)
            all_data.extend(data)
    return all_data


MODE_TO_FUNCTION = {
    'calk': calk,
}


def main():
    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    args = arg_parser.parse_args()
    parser_mode = args.mode
    function = MODE_TO_FUNCTION.get(parser_mode)
    if function is not None:
        results = function(args.files)
        if args.report:
            with open(f'{args.report}.csv', 'w', encoding='utf-8') as file:
                header = ', '.join(results[0].keys())
                file.write(header + '\n')
                print(header)
                for row in results:
                    print(row)
                    line = '{department}, {name}, {hours}, {rate}, {payout}'.format(**row)
                    file.write(line + '\n')

        else:
            pretty_output(results)


if __name__ == '__main__':
    main()

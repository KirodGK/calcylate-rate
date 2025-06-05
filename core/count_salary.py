from core.parse_header import parse_header
from utils import counter


def count_salary(files):
    all_data = []
    try:
        for path in files:
            with open(path, 'r') as file:
                lines = file.read().split('\n')
                if not lines:
                    continue
                header = parse_header(lines[0])
                data = counter(data=lines[1:], header=header)
                all_data.extend(data)
        return all_data
    except IOError:
        print(f'По указному пути файл отсутствует. Путь: {path}')

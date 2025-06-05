from typing import List, Dict, Union
from core.parse_header import parse_header
from utils import counter


def count_salary(files: List[str]) -> List[Dict[str, Union[str, int]]]:
    all_data: List[Dict[str, Union[str, int]]] = []
    try:
        for path in files:
            with open(path, 'r', encoding='utf-8') as file:
                lines = file.read().split('\n')
                if not lines or not lines[0].strip():
                    continue
                header = parse_header(lines[0])
                data = counter(data=lines[1:], header=header)
                all_data.extend(data)
        return all_data
    except IOError:
        print(f'По указанному пути файл отсутствует. Путь: {path}')
        return []


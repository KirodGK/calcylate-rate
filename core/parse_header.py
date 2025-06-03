
header_template: dict = {
    'id': 0,
    'name': 0,
    'email': 0,
    'department': 0,
    'hours_worked': 0,
    'rate': 0
}

FIELD_ALIASES = {
    'id': ['id'],
    'name': ['name'],
    'email': ['email'],
    'department': ['department'],
    'hours_worked': ['hours_worked'],
    'rate': ['hourly_rate', 'rate', 'salary']
}
# def parse_header(data):
#     if (data == ''):
#         return 'Нет данных'
#     header = (header[x] == x for x in data if x in header.key())
#     return header



# def parse_header(line):
#     if not line.strip():
#         return 'Нет данных'
    
#     fields = line.strip().split(',')
#     positions = {field: index for index, field in enumerate(fields) if field in header_template}
#     return positions


def parse_header(line: str):
    if not line.strip():
        return 'Нет данных'
    
    fields = [f.strip().lower() for f in line.strip().split(',')]  # нормализуем
    
    result = {}
    for logical_name, aliases in FIELD_ALIASES.items():
        for alias in aliases:
            if alias in fields:
                result[logical_name] = fields.index(alias)
                break  # нашли — выходим из цикла
    
    return result
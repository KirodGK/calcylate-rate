from constants import FIELD_ALIASES

header_template: dict = {
    'id': 0,
    'name': 0,
    'email': 0,
    'department': 0,
    'hours_worked': 0,
    'rate': 0
}


def parse_header(line: str):
    if not line.strip():
        return 'Нет данных'
    fields = [f.strip().lower() for f in line.strip().split(',')]
    result = {}
    for logical_name, aliases in FIELD_ALIASES.items():
        for alias in aliases:
            if alias in fields:
                result[logical_name] = fields.index(alias)
                break
    return result

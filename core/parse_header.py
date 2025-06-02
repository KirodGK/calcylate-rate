
header_template: dict = {
    'id': 0,
    'name': 0,
    'email': 0,
    'department': 0,
    'hours_worked': 0,
    'rate': 0
}

# def parse_header(data):
#     if (data == ''):
#         return 'Нет данных'
#     header = (header[x] == x for x in data if x in header.key())
#     return header



def parse_header(line):
    if not line.strip():
        return 'Нет данных'
    
    fields = line.strip().split(',')
    positions = {field: index for index, field in enumerate(fields) if field in header_template else }
    return positions
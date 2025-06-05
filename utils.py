def counter(data: list[list[str]], header: dict) -> list[dict]:
    formatted = []

    for dataString in data:
        try:
            # print(dataString.split(','))
            # print(header['name'])
            splitDataString = dataString.split(',')
            name = splitDataString[header['name']]
            department = splitDataString[header['department']]
            hours = int(splitDataString[header['hours_worked']])
            rate = int(splitDataString[header['rate']])
            payout = hours * rate

            formatted.append({
                'department': department,
                'name': name,
                'hours': hours,
                'rate': rate,
                'payout': payout
            })
        except (IndexError, KeyError, ValueError) as e:
            print(f"Ошибка при обработке строки {dataString}: {e}")
            continue  # пропускаем ошибочную строку

    return formatted

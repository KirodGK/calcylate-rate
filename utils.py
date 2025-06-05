from typing import List, Dict


def counter(data: List[str],
            header: Dict[str, int]) -> List[Dict[str, int | str]]:
    formatted = []
    for dataString in data:
        try:
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
            continue

    return formatted

from typing import Dict, List

FIELD_ALIASES: Dict[str, List[str]] = {
    'id': ['id'],
    'name': ['name'],
    'email': ['email'],
    'department': ['department'],
    'hours_worked': ['hours_worked'],
    'rate': ['hourly_rate', 'rate', 'salary']
}

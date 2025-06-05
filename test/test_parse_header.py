from core.parse_header import parse_header


def test_parse_header_with_valid_aliases():
    line = "Name,Email,Department,hours_worked,Rate,ID"
    result = parse_header(line)

    assert isinstance(result, dict)
    assert result['id'] == 5
    assert result['name'] == 0
    assert result['email'] == 1
    assert result['department'] == 2
    assert result['hours_worked'] == 3
    assert result['rate'] == 4


def test_parse_header_with_empty_line():
    assert parse_header("") == "Нет данных"

from utils import counter


def test_counter_valid_data():
    header = {'name': 0, 'department': 1, 'hours_worked': 2, 'rate': 3}
    data = [
        "Alice,Engineering,40,25",
        "Bob,HR,35,30"
    ]
    result = counter(data, header)

    assert len(result) == 2
    assert result[0]['name'] == "Alice"
    assert result[0]['payout'] == 1000.0

import price_info as Pinfo

def test_cost_of_fruit():
    fruit_name = 'watermelon'
    fruit_quantity = 5
    expected_result = 32.50
    test_result = Pinfo.cost_of_fruits(fruit_name, fruit_quantity)
    assert (test_result == expected_result)

def test_total_cost():
    expected_result = 46.75
    test_result = Pinfo.total_cost_shopping()
    assert (test_result == expected_result)
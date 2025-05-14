import Lab_2.bmi as BMI

def test_calculate_bmi_ow():
    expected_result = 1
    weight = 100
    test_result = BMI.calculate_bmi(1.73, weight)
    assert (test_result == expected_result)

def test_calculate_bmi_uw():
    expected_result = -1
    weight = 20
    test_result = BMI.calculate_bmi(1.73, weight)
    assert (test_result == expected_result)

def test_calculate_bmi_nw():
    expected_result = 0
    weight = 50
    test_result = BMI.calculate_bmi(1.73, weight)
    assert (test_result == expected_result)
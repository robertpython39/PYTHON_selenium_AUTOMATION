import pytest
from All_Buttons import TestAllButtons

@pytest.mark.functional
def test_all_buttons_web():
    my_url = TestAllButtons()
    my_url.test_button_1()
    my_url.test_button_2()
    my_url.test_button_3()
    my_url.test_button_4()
    my_url.test_button_5()
    my_url.test_button_6()
    my_url.test_button_7()
    my_url.test_button_8()
    my_url.test_button_9()
    my_url.test_button_10()
    my_url.test_button_11()
    my_url.test_button_12()
    my_url.test_button_13()
    my_url.test_button_14()
    my_url.test_button_15()
import pytest
from All_Buttons import TestAllButtons

@pytest.mark.functional
def test_all_buttons_web():
    my_url = TestAllButtons()
    for i in range(1, 16):
        method_name = f'test_button_{i}'
        getattr(my_url, method_name)()

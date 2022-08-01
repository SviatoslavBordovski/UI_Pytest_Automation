import pytest

def first_tc_login_params():
    params_list = [
        ("Admin", "admin123"),
        pytest.param("random_username", "admin123",
                     marks=pytest.mark.xfail(reason="Non-existing username entered")),
        pytest.param("Admin", "qwerty123!",
                     marks=pytest.mark.xfail(reason="Incorrect password entered")),
        pytest.param("qwertyADMIN", "qwertyADMIN",
                     marks=pytest.mark.xfail(reason="Wrong credentials")),
        pytest.param(" ", "admin123",
                     marks=pytest.mark.xfail(reason="Empty username")),
        pytest.param("Admin", " ",
                     marks=pytest.mark.xfail(reason="Empty password"))
    ]

    return params_list

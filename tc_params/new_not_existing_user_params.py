import pytest

def third_tc_new_user_params():
    params_list = [
        ("Charlie Carter", "q1w2e3r4t5y6u7i8o9!~!", "q1w2e3r4t5y6u7i8o9!~!"),
        pytest.param("Charlie Carter", "q1w2e3r4t5y6u7i8o9!~!", "",
                     marks=pytest.mark.xfail(reason="Non-existing employee name and too short password entered")),
        pytest.param("", "q1w2e3r4t5y6u7i8o9!~!", "q1w2e3r4t5y6u7i8o9!~!",
                     marks=pytest.mark.xfail(reason="Empty username field, 'required' validation message shown up")),
        pytest.param("Charlie Carter", "q1w2e3", "q1w2e3r4t5y6u7i8o9!~!",
                     marks=pytest.mark.xfail(reason="Incorrect new password filled in"))
    ]

    return params_list

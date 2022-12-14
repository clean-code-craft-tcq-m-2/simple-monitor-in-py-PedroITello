from battery_state import temp_is_ok, state_of_charge_is_ok, charge_rate_is_ok


# Call functions and made evaluations
def battery_is_ok(temperature, soc, change_rate):
    temp_result = temp_is_ok(temperature)
    soc_result = state_of_charge_is_ok(soc)
    cr_result = charge_rate_is_ok(change_rate)
    return battery_evaluation(temp_result, soc_result, cr_result)


def battery_evaluation(temp, soc, change_rate):
    return temp and soc and change_rate

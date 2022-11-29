from check_functions import temp_is_ok, soc_is_ok, change_rate_is_ok


# Call functions and made evaluations
def batery_test(temperature, soc, change_rate):
    return (
        temp_is_ok(temperature),
        soc_is_ok(soc),
        change_rate_is_ok(change_rate)
    )

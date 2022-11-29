# Function for check temp
def temp_is_ok(temperature):
    if temperature < 0 or temperature > 45:
        print('Temperature is out of range!')
        return False
    else:
        return True


# Function for check state of charge
def soc_is_ok(soc):
    if soc < 20 or soc > 80:
        print('State of Charge is out of range!')
        return False
    else:
        return True


# Function for check change rate
def change_rate_is_ok(charge_rate):
    if charge_rate > 0.8:
        print('Charge rate is out of range!')
        return False
    else:
        return True

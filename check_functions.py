# Function for check temp
def temp_is_ok(temperature):
    # Update ranges using article from research
    # https://batteryuniversity.com/article/bu-410-charging-at-high-and-low-temperatures
    if temperature < -20 or temperature > 50:
        print('Temperature is out of range!')
        return False
    else:
        return True


# Function for check state of charge
def soc_is_ok(soc):
    # Updated ranges using article from research
    # https://www.sciencedirect.com/science/article/pii/S2352484719310911
    if soc < 20 or soc > 100:
        print('State of Charge is out of range!')
        return False
    else:
        return True


# Function for check change rate
def change_rate_is_ok(charge_rate):
    if charge_rate < 0 or charge_rate > 0.8:
        print('Charge rate is out of range!')
        return False
    else:
        return True

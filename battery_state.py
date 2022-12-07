from settings import *

# Function for check temp
def temp_is_ok(temperature):
    # Update ranges using article from research
    # https://batteryuniversity.com/article/bu-410-charging-at-high-and-low-temperatures
    if temperature < TEMPERATURE_MIN_CHARGE_TEMP or temperature > TEMPERATURE_MAX_CHARGE_TEMP:
        print('Temperature is out of range!')
        return False
    else:
        return True


# Function for check state of charge
def state_of_charge_is_ok(state_of_charge):
    # Updated ranges using article from research
    # https://www.sciencedirect.com/science/article/pii/S2352484719310911
    if state_of_charge < STATE_OF_CHARGE_MIN_LIMIT or state_of_charge > STATE_OF_CHARGE_MAX_LIMIT:
        print('State of Charge is out of range!')
        return False
    else:
        return True


# Function for check charge rate
def charge_rate_is_ok(charge_rate):
    if charge_rate < 0 or charge_rate > 0.8:
        print('Charge rate is out of range!')
        return False
    else:
        return True

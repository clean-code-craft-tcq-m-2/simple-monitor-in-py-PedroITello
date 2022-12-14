from temp_manager import temp_conversor
from settings import (TEMPERATURE_MIN_CHARGE_TEMP,
                      TEMPERATURE_MAX_CHARGE_TEMP,
                      STATE_OF_CHARGE_MIN_LIMIT,
                      STATE_OF_CHARGE_MAX_LIMIT,
                      CHARGE_RATE_MIN_LIMIT,
                      CHARGE_RATE_MAX_LIMIT,
                      CURRENT_LANGUAGE)
if CURRENT_LANGUAGE == "EN":
    from lang_en import (BATTERY_IS_OK_MESSAGE,
                         STATE_OF_CHARGE_IS_OK_MESSAGE,
                         CHARGE_RATE_IS_OK_MESSAGE)
else:
    from lang_de import (BATTERY_IS_OK_MESSAGE,
                         STATE_OF_CHARGE_IS_OK_MESSAGE,
                         CHARGE_RATE_IS_OK_MESSAGE)


# Function for check temp
def temp_is_ok(temperature):
    # Update ranges using article from research
    # https://batteryuniversity.com/article/bu-410-charging-at-high-and-low-temperatures
    if (temperature < temp_conversor(TEMPERATURE_MIN_CHARGE_TEMP)
            or temperature > temp_conversor(TEMPERATURE_MAX_CHARGE_TEMP)):
        print(BATTERY_IS_OK_MESSAGE)
        return False
    else:
        return True


# Function for check state of charge
def state_of_charge_is_ok(state_of_charge):
    # Updated ranges using article from research
    # https://www.sciencedirect.com/science/article/pii/S2352484719310911
    if (state_of_charge < STATE_OF_CHARGE_MIN_LIMIT
            or state_of_charge > STATE_OF_CHARGE_MAX_LIMIT):
        print(STATE_OF_CHARGE_IS_OK_MESSAGE)
        return False
    else:
        return True


# Function for check charge rate
def charge_rate_is_ok(charge_rate):
    if (charge_rate < CHARGE_RATE_MIN_LIMIT
            or charge_rate > CHARGE_RATE_MAX_LIMIT):
        print(CHARGE_RATE_IS_OK_MESSAGE)
        return False
    else:
        return True

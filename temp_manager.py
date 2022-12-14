from settings import TEMPERATURE_UNIT


def temp_conversor(input):
    if(TEMPERATURE_UNIT == "C"):
        return input
    else:
        return (input*1.8) + 32

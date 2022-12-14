from battery_manager import battery_is_ok

# Main method
if __name__ == '__main__':

    assert(battery_is_ok(123, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is True)

from check_module import batery_test

# Main method
if __name__ == '__main__':

    assert(batery_test(25, 70, 0.7)) == (True, True, True)
    assert(batery_test(50, 85, 0)) == (True, True, True)

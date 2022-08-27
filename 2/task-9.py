# regex validate PIN code
def validate_pin(pin):
    if pin.isdigit() == False:
        return False
    elif len(pin) == 6 or len(pin) == 4:
        return True
    else:
        return False
print(validate_pin(1234.0))

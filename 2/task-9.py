# regex validate PIN code
def validate_pin(pin):
    if pin.isdigit() == True and (len(pin) == 6 or len(pin) == 4):
        return True
    else:
        return False

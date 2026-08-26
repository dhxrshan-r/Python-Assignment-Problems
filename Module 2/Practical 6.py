def fahrenheit_to_celsius(temp):
    return (temp - 32) * (5 / 9)

def is_nice_outside(temperature, in_fahrenheit, is_raining):
    if in_fahrenheit:
        temperature = fahrenheit_to_celsius(temperature)
    return (not is_raining) and ((temperature > 4) and (temperature < 35))
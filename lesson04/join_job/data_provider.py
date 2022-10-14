from random import randint

def get_temperature(sensor):
    return randint(-20, 0) if sensor else randint(0, 20)

def get_preassure(sensor):
    return randint(720, 750) if sensor else randint(750, 770)

def  get_wind_speed(sensor):
    return randint(0, 30) if sensor else randint(30, 50)

def data_collection(sensor = 1):
    return (get_temperature(sensor), get_preassure(sensor), get_wind_speed(sensor))
import unittest
def main_function(**keywords):
    time = keywords['time']
    speed = keywords['speed']
    weight = keywords['weight']


    if time < 0:
        raise ValueError('Write something > 0')
    if speed < 0:
        raise ValueError('Write something > 0')
    if weight < 0:
        raise ValueError('Write something > 0')



    print(f'A vehicle weighing {weight} kg moved for {time} seconds at a speed of {speed} m/s and covered a distance of {time*speed} meters')
main_function(speed = 3, time = 10, weight = 1000)

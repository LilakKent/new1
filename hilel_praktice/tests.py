from hilel_praktice.dz13 import main_function

def test():
    dict = main_function(speed=3, time=21, weight=78)
    assert dict['speed'] >= 0
    assert dict['time'] >= 0
    assert dict['weight'] >= 0


main_function
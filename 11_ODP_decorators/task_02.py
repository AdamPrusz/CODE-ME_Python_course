# Utwórz dekorator @timepassed mierzący czas działania dowolnej funkcji.

import time

def timepassed(func):
    pass

    def example_function():
        print('Start')
        time.sleep(5)
        print('Koniec')

    return example_function()



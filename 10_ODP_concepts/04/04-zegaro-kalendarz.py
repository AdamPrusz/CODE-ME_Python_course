# 4▹ Utwórz klasę zegaro-kalendarza. Zegaro-kalendarza łączy cechy zegara oraz kalendarza.
# Zaimplementuj dziedziczenie wielokrotne. Nasz zegaro-kalendarz powinen móc podawać aktualną datę oraz
# wyświetlać ile dni ma dany miesiąc. Dodatkowo utwórz sposób wyświetlania tak, aby zegaro-kalendarz zawierał
# datę, godzinę oraz widok dni ułożonych tygodniowo. Dla uproszczenia przyjmij 7 dni w tygodniu zawsze zaczyna
# się od pierwszego dnia.
#
# Utwórz obiekty, które będą przekazywać różne strefy czasowe i wyświetlać dzięki temu inne czasy zegara

from datetime import date, datetime
from calendar import monthrange
import calendar

class Clock:
    def __init__(self):
        self.time = datetime.now()
        self.day = date.today()
        current_time = self.time.strftime("%H:%M:%S")
        print("Current Time is", current_time)


class Calendar:
    def current_date(self):
        print("Today's date is", self.day)

    def print_days(self):
        print("Current month has got", monthrange(self.day.year, self.day.month)[1], "days")
        print(calendar.month(self.day.year, self.day.month))


class Clock_calendar(Clock, Calendar):
    def __init__(self):
        super().__init__()
        print('************')
        super().current_date()
        print('************')
        super().print_days()

if __name__ == '__main__':
    element_1 = Clock_calendar()





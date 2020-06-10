import pytest
from datetime import datetime

class CalendarModule():
    def check_day(self, str_day):
        weekday = datetime.strptime(str_day, '%m %d %Y').weekday()
        print(f'{weekday}')
        return self.get_week_day(weekday)

    @staticmethod
    def get_week_day(number):
        return {
            6:'SUNDAY',
            0:'MONDAY',
            1:'TUESDAY',
            2:'WEDNESDAY',
            3:'THURSDAY',
            4:'FRIDAY',
            5:'SATURDAY',
        }[number]

class TestCalendar:
    def test_input_hackerrank(self):
        cm = CalendarModule()
        assert 'WEDNESDAY' == cm.check_day('08 05 2015')

        assert 'SUNDAY' == cm.check_day('02 29 2004')
    
    def test_get_week_day(self):
        assert 'WEDNESDAY' == CalendarModule().get_week_day(2)
        assert 'SUNDAY' == CalendarModule().get_week_day(6)
        assert 'MONDAY' == CalendarModule().get_week_day(0)

if __name__ == '__main__':
    date_input = input()
    c = CalendarModule()
    weekday = c.check_day(date_input)
    print(weekday)

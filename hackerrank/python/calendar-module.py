import pytest
from datetime import datetime

class CalendarModule():
    def check_day(self, str_day):
        weekday = datetime.strptime(str_day, '%d %m %Y').weekday()
        return self.get_week_day(weekday)

    @staticmethod
    def get_week_day(number):
        return {
            1:'SUNDAY',
            2:'MONDAY',
            3:'TUESDAY',
            4:'WEDNESDAY',
            5:'THURSDAY',
            6:'FRIDAY',
            7:'SATURDAY',
        }[number]

class TestCalendar:
    def test_input_hackerrank(self):
        cm = CalendarModule()
        assert 'WEDNESDAY' == cm.check_day('08 05 2015')
    
    def test_get_week_day(self):
        assert 'WEDNESDAY' == CalendarModule().get_week_day(4)
        assert 'SUNDAY' == CalendarModule().get_week_day(1)
        assert 'MONDAY' == CalendarModule().get_week_day(2)
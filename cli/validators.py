from PyInquirer import (ValidationError, Validator)
import re


class StockValidator(Validator):
    pattern = r'[A-Za-z][\S]*'

    def validate(self, stock):
        if len(stock.text):
            if re.match(self.pattern, stock.text):
                return True
            else:
                raise ValidationError(
                    message="Invalid Stock Symbol",
                    cursor_position=len(stock.text))
        else:
            raise ValidationError(
                message="You can't leave this blank",
                cursor_position=len(stock.text))


class EmptyValidator(Validator):
    def validate(self, value):
        if len(value.text):
            return True
        else:
            raise ValidationError(
                message="You can't leave this blank",
                cursor_position=len(value.text))


class DateValidator(Validator):
    pattern = r'[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}'

    def validate(self, date):
        if len(date.text):
            if re.match(self.pattern, date.text):
                return True
            else:
                raise ValidationError(
                    message="Invalid Date",
                    cursor_position=len(date.text))
        else:
            raise ValidationError(
                message="You can't leave this blank",
                cursor_position=len(date.text))

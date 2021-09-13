import sys
import click
from pyfiglet import figlet_format

from cli.CapmParameters import CAPMParameters
from .tools import *
from .capm import calculate_capm_values
from .validators import StockValidator, DateValidator
from PyInquirer import (Token, prompt, style_from_dict, print_json)

style = style_from_dict({
    Token.QuestionMark: '#fac731 bold',
    Token.Answer: '#4688f1 bold',
    Token.Instruction: '',  # default
    Token.Separator: '#cc5454',
    Token.Selected: '#0abf5b',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Question: '',
})


def ask_stock_symbol():
    return [
        {
            'type': 'list',
            'name': 'stock_symbol',
            'message': 'Stock Symbol:',
            'choices': ['TSLA', 'F', 'EXPE', 'BKNG', 'MSFT', 'custom']
        }
    ]


def ask_custom_symbol():
    return [
        {
            'type': 'input',
            'name': 'stock_symbol',
            'message': 'Stock Symbol',
            'default': "GOOGL",
            'validate': StockValidator
        }
    ]


def ask_custom_date():
    return [
        {
            'type': 'input',
            'name': 'start_date',
            'message': 'Start Date dd-mm-yyyy',
            'validator': DateValidator
        },
        {
            'type': 'input',
            'name': 'end_date',
            'message': 'End Date dd-mm-yyyy',
        }
    ]


def ask_custom_index():
    return [
        {
            'type': 'input',
            'name': 'index',
            'message': 'Index',
        }
    ]


@click.command()
def main():
    click.echo(click.style(figlet_format("Finance Tools"), fg='green'))
    click.echo(click.style("By team 23", fg='blue'))

    dates = [[2016, 8, 1], [2021, 9, 1]]
    if not click.confirm('Continue with default (2016 - 2021) date range?'):
        date_res = prompt(ask_custom_date(), style=style)
        print_json(date_res)
        start = (date_res.get("start_date")).split("-").reverse()
        end = (date_res.get("end_date")).split("-").reverse()
        dates[0] = start
        dates[1] = end

    index = "^GSPC"
    if not click.confirm("use S&P 500 as index?"):
        click.echo("choosing another index")
        index = prompt(ask_custom_index(), style=style).get("index")

    stock_ticker = prompt(ask_stock_symbol(), style=style)

    if stock_ticker['stock_symbol'] == "custom":
        stock_ticker = prompt(ask_custom_symbol(), style=style)

    start_date = datetime.datetime(*dates[0])
    end_date = datetime.datetime(*dates[1])
    params = CAPMParameters(start_date, end_date, 'm', stock_ticker.get("stock_symbol"), index)
    click.echo("\n")
    click.echo(calculate_capm_values(params.to_dict()))


if __name__ == '__main__':
    main()

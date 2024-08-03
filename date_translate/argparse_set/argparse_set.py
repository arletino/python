import argparse
from logging_set import logging_set


logger = logging_set.get_logger(__name__)
DESCRIPTION='Convert date from "3-я среда мая" to DD-MM-YY formate'
DATE_HELP='Input date in format "3-я среда мая"'
YEAR_HELP='Setup year for convert date'

def checker_date(text_date: list[str]) -> bool: 
    '''Check format input date'''
    if  not (1 < len(text_date) < 4):
        try:
            raise argparse.ArgumentTypeError()
        except argparse.ArgumentTypeError:
            msg = f'Input date wrong format {' '.join(text_date)}'
            logger.warning(msg)
            return False
    return True

def checker_year(year):
    '''Check type input year'''
    try:
        year = int(year)
    except ValueError as e:
        msg = f'Input year wrong format {year}'
        logger.warning(msg)
    return year

def get_argparse():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument( # Required parameter 'date'
        'date',  
        help=DATE_HELP, 
        nargs='*'
        )
    parser.add_argument( # Optional parameter 'year'
            '-y',
            '--year', 
            type=checker_year,
            default=None, 
            nargs='?',
            help=YEAR_HELP
            )
    args = parser.parse_args()
    if checker_date(args.date):
        msg='Parsing arguments is done'
        logger.info(msg)
        return args.date, args.year
    else:
        msg = f'Input args is wrong {args}'
        print(parser.parse_args(['-h']))
        parser.error()

from datetime import datetime, MINYEAR, MAXYEAR
from logging_set import logging_set



WEEK = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
YEAR = 2024
FORMAT = '%d-%m-%Y'

logger = logging_set.get_logger(__name__)

def is_leap(year: int) -> bool:
    return bool(not year % 4 and year % 100 or not year % 400)

def months(year: str=YEAR) -> str:
    return (('янв', 31), ('фев', 29 if is_leap(year) else 28), ('мар', 31),
            ('апр', 30), ('мая', 31), ('июн', 30), ('июл', 31), ('авг', 31),
            ('сен', 30), ('окт', 31), ('ноя', 30), ('дек', 31))

def check_day(week: str) -> int:
    if not (week[0].isdigit() and 0 < int(week[0]) < 6):
        msg = f'Day is not number, less 0 or more 7 - {week[0]}'
        logger.exception(msg)
        raise ValueError
    return int(week[0])

def check_weekday(weekday: str) -> str:
    if weekday not in WEEK:
        msg = f'Weekday is wrong {weekday}'
        logger.exception(msg)
        raise ValueError
    return weekday
    
def check_year(year: str) -> int:
    try:
        year = int(year)
    except ValueError:
        msg = f'Year is not a number {year}'
        logger.exception(msg)
        raise ValueError
    if  not (MINYEAR <= year <= MAXYEAR):
        msg = f'Year is too big or too small {year}'
        logger.exception(msg)
        raise ValueError
    return year

def parse_date(date_txt: list[str]) -> str:
    match date_txt:
        case week, weekday:
            week, weekday = date_txt
            month = months()[datetime.now().month - 1][0]
        case week, weekday, month:
            week, weekday, month = date_txt
        case _:
            try:
                raise ValueError
            except ValueError:
                msg = f'Too mach parameters {_}'
                logger.exception(msg)
                raise ValueError
    week = check_day(week)
    weekday = check_weekday(weekday) 
    for month_num, m in enumerate(months(), 1):
        if month[:3] == m[0]:
            return week, weekday, month_num
    msg = f'Weekday is wrong {weekday}'
    logger.exception(msg)
    raise ValueError

def get_iso_date(text_date, year=None):
    '''Convert date to iso format
    >>> get_iso_date(['4-я', 'воскресенье', 'июля'])
    28-07-2024

    >>> get_iso_date(['4-я', 'воскресенье'])
    28-07-2024 

    >>> get_iso_date(['4-я', 'воскресенье', ''2023'])
    23-07-2023
    '''
    week, weekday, month = parse_date(text_date)
    if year is None:
        year = datetime.now().year
    else:
        year = check_year(year)
    first_day_of_month = datetime.strptime(f'01.{month}.{year}', '%d.%m.%Y').weekday()
    current_week = WEEK[first_day_of_month:] + WEEK[:first_day_of_month]
    day = None
    for i in range(months(year)[month - 1][1]):
        if weekday == current_week[i % 7]:
            week -= 1
            if not week:
                day = i + 1
                break
    return str(datetime.strptime(f'{day}.{month}.{year}', '%d.%m.%Y').date().strftime(FORMAT))


from logging_set import logging_set
from argparse_set import argparse_set
from src import convert_date


logger = logging_set.get_logger(__name__)

def main():
    args = argparse_set.get_argparse()
    text_date, year = args
    logger.info(args)
    str_date = convert_date.get_iso_date(text_date, year)
    logger.info(f'Date converted successfully {str_date}')

if __name__ == "__main__":
    main()

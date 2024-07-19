import logging

FORMAT =  (
    '[{color}] ;'
    '{levelname:<8} - {asctime}.; '
    'module: "{name}"; ' 
    'line: {lineno:03d}; '
    'function "{funcName}"; '
    'at {created}; '
    'message: {msg}')

LOG_FILE = './log.txt'
FILEMODE = 'a'
ENCODING = 'utf-8'
STYLE = '{'


class CustomFilter(logging.Filter):

    COLOR = {
            "DEBUG": "GREEN",
            "INFO": "GREEN",
            "WARNING": "YELLOW",
            "ERROR": "RED",
            "CRITICAL": "RED",
        }
    
    def filter(self, record):
        record.color = CustomFilter.COLOR[record.levelname]
        return True



def get_file_handler():
    file_handler = logging.FileHandler(filename=LOG_FILE, mode=FILEMODE, encoding=ENCODING)
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter(FORMAT, style=STYLE))
    return file_handler

def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(FORMAT, style=STYLE))
    return stream_handler

def get_logger(name):
    logger = logging.getLogger(name)
    logger.addFilter(CustomFilter())
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger
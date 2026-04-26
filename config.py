import logging
from logging.handlers import RotatingFileHandler

LOG_FILE_NAME = "bot.log"
PORT = '8080'
OWNER_ID = 7560349494
MSG_EFFECT = 5046509860389126442

# AROLink URL Shortener Configuration
AROLINK_API_TOKEN = "4134296f6ba51789996b73ae880bf798671b6d9b"
AROLINK_API_URL = "https://arolink.com/api"

# URL Shortener Providers Configuration
URL_SHORTENERS = {
    'arolink': {
        'name': 'Arolink',
        'api_url': 'https://arolink.com/api',
        'api_token': AROLINK_API_TOKEN,
        'format': 'text',
        'active': True
    }
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger

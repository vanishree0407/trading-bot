import logging
import os

def setup_logger():
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, "app.log")

    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)
    
    # Avoid adding duplicate handlers if the logger is imported multiple times
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR) # Only log errors to console by default

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

logger = setup_logger()

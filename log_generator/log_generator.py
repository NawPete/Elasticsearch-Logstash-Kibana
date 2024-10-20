import time
import logging
import random
import socket

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

log_types = ["INFO", "ERROR", "WARNING", "DEBUG"]
host_name = socket.gethostname()

while True:
    log_type = random.choice(log_types)
    message = f"Log from {host_name} - Type: {log_type}"
    if log_type == "INFO":
        logger.info(message)
    elif log_type == "ERROR":
        logger.error(message)
    elif log_type == "WARNING":
        logger.warning(message)
    elif log_type == "DEBUG":
        logger.debug(message)
    time.sleep(5)

import os
import logging  #ready made package, to maintain the logs
from datetime import datetime

# Define the log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory path where logs will be stored
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)

# Create the logs directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# include the timestamp, line number, log level, and the message itself.
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d - %(levelname)s - %(message)s"
)
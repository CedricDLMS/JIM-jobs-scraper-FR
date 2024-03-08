import os
import datetime as dt
import logging
from pathlib import Path
import sys

def create_db_dir():
    """
    Creates database directory for scraped jobs.
    """
    job_dir = "job_db"
    if not os.path.exists(job_dir):
        os.mkdir(job_dir)
        print('Job database directory created successfully.')

def create_log_dir():
    """
    Sets up logging file for the scraper.
    """
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
        print('Job database directory created successfully.')
    LOGGING_DIR = f'./logs/job-scraping-{dt.datetime.today().strftime("%Y%m%d")}.log'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)-8s %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(Path(LOGGING_DIR)),
        ]
    )
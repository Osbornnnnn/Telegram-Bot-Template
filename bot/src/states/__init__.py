import datetime
from telegram.ext import JobQueue
from .. import config

def setup(job_queue: JobQueue):
    # example_func_time - время когда будет выполнятся функция (читайте документацию).
    # example_func - функция которая будет выполнятся.
    # ------------------------------------------------------
    # example_func_time = datetime.time(hour=9, tzinfo=config.TIMEZONE)
    # job_queue.run_daily(example_func, example_func_time)
    pass

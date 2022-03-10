from functools import wraps
from time import sleep


def try_to_run(attempts=1, delay=0, exceptions=(Exception,)):
    def wrapper(original):
        @wraps(original)
        def retry(*args, **kwargs):
            n_tries = 0
            while n_tries < attempts:
                try:
                    value = original(*args, **kwargs)
                    return value
                except exceptions:
                    n_tries += 1
                    print(
                        f"Trying again after {delay} secs. "
                        f"Number of attempts left {attempts - n_tries}"
                    )
                    sleep(delay)
                    if n_tries == attempts:
                        raise

        return retry

    return wrapper

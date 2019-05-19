import time

from Lesson12.exceptions import TestErrorException


class Waiter:

    @staticmethod
    def wait(waiter, max_time, delay=1):
        cur_time = 0
        while cur_time < max_time:
            if waiter() is True:
                return

            cur_time = cur_time + delay
            time.sleep(delay)

        raise TestErrorException("Cant more wait.")
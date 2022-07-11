import os
import time


def print_ts(message):
    print("[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), message))


def run(interval, command):
    print_ts("-"*100)
    print_ts("Command %s" % command)
    print_ts("Starting every %s seconds." % interval)
    print_ts("-"*100)
    while True:
        try:
            # execute the command
            print_ts("Starting command.")
            status = os.system(command)
            print_ts("-" * 100)
            print_ts("Command status = %s." % status)

            # sleep for the remaining seconds of interval
            time_remaining = interval - time.time() % interval
            print_ts("Sleeping until %s (%s seconds)..." % ((time.ctime(time.time() + time_remaining)), time_remaining))
            time.sleep(time_remaining)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    _interval = 60 * 60
    _command = r"python login.py"
    run(_interval, _command)

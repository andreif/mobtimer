import argparse
import os
from datetime import timedelta

OS = os.uname()[0]


def run():
    parser = argparse.ArgumentParser(description='A simple timer for mob programming.')
    parser.add_argument('minutes', type=int, nargs='?', default=20,
                        help='Duration of each mob in minutes. Default: 20')

    args = parser.parse_args()

    if OS == 'Darwin':
        from .macos import App
        App.duration = timedelta(minutes=args.minutes)
        App.run()
    else:
        raise NotImplementedError(OS)

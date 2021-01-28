#!/usr/bin/env python3

import click
import time

@click.command()
@click.option('-p', '--pomodoros', default=4, help='Number of pomodoros.')
# @click.option('-l', '--length', default=5, help='Pomodoro\'s length.')
@click.option('-s', '--short-break', default=5, help='Short break.')
@click.option('-l', '--long-break', default=15, help='Long break.')
def main(pomodoros, short_break, long_break):
    """Simple program for Pomodoro Technique."""
    length = 5
    with click.progressbar(range(length*2),
                        label='Modifying user accounts') as bar:
        for menute in bar:
            time.sleep(1)
    

if __name__ == '__main__':
    main()

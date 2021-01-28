#!/usr/bin/env python3

import click
import time

@click.command()
@click.option('-p', '--pomodoros', default=4, help='Number of pomodoros.')
@click.option('-s', '--short-break', default=2, help='Short break.')
@click.option('-l', '--long-break', default=5, help='Long break.')
@click.option('--pomodoros_length', default=3, help='Pomodoro\'s length.')
def main(pomodoros, short_break, long_break, pomodoros_length):
    """Simple program for Pomodoro Technique."""
    for pomo in range(1, pomodoros+1):
        pomodoros_length = pomodoros_length * 1
        progressbar_label = f'Pomodoro {pomo}'
        pomodoro_timer(pomodoros_length, progressbar_label)

                
def pomodoro_timer(pomodoros_length, progressbar_label):
    with click.progressbar(range(pomodoros_length),
                            label=progressbar_label) as bar:
            for menute in bar:
                time.sleep(1)

if __name__ == '__main__':
    main()

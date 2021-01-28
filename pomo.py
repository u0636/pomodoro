#!/usr/bin/env python3

import click
import time

@click.command()
@click.option('-p', '--pomodoros', default=4, help='Number of pomodoros.')
@click.option('-s', '--short-break', default=5, help='Short break.')
@click.option('-l', '--long-break', default=15, help='Long break.')
@click.option('--pomodoros_length', default=25, help='Pomodoro\'s length.')
def main(pomodoros, short_break, long_break, pomodoros_length):
    """Tiny tool for Pomodoro Technique."""
    for pomo in range(1, pomodoros+1):
        length = pomodoros_length
        progressbar_label = f'Pomodoro {pomo}\t'
        progressbar_color = 'bright_red'
        pomodoro_timer(length, progressbar_label, progressbar_color)
        if pomo == pomodoros:
            length = long_break
            progressbar_label = 'Long break\t'
            progressbar_color = 'bright_green'
            pomodoro_timer(length, progressbar_label, progressbar_color)
        else:
            length = short_break
            progressbar_label = 'Short break\t'
            progressbar_color = 'bright_blue'
            pomodoro_timer(length, progressbar_label, progressbar_color)

def pomodoro_timer(length, progressbar_label, progressbar_color):
    length = length * 60
    fill_char = click.style('#', fg=progressbar_color)
    empty_char = click.style('-', fg='white')
    with click.progressbar(range(length),
                            label=progressbar_label,
                            fill_char=fill_char,
                            empty_char=empty_char) as bar:
            for menute in bar:
                time.sleep(1)

if __name__ == '__main__':
    main()

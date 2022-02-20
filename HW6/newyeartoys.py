import random
import click
from enum import IntEnum


@click.group()
def cli():
    pass


class Colors(IntEnum):
    Red = 1
    Orange = 2
    Yellow = 3
    Green = 4
    Blue = 5
    Purple = 6


class Toys(IntEnum):
    angel = 1
    elk = 2
    boot = 3
    balloon = 4
    garland = 5


@click.command()
@click.option('--toys')
def toys(toys):
    colors = (1, 2, 3, 4, 5, 6)
    toys = (1, 2, 3, 4, 5)
    a = random.choice(toys)
    b = random.choice(colors)
    res = str("Random christmas toys - " + Colors(b).name + " " + Toys(a).name)
    # click.echo(Toys(a).name)
    click.echo(res)


cli.add_command(toys)

if __name__ == '__main__':
    cli()

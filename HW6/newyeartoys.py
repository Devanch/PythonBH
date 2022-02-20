import random
import click
from enum import IntEnum, unique


@click.group()
def cli():
    pass


@unique
class Colors(IntEnum):
    Red = 1
    Orange = 2
    Yellow = 3
    Green = 4
    Blue = 5
    Purple = 6

@unique
class Toys(IntEnum):
    angel = 1
    elk = 2
    boot = 3
    balloon = 4
    garland = 5


@click.command()
@click.option('--toys')
def toys(toys):
    rundom_toy = random.choice(list(Toys))
    rundom_color = random.choice(list(Colors))
    res = str("Random christmas toys - " + Colors(rundom_color).name + " " + Toys(rundom_toy).name)
    # click.echo(Toys(a).name)
    click.echo(res)


cli.add_command(toys)


if __name__ == '__main__':
    cli()

import random
import click


@click.group()
def cli():
    pass


@click.command()
@click.option('--toys')
def toys(toys):
    colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple')
    toys = ('angel', 'elk', 'boot', 'balloon', 'garland')
    res = "Random christmas toys - " + random.choice(colors) + " " + random.choice(toys)
    click.echo(res)


cli.add_command(toys)

if __name__ == '__main__':
    cli()

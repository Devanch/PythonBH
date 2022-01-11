import click
import datetime

@click.group()
def cli():
    pass

@click.command()
@click.option('--hourss', default = '1', help='--hourse')
def newyear(hourss):
    # date1 = datetime.datetime(2023,1,1)
    # date2 = datetime.datetime.today()
    # delta = date1 - date2 if date1 > date2 else date2 - date1
    if hourss == 1:
        date1 = datetime.datetime(2023,1,1)
        date2 = datetime.datetime.today()
        delta3 = date1 - date2 if date1 > date2 else date2 - date1
        click.echo(delta3)
    else: 
        date1 = datetime.datetime(2023,1,1)
        date2 = datetime.datetime.today()
        delta = date1 - date2 if date1 > date2 else date2 - date1
        click.echo(delta.microseconds)
    
# click.echo
cli.add_command(newyear)

if __name__ == '__main__':
    cli()



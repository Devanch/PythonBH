import click
import datetime

@click.group()
def cli():
    pass

@click.command()
@click.option('--hourss', help='--hourse')
def newyear(hourss):
    date1 = datetime.datetime(2023,1,1)
    date2 = datetime.datetime.today()
    delta = date1 - date2 if date1 > date2 else date2 - date1
    if hourss == '1':
        dy = delta.days
        hr = delta.seconds//3600 
        click.echo(str(dy) + ' days, ' + str(hr)+ ' hours')
    else: 
        click.echo(str(delta.days) + ' days')
    
# click.echo
cli.add_command(newyear)

if __name__ == '__main__':
    cli()


    # date1 = datetime.datetime(2023,1,1)
    # date2 = datetime.datetime.today()
    # delta = date1 - date2 if date1 > date2 else date2 - date1
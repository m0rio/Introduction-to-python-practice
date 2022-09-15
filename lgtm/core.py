from ast import keyword
from email import message
from email.policy import default
import click
from lgtm.drawer import save_with_message
from lgtm.image_source import get_image

@click.option('--message', '-m', default='LGTM',show_default=True, help='画像に乗せる文字列')
@click.argument('keyword')
def cli():
    """LGTM画像生成ツール"""
    lgtm(keyword, message)
    click.echo('lgtm')

def lgtm(keyword, message):
    with get_image(keyword) as fp:
        save_with_message(fp, message)

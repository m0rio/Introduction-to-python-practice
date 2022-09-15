from io import BytesIO
from pathlib import Path
import re
import requests

class LocalImage:
    """ファイルから画像取得"""

    def __init___(self, path):
        self._path = path

    def get_image(self):
        return open(self._path, 'rb')

class RemoteImage:
    """URLから画像を取得する"""

    def __init__(self, path):
        self._url = path

    def get_image(self):
        data = requests.get(self._url)
        #requests.get()で取得できるのはバイトデータなので、ファイルオブジェクトに変換する
        return BytesIO(data.content)

class _LoremFicker(RemoteImage):
    """キーワードで画像検索する"""

    LOREM_FLICER_URL = 'https://loremflickr.com'
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, keyword):
        super().__init__(self._build_url(keyword))

    def _build_url(self, keyword):
        return (f'{self.LOREM_FLICER_URL}/{self.WIDTH}/{self.HEIGHT}/{keyword}')

KeywordImage = _LoremFicker

def imageSource(keyword):
    """最適なイメージソースクラスを返す"""
    keyword = str(keyword)
    if keyword.startswith(('http://', 'https://')):
        return RemoteImage(keyword)
    elif Path(keyword).exists():
        return LocalImage(keyword)
    else:
        return KeywordImage(keyword)

def get_image(keyword):
    """画像のファイルオブジェクトを返す"""
    return imageSource(keyword).get_image()
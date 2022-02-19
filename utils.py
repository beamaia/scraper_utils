from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

import re

def get_html_doc(url: str) -> str:
    return urlopen(url).read()

def remove_tags(string: str) -> str:
        TAG_RE = re.compile(r"<[^>]+>")
        return TAG_RE.sub("", str(string))

def download_csv(file_url:str, file_path:str) -> None:
    req = requests.get(file_url)
    url_content = req.content
    
    csv_file = open(file_path, 'wb')
    csv_file.write(url_content)
    csv_file.close()
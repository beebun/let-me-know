import sqlite3
import urllib
import requests

def run():
  series_name = ['prison break', 'silicon valley']
  for name in series_name:
    search_keyword = urllib.quote(name)
    r = requests.get('https://thepiratebay.org/search/' + search_keyword + '/0/99/0')
    print(r.text)

if __name__ == '__main__':
  run()
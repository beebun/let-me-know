import sqlite3
import urllib
import requests

def run():
  conn = sqlite3.connect('db')
  c = conn.cursor()
  c.execute("insert into series values(1,'Prison Break',5,'2017-05-21 21:11:00')")
  conn.commit()
  c.execute("SELECT * FROM series")
  print c.fetchone()
  series_name = ['prison break', 'silicon valley']
  for name in series_name:
    pass
    # search_keyword = urllib.quote(name)
    # r = requests.get('https://thepiratebay.org/search/' + search_keyword + '/0/99/0')
    # print(r.text)


if __name__ == '__main__':
  run()
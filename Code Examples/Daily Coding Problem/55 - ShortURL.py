'''
Implement a URL shortener with the following methods:

    shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
    restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?
'''


global db  # database of pairs of <short_url, url>. 
db = {}  # Here we use a dummy db. But in applications a connection to an actual db must be made

def int_to_string(cur_id):
  '''returns the current generated id to a 6-char string'''
  if cur_id > 62 ** 6:
    raise ValueError('No more 6-char strings left.')
  
  import string
  chars = string.digits + string.ascii_letters 
  short_url = ''
  
  while cur_id > 62:
    idx = cur_id // 62
    short_url += chars[idx]
    cur_id = idx
  short_url += chars[cur_id]
  
  rev_string = short_url[::-1]
  if len(rev_string) < 6:
    rev_string = '0' * (6 - len(rev_string)) + rev_string
  return rev_string

def shorten(url, cur_id):
  if url in db.values():
    return next( ( key for key in db if db[key] == url ) )
  short_url = int_to_string(cur_id)
  db[short_url] = url
  return short_url

def restore(short_url):
  return db.get(short_url)

cur_id = 1  # this must be retrived from a database
print(shorten('asd', cur_id))
print(shorten('asd', cur_id))
cur_id = 2
print(shorten('fghghj', cur_id))
print(restore('000002'))

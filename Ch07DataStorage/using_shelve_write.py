import shelve

with shelve.open('my_shelve.db') as db:
    db['isim']='Alice'
    db['yaş']='30'
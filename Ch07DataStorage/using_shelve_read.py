import shelve

with shelve.open('my_shelve.db') as db:
    print(db['isim'])
    print(db['yaş'])
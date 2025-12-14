import datetime as dt

def date_format(d):
    d = str(d).replace('-', '.')
    dd = d.split('.')
    this_date = dt.date(int(dd[0]), int(dd[1]), int(dd[2]))
    return this_date

print(date_format('2011.01.01'))
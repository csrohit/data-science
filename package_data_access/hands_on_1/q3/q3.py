import datetime
def func1(y,m,d,h,mi,se,ms):
    input_date = datetime.date(y,m,d)
    input_date1= datetime.datetime(y,m,d) + datetime.timedelta(microseconds=ms, seconds=se, minutes=mi, hours=h)
    t = input_date1 - datetime.timedelta(microseconds=1, seconds=2, days=3, minutes=2)
    day = t.day
    year = t.year
    month = t.month
    minute = t.minute
    second = t.second
    return input_date, input_date1, t, day, year, month, minute, second


def func2(y,m,d,h,mi,se,ms):
    s= datetime.datetime(y,m,d) + datetime.timedelta(microseconds=ms, seconds=se, minutes=mi, hours=h)
    x= s
    q= s.strftime("%a %b %d %H %M: %S %Y")
    z= datetime.datetime(year=y, month=m, day=d, hour=h, minute=mi, second=se)
    return x,q,z


if __name__ == '__main__':
    y,m,d,ms,se,da,mi = map(int, input().split())
    print(*func1(y,m,d,ms,se,da,mi), sep='\n')
    print(*func2(y,m,d,ms,se,da,mi), sep='\n')

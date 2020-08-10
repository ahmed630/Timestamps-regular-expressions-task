import re
timestap_regular_expression = r'^(\d{4})[\-/](\d{2})[\-/](\d{2})(?:T(\d{2}):(\d{2}):(\d{2})Z)?'


def print_date(timestamp):
    m = re.match(timestap_regular_expression, timestamp)
    print(f'Year:    {m[1]}')
    print(f'Month:   {m[2]}')
    print(f'Day:     {m[3]}')
    print(f'Hours:   {m[4]}')
    print(f'Minutes: {m[5]}')
    print(f'Seconds: {m[6]}')

def main():
    t1 = '2014/08/18'
    t2= '2014/08/18T13:03:25Z'
    print_date(t1)
    print('\n\n')
    print_date(t2)

if __name__=='__main__':
    main()
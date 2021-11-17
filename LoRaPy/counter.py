file_name = 'log_counter.txt'


def get_current():
    try:
        f = open(file_name, 'r')
        counter = f.read(-1)
        f.close()
        counter_int = int(counter)
    except IOError:
        counter_int = 1

    counter_new = counter_int + 1
    f = open(file_name, 'w+')
    f.write(str(counter_new))
    f.close()

    return counter_int


def set_next(i):
    f = open(file_name, 'w+')
    counter = i + 1
    f.write(str(counter))
    f.close()

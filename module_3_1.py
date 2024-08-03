calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    global calls
    count_calls()
    a = len(string)
    b = string.upper()
    c = string.lower()
    string = a, b, c
    return string
def is_contains(string, list_to_search):
    global calls
    count_calls()
    a = False
    b = string.upper()
    count = len(list_to_search)
    for i in range(count):
        c = list_to_search[i].upper()
        if b == c:
            a = True
    return a
print(string_info('Student'))
print(string_info('Anatolii'))
print(string_info('Karpov'))
print(is_contains('Student',['stud', 'StaRt', 'sTuDeNT']))
print(is_contains('Task',['trak', 'train']))
print(calls)

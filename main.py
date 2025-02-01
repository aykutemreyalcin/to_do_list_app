to_do_list = []

def add(event):
    to_do_list.append(event)

def remove(event):
    if event in to_do_list:
        to_do_list.remove(event)
    else:
        print(f'{event} is not in "to do list".')

def view():
    print(18*'_')
    print('|   To Do List   |')
    if len(to_do_list)>0:   
        for i in to_do_list:
            print(f'|● {i}' + (14-len(i))*' ' + '|')#18
    else:
        print('|Nothing         |')
    print(18*'¯')

while True:
    what = (input('what do you want\n1 --> add to list\n2 --> remove from list\n3 --> view the list\n4 --> exit\n'))
    if what == '1':
        event = input('what do you want to add?\n')
        add(event)
    elif what == '2':
        event = input('what do you want to remove?\n')
        remove(event)
    elif what == '3':
        view()
    elif what == '4':
        break
    else:
        print('wrong choice')

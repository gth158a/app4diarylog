import os
import journal

# load file
# if file does not existj, create it

# add entries to file

# save

#display entires

def print_hearder():
    print('-----------------------------')
    print('    PERSONAL JOURNAL APP')
    print('-----------------------------')
    print()

def list_entries(data):
    entries = reversed(data)

    for i,e in enumerate(entries):
        print('[{}] {}'.format(i+ 1, e))


def add_entries(entries):
    entry = input('type away ')
    entries.append(entry)

    return entries



def get_action():
    print('What would you like to do with your journal')
    cmd = None
    journal_name = 'default'
    entries = journal.load(journal_name)

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd or E[x]it? ')
        cmd.lower().strip()

        if cmd == 'l':
            print('Listing entries')
            list_entries(entries)
        elif cmd == 'a':
            print('Add entries')
            add_entries(entries)
        elif cmd != 'x':
            print('Sorry! We don\'t understand {}'.format(cmd))

    print('Done goodbye!')
    journal.save(journal_name, entries)


def main():
    print_hearder()
    get_action()



main()

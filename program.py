import os
import journal


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
    cmd = 'Empty'
    journal_name = 'default'
    entries = journal.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd or E[x]it? ')
        cmd.lower().strip()

        if cmd == 'l':
            print('Listing entries')
            list_entries(entries)
        elif cmd == 'a':
            print('Add entries')
            add_entries(entries)
        elif cmd != 'x' and cmd:
            print('Sorry! We don\'t understand {}'.format(cmd))

    print('Done goodbye!')
    journal.save(journal_name, entries)


def main():
    print_hearder()
    get_action()


#__name__
#__file__

if __name__ == '__main__':
    main()

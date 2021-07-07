def rem_to_newlines(f):
    fl = open(f).readlines()
    return [s.rstrip('\n') for s in fl]
print(remove_newlines("b.txt"))
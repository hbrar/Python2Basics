count = 0
while count < 4:
    resp = raw_input("Do you want to continue?")
    if resp in ('n','no','nay'):
        print 'Good Bye!'
        break
    if resp in ('y','yes','yeh'):
        count = count + 1
        if not(count == 4):
            print 'Attempt: ', count + 1
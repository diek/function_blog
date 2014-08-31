def demo_return(num):
    ''' test what happens when program execution reaches return
    '''
    if num < 10:
        return num + 5
    else:
        return num - 5

    print 'This will never print'

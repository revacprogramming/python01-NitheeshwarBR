x=list()
fx=list()
while True:
    try:
        print('Xi:')
        x=float(input())
        for i in x:
            x.append(i)
    except:
        
        while True:
            try:
                print('fi:')
                fx=float(input())
                for i in fx:
                    fx.append(i)
            except:
                break



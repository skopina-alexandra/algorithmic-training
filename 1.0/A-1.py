troom,tcond = map(int, input().split())
mode = input()

match mode:
    case "freeze":
        if troom <= tcond:
            print(troom)
        else:
            print(tcond)
    case "heat":
        if tcond <= troom:
            print(troom)
        else:
            print(tcond)
    case "fan":
        print (troom)
    case "auto":
        print (tcond)
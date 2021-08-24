b = (input("type your name "))
print ("hello " + (b))
x = int(0)
print ("\033[93mwhat do you want to know\033[0m")
while x == 0 :
    print (" ")
    print ("navne mitt = 1")
    print ("hobbiene mine = 2")
    print ("code språkene jeg kan = 3")
    print ("hvor gamel jeg er = 4")
    print ("ikke fler spørsmål = 5")

    a = int(input())

    if (a) == 1:
        print ("\033[93mjeg heter Mathias transeth\033[0m")
    elif a == 2:
        print ("\033[93mjeg liker dataspill, spille instrumenter.\033[0m")
        print ("\033[93mog jeg drivel lit med coding i fritien.\033[0m")
    elif a == 3:
        print("\033[93mjeg har brukt lua, python, a tiny bit of java and C# and php\033[0m")
    elif a == 4:
        print ("\033[93mjeg er 17 år\033[0m")
    elif a == 5:
        print ("\033[93mgood bye\033[0m")
        x = 1

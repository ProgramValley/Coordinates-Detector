import pyautogui

def manual():

    print("\nCoordinates Detector v 1.25\nCopyright(c) 2018 Program Valley\n\nEnter number of slots you will need\n"
          "Type :new: for new slot\nHold :ctrl+c for stop detecting")
    print("For correct save enter it like : X 411 Y 545 RGB 12, 12 ,12 :\nIn :start>>>: type :delete: for delet all saves\n ")

manual()
save = 10
overwrite = input("overwrite old saves ? Y/N >>>")
print("OK")
slot = 1
empty = 1
start = "start"
end = "end"
manuael = "manual"
openn = "open"




if overwrite.lower() == "y" :
    file = open("slots.txt" , "w")
    file.write("")
    file.close()


if start == "start":
    while empty <= save:
        prikaz = input("start >>>")

        if prikaz.lower() == "new":

            print(pyautogui.displayMousePosition())
            xcords = input("save X cords >>>")
            ycords = input("save Y cords >>>")
            file = open("slots.txt", "a")
            file.write("\n" + str(slot) + "-" + "X: " + xcords + " Y: " + ycords)
            file.close()
            empty = empty + 1
            slot = slot + 1

        if prikaz.lower() ==("open"):
            filee = open("slots.txt", "r" )
            print(filee.read()+"\n")
            filee.close()

        if prikaz.lower() ==("delete"):
            filee = open("slots.txt", "w")
            filee.write("")
            filee.close()
            print("OK")

konec = input("end ? YES/NO >>>")
if konec.lower() == "yes":
    print("OK")



while konec.lower() == "no":
    save = 10
    overwrite = "no"
    print("OK")
    empty = 1
    start = "start"

    if overwrite.lower() == "yes":
        file = open("slots.txt", "w")
        file.write("")
        file.close()

    if start == "start":
        while empty <= save:
            prikaz = input("start >>>").lower()

            if prikaz.lower() == ("new"):

                print(pyautogui.displayMousePosition())
                xcords = input("save X cords >>>")
                ycords = input("save Y cords >>>")
                file = open("slots.txt", "a")
                file.write("\n" + str(slot) + "-" + "X: " + xcords + " Y: " + ycords)
                file.close()
                empty = empty + 1
                slot = slot + 1

            if prikaz.lower() == ("open"):
                filee = open("slots.txt", "r" )
                print(filee.read()+"\n")
                filee.close()

            if prikaz.lower() == ("delete"):
                filee = open("slots.txt", "w")
                filee.write("")
                filee.close()
                print("OK")


    konec = input("end ? YES/NO >>>")
    if konec.lower() == "yes" or "end":
        print("OK")
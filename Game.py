import time

## Something To note here is that "loader" just means table. When I was making this I decided to make it loader. Dont know why, Just did

class BoardGame:
    def __init__(self, loader):
        self.loader = loader

    ## !This is just the old version of the makeloader()!     
    ## Didn't wanna keep making ugly tables so I made this function. the x is well... the X and same with the y. The name is just the name of the table
    ##def maketable(self, x, y, name):
    ##    table = []
    ##    for i in range(1, x*y):
    ##      if i == 1:
    ##        table.append(name)
    ##      else:
    ##        table.append("0-0")
    ##    return table

    ## Sets the self.loader (loader is just the table) 
    def loadloader(self, loader):
        self.loader = loader

    ## Todo: Work on this. Make It a main feature
    def loadfromfile(self, filename):
        table = ""
        try:
            with open(filename, "r+") as file:
                for line in file.readlines():
                    table = table + line
                self.loader = eval("[" + table + "]")
            return True
        except:
            print("File Name Is Incorrect Or Code Error On Our Side")
            return False
            time.sleep(1)

    ## Pretty self explanitory. sets the selected X and Y. The setto is just what you want the place to be set too
    def setxy(self, x, y, table, setto):
        if ((y-1) * self.exit + x ) % self.exit == 0:
            setto += "-\n"
            table[(y-1) * self.exit + x] = setto
        else:
            table[(y-1) * self.exit + x] = setto
        self.loader = table

    ## makes a table string i.e. maketablestring("1", "9", true) -> "1-9-\n". If you couldn't tell, addnewline just adds "-\n" to the end
    def maketablestring(self, item, health, addnewline):
        if addnewline:
            return item + "-" + health + "-\n"
        return item + "-" + health

    ## Prints the name (Yet again doesn't have to be the name. Could be whatever)
    def printloadertablename(self, loader):
        ## Name is index 0
        printstring = ""
        v = 0
        for x in loader:
            if v == 0:
                print(loader[0])
            else:
                g = x.split("-")
                if len(g) == 3:
                    g[0] = g[0] + g[2]
                printstring = printstring + g[0]
            v += 1
            
        print(printstring)

    ## Prints the health (Doesn't Really have to be health. Could be what ever you want it to)
    def printloadertablehealth(self, loader):
        printstring = ""
        v = 0
        for x in loader:
            if v == 0:
                print(loader[0])
            else:
                g = x.split("-")
                if len(g) == 3:
                    g[1] = g[1] + g[2]
                printstring = printstring + g[1]
            v += 1

        print(printstring)

    ## Prints the entire String i.e. "1-1" or "Name-Health"
    def entireprintloadertable(self, loader):
        ## Name is index 0
        printstring = ""
        v = 0
        for x in loader:
            if v == 0:
                print(loader[0])
            else:
                printstring = printstring + x + " "
            v += 1
            
        print(printstring)

    ## Basically returns the loader (loader is just the table)
    def getloadertable(self):
        return self.loader

    ## Didn't wanna keep making ugly tables so I made this function. the x is well... the X and same with the y. table should just be ["insert name of table here"] and thats it, Anything else and this code straight up brakes
    def makeloader(self, table, exit):
        self.exit = exit
        for i in range(0, len(table)):
            if i % exit == 0 and not i == 0:
                table[i] = table[i] + "-\n"
        return table
    
    ## Exit is just how long each printed line is
    def setexit(self, exit):
        self.exit = exit

    ## Exit is just how long each printed line is
    def getexit(self):
        return self.exit

    ## Basically, Just give it the x, y and table and it finds the respective item. (Name not included)
    def getxy(self, x, y, table):
        try:
            return table[(y-1) * self.exit + x]
        except:
            return "notpog"

    ## Todo: Make This thing better 
    def save(self, filename):
        try:
            with open(filename, "x") as file:
                file.write(str(self.loader).split("[")[1].split("]")[0])
        except:
            with open(filename, "r+") as file:
                for line in file.readlines():
                    line = ""
                
                file.write(str(self.loader).split("[")[1].split("]")[0])


    

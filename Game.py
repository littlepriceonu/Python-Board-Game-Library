import time

class BoardGame:
    def __init__(self, loader):
        self.loader = loader

    def maketable(self, x, y, name):
        table = []
        for i in range(1, x*y):
          if i == 1:
            table.append(name)
          else:
            table.append("0-0")
        return table

    def loadloader(self, loader):
        self.loader = loader

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


    def setxy(self, x, y, table, setto):
        if ((y-1) * self.exit + x ) % self.exit == 0:
            setto += "-\n"
            table[(y-1) * self.exit + x] = setto
        else:
            table[(y-1) * self.exit + x] = setto
        self.loader = table

    def maketablestring(self, item, health, addnewline):
        if addnewline:
            return item + "-" + health + "-\n"
        return item + "-" + health

    def printloadertablepos(self, loader):
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

    def getloadertable(self):
        return self.loader

    def makeloader(self, table, exit):
        self.exit = exit
        for i in range(0, len(table)):
            if i % exit == 0 and not i == 0:
                table[i] = table[i] + "-\n"
        return table
    
    def setexit(self, exit):
        self.exit = exit

    def getexit(self):
        return self.exit

    def getxy(self, x, y, table):
        try:
            return table[(y-1) * self.exit + x]
        except:
            return "notpog"

    def save(self, filename):
        try:
            with open(filename, "x") as file:
                file.write(str(self.loader).split("[")[1].split("]")[0])
        except:
            with open(filename, "r+") as file:
                for line in file.readlines():
                    line = ""
                
                file.write(str(self.loader).split("[")[1].split("]")[0])


    

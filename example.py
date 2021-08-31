from Game import BoardGame

i = ["Testing Board", 
    "0-1","0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1","0-1"
    ,"0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1","0-1"
    ,"0-1", "0-1", "1-1", "0-1", "0-1", "0-1", "0-1", "0-1","0-1"
    ,"0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1","0-1"
    ,"0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1","0-1"
    ,"0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1","0-1"]


BG = BoardGame(i)

loader = BG.makeloader(i, 9)

print(BG.getxy(5, 4, i))

BG.printloadertablename(loader)

print("----------------\n")

BG.printloadertablehealth(loader)


BG.save("sf")

def setxy(self, x, y, table, setto):
	table[(y-1) * self.exit + x] = setto

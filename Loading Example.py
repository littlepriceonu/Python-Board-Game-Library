from Game import BoardGame

i = ["Testing Table"]

BG = BoardGame(i)

BG.loadfromfile("sf")

BG.printloadertablepos(BG.getloadertable())


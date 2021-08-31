from Game import BoardGame

i = ["Testing Table"]

BG = BoardGame(i)

BG.loadfromfile("sf") ## sf Would be a file with the table in it

BG.printloadertablepos(BG.getloadertable())


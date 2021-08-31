from Game import BoardGame

i = ["Testing Table"]

BG = BoardGame(i)

BG.loadfromfile("sf") ## sf Would be a file with the table in it. See example.py for table example

BG.printloadertablepos(BG.getloadertable())


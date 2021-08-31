from Game import BoardGame

i = ["Testing Table"]

BG = BoardGame(i)

BG.loadfromfile("sf") ## Sf would be a file that looks like the following multy line comment

"""
    "0-1","0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1","0-1"
    ,"0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1","0-1"
    ,"0-1", "0-1", "1-1", "0-1", "0-1", "0-1", "0-1", "0-1","0-1"
    ,"0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1","0-1"
    ,"0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1","0-1"
    ,"0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1", "0-1","0-1"
"""

BG.printloadertablepos(BG.getloadertable())

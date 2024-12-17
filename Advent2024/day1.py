def splitList():
        location = open("./Advent2024/Locations.txt", "r")
        linha = location.readlines()
        for line in linha:
            print(line.split("   "))
    
        location.close()

splitList()
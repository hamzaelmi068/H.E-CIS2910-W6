
# takes in nAggressive, nPassive >= 0
# returns the number of possible arrangements of dogs
# Examples:
# |  Input  |  Output  |
# |---------|----------|
# |   0,0   |     1    |
# |---------|----------|
# |   1,1   |     2    |
# |---------|----------|
# |   0,2   |     0    |
# |---------|----------|
# |   2,2   |    12    |
# |---------|----------|
def dogArrangements( nPassive, nAggressive ):
    if nPassive == 0 or nAggressive == 0:
        return 1
    
    # since the passive dogs can be placed anywhere, we can consider the following
    totalSlots = nPassive + nAggressive + nAggressive - 1 # the -1 accounts for the seperator between aggresive dogs

    # to keep track of our arrangements
    track_Arrangement = 0

    return 0

# Testing code provided in main():
def main():
    testArgs = [[0,0,1],[1,1,2],[0,2,0],[2,2,12]]
    for arg in testArgs:
        passive, aggressive, answer = arg
        result = dogArrangements(passive,aggressive)
        if result != answer:
            print(f"Failed dogArrangements test with args nPassive={passive} nAggressive={aggressive}.\nExpected: {answer}, Got: {result}")
        else:
            print(f"Passed dogArrangements test with args nPassive={passive} nAggressive={aggressive}.")
    return 0

if __name__ == '__main__':
    main()

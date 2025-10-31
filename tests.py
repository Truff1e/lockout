from index import goalIndex



def lengthsOfGoalsTest():
    for goalId in goalIndex:
        goal = goalIndex[goalId]
        if len(goal) != 4:
            print(goal)



if __name__ == '__main__':
    lengthsOfGoalsTest()

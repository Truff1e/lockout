from index import getFullGoalIndex



def lengthsOfGoalsTest():
    for goalId in getFullGoalIndex():
        goal = getFullGoalIndex()[goalId]
        if len(goal) != 4:
            print(goal)



if __name__ == '__main__':
    lengthsOfGoalsTest()

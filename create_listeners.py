from index import getFullGoalIndex
import os


def createListeners():

    goalDictionary = getFullGoalIndex()

    try:
        os.mkdir('./listeners')
    except FileExistsError:
        print('Listeners directory already exists. Proceeding...')
        pass

    for goalId in goalDictionary:

        template = '''{
            "criteria": {
              "<CRITERIA>": {
                "trigger": "minecraft:<TRIGGER>",
                "conditions": {
                  "<CONDITION>": {
                    <CONDITION_VALUE>
                  }
                }
              }
            },
            "requirements": [
              [
                "<CRITERIA>"
              ]
            ],
            "rewards": {
              "function": "lockout:goals/<GOALID>"
            }
        }'''

        goal = goalDictionary[goalId]
        goalType = goalId[0]

        if goalType == 'I':
            criteria = 'getitem'
            item = goal[1]
            trigger = 'inventory_changed'
            condition = 'items'
            condition_value = f'"items": "minecraft:{item}"'
        
            file = open(f'listeners/{goalId.lower()}.json', 'w')
            template = template.replace('<CRITERIA>', criteria)
            template = template.replace('<TRIGGER>', trigger)
            template = template.replace('<CONDITION>', condition)
            template = template.replace('<CONDITION_VALUE>', condition_value)
            template = template.replace('<GOALID>', goalId.lower())

            file.write(template)
            file.close()

        elif goalType == 'K':
            criteria = 'killentity'
            entity = goal[0][5:].lower().replace(' ', '_')
            trigger = 'player_killed_entity'
            condition = 'entity'
            condition_value = f'"type": "minecraft:{entity}"'
        
            file = open(f'listeners/{goalId.lower()}.json', 'w')
            template = template.replace('<CRITERIA>', criteria)
            template = template.replace('<TRIGGER>', trigger)
            template = template.replace('<CONDITION>', condition)
            template = template.replace('<CONDITION_VALUE>', condition_value)
            template = template.replace('<GOALID>', goalId.lower())

            file.write(template)
            file.close()

        elif goalType == 'D':
            criteria = 'dieto'
            entity = goal[0][7:].lower().replace(' ', '_')
            trigger = 'entity_killed_player'
            condition = 'entity'
            condition_value = f'"type": "minecraft:{entity}"'
        
            file = open(f'listeners/{goalId.lower()}.json', 'w')
            template = template.replace('<CRITERIA>', criteria)
            template = template.replace('<TRIGGER>', trigger)
            template = template.replace('<CONDITION>', condition)
            template = template.replace('<CONDITION_VALUE>', condition_value)
            template = template.replace('<GOALID>', goalId.lower())

            file.write(template)
            file.close()

        elif goalType == 'E':
            criteria = 'eat'
            food = goal[0][4:].lower().replace(' ', '_')
            trigger = 'consume_item'
            condition = 'item'
            condition_value = f'"items": "minecraft:{food}"'
        
            file = open(f'listeners/{goalId.lower()}.json', 'w')
            template = template.replace('<CRITERIA>', criteria)
            template = template.replace('<TRIGGER>', trigger)
            template = template.replace('<CONDITION>', condition)
            template = template.replace('<CONDITION_VALUE>', condition_value)
            template = template.replace('<GOALID>', goalId.lower())

            file.write(template)
            file.close()

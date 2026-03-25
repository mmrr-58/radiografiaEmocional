from database import *

questions = [
    ['sleep', 'daily', 'How much did you sleep last night?', 'range'],
    ['sleep', 'daily', 'On a scale of 1-10, how rested do you feel?', 'scale'],
    ['sleep', 'daily', 'Did you wake up during the night? [y/n]', 'yesno'],
    ['mood', 'weekly', 'Do you feel loved? [y/n]', 'yesno'],
    ['mood', 'daily', 'On a scale of 1-10, would you rate your overall mood', 'scale'],
    ['mood', 'weekly', 'On a scale of 1-10, how often did you feel sadness, emptiness or hopelessness?', 'scale'],
    ['mood', 'weekly', 'On a scale of 1-10, how often did you feel happiness, gratitude or excitement?', 'scale'],
    ['mood', 'daily', 'On a scale of 1-10, how would you describe your stress level', 'scale'],
    ['mood', 'daily', 'On a scale of 1-10 how fullfilled did you feel with the day?', 'scale'],
    ['social', 'weekly', 'On a scale of 1-10, how connected to people around you do you feel?', 'scale'],
    ['social', 'weekly', 'On a scale of 1-10, how much loneliness did you feel', 'scale'],
    ['social', 'weekly', 'How would you describe your relationship with other people', 'open'],
    ['performance', 'daily', 'On a scale of 1-10, how deeply concentrated did you feel', 'scale'],
    ['performance', 'daily', 'On a scale of 1-10, how much attention were you able to use', 'scale'],
    ['performance', 'daily', 'On a scale of 1-10, how difficult was it to make decisions?', 'scale'],
    ['other', 'daily', 'Anything else that was not asked', 'open']
]

for item in questions:
    createQuestion(item[0], item[1], item[2], item[3])
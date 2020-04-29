import json, os
from datetime import datetime
from random import randint as ri
from random import choice as rc

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\Server\\html\\Users\\'

def addScore(score,topic,date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
    user['scores'].append({'date':date,
                           'score':score,
                           'topic':topic})

def buildUser():
    user = {}
    user['name'] = input()
    user['password'] = input()
    user['rank'] = 'Member'
    user['scores'] = []
    return user

def finish(fileName):
    with open(path+fileName+'.json','w') as file:
        json.dump(user,file,indent=4)


##user = buildUser()
##addScore(1,1)
##finish(user['name'])

fileName = input()

with open(path+fileName+'.json') as file:
    user = json.load(file)

for i in range(0,100):
    addScore(ri(0,100),rc(['English','Maths','Science','Geography']))

finish(fileName)


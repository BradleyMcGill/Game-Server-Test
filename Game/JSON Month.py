import json, os
import datetime
from random import randint as ri
from random import choice as rc

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\Server\\html\\Users\\'

def addScore(score,topic,modifier = 0):
    date = (datetime.datetime.now()+ datetime.timedelta(days=modifier)).strftime("%Y-%m-%d %H:%M:%S")
    user['scores'].append({'date':date,
                           'score':score,
                           'topic':topic})

def buildUser():
    user = {}
    user['name'] = input()
    user['password'] = 'pass'
    user['rank'] = 'Member'
    user['scores'] = []
    finish(user['name'],user)

def finish(fileName,user):
    with open(path+fileName+'.json','w') as file:
        json.dump(user,file,indent=4)


def simulateDays(days):
    for i in range(0,days):
        for z in range(ri(0,20)):
            for subject in ['Maths','English','Science','Geography']:
                if ri(0,3) == 0:
                    addScore(ri(50,100) + (ri(0,10) / ri(1,10)),subject,i)

##buildUser()

fileName = input()

with open(path+fileName+'.json') as file:
    user = json.load(file)

simulateDays(30)

finish(fileName,user)

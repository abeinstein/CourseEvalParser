# Model for Eval Parser

class Dept:
    def __init__(self, name):
        self.name = name
        self.teachers = []
    
    # This function will check if a teacher object is already in the dictionary, and
    # if it is, it will add another class's stat dictionary. 
    def addTeacher(self, teacher, statDict):
        if not isinstance(teacher, Teacher):
            print "Incorrect Type for Teacher"
        elif not self.getTeacher(teacher.name):
            self.teachers.append(teacher)
        else:
            for index, t in enumerate(self.teachers):
                if t.name == teacher.name:
                    t.addClassStats(statDict)
                    self.teachers[index] = t
                    
    
    # This function returns a teacher object if that teacher is in the dept,
    # or returns None if that teacher is not in the dept.
    def getTeacher(self,name):
        for teacher in self.teachers:
            if name == teacher.name:
                return teacher
                break
        return None
        
    # This function, given a particular query (organized, understandable, etc.) 
    # will produce an ordered list of teachers
    def rankTeachers(self, query):
        if query is "organized":
            return self.teachers.sort(key=lambda teacher: teacher.scoreDict['organized'], reverse=True)
        elif query is "understandable":
            return self.teachers.sort(key=lambda teacher: teacher.scoreDict['understandable'], reverse=True)
        elif query is "interesting":
            return self.teachers.sort(key=lambda teacher: teacher.scoreDict['interesting'], reverse=True)
        elif query is "attitude":
            return self.teachers.sort(key=lambda teacher: teacher.scoreDict['attitude'], reverse=True)
        elif query is "accessible":
            return self.teachers.sort(key=lambda teacher: teacher.scoreDict['accessible'],reverse=True)
        elif query is "overall":
            return self.teachers.sort(key=lambda teacher: teacher.scoreDict['overall'], reverse=True)
        else:
            print "Invalid query"
            return None
        
        

class Teacher:
    def __init__(self, name, stats): # stats is a dictionary of parsed stats
        self.name = name
        self.rawDict = {}
        self.scoreDict = {}
        if 'organized' in stats:
            self.rawDict['organized'] = [stats['organized']]
            self.scoreDict['organized'] = getQueryScore(self.rawDict['organized'])
        else:
            self.rawDict['organized'] = []
            self.scoreDict['organized'] = 0.0
        if 'understandable' in stats:
            self.rawDict['understandable'] = [stats['understandable']]
            self.scoreDict['understandable'] = getQueryScore(self.rawDict['understandable'])
        else:
            self.rawDict['understandable'] = []
            self.scoreDict['understandable'] = 0.0
        if 'interesting' in stats:
            self.rawDict['interesting'] = [stats['interesting']]
            self.scoreDict['interesting'] = getQueryScore(self.rawDict['interesting'])
        else:
            self.rawDict['interesting'] = []
            self.scoreDict['interesting'] = 0.0
        if 'attitude' in stats:
            self.rawDict['attitude'] = [stats['attitude']]
            self.scoreDict['attitude'] = getQueryScore(self.rawDict['attitude'])
        else:
            self.rawDict['attitude'] = []
            self.scoreDict['attitude'] = 0.0
        if 'accessible' in stats:
            self.rawDict['accessible'] = [stats['accessible']]
            self.scoreDict['accessible'] = getQueryScore(self.rawDict['accessible'])
        else:
            self.rawDict['accessible'] = []
            self.scoreDict['accessible'] = 0.0
        if 'overall' in stats:
            self.rawDict['overall'] = [stats['overall']]
            self.scoreDict['overall'] = getQueryScore(self.rawDict['overall'])
        else:
            self.rawDict['overall'] = []
            self.scoreDict['overall'] = 0.0
        
    def addClassStats(self, stats):
        if 'organized' in stats:
            self.rawDict['organized'].append(stats['organized'])
            self.scoreDict['organized'] = getQueryScore(self.rawDict['organized'])
        if 'understandable' in stats:
            self.rawDict['understandable'].append(stats['understandable'])
            self.scoreDict['understandable'] = getQueryScore(self.rawDict['understandable'])
        if 'interesting' in stats:
            self.rawDict['interesting'].append(stats['interesting'])
            self.scoreDict['interesting'] = getQueryScore(self.rawDict['interesting'])
        if 'attitude' in stats:
            self.rawDict['attitude'].append(stats['attitude'])
            self.scoreDict['attitude'] = getQueryScore(self.rawDict['attitude'])
        if 'accessible' in stats:
            self.rawDict['accessible'].append(stats['accessible'])
            self.scoreDict['accessible'] = getQueryScore(self.rawDict['accessible'])
        if 'overall' in stats:
            self.rawDict['overall'].append(stats['overall'])
            self.scoreDict['overall'] = getQueryScore(self.rawDict['overall'])
        
#This function will calculate a score for a given list of stats. 
def getQueryScore(rawStatList):
    totalScore = 0.0
    for classStat in rawStatList:
        classScore = calculateScore(classStat)
        totalScore += classScore
    totalScore = totalScore / len(rawStatList)
    return totalScore

def calculateScore(listOfRatings):
    score = 0.0
    #numberOfRatings = sum(listOfRatings)
    numberOfRatings = 0
    if len(listOfRatings) == 5: # i.e. No N/A section
        weightedSum = 0.0
        for i in range(1,6):
            weightedSum += listOfRatings[i-1] * i
            numberOfRatings += listOfRatings[i-1]
        score = weightedSum / numberOfRatings
    elif len(listOfRatings) == 6: # i.e. N/A section
        weightedSum = 0.0
        for i in range(1,6):
            weightedSum += listOfRatings[i] * i
            numberOfRatings += listOfRatings[i]
        score = weightedSum / numberOfRatings 
    return score           

def numToKeyword(n):
    if n is 1:
        return "organized"
    elif n is 2:
        return "understandable"
    elif n is 3:
        return "interesting"
    elif n is 4:
        return "attitude"
    elif n is 5:
        return "accessible"
    elif n is 6:
        return "overall"


    
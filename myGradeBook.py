#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 14:45:48 2020

@author: evenmyrennybo
"""

def readGrades(gradeFileName):
    
    try: 
        
        gradeFileName = open(gradeFileName, 'r') #open the file
        
        gradeList = [] #make an empty list
        #for loop that will read every line and put in into lists inside a list
        for EachLine in gradeFileName:
        
            EachLine = EachLine.split()
            gradeList.append(EachLine)
        #return the list of lists
        return gradeList
        
        gradeFileName.close()
        
    #except File not found errors
    except FileNotFoundError:
        
        print('File not found')
        
        
def convertGradestoInt(stringGradesList):
    #the for list is seperating the numbers from the names
    for row in stringGradesList:
        #this loop is reading and converting the string numbers into integer numbers
        for index in range(1, len(row)):
            row[index] = int(row[index])
    #return the integers number
    return stringGradesList


    
def findLargest(studentGrades):
     
    #use the first number as the largest
    largest = studentGrades[1]
    #use the loop to find the highest number  
    for i in studentGrades:
        #everytime a number is higher than the largest, it changes to largest
        if i > largest:
            largest = i
    
    return largest
            
    
    
def calculateAverage(gradeList):
    
    #find the total, by finding the total of the list and divide it by how many objects it is in the list
    
    total = sum(gradeList)/len(gradeList)
    return total
    
    

def createGradebook():
    #make the gradebook
    grades = readGrades('studentsAndGrades.txt')
    
    gradesInt = convertGradestoInt(grades)
    #have an empty list that will be appended to later
    finalList = []
    
    
    #this for loop is reading the out data in the other functions and put them in a list
    for i in range(len(gradesInt)):
        #the empty list the data gets appended to
        grade = []
        #this append the names into the list
        grade.append(gradesInt[i][0])
        
        #this appends the largest number to the list
        grade.append(findLargest(gradesInt[i][1:]))
        
        #this appends the average grades into the lis
        grade.append(calculateAverage(gradesInt[i][1:]))
        #takes the list we made and appends it to a list, where all the values we need is going to be listed
        finalList.append(grade)
            
    
    return finalList
    
    
def printGradebook(gradeBook):
    
   #make the headliner
    print('\n\n\t\t High' + '\tAverage\n' + 'Names\tGrade\t Grade' + '\n'+('='*24)+'\n')
    
    #this for loop will read each line form the list in creatgradeBook 
    #and formate it to be a nice output
    for i in gradeBook:
        print('{:10}'.format(i[0]),'{:0}'.format(i[1]),'{:9.2f}'.format(i[2]))
    
    
    
   
    
    
    
                     

printGradebook(createGradebook())
        
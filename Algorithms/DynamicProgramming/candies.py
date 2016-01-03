'''
Optimize candy distribution amongst student based on their grade

Constraints:

1) The seating order for students is provided and is fixed
2) Every student should have at least 1 candy
3) For two consecutive students, student with higher grade should have more candies than student with lower grade
4) For two consecutive students, student with equal grade can have different amount of candies

Complete problem: https://www.hackerrank.com/challenges/stockmax
'''


def minCandiesRequired(studentGrades):
    '''
    method to calculate candies required for the student in the class based on their grades
    '''
    candiesTable = [1]

    for idx in range(1, len(studentGrades)):
        prevStudentGrade = studentGrades[idx-1]
        currStudentGrade = studentGrades[idx]

        if currStudentGrade > prevStudentGrade:
            candiesTable.append(candiesTable[-1]+1)
        else:
            candiesTable.append(1)
            tmpIdx = idx
            while tmpIdx >= 1 and studentGrades[tmpIdx-1] > studentGrades[tmpIdx] and candiesTable[tmpIdx-1] == candiesTable[tmpIdx]:
                 candiesTable[tmpIdx-1] = candiesTable[tmpIdx] + 1
                 tmpIdx -= 1
    return sum(candiesTable)


if __name__ == "__main__":
    ipFile = open('candies_input.txt')

    totatStudents = int(ipFile.readline())
    studentGrades = []
    for _ in range(totatStudents):
        studentGrades.append(int(ipFile.readline()))

    print minCandiesRequired(studentGrades)
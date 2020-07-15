from user_service import createUserRecord
from utils import RECORD_SEPARATOR

def readUserRecordsFromInputFiles(inputFilesPaths):
  userRecords = []
  for inputFilePath in inputFilesPaths:
    with open(inputFilePath) as file:
      for line in file:
        line = line.strip()
        id, *fullName, department = line.split(RECORD_SEPARATOR)
        * givenNames, lastName = fullName
        userRecords.append(createUserRecord(id, givenNames, lastName, department))
  return userRecords

def writeUserRecordsToOutputFile(outputFilePath, userRecords):
  with open(outputFilePath, 'a') as file:
    for userRecord in userRecords:
        file.write(userRecord + '\n')
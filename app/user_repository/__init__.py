from user_service import createUserRecord
from utils import RECORD_SEPARATOR

def readUsersFromInputFiles(inputFilesPaths):
  users = []
  for inputFilePath in inputFilesPaths:
    with open(inputFilePath) as file:
      for line in file:
        line = line.strip()
        users.append(line)
  return users

def writeUserRecordsToOutputFile(outputFilePath, userRecords):
  with open(outputFilePath, 'a') as file:
    for userRecord in userRecords:
        file.write(userRecord + '\n')
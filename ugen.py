from utils import RECORD_SEPARATOR, HELP_FLAG_LONG, HELP_FLAG_SHORT, OUTPUT_FLAG_LONG, OUTPUT_FLAG_SHORT, HELP_MESSAGE
from userRepository import readUserRecordsFromInputFiles, writeUserRecordsToOutputFile

import sys

def main(args):
  if HELP_FLAG_SHORT in args or HELP_FLAG_LONG in args:
    return HELP_MESSAGE

  if OUTPUT_FLAG_SHORT not in args and OUTPUT_FLAG_LONG not in args:
    return HELP_MESSAGE

  if len(args) < 4:
    return HELP_MESSAGE
  
  _, _, outputFilePath, *inputFilesPaths = args
  
  userRecords = readUserRecordsFromInputFiles(inputFilesPaths)
  writeUserRecordsToOutputFile(outputFilePath, userRecords)

print(main(sys.argv))


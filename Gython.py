### this file is very important for Gython to work. Please do not remove ###
# also I made it ez to use to make so you can use it in your projects

import sys
import os
import time
from typing_extensions import *
from typing_extensions import Self
from colorama import Fore as __Fore__
from colorama import Style as __Style__
from colorama import Back as __Back__
import webbrowser as __webbrowser__
import requests as __requests__
from bs4 import BeautifulSoup as __BeautifulSoup__
# Version
Version = "2.3.6"
# Colors
class ColorPanel:
  GREEN = f"{__Fore__.GREEN}"
  RESET = f"{__Style__.RESET_ALL}"
  RESETCOLOR = f"{__Fore__.RESET}"
  RED  = f"{__Fore__.RED}"
  BLUE = f"{__Fore__.BLUE}"
  YELLOW = f"{__Fore__.YELLOW}"
  CYAN = f"{__Fore__.CYAN}"
  MAGENTA = f"{__Fore__.MAGENTA}"
  WHITE = f"{__Fore__.WHITE}"
  BLACK = f"{__Fore__.BLACK}"
  LIGHTBLACK = f"{__Fore__.LIGHTBLACK_EX}"
  LIGHTBLUE = f"{__Fore__.LIGHTBLUE_EX}"
  LIGHTCYAN = f"{__Fore__.LIGHTCYAN_EX}"
  LIGHTGREEN = f"{__Fore__.LIGHTGREEN_EX}"
  LIGHTMAGENTA = f"{__Fore__.LIGHTMAGENTA_EX}"
  LIGHTRED = f"{__Fore__.LIGHTRED_EX}"
  LIGHTWHITE = f"{__Fore__.LIGHTWHITE_EX}"
  LIGHTYELLOW = f"{__Fore__.LIGHTYELLOW_EX}"
  class BackgroundColors:
    LIGHTGREEN = f"{__Back__.LIGHTGREEN_EX}"
    BLACK = f"{__Back__.BLACK}"
    RESET = f"{__Back__.RESET}"
    GREEN = f"{__Back__.GREEN}"
    BLUE = f"{__Back__.BLUE}"
    RED = f"{__Back__.RED}"
    YELLOW = f"{__Back__.YELLOW}"
    CYAN = f"{__Back__.CYAN}"
    MAGENTA = f"{__Back__.MAGENTA}"
    WHITE = f"{__Back__.WHITE}"
    LIGHTBLACK = f"{__Back__.LIGHTBLACK_EX}"
    LIGHTBLUE = f"{__Back__.LIGHTBLUE_EX}"
    LIGHTCYAN = f"{__Back__.LIGHTCYAN_EX}"
    LIGHTGREEN = f"{__Back__.LIGHTGREEN_EX}"
    LIGHTMAGENTA = f"{__Back__.LIGHTMAGENTA_EX}"
    LIGHTRED = f"{__Back__.LIGHTRED_EX}"
    LIGHTWHITE = f"{__Back__.LIGHTWHITE_EX}"
    LIGHTYELLOW = f"{__Back__.LIGHTYELLOW_EX}"
class TextEditPanel:
  ITALIC = "\x1B[3m"
  BOLD = "\x1B[1m"
  ITALIC_END = "\x1B[0m"
  BOLD_END = "\x1B[0m"
  UNDERLINE = "\x1B[4m"
  UNDERLINE_END = "\x1B[0m"
  
class GyWebPackages:
  import os
  import sys
  import webbrowser as wb

Credits = f"""-----------------------------------------------
Green's Coding: 
https://replit.com/@GreenGaming6 (Creator/Publisher)
Project On Replit:
https://replit.com/@GreenGaming6/Gython (Project)
-------------------------------------------------------------------------
This is an open-source repl made on REPLIT.com, Please do not edit or do anything and publish without permission.
If you make a project using this please do credits [if you dont want it's ok], Thanks for reading."""
# Error Codes
__ERRORCODE001 = f"""
{__Fore__.RED}(CodeError):
(PrintDone) Value must be a Boolean Value 'True' or 'False', Please Try Again.
ErrorCode: 001
"""
__ERRORCODE002 = f"""
    {__Fore__.RED}(CodeError):
    Value must be an Integer Value, Please Try Again.
    ErrorCode: 002
    """
__ERRORCODE003 = f"""
{__Fore__.RED}(CodeError):
Value must be a String Value, Please Try Again.
ErrorCode: 003
"""

__ERRORCODE004 = f"""
{__Fore__.RED}(CodeError):
Value must be a List Value, Please Try Again.
ErrorCode: 004
"""


__ERRORCODE005 = f"""
{__Fore__.RED}(CodeError):
Invalid Value, Please Try Again.
ErrorCode: 005
"""

__ERRORCODE006 = f"""
{__Fore__.RED}(CodeError):
Unreachable or No Value, Please Try Again.
ErrorCode: 006
"""

__ERRORCODE007 = f"""
{__Fore__.RED}(CodeError):
Value/File does not exist, Please Try Again.
ErrorCode: 007
"""

__ERRORCODE008 = f"""
{__Fore__.RED}(CodeError):
Value does not exist, Use 1-5, Please Try Again.
ErrorCode: 008
"""
# Classes
class GyPlus:
  def SayErrorCode(errorcode):
    if errorcode == "001":
      Say(__ERRORCODE001)
    elif errorcode == "002":
      Say(__ERRORCODE002)
    elif errorcode == "003":
      Say(__ERRORCODE003)
    elif errorcode == "004":
      Say(__ERRORCODE004)
    elif errorcode == "005":
      Say(__ERRORCODE005)
    elif errorcode == "006":
      Say(__ERRORCODE006)
  def Warn(warn, level):
    if level == 1 or level == "1":
      Say(f"{ColorPanel.LIGHTRED}{warn}{ColorPanel.RESETCOLOR}")
    elif level == 2 or level == "2":
      Say(f"{ColorPanel.LIGHTYELLOW}{warn}{ColorPanel.LIGHTYELLOW}")
    elif level == 3 or level == "3":
      Say(f"{ColorPanel.YELLOW}{warn}{ColorPanel.RESETCOLOR}")
    elif level == 4 or level == "4":
      Say(f"{ColorPanel.RED}{warn}{ColorPanel.RESETCOLOR}")
    elif level == 5 or level == "5":
      Say(f"{ColorPanel.MAGENTA}{warn}{ColorPanel.RESETCOLOR}")
    elif level:
      Say(__ERRORCODE008)
######### Functions #########
import random
# Makes Mathematical Problems
def Maths(num1, num2, operator):
  num1 = int(num1)
  num2 = int(num2)
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*" or "x".lower():
    return num1 * num2
  elif operator == "/":
    return num1 / num2
  elif operator == "^":
    return num1 ^ num2
# Basically the print() function
def Say(string):
  string = str(string)
  print(string)
# Basically the input() function
def TextInput(string):
  string = str(string)
  input(string)
# These turn str/bool/int/float into str/bool/int/float
def TurnToString(variable):
  variable = str(variable)
def TurnToInteger(variable):
  variable = int(variable)
def TurnToFloat(variable):
  variable = float(variable)
def TurnToBoolean(variable):
  variable = bool(variable)
# Exits Gython
def Exit():
  sys.exit()
# Clears the console
def Clear():
  os.system("clear")
# basically the time.sleep() function
def Wait(seconds):
  time.sleep(int(seconds))
# Get Time
def GetTime():
  return time.time()
# Checks if an Event is active.
def IsEventActive():
  Say("No Event is Active today, Be sure to check later!")
# Sets a Timer
def timer(seconds, minutes, hours, days, PrintDone):
  seconds = int(seconds)
  seconds = minutes/60
  seconds = hours/3600
  seconds = days/86400
  time.sleep(seconds)
  PrintDone = bool(PrintDone)
  if PrintDone == True:
    print("Timer Completed!")
  elif PrintDone == False:
    return
  else:
    Say(f"{__ERRORCODE001}")
# Gets a Random Number
def Random(min, max):
  min = int(min)
  max = int(max)
  random.randint(min, max)
# Creates A Dictionary
def CreateDictionary(key, value):
  key = str(key)
  value = str(value)
  dictionary = {key: value}
  return dictionary
# Check the type
def TypeCheck(VALUE, PrintOrNo):
  type(VALUE)
  if PrintOrNo == True:
    print(type(VALUE))
  elif PrintOrNo == False:
    return type(VALUE)
  elif PrintOrNo:
    Say(f"{__ERRORCODE005}")
# Checks if value is true
def IsTrue(value):
  if value == True:
    Say(f"{value} is True")
  elif value == False:
    Say(f"{value} is False")
  elif value:
    Say(f"{value} is not True and is not False")
# Checks if value is false
def IsFalse(value):
  if value == True:
    Say(f"{value} is True")
  elif value == False:
    Say(f"{value} is False")
  elif value:
    Say(f"{value} is not True and is not False")
# credits
def credit():
  Say(Credits)
# deletes a var
def delete(variable):
  del variable
# makes a folder
def makefolder(directory):
  os.mkdir(directory)
  Say("Made Folder Successfully.")
# makes a file
def makefile(file):
  os.mkfifo(file)
  Say("Made File Successfully")
# deletes a file
def deletefile(file):
  os.remove(file)
  Say("Removed File Successfully")
# deletes a folder
def deletefolder(folder):
  os.removedirs(folder)
  Say("Removed Folder Successfully")
# gets the current directory
def getdir():
  directory = os.getcwd()
  Say(f"The Current Directory is {directory}")
# reads a file
def readfile(file):
  file = str(file)
  with open(file, "r") as f:
    contents = f.read()
    Say(f"The contents of the file {file} are:\n{contents}")
# writes a file
def writefile(file, text):
    file = str(file)
    with open(file, "w") as f:
        f.write(text)
    Say(f"The file {file} has been written with the text {text} ")
# removes a file
def removedir(directory):
  os.rmdir(directory)
  Say("Removed Directory Successfully")
# pops a value from a list
def pop(list, index):
  list = list
  index = int(index)
  list.pop(index)
  Say(f"Popped {index} from {list}")
# adds a value to a list
def addvalue(list, value):
  list = list
  value = value
  list.append(value)
# removes a value from a list
def removevalue(list, value):
  list=list
  value = value
  list.remove(value)
# gets the length
def GetLength(value):
  value = value
  length = len(value)
# web scrapes a selected website\
def webscrape(url):
  response = __requests__.get(url)
  html_content = response.text
  soup = __BeautifulSoup__(html_content, "html.parser")
  return soup.prettify()

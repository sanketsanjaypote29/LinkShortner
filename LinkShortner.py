#Importing Python Modules
#pyshorteners
import pyshorteners

shorteners = pyshorteners.Shortener()
Long_link = input("Please Enter Long Link input:")
Short_link = shorteners.tinyurl.short(Long_link)
print(Short_link)

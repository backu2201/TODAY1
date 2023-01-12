import win32api
import os
def GetDrives():
    drives=win32api.GetLogicalDriveStrings()
    drives=drives.split('\000')
    #print(drives)
    return drives
print(GetDrives())
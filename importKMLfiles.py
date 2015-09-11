# importKMLfiles.py
# March 4, 2015
# Copyright 2015 RTI International All Rights Reserved
# CC BY. This work is licensed under a Creative Commongs Attribution License. (US/v4.0)
# https://creativecommons.org/licenses/by/4.0/
# David Chrest
# RTI International
# 3040 Corwallis Rd.
# Research Triangle Park, NC 27709
#
# Imports .kml (KML line segments) files generated from the Moves mobile app 
# to Feature Classes in ESRI File Geodatabases.
# Once complete, Geospatial analysis, data visulization,
# and cartographic display is possible utilizing ArcGIS software.
#
# Note: Moves mobile app develeped by ProtoGeo,
# acquired by Facebook April 14, 2014.
# https://www.moves-app.com.


#Import necessary modules.
import arcpy
import os
import glob


#List of subfoldes with .kml files that are within each daily, monthly, weekly, yearly parent folders.
folderList = ["activities", "places", "storyline"]

#List of Years used when copying Feature Classes within individual .gdb files
#created when importing the KML files .
yearList = ["2013", "2014", "2015"]

#Import Yearly KML files to kml_yearly.gdb from
#activities, places, storyline subfolders in Yearly parent folder.
#===========================================================================================================
arcpy.env.workspace = r"C:\Projects\iSHARE\moves\moves_export_20150602\GeoDatabase_KMLimport\kml_yearly.gdb"

#Import KML files. Tool imports each KML file to its own File GDB.
for folder in folderList:
    kmlFiles = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\yearly" + os.sep + folder + os.sep + "*.kml")
    for kml in kmlFiles:
        dirname, filename = os.path.split(kml)
        basename, extension = os.path.splitext(filename)
        kmlOutfile = basename
        arcpy.KMLToLayer_conversion(kml, r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\yearly")
        print "Imported " + filename + " to " + kmlOutfile + ".gdb"


#Copy Feature Class of each imported KML file from its own File GDB over to the kml_yearly.gdb.
for folder in folderList:
    for year in yearList:
        yearDir = r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\yearly"
        lineFC = ".gdb\Placemarks\Polylines"
        pointFC = ".gdb\Placemarks\Points"
        
        if arcpy.Exists(yearDir + os.sep + folder + "_" + year + lineFC):
            arcpy.CopyFeatures_management(yearDir + os.sep + folder + "_" + year + lineFC, folder + "_" + year + "_lines")
            print "Copied " + yearDir + os.sep + folder + "_" + year + lineFC + " to " + folder + "_" + year + "_lines in kml_yearly.gdb"

        if arcpy.Exists(yearDir + os.sep + folder + "_" + year + pointFC):
            arcpy.CopyFeatures_management(yearDir + os.sep + folder + "_" + year + pointFC, folder + "_" + year + "_points")
            print "Copied " + yearDir + os.sep + folder + "_" + year + pointFC + " to " + folder + "_" + year + "_points in kml_yearly.gdb"


#Delete the individual File GDBs created when importing KML files.
fileGDB = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\yearly" + os.sep + "*.gdb")
for GDB in fileGDB:
    arcpy.Delete_management(GDB)
    print "Deleted " + GDB


#Delete the .lyr files created when importing KML files.
lyrFiles = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\yearly" + os.sep + "*.lyr")
for lyr in lyrFiles:
    os.remove(lyr)
    print "Deleted " + lyr


#Import Monthly KML files to kml_monthly.gdb from
#activities, places, storyline subfolders in Monthly parent folder.
#===========================================================================================================
arcpy.env.workspace = r"C:\Projects\iSHARE\moves\moves_export_20150602\GeoDatabase_KMLimport\kml_monthly.gdb"

#Import KML files. Tool imports each KML file to its own File GDB.
for folder in folderList:
    kmlFiles = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\monthly" + os.sep + folder + os.sep + "*.kml")
    for kml in kmlFiles:
        dirname, filename = os.path.split(kml)
        basename, extension = os.path.splitext(filename)
        kmlOutfile = basename
        arcpy.KMLToLayer_conversion(kml, r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\monthly")
        print "Imported " + filename + " to " + kmlOutfile + ".gdb"


#Copy Feature Class of each imported KML file from its own File GDB over to the kml_monthly.gdb.
kmlMonths = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\monthly\activities" + os.sep + "*.kml")
monthList = kmlMonths
monthList = [w[-11:-4] for w in monthList]

for folder in folderList:
    for month in monthList:
        monthE = month.replace('-', '_')
        monthDir = r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\monthly"
        lineFC = ".gdb\Placemarks\Polylines"
        pointFC = ".gdb\Placemarks\Points"

        if arcpy.Exists(monthDir + os.sep + folder + "_" + month + lineFC):
            arcpy.CopyFeatures_management(monthDir + os.sep + folder + "_" + month + lineFC, folder + "_" + monthE + "_lines")
            print "Copied " + monthDir + os.sep + folder + "_" + month + lineFC + " to " + folder + "_" + monthE + "_lines in kml_monthly.gdb"

        if arcpy.Exists(monthDir + os.sep + folder + "_" + month + pointFC):
            arcpy.CopyFeatures_management(monthDir + os.sep + folder + "_" + month + pointFC, folder + "_" + monthE + "_points")
            print "Copied " + monthDir + os.sep + folder + "_" + month + pointFC + " to " + folder + "_" + monthE + "_points in kml_monthly.gdb"


#Delete the individual File GDBs created when importing KML files.
fileGDB = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\monthly" + os.sep + "*.gdb")
for GDB in fileGDB:
    arcpy.Delete_management(GDB)
    print "Deleted " + GDB


#Delete the .lyr files created when importing KML files.
lyrFiles = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\monthly" + os.sep + "*.lyr")
for lyr in lyrFiles:
    os.remove(lyr)
    print "Deleted " + lyr


#Import Weekly KML files to kml_weekly.gdb from
#activities, places, storyline subfolders in Weekly parent folder.
#===========================================================================================================
arcpy.env.workspace = r"C:\Projects\iSHARE\moves\moves_export_20150602\GeoDatabase_KMLimport\kml_weekly.gdb"

#Import KML files. Tool imports each KML file to its own File GDB.
for folder in folderList:
    kmlFiles = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\weekly" + os.sep + folder + os.sep + "*.kml")
    for kml in kmlFiles:
        dirname, filename = os.path.split(kml)
        basename, extension = os.path.splitext(filename)
        kmlOutfile = basename
        arcpy.KMLToLayer_conversion(kml, r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\weekly")
        print "Imported " + filename + " to " + kmlOutfile + ".gdb"


#Copy Feature Class of each imported KML file from its own File GDB over to the kml_monthly.gdb.
kmlWeeks = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\weekly\activities" + os.sep + "*.kml")
weekList = kmlWeeks
weekList = [w[-12:-4] for w in weekList]

for folder in folderList:
    for week in weekList:
        weekE = week.replace('-', '_')
        weekDir = r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\weekly"
        lineFC = ".gdb\Placemarks\Polylines"
        pointFC = ".gdb\Placemarks\Points"

        if arcpy.Exists(weekDir + os.sep + folder + "_" + week + lineFC):
            arcpy.CopyFeatures_management(weekDir + os.sep + folder + "_" + week + lineFC, folder + "_" + weekE + "_lines")
            print "Copied " + weekDir + os.sep + folder + "_" + week + lineFC + " to " + folder + "_" + weekE + "_lines in kml_monthly.gdb"

        if arcpy.Exists(weekDir + os.sep + folder + "_" + week + pointFC):
            arcpy.CopyFeatures_management(weekDir + os.sep + folder + "_" + week + pointFC, folder + "_" + weekE + "_points")
            print "Copied " + weekDir + os.sep + folder + "_" + week + pointFC + " to " + folder + "_" + weekE + "_points in kml_monthly.gdb"


#Delete the individual File GDBs created when importing KML files.
fileGDB = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\weekly" + os.sep + "*.gdb")
for GDB in fileGDB:
    arcpy.Delete_management(GDB)
    print "Deleted " + GDB


#Delete the .lyr files created when importing KML files.
lyrFiles = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\weekly" + os.sep + "*.lyr")
for lyr in lyrFiles:
    os.remove(lyr)
    print "Deleted " + lyr


#Import Daily KML files to kml_daily.gdb from
#activities, places, storyline subfolders in Daily parent folder.
#===========================================================================================================
arcpy.env.workspace = r"C:\Projects\iSHARE\moves\moves_export_20150602\GeoDatabase_KMLimport\kml_daily.gdb"

#Import KML files. Tool imports each KML file to its own File GDB.
for folder in folderList:
    kmlFiles = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\daily" + os.sep + folder + os.sep + "*.kml")
    for kml in kmlFiles:
        dirname, filename = os.path.split(kml)
        basename, extension = os.path.splitext(filename)
        kmlOutfile = basename
        
        if "coordinates" in open(kml).read():      
            arcpy.KMLToLayer_conversion(kml, r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\daily")
            print "Imported " + filename + " to " + kmlOutfile + ".gdb"


#Copy Feature Class of each imported KML file from its own File GDB over to the kml_daily.gdb.
kmlDays = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\daily\activities" + os.sep + "*.kml")
dayList = kmlDays
dayList = [w[-12:-4] for w in dayList]

for folder in folderList:
    for day in dayList:
        dayE = day.replace('-', '_')
        dayDir = r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\daily"
        lineFC = ".gdb\Placemarks\Polylines"
        pointFC = ".gdb\Placemarks\Points"

        if arcpy.Exists(dayDir + os.sep + folder + "_" + day + lineFC):
            arcpy.CopyFeatures_management(dayDir + os.sep + folder + "_" + day + lineFC, folder + "_" + dayE + "_lines")
            print "Copied " + dayDir + os.sep + folder + "_" + day + lineFC + " to " + folder + "_" + dayE + "_lines in kml_daily.gdb"

        if arcpy.Exists(dayDir + os.sep + folder + "_" + day + pointFC):
            arcpy.CopyFeatures_management(dayDir + os.sep + folder + "_" + day + pointFC, folder + "_" + dayE + "_points")
            print "Copied " + dayDir + os.sep + folder + "_" + day + pointFC + " to " + folder + "_" + dayE + "_points in kml_daily.gdb"



#Delete the individual File GDBs created when importing KML files.
fileGDB = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\daily" + os.sep + "*.gdb")
for GDB in fileGDB:
    arcpy.Delete_management(GDB)
    print "Deleted " + GDB


#Delete the .lyr files created when importing KML files.
lyrFiles = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\daily" + os.sep + "*.lyr")
for lyr in lyrFiles:
    os.remove(lyr)
    print "Deleted " + lyr


#Import Full KML files to kml_daily.gdb from
#activities, places, storyline subfolders in Full parent folder.
#===========================================================================================================
arcpy.env.workspace = r"C:\Projects\iSHARE\moves\moves_export_20150602\GeoDatabase_KMLimport\kml_full.gdb"

#Import KML files. Tool imports each KML file to its own File GDB.
kmlFiles = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\full" + os.sep + "*.kml")
for kml in kmlFiles:
    dirname, filename = os.path.split(kml)
    basename, extension = os.path.splitext(filename)
    kmlOutfile = basename
       
    arcpy.KMLToLayer_conversion(kml, r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\full")
    print "Imported " + filename + " to " + kmlOutfile + ".gdb"



#Copy Feature Class of each imported KML file from its own File GDB over to the kml_full.gdb.
for folder in folderList:
    fullDir = r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\full"
    lineFC = ".gdb\Placemarks\Polylines"
    pointFC = ".gdb\Placemarks\Points"

    if arcpy.Exists(fullDir + os.sep + folder + lineFC):
        arcpy.CopyFeatures_management(fullDir + os.sep + folder + lineFC, folder + "_lines")
        print "Copied " + fullDir + os.sep + folder + lineFC + " to " + folder + "_lines in kml_full.gdb"

    if arcpy.Exists(fullDir + os.sep + folder + pointFC):
        arcpy.CopyFeatures_management(fullDir + os.sep + folder + pointFC, folder + "_points")
        print "Copied " + fullDir + os.sep + folder + pointFC + " to " + folder + "_points in kml_full.gdb"



#Delete the individual File GDBs created when importing KML files.
fileGDB = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\full" + os.sep + "*.gdb")
for GDB in fileGDB:
    arcpy.Delete_management(GDB)
    print "Deleted " + GDB


#Delete the .lyr files created when importing KML files.
lyrFiles = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\kml\full" + os.sep + "*.lyr")
for lyr in lyrFiles:
    os.remove(lyr)
    print "Deleted " + lyr

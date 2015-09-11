# importGPXfiles.py
# March 3, 2015
# CC BY. This work is licensed under a Creative Commongs Attribution License. (US/v4.0)
# https://creativecommons.org/licenses/by/4.0/
# David Chrest
# RTI International
# Research Triangle Park, NC 27709
#
# Imports .gpx (GPS points) files generated from the Moves mobile app 
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


#List of subfoldes with .gpx files that are within each daily, monthly, weekly, yearly parent folders.
folderList = ["activities", "cycling", "places", "running", "storyline", "transport", "walking"]

#Import Yearly GPX files to gpx_yearly.gdb from
#activities, cycling, places, running, storyline, transport, and walking subfolders in Yearly parent folder.
#===========================================================================================================
arcpy.env.workspace = r"C:\Projects\iSHARE\moves\moves_export_20150602\GeoDatabase_GPXimport\gpx_yearly.gdb"

for folder in folderList:
    gpxFiles = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\gpx\yearly" + os.sep + folder + os.sep + "*.gpx")
    for gpx in gpxFiles:
        dirname, filename = os.path.split(gpx)
        basename, extension = os.path.splitext(filename)
        gpxOutfile = basename
        arcpy.GPXtoFeatures_conversion(gpx, gpxOutfile)
        print "Imported " + gpxOutfile + " to gpx_yearly.gdb"


#Import Weekly GPX files to gpx_weekly.gdb from
#activities, cycling, places, running, storyline, transport, and walking subfolders in Weekly parent folder.
#===========================================================================================================
arcpy.env.workspace = r"C:\Projects\iSHARE\moves\moves_export_20150602\GeoDatabase_GPXimport\gpx_weekly.gdb"

for folder in folderList:
    gpxFiles = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\gpx\weekly" + os.sep + folder + os.sep + "*.gpx")
    for gpx in gpxFiles:
        dirname, filename = os.path.split(gpx)
        basename, extension = os.path.splitext(filename)
        gpxOutfile = basename
        arcpy.GPXtoFeatures_conversion(gpx, gpxOutfile)
        print "Imported " + gpxOutfile + " to gpx_weekly.gdb"


#Import Monthly GPX files to gpx_monthly.gdb from
#activities, cycling, places, running, storyline, transport, and walking subfolders in Monthly parent folder.
#===========================================================================================================
arcpy.env.workspace = r"C:\Projects\iSHARE\moves\moves_export_20150602\GeoDatabase_GPXimport\gpx_monthly.gdb"

for folder in folderList:
    gpxFiles = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\gpx\monthly" + os.sep + folder + os.sep + "*.gpx")
    for gpx in gpxFiles:
        dirname, filename = os.path.split(gpx)
        basename, extension = os.path.splitext(filename)
        gpxOutfile = basename
        arcpy.GPXtoFeatures_conversion(gpx, gpxOutfile)
        print "Imported " + gpxOutfile + " to gpx_monthly.gdb"


#Import Daily GPX files to gpx_daily.gdb from
#activities, cycling, places, running, storyline, transport, and walking subfolders in Daily parent folder.
#===========================================================================================================
arcpy.env.workspace = r"C:\Projects\iSHARE\moves\moves_export_20150602\GeoDatabase_GPXimport\gpx_daily.gdb"

for folder in folderList:
    gpxFiles = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\gpx\daily" + os.sep + folder + os.sep + "*.gpx")
    for gpx in gpxFiles:
        dirname, filename = os.path.split(gpx)
        basename, extension = os.path.splitext(filename)
        gpxOutfile = basename
        arcpy.GPXtoFeatures_conversion(gpx, gpxOutfile)
        print "Imported " + gpxOutfile + " to gpx_daily.gdb"


#Import Full GPX files to gpx_full.gdb from full folder.
#===========================================================================================================
arcpy.env.workspace = r"C:\Projects\iSHARE\moves\moves_export_20150602\GeoDatabase_GPXimport\gpx_full.gdb"

gpxFiles = glob.glob(r"C:\Projects\iSHARE\moves\moves_export_20150602\gpx\full" + os.sep + "*.gpx")
for gpx in gpxFiles:
    dirname, filename = os.path.split(gpx)
    basename, extension = os.path.splitext(filename)
    gpxOutfile = basename
    arcpy.GPXtoFeatures_conversion(gpx, gpxOutfile)
    print "Imported " + gpxOutfile + " to gpx_full.gdb"



    

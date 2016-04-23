# Organize your pictures, videos and then sync them to your other folders

##Introduction
I have had both Androids and an iPhones with tons of pictures and videos on them for the past several years. On top of that my wife has had her set of iphones over the years as well. Cloud storage is great but I’m not a big fan of paying for monthly storage nor do I accept having the quality of my picture degraded when getting uploaded to free tiered services.

So, if you’re like me with plenty of hard drives around and you don’t want to buy a Drobo. Why not pull down your files onto these drives in an organized fashion so that you can actually find where your pictures are and also synchronize copies of your files across your different hard drives.

##Summary
These Python scripts have 2 major functions:
- Organize my pictures and videos into their own directories once I have pulled these related files off of my phones.
- Synchronizes these folders onto other hard drives so that I have a backup of my files in another location.

##Output of Organize Script
This script will do the following:
- It takes the pictures from a specified folder and puts them into another. The destination of these files will be in a folder with the format “year”/”year-month”. It also takes the videos and puts them in its own folder. For example, it will look something like this for the pictures: 

  ![alt tag](https://github.com/RobsRepo/Organize-Pics-Vids-and-Sync-Them/blob/master/pictures.png)

  And this for the videos:

  ![alt tag](https://github.com/RobsRepo/Organize-Pics-Vids-and-Sync-Them/blob/master/videos.png)

- If a file is already there, the file in the origin folder will not be moved.
- If a file has the same name, but has different contents, the file that is going to be moved will be suffixed with a number on the end of it.
- After the files have been moved, a log report will be available as a csv file with whether or not the file was moved, the original file and the destination of where this file was moved to.

##Output of Synchronize Script
This script will do the following:
- This script can be used to synchronize any folder (not just the picture/video folder).
- Copy the files of a folder and all of its subfolders to another folder.
- It will not overwrite an existing file if it already exists in that folder.
- It will rename the file if there is another file with the same name but not the same contents.
- Once all of the files have been synchronized over a csv log report will be produced that indicates whether or not the file got copied, the original file path and the destination file path.

##To Run the Organize Script:
Inside config.properties, under "[Move_Config]", make sure you have the following 4 properties filled out correctly.
- directory="This represents the root directory to where your pictures and videos are"
- videoDirectory="Where you would like to have your videos stored"
- picturesDirectory="Where you would like to have your pictures stored"
- logFileName="The csv log report on what got moved and what did not"

Once all of that is filled out, run the following: “python OrganizePicsVideos.py”

##To Run the Synchronize Script:
Inside config.properties, under "[Copy_Config]", make sure you have the following 3 properties filled out correctly.
- originDirectory="The root folder of the folder you would like to copy/sync"
- destinationDirectory="The destination of where you would like the files copied to"
- logFileName="The csv log report on what got copied over and what did not"

Once all of that is filled out, run the following: “python SyncFolder.py”

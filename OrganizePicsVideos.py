from FileOrganizer import FileOrganizer
import os.path
import time
import shutil
import ConfigParser

class OrganizePicsVideos(FileOrganizer):

    def __init__(self):
        config = ConfigParser.RawConfigParser()
        config.readfp(open('config.properties'))
        self.directory = config.get("Move_Config", "directory")
        self.video_directory = config.get("Move_Config", "videoDirectory")
        self.pictures_directory = config.get("Move_Config", "picturesDirectory")
        self.log_file_name = config.get("Move_Config", "logFileName")
        FileOrganizer.__init__(self,self.log_file_name)

    def move_file(self,base_directory,current_full_file_path,current_file_name):
        version_year, version_folder = self.create_version_directory(current_full_file_path)
        version_dir = base_directory + "/" + version_year + "/" + version_folder
        self.create_directory(version_dir)
        file_exists, file_name = self.file_exist_in_directory(version_dir, current_full_file_path)
        new_file =  version_dir + "/" + file_name

        if not file_exists:
            shutil.move(current_full_file_path, new_file)
            self.write_item_to_log("Moving",current_full_file_path,new_file)
            print "Moving: " + current_full_file_path + " To: " + new_file
        else:
            self.write_item_to_log("NOT Moving",current_full_file_path,new_file)
            return "NOT Moving: " + current_full_file_path + " To: " + new_file

    def move_files(self):
        file_move_count = 0

        for dirpath, dirs, files in os.walk(self.directory):
            for current_file in files:
                if not current_file.startswith("."):
                    # CURRENT file location full path
                    current_full_file_path = dirpath + "/" + current_file
                    #grab the file extension
                    filename1, file_extension = os.path.splitext(current_full_file_path)
                    #move the files
                    file_move_count += 1
                    if file_extension.lower() in (".mov", ".mp4"):
                        self.move_file(self.video_directory,current_full_file_path,current_file)
                    else:
                        self.move_file(self.pictures_directory,current_full_file_path,current_file)

        print "Total files moved: " + str(file_move_count)

sf = OrganizePicsVideos()
sf.move_files()

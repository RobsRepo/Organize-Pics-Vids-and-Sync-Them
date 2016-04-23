from FileOrganizer import FileOrganizer
import os.path
import ConfigParser
import shutil

class SyncFolder(FileOrganizer):

    def __init__(self):
        config = ConfigParser.RawConfigParser()
        config.readfp(open('config.properties'))
        self.origin_directory = config.get("Copy_Config", "originDirectory")
        self.destination_directory = config.get("Copy_Config", "destinationDirectory")
        self.log_file_name = config.get("Copy_Config", "logFileName")
        FileOrganizer.__init__(self,self.log_file_name)

    def copy_file(self,origin_directory,destination_directory,dir_path,current_file):
        new_post_fix_dir_path = dir_path.replace(origin_directory, "")
        copy_dir = destination_directory + new_post_fix_dir_path
        origin_file_path = dir_path+"/"+current_file
        self.create_directory(copy_dir)
        file_exists, file_name = self.file_exist_in_directory(copy_dir, origin_file_path)
        dest_file_path = copy_dir+"/"+file_name

        if not file_exists:
            shutil.copy2(origin_file_path, dest_file_path)
            self.write_item_to_log("Copying",origin_file_path,dest_file_path)
            print "Copying: " + origin_file_path + " To: " + dest_file_path
        else:
            self.write_item_to_log("NOT Copying",origin_file_path,dest_file_path)
            print "NOT Copying: " + origin_file_path + " To: " + dest_file_path

    def sync_folders(self):
        file_copy_count = 0
        for dirPath, dirs, files in os.walk(self.origin_directory):
            for current_file in files:
                if not current_file.startswith("."):
                    file_copy_count+=1
                    self.copy_file(self.origin_directory, self.destination_directory, dirPath, current_file)

        print "Total files scanned: " + str(file_copy_count)

sf = SyncFolder()
sf.sync_folders()

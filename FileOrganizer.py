import os.path
import time
import filecmp

class FileOrganizer:

    def __init__(self,log_file_name):
        self.log_file_name = log_file_name
        self.write_item_to_log("Action","Origin","Destination")

    def create_directory(self,d):
        if not os.path.exists(d):
            os.makedirs(d)

    def file_exist_in_directory(self,directory_to_check,file_to_check):
        return_val = False
        file_name = os.path.basename(file_to_check)

        modifiedTime = os.path.getmtime(file_to_check)
        createTime = os.path.getctime(file_to_check)
        time_string = ""
        date_format = '%Y-%m-%d-%H-%M-%S'
        if modifiedTime < createTime:
            time_string = time.strftime(date_format, time.localtime(modifiedTime))
        else:
            time_string = time.strftime(date_format, time.localtime(createTime))

        # Check if this file name exists in the destination directory
        if os.path.isfile(directory_to_check + "/" + file_name):
            new_file_counter = 1
            while os.path.isfile(directory_to_check + "/" + os.path.splitext(file_name)[0] + "-" + str(new_file_counter) + os.path.splitext(file_name)[1]):
                new_file_counter = new_file_counter + 1
            file_name = os.path.splitext(file_name)[0] + "-" + str(new_file_counter) + os.path.splitext(file_name)[1]

        # Check to see if this file exists as a different name in the destination directory
        for file in os.listdir(directory_to_check):
            if not file.startswith("."):
                if filecmp.cmp(directory_to_check+"/"+file, file_to_check):
                    return_val = True
                    break

        return return_val, time_string + "-" + file_name

    def create_version_directory(self,current_full_file_path):
        modifiedTime = os.path.getmtime(current_full_file_path)
        createTime = os.path.getctime(current_full_file_path)
        year = ""
        year_month = ""
        if modifiedTime < createTime:
            year = time.strftime('%Y', time.localtime(modifiedTime))
            year_month = time.strftime('%Y-%m', time.localtime(modifiedTime))
        else:
            year = time.strftime('%Y', time.localtime(createTime))
            year_month = time.strftime('%Y-%m', time.localtime(createTime))
        return (year, year_month)

    def write_item_to_log(self,status,origin_file,dest_file):
        with open(self.log_file_name, 'a') as f:
            f.write(status + "," + origin_file + "," + dest_file + '\n')

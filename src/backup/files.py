import os, time
from zipfile import ZipFile
from datetime import datetime


def backup_files(data, day, month, year):
    if data["enable_file_backup"]:
        print("File Backup Enabled")

        # Create Backup
        date = f"{day}_{month}_{year}"
        dir_file_store = f"{data['backup_file_store']}"
        path_file_store = f"{dir_file_store}/file_backup_{date}.zip"
        try:
            create_zip_file = open(path_file_store, 'x')
            create_zip_file.close()
        except FileExistsError:
            pass

        # Compress Backup
        with ZipFile(path_file_store, mode='w') as zip_file:
            for f in data['backup_file_list']:
                print(f"File Backup: {f}")
                zip_file.write(f)

        # Delete old backups
        number_of_copies = data['backup_file_copies']
        dir_list = os.listdir(dir_file_store)

        one_day_since_epoch = 86400.0
        desired_antiquity = one_day_since_epoch * number_of_copies
        today_timestamp = datetime(int(year), int(month), int(day), 0, 0).timestamp()
        top_antiquity = today_timestamp - desired_antiquity

        for file in dir_list:
            path_file = f"{dir_file_store}/{file}"
            file_sec_modified_time = os.path.getmtime(path_file)

            if file_sec_modified_time < top_antiquity:
                print(f"Delete old backups: {path_file}")
                os.remove(path_file)
        print(f"File Backup Complete: {path_file_store}")


        # Falta construir la subida a S3
    else:
        print("File Backup Disabled")

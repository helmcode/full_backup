from zipfile import ZipFile

def backup_files(data):
    if data["enable_file_backup"]:
        print("File Backup Enabled")

        print(data["backup_file_store"])
        print(data["backup_file_copies"])

        print(data["backup_file_list"])
    else:
        print("File Backup Disabled")

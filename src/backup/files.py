from zipfile import ZipFile

def backup_files(data, date):
    if data["enable_file_backup"]:
        print("File Backup Enabled")

        path_file_store = f"{data['backup_file_store']}/file_backup_{date}.zip"
        try:
            create_zip_file = open(path_file_store, 'x')
            create_zip_file.close()
        except FileExistsError:
            pass

        with ZipFile(path_file_store, mode='w') as zip_file:
            for f in data['backup_file_list']:
                print(f"File Backup: {f}")
                zip_file.write(f)

        # Falta eliminar copias antiguas y guardar solo las copias indicadas aquí:
        number_of_copies = data['backup_file_copies']
        print(f"File Backup Complete: {path_file_store}")
    else:
        print("File Backup Disabled")

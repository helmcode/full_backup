import yaml, os

# Local Imports
from backup.files import backup_files


def main():
    config_file = os.environ['FULL_BACKUP_CONFIG']

    try:
        with open(config_file) as file:
            try:
                data = yaml.safe_load(file)
                if data["enable_global_backup"]:
                    print("Global Backup Enabled")

                    # File Backup
                    backup_files(data)
                else:
                    print("Global Backup Disabled")

            except yaml.YAMLError as exception:
                print(exception)
    except FileNotFoundError:
        print("Configuration file doesn't exist or is incorrect. Please, verify that the FULL_BACKUP_CONFIG environment variable is correct")



# Start App
if __name__ == "__main__":
    main()

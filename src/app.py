import yaml, os, datetime

# Local Imports
from backup.files import backup_files


def main():
    config_file = os.environ['FULL_BACKUP_CONFIG']
    day = datetime.datetime.now().strftime("%d")
    month = datetime.datetime.now().strftime("%m")
    year = datetime.datetime.now().strftime("%Y")

    try:
        with open(config_file) as file:
            try:
                data = yaml.safe_load(file)
                if data['enable_global_backup']:
                    print("Global Backup Enabled")

                    # File Backup
                    backup_files(data, day, month, year)
                else:
                    print("Global Backup Disabled")

            except yaml.YAMLError as exception:
                print(f"Configuration file is incorrect. Please review this error:\n{exception}")
    except FileNotFoundError as exception:
        print(f"Configuration file does not exist or is incorrect. Please review this error:\n{exception}")


# Start App
if __name__ == "__main__":
    main()

import os
import argparse
import shutil

# Create argument parser
parser = argparse.ArgumentParser(description='Backup log files')
parser.add_argument('log_directory', help='path to log directory')
parser.add_argument('backup_directory', help='path to backup directory')

# Parse command-line arguments
args = parser.parse_args()

# Get the list of log files in the log directory
log_files = [
    f for f in os.listdir(args.log_directory)
    if os.path.isfile(os.path.join(args.log_directory, f))
]

# Move each log file to the backup directory
for log_file in log_files:
    log_file_path = os.path.join(args.log_directory, log_file)
    backup_file_path = os.path.join(args.backup_directory, log_file)
    shutil.move(log_file_path, backup_file_path)

print("The files have been successfully moved to "
      + args.backup_directory
      + " directory")

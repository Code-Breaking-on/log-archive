#!/usr/bin/env python3

import argparse
import os
import tarfile
from datetime import datetime
import shutil

def archive_logs(log_dir):
    # Validate the directory
    if not os.path.isdir(log_dir):
        print(f"Error: '{log_dir}' is not a valid directory.")
        return

    # Generate timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    archive_name = f"logs_archive_{timestamp}.tar.gz"
    
    # Create archive directory if not exists
    archive_dir = os.path.join(os.getcwd(), 'archives')
    os.makedirs(archive_dir, exist_ok=True)

    archive_path = os.path.join(archive_dir, archive_name)

    # Create tar.gz archive
    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(log_dir, arcname=os.path.basename(log_dir))

    # Log the archive
    log_entry = f"{timestamp} - Archived {log_dir} to {archive_path}\n"
    with open("archive_log.txt", "a") as log_file:
        log_file.write(log_entry)

    print(f"✅ Logs archived to {archive_path}")

def main():
    parser = argparse.ArgumentParser(description="Archive logs from a directory.")
    parser.add_argument("log_directory", help="The path to the log directory.")
    args = parser.parse_args()

    archive_logs(args.log_directory)

if __name__ == "__main__":
    main()

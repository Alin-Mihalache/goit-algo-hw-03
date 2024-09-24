import os
import shutil
import sys
from pathlib import Path
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Recursively copy and sort files by extension.")
    parser.add_argument("source", help="Path to the source directory")
    parser.add_argument("destination", nargs='?', default="dist", help="Path to the destination directory (default: dist)")
    return parser.parse_args()

def copy_files_recursively(src_dir, dest_dir):
    try:
        # Iterate over all items in the source directory
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            
            if os.path.isdir(src_path):
                # Recursively process subdirectories
                copy_files_recursively(src_path, dest_dir)
            elif os.path.isfile(src_path):
                # Get file extension
                file_extension = Path(src_path).suffix.lstrip(".")
                if file_extension == "":
                    file_extension = "no_extension"
                
                # Create the destination subdirectory path based on the file extension
                dest_path = os.path.join(dest_dir, file_extension)
                
                # Ensure the destination subdirectory exists
                os.makedirs(dest_path, exist_ok=True)
                
                # Copy the file to the destination subdirectory
                shutil.copy2(src_path, dest_path)
                print(f"Copied {src_path} to {dest_path}")
    except Exception as e:
        print(f"An error occured while procesing {src_path}: {e}")
        
def main():
    args = parse_arguments()
    
    source_dir = args.source
    destination_dir = args.destination
    
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exists.")
        sys.exit(1)
        
    # Check if the source path is a directory
    if not os.path.isdir(source_dir):
        print(f"Source path {source_dir} ist not a directory.")
        sys.exit(1)
        
    try:
        # Start the recursive copying process
        copy_files_recursively(source_dir, destination_dir)
        print(f"Files have been copied and sorted into {destination_dir}")
    except Exception as e:
        print(f"An error occured: {e}")
        sys.exit(1)
        
if __name__ == "__main__":
    main()               
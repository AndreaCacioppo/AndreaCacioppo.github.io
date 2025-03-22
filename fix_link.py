#!/usr/bin/env python3
import os
import sys

def replace_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Skipping {file_path}: {e}")
        return

    # Replace the specified strings
    new_content = content.replace("andreacacioppo.github.io", "andreacacioppo.github.io")
    new_content = new_content.replace("andreacacioppo.github.io", "andreacacioppo.github.io")

    # Write back if changes occurred
    if new_content != content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Modified: {file_path}")
        except Exception as e:
            print(f"Error writing to {file_path}: {e}")

def main():
    # Use current folder as default if no folder is provided.
    if len(sys.argv) < 2:
        folder_path = os.getcwd()
        print(f"No folder provided. Using current directory: {folder_path}")
    else:
        folder_path = sys.argv[1]

    # Recursively traverse through the directory
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            replace_in_file(file_path)

if __name__ == "__main__":
    main()
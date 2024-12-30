import os
import re

def remove_text_above_first_main_header_in_file(file_path: str):
    """Remove all content above the first # header in a single file."""
    # Only process .md files, skip index.md
    if not file_path.lower().endswith(".md"):
        return  # Not a markdown file, skip
    if os.path.basename(file_path).lower() == "index.md":
        return  # Skip index.md

    if not os.path.isfile(file_path):
        return  # Path doesn't exist or isn't a file

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into lines
    lines = content.splitlines()

    new_lines = []
    found_header = False

    for line in lines:
        # Check if it starts with "# "
        if not found_header and re.match(r'^\s*#\s', line):
            found_header = True
        # Once we've found the first # header, keep everything from there on
        if found_header:
            new_lines.append(line)

    new_content = "\n".join(new_lines)

    # Write modified content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)


def remove_text_above_first_main_header_in_directory(root_dir: str):
    """Remove all content above the first # header in every .md file under root_dir."""
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            full_path = os.path.join(root, file)
            remove_text_above_first_main_header_in_file(full_path)


if __name__ == "__main__":
    # Prompt user for either a single file path or a directory
    path = input("Enter a single .md file path OR a directory path: ").strip()

    if not path:
        print("No path provided. Exiting.")
        exit(0)

    if os.path.isfile(path):
        # Process just the single file
        remove_text_above_first_main_header_in_file(path)
        print(f"Done trimming content in file: {path}")

    elif os.path.isdir(path):
        # Process all .md files in the directory (recursive)
        remove_text_above_first_main_header_in_directory(path)
        print(f"Done trimming content in directory: {path}")

    else:
        print("Path is not a valid file or directory. Exiting.")

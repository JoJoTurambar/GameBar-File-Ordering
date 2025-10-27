import os
import re

# unique games
UNIQUE_GAMES = []

# Load all files in the current directory
def load_files_in_directory(directory):
    files = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)) and not filename.endswith('.py'):
            files.append(filename)
    return files

def is_date_or_time(part):
    # Check for date format dd-mm-yyyy i.e. 07-02-2025
    re1 = re.compile(r'\d{2}-\d{2}-\d{4}')
    if re1.fullmatch(part):
        return True
        
    # Check for date format dd-mm-yyyy i.e. 2025-02-07
    re2 = re.compile(r'\d{4}-\d{2}-\d{2}')
    if re2.match(part):
        return True
    
    # Check for time format hh_mm_ss i.e. 21_59_54 4_02_15 4-02-15
    re3 = re.compile(r'\d{1,2}[-_]\d{1,2}[-_]\d{1,2}')
    if re3.match(part):
        return True
        
    return False

def clean(filename):
    name, _ = os.path.splitext(filename)
    parts = name.split()

    cleanFile = ' '.join(part for part in parts if not is_date_or_time(part))
    return cleanFile

# Create directory if it doesn't exist and add files to it
def reubicate_files(filenames):

    current_dir = os.getcwd()

    for file in filenames:
        # Create directory for new game
        cleanFile = clean(file)
        newDir = os.path.join(current_dir, cleanFile)

        if not os.path.exists(newDir):
            os.makedirs(newDir)

        # Move file
        src = os.path.join(current_dir, file)
        dst = os.path.join(newDir, file)

        os.rename(src, dst)

# Main
fileNames = load_files_in_directory(os.getcwd())
reubicate_files(fileNames)
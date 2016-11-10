import os
import sys
import exifread
import time
import logging

def get_exif_original_date_time(filename):
    """Returns the original date and time of the specified JPEG file
    """
    logging.debug('Processing {}'.format(filename))
    f = open(filename, 'rb')
    args = exifread.process_file(f, stop_tag='EXIF DateTimeOriginal')
    orig_date_time = str(args['EXIF DateTimeOriginal'])
    return time.strptime(orig_date_time, '%Y:%m:%d %H:%M:%S')

def find_files_with_extension(directory_name, extension):
    """Parses contents of the specified directory, looking for file with the specified extension,
       returns list of matching files
    """
    logging.debug('Directory is: {}'.format(directory_name))
    dirlist = os.listdir(directory_name)
    logging.debug(dirlist)

    matching_files = []

    for file in dirlist:
        if os.path.isdir(file): continue    # skip directories
        file_ext = os.path.splitext(file)[1].strip('.').lower()
        logging.debug('File ext is {}'.format(file_ext))
        if file_ext == extension.lower():
            logging.debug('Found a file: {}'.format(file))
            matching_files.append(file)

    return matching_files

def display_results(directory_name, matching_files):
    # Create a dictionary of the files with their dates
    files_by_date = dict()
    for file in matching_files:
        orig_date_time = get_exif_original_date_time(os.path.join(directory_name, file))
        files_by_date[file] = int('{:04}{:02}{:02}'.format(orig_date_time.tm_year, orig_date_time.tm_mon, orig_date_time.tm_mday))

    # Sort the dictionary by value, newest file first
    # - returns a list of tuples (file:date)
    # - see https://docs.python.org/2/howto/sorting.html#sortinghowto
    sorted_dates = sorted(files_by_date.items(), key=lambda x: x[1], reverse=True)

    # Display each file and its date
    for item in sorted_dates:
        print('Date: {}\t File: {}'.format(item[1], item[0]))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # We expect one argument, a directory containing JPEG files
    if len(sys.argv) < 2:
        print('ERROR: Please specify a directory', file=sys.stderr)
    else:
        matching_files = find_files_with_extension(sys.argv[1], 'jpg')
        display_results(sys.argv[1], matching_files)

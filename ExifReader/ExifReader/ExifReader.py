import os
import sys
import exifread
import time
import logging
import argparse
import subprocess

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
            matching_files.append(os.path.join(directory_name, file))

    return matching_files

def sort_results(matching_files):
    # Create a dictionary of the files with their dates
    files_by_date = dict()
    for file in matching_files:
        orig_date_time = get_exif_original_date_time(file)
        files_by_date[file] = int('{:04}{:02}{:02}'.format(orig_date_time.tm_year, orig_date_time.tm_mon, orig_date_time.tm_mday))

    # Sort the dictionary by value, newest file first
    # - returns a list of tuples (file:date)
    # - see https://docs.python.org/2/howto/sorting.html#sortinghowto
    sorted_dates = sorted(files_by_date.items(), key=lambda x: x[1], reverse=True)

    return sorted_dates
    
def display_results(sorted_dates):
    # Display each file and its date
    for item in sorted_dates:
        print('Date: {}\t File: {}'.format(item[1], item[0]))
    print('{} files'.format(len(sorted_dates)))

def copy_files(dest_dir, sorted_files, dry_run):
    logging.info('Copying files from {}'.format(dest_dir))
    num_copies = 0
    
    for item in sorted_files:
        # item[0] = path_to_file, item[1] = date
        path_to_file = item[0]

        # use the item's date as its destination directory
        target_dir = os.path.join(dest_dir, str(item[1]))

        if not dry_run and not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # copy file to destination
        logging.info('Reading {}'.format(path_to_file))
        if not dry_run:
            src_file = open(path_to_file, 'rb')
            contents = src_file.read()
            src_file.close()        

        target_file_name = os.path.join(target_dir, os.path.basename(path_to_file))
        logging.info('Writing {}'.format(target_file_name))
        if not dry_run:
            dest_file = open(target_file_name, 'wb')
            dest_file.write(contents)
            dest_file.close()

        num_copies += 1

    logging.info('Copied {} files'.format(num_copies))

def main():
    parser = argparse.ArgumentParser(description="JPEG sorter")
    parser.add_argument("src", help="source directory")
    parser.add_argument("--display", help="display candidates", action="store_true")
    parser.add_argument("--log", help="set log level", default=logging.WARNING)
    parser.add_argument("--dest", help="destination directory")
    parser.add_argument("--dry_run", help="perform a dry-run (don't move anything)", action="store_true")

    args = parser.parse_args()

    logging.basicConfig(level=args.log.upper())

    if args.src:
        matching_files = find_files_with_extension(args.src, 'jpg')
        sorted_files = sort_results(matching_files)
        
        if args.display:
            display_results(sorted_files)

        if args.dest:
            # User wants to move the files to a new tree rooted at args.dest
            if not os.path.exists(args.dest):
                logging.info("Creating dir: {}".format(args.dest)) 
                os.makedirs(args.dest)

            move_files(args.dest, sorted_files, args.dry_run)

if __name__ == "__main__":
    main()

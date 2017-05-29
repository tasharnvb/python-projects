def check_for_duplicate(u_file, string):
    """Check if the given string is in the file"""
    try:
        given_file = open(u_file, 'r')
    except IOError as e:
        print('Unable to open the file ' + u_file, '\nEnding program.')
        print(e)
        sys.exit()
    else:
        with given_file:
            f_list = given_file.read().splitlines()
        for line in f_list:
            if string in line:
                return True
        return False

# If this is run as a stand-alone script, check the number of arguments before running
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print(str(len(sys.argv)) + ' arguments found, expected: 3 (script_name file_name string)')
    else:
        f_name = sys.argv[1]
        text = sys.argv[2]
        if check_for_duplicate(f_name, text):
            print('"' + text + '"' + ' was found in file ' + '"' + f_name + '"')
        else:
            print('File ' + '"' + f_name + '"' + ' does not contain the string ' + '"' + text + '"')

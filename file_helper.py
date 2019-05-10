import os


def size_convert(bytes, to_unit='Mb'):
    if "Mb" == to_unit:
        return bytes/1024

def get_stats(path):
    if not os.path.exists(path):
        raise OSError('No path to file %s' %path)

    stats = {}
    stats['size'] = os.path.getsize(path)
    stats['last mod'] = os.path.getmtime(path)

    if os.path.isdir(path):
        _path_to, name = os.path.split(path)
        stats['parent path'] = _path_to
        stats['directory'] = name

    elif os.path.isfile(path):
        name, extension = os.path.splitext(path)
        stats['name'] = name
        stats['extension'] = extension

    return stats


def recursive_find_files(start_directory, pattern='', file_extension=''):
    found_files = []
    for root, directories, filenames in os.walk(start_directory):
        for filename in filenames:
            if pattern in filename:
                name, extension = os.path.splitext(filename)
                if file_extension in extension:
                    found_files.append(os.path.join(root, filename))
    return found_files


def recursive_find_directories(start_directory, pattern=''):
    found_dirs = []
    for root, directories, filenames in os.walk(start_directory):
        for directory in directories:
            if pattern in directory:
                found_dirs.append(os.path.join(root, directory))
    return found_dirs


if __name__ == "__main__":
        #print recursive_find_files('/home/rankink', pattern='key', file_extension='.db')
        #print recursive_find_directories('/home/rankink', pattern='FileBrowser')
        stats = get_stats('/home/rankink/Documents/Camera_Specs.ods')
        print stats
        stats = get_stats('/home/rankink')
        print stats
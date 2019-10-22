import os

directories = []
total_size = 20*1024
root_path = '/home/zurikato/video-backup/'
# root_path = '/media/aleco/DATOS/Films/peliculas/'


folder_size = 0
print "folder size: ", folder_size

def sorted_ls(path):
    mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
    return list(sorted(os.listdir(path), key=mtime))

def delete_files():
    del_list = sorted_ls(root_path)[0:60]
    for dfile in del_list:
        os.remove(root_path + dfile)

def do_main():
    for f in os.listdir(root_path):
        if os.path.isdir(root_path + f):
            directories.append(root_path + f)
    folder_size = total_size / len(directories)
    for d in directories:
        print d
        sum = 0
        for f in os.listdir(d):
            file = d + "/" + f
            if os.path.isfile(file):
                # getting size in bytes
                sum += os.path.getsize(file)
        sum_mb = sum / (1024*1024)
        print("size: " + str(sum_mb))
        print("folder size: " + str(folder_size))

        if sum_mb >= folder_size:
            delete_files()

do_main()

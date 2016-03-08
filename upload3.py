import os
path="/tmp/motion/"
def upload_files():
    if not os.path.exists(path):
        return
    dir_list = os.listdir(path)
    for file_name in dir_list:
        file_full_path = path + file_name
        cmd = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload " + file_full_path
        os.system(cmd)
        os.remove(file_full_path)

if __name__ == "__main__":
    upload_files()

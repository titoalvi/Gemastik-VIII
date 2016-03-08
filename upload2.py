import os

path="/home/pi"
def upload_files():
	if not os.path.exists(path):
		return
	dir_list = os.listdir(path)
	for file_name in dir_list:
		if "avi" in file_name:
			print "upload video"
			cmd = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /tmp/motion/"+"*.avi "+file_name+".avi"
			os.system(cmd)
			#os.remove (path + file_name)

if __name__ == "__main__":
	upload_files()

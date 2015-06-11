import shutil
import os
from config import config

def clean_dir(s):
	if os.path.exists(s):
		shutil.rmtree(s)
	os.mkdir(s)

def make_post_dir():
	# call cleanDir() first
	os.mkdir(config['targetFolder'] + config['targetPostURL'] + "/")

def create_page_folder(idx):
	path = config['targetFolder'] + config['targetPageFolder'] + "/" + str(idx)
	if os.path.exists(path):
		shutil.rmtree(path)
	os.makedirs(path)
	return path

def copy_css_file():
	shutil.copytree(config['templateCSSFolder'], config['targetFolder'] + config['targetCSSFolder'])

def sort_by_time(x, y):
	if x['TimeStr'] < y['TimeStr']:
		return 1
	else:
		return -1

def copy_server_file():
	shutil.copy(config['httpServerPath'], config['targetFolder'] + "/httpserver.py")

def write_as_index(s):
	open(config['targetFolder'] + "/index.html", "w").write(s)


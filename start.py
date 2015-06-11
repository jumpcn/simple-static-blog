# coding=utf-8
from config import config
import os
import utils
from MultiThreaded import PostGenerateThread
import time
from PageGenerator import PageGenerator
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Main:

	def __init__(self):
		
		# getPostFolder
		self.PostFolder = config['post_folder']
		self.targetFolder = config['targetFolder']
		self.PostList = []
		self.get_post_list()

	def get_post_list(self):
		for parent, dirs, fileList in os.walk(self.PostFolder):
			self.PostList = fileList
		self.PostList = map(lambda x: config['post_folder'] + "/" + x, self.PostList)
		self.PostList = [i for i in self.PostList if i[-3:] == ".md"]

	def work_flow(self):
		# print self.PostList
		utils.clean_dir(self.targetFolder)
		utils.make_post_dir()
		post_gen = PostGenerateThread(self.PostList)
		while not post_gen.finish:
			time.sleep(0.1)
		page_gen = PageGenerator(self.PostList)
		utils.copy_css_file()
		utils.copy_server_file()
		#for x in page_gen.all_info: print x
		print "All over"




m = Main()
m.work_flow()

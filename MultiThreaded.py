from PostGenerator import PostGenerator
from threadpool import ThreadPool
from threadpool import makeRequests
import datetime

MAX_GENERATOR = 2
class PostGenerateThread:

	def __init__(self, file_list):
		self.file_list = file_list
		self.finish = False
		self.gen()

	def gen(self):
		start_time = datetime.datetime.now()
		pool = ThreadPool(MAX_GENERATOR)
		request = makeRequests(self.worker, self.file_list)
		for req in request:
			pool.putRequest(req)
		pool.wait()
		self.finish = True
		print "Generate Post Time: ", (datetime.datetime.now() - start_time).microseconds / 1000000.0, "s"

	@staticmethod
	def worker(file_path):
		try:
			m = PostGenerator(file_path)
			m.generator()
		except IndexError:
			print file_path + " can't convert to markdown"
		# print filePath + " generated successful!"


# p = PostGenerateThread([])





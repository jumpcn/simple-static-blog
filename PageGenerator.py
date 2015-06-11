# coding=utf-8
from config import config
from mdfilesplitter import MDFileSplitter
from utils import sort_by_time
from utils import create_page_folder
from utils import write_as_index
import sys
from jinja2 import Template

reload(sys)
sys.setdefaultencoding('utf8')


class PageGenerator:
	def __init__(self, file_list):
		self.fileList = file_list
		divide = int(config['pageCount'])
		self.all_info = []
		for x in file_list:
			info = MDFileSplitter(x).get_info()
			info['url'] = "../../post/" + info['url'][0:-3] + ".html"
			self.all_info.append(info)
		self.all_info.sort(sort_by_time)
		total = len(self.all_info)
		page_num = total / int(divide)
		template = Template(unicode(open(config['templatePage']).read(), "utf-8"))

		if total % divide != 0:
			page_num += 1
		for p in xrange(page_num + 1):
			l = p * divide
			r = (p + 1) * divide
			if r >= total:
				r = total
				has_next = False
			else:
				has_next = True
			if l == 0:
				has_pre = False
			else:
				has_pre = True
			article_slice = self.all_info[l:r]
			path = create_page_folder(p + 1)
			result = template.render(article_list=article_slice, Title=config['BlogName'], Pre=has_pre, Next=has_next,
			                         prePageURL="../../page/" + str(p), nextPageURL="../../page/" + str(p + 2))
			open(path + "/index.html", "w").write(result)
			if p == 0:
				write_as_index(result)
			if r == total:
				break

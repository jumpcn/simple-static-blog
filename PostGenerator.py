# -*- coding: utf-8 -*-
from jinja2 import Template
from config import config
from post import Post
from mdfilesplitter import MDFileSplitter
import sys
# template = Template('Hello {{name}}!')
# print template.render(name='Isun')

reload(sys)
sys.setdefaultencoding('utf8')


class PostGenerator:
	def __init__(self, article_path):
		# get file_path to URL
		self.URL = str(article_path.split('/')[-1]).replace(".md", "")
		# split MD file to get info
		self.info = MDFileSplitter(article_path).get_info()
		# convert to MD
		self.articleMD = Post(self.info['Content']).get_markdown()

	def generator(self):
		# render to html
		template = Template(unicode(open(config['templatePost']).read(), "utf-8"))
		result = template.render(Title=self.info['title'], ArticleMarkdown=self.articleMD)
		open(config['targetFolder'] + config['targetPostURL'] + "/" + self.URL + ".html", "w").write(result)

# m = PostGenerator("./posts/dp-problems-on-leetcode.md")
# m.generator()

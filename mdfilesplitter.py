# coding=utf-8
import os
class MDFileSplitter:

    def __init__(self, s):
        self.path = s
        self.file = open(s)
        self.article_summary = ""
        self.splitter()

    def splitter(self):
        url = os.path.basename(self.path)
        title = self.file.readline().replace(' ', '').replace('\'', '').replace('title:', '').strip()  # title
        time_in = map(lambda x: x.strip(), str(self.file.readline()).split(' '))  # time
        time_str = time_in[1] + ' ' + time_in[2]
        categories = self.file.readline().replace(' ', '').replace('categories:', '')  # categories
        #  skip article splitter
        self.file.readline()
        # contents
        content = self.file.read()

        # summary
        self.article_summary = {'url': url, 'title': title, 'TimeStr': time_str, 'Categories': categories,
                                'Content': content}

    def get_info(self):
        return self.article_summary

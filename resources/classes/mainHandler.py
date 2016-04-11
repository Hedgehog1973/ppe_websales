from handler import *
from databases import *
from .. import funct

class MainHandler(Handler):
	def get(self, page_name=""):
		if not self.user:
			self.redirect('/login')
		else:
			self.render('home.html', user=self.user)
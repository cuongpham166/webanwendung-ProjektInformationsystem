 #coding: utf-8

# In dieser Variante die Markup-Erzeugung mit Hilfe einer Template-Engine durchführen


import codecs
import os.path
import string

from mako.template import Template
from mako.lookup import TemplateLookup

class View_kunden(object):
	def __init__(self):
		self.path_tpl = os.path.join(os.path.abspath("./"), "content")
		self.lookup_o = TemplateLookup(directories=[self.path_tpl])

	def readFile_p(self, fileName_spl):

		content = ''
		with codecs.open(os.path.join('content', fileName_spl), 'r', 'utf-8') as fp_o:
			content = fp_o.read()

		return content

	def createKundenList(self, data_opl):
		template_o = self.lookup_o.get_template("KundenList.tpl")
		return template_o.render(data_o=data_opl)

	def createKundenForm(self, id_spl, data_opl):
		id_s = id_spl
		data_opl.append(id_spl)
		print (data_opl)
		template_o = self.lookup_o.get_template("KundenForm.tpl")
		return template_o.render(data_o = data_opl)
###########################################################################################################

class View_projekt(object):
	def __init__(self):
		self.path_tpl = os.path.join(os.path.abspath("./"), "content")
		self.lookup_o = TemplateLookup(directories=[self.path_tpl])

	def readFile_p(self, fileName_spl):

		content = ''
		with codecs.open(os.path.join('content', fileName_spl), 'r', 'utf-8') as fp_o:
			content = fp_o.read()

		return content

	def createProjektList(self, data_opl):
		template_o = self.lookup_o.get_template("ProjektList.tpl")
		return template_o.render(data_o=data_opl)

	def createProjektForm(self, data_opl):
		
		print (data_opl)
		template_o = self.lookup_o.get_template("ProjektForm.tpl")
		return template_o.render(data_o = data_opl)

#############################################################################################

class View_mitarbeiter(object):
	def __init__(self):
		self.path_tpl = os.path.join(os.path.abspath("./"), "content")
		self.lookup_o = TemplateLookup(directories=[self.path_tpl])

	def readFile_p(self, fileName_spl):

		content = ''
		with codecs.open(os.path.join('content', fileName_spl), 'r', 'utf-8') as fp_o:
			content = fp_o.read()

		return content

	def createMitarbeiterList(self, data_opl):
		template_o = self.lookup_o.get_template("MitarbeiterList.tpl")
		return template_o.render(data_o=data_opl)

	def createMitarbeiterForm(self, id_spl, data_opl):
		id_s = id_spl
		data_opl.append(id_spl)
		print (data_opl)
		template_o = self.lookup_o.get_template("MitarbeiterForm.tpl")
		return template_o.render(data_o = data_opl)
#############################################################################################

class View_aufwendung(object):
	def __init__(self):
		self.path_tpl = os.path.join(os.path.abspath("./"), "content")
		self.lookup_o = TemplateLookup(directories=[self.path_tpl])

	def readFile_p(self, fileName_spl):
		content = ''
		with codecs.open(os.path.join('content', fileName_spl), 'r', 'utf-8') as fp_o:
			content = fp_o.read()

		return content

	def createAufwendungForm(self,data_opl):
		#id_s1=id_spl
		template_o = self.lookup_o.get_template("AufwendungForm.tpl")
		return template_o.render(data_o = data_opl)

#############################################################################################
class View_homepage(object):
	def __init__(self):
		self.path_tpl = os.path.join(os.path.abspath("./"), "content")
		self.lookup_o = TemplateLookup(directories=[self.path_tpl])

	def readFile_p(self, fileName_spl):

		content = ''
		with codecs.open(os.path.join('content', fileName_spl), 'r', 'utf-8') as fp_o:
			content = fp_o.read()

		return content

	def createHomepage(self):
		template_o = self.lookup_o.get_template("Homepage.tpl")
		return template_o.render()
##############################################################################################
class View_ubersicht(object):

	def __init__(self):
		self.path_tpl = os.path.join(os.path.abspath("./"), "content")
		self.lookup_o = TemplateLookup(directories=[self.path_tpl])

	def readFile_p(self, fileName_spl):

		content = ''
		with codecs.open(os.path.join('content', fileName_spl), 'r', 'utf-8') as fp_o:
			content = fp_o.read()

		return content

	def createUbersicht(self, data_opl):
		template_o = self.lookup_o.get_template("ProjektUbersicht.tpl")
		return template_o.render(data_o=data_opl)


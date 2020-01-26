# coding: utf-8

import os
import os.path
import codecs

import json

class Database_kunden(object):
	def __init__(self):
		self.data_o = {}
		self.readData_p()
		self.data_o_count = len(self.data_o)

	def create_px(self, data_opl):
		id_s = None

		if self.data_o_count !=0:
			id_s=str(self.data_o_count)
			self.data_o[id_s]=data_opl
			self.saveData_p()
			#print (data_opl)
			self.data_o_count +=1

		else:
			id_s=str(0)
			self.data_o[id_s]=data_opl
			self.saveData_p()
			self.data_o_count +=1
			#print (data_opl)

		return id_s

	def read_px(self, id_spl = None):

		data_o = None
		if id_spl == None:
			data_o = self.data_o
		else:
			if id_spl in self.data_o:
				data_o = self.data_o[id_spl]
		return data_o

	def update_px(self, id_spl, data_opl):
		status_b = False
		if id_spl in self.data_o:
			self.data_o[id_spl] = data_opl
			self.saveData_p()
			status_b = True 
		return status_b

	def saveData_p(self):
		with codecs.open(os.path.join('data','kunden.json'),'w', 'utf-8') as fp_o:
			json.dump(self.data_o, fp_o)

	def delete_px(self, id_spl):
		status_b = True
		if id_spl in self.data_o:
			for i in range(int(id_spl), self.data_o_count-1):
				self.data_o[str(i)]=self.data_o[str(i+1)]
			self.data_o.pop(str(self.data_o_count-1))
			self.data_o_count -= 1
			status_b = True
			self.saveData_p();
		return status_b

	def getDefault_px(self):
		return ["","","",""]

       
	def readData_p(self):
		try:
			fp_o = codecs.open(os.path.join('data', 'kunden.json'), 'r', 'utf-8')
		except:
			self.data_o = {}
			self.saveData_p()
		else:
			with fp_o:
				self.data_o = json.load(fp_o)
		return

##############################################################################################################

class Database_projekt(object):
	def __init__(self):
		self.data_o = {}
		self.readData_p()
		self.data_o_count = len(self.data_o)

	def create_px(self, data_opl):
		id_s = None

		if self.data_o_count !=0:
			id_s=str(self.data_o_count)
			self.data_o[id_s]=data_opl
			self.saveData_p()
			#print (data_opl)
			self.data_o_count +=1

		else:
			id_s=str(0)
			self.data_o[id_s]=data_opl
			self.saveData_p()
			self.data_o_count +=1
			#print (data_opl)

		return id_s

	def read_px(self, id_spl = None):

		data_o = None
		if id_spl == None:
			data_o = self.data_o
		else:
			if id_spl in self.data_o:
				data_o = self.data_o[id_spl]
		return data_o

	def update_px(self, id_spl, data_opl):
		status_b = False
		if id_spl in self.data_o:
			self.data_o[id_spl] = data_opl
			self.saveData_p()
			status_b = True 
		return status_b

	def saveData_p(self):
		with codecs.open(os.path.join('data','projekt.json'),'w', 'utf-8') as fp_o:
			json.dump(self.data_o, fp_o)

	def delete_px(self, id_spl):
		status_b = True
		if id_spl in self.data_o:
			for i in range(int(id_spl), self.data_o_count-1):
				self.data_o[str(i)]=self.data_o[str(i+1)]
			self.data_o.pop(str(self.data_o_count-1))
			self.data_o_count -= 1
			status_b = True
			self.saveData_p();
		return status_b

	def getDefault_px(self):
		return ["","","","","",""]

       
	def readData_p(self):
		try:
			fp_o = codecs.open(os.path.join('data', 'projekt.json'), 'r', 'utf-8')
		except:
			self.data_o = {}
			self.saveData_p()
		else:
			with fp_o:
				self.data_o = json.load(fp_o)
		return

#################################################################################################

class Database_mitarbeiter(object):
	def __init__(self):
		self.data_o = {}
		self.readData_p()
		self.data_o_count = len(self.data_o)

	def create_px(self, data_opl):
		id_s = None

		if self.data_o_count !=0:
			id_s=str(self.data_o_count)
			self.data_o[id_s]=data_opl
			self.saveData_p()
			print (data_opl)
			self.data_o_count +=1

		else:
			id_s=str(0)
			self.data_o[id_s]=data_opl
			self.saveData_p()
			self.data_o_count +=1
			print (data_opl)

		return id_s

	def read_px(self, id_spl = None):

		data_o = None
		if id_spl == None:
			data_o = self.data_o
		else:
			if id_spl in self.data_o:
				data_o = self.data_o[id_spl]
		return data_o

	def update_px(self, id_spl, data_opl):
		status_b = False
		if id_spl in self.data_o:
			self.data_o[id_spl] = data_opl
			self.saveData_p()
			status_b = True 
		return status_b

	def saveData_p(self):
		with codecs.open(os.path.join('data','mitarbeiter.json'),'w', 'utf-8') as fp_o:
			json.dump(self.data_o, fp_o)

	def delete_px(self, id_spl):
		status_b = True
		if id_spl in self.data_o:
			for i in range(int(id_spl), self.data_o_count-1):
				self.data_o[str(i)]=self.data_o[str(i+1)]
			self.data_o.pop(str(self.data_o_count-1))
			self.data_o_count -= 1
			status_b = True
			self.saveData_p();
		return status_b

	def getDefault_px(self):
		return ["","",""]

       
	def readData_p(self):
		try:
			fp_o = codecs.open(os.path.join('data', 'mitarbeiter.json'), 'r', 'utf-8')
		except:
			self.data_o = {}
			self.saveData_p()
		else:
			with fp_o:
				self.data_o = json.load(fp_o)
		return


class Database_aufwendung(object):
	def __init__(self):
		self.data_o = {}
		self.readData_p()
		self.data_o_count = len(self.data_o)

	def create_px(self, data_opl):
		id_s1 = None

		if self.data_o_count !=0:
			id_s1=str(self.data_o_count)
			self.data_o[id_s1]=data_opl
			self.saveData_p()
			print (data_opl)
			self.data_o_count +=1

		else:
			id_s1=str(0)
			self.data_o[id_s1]=data_opl
			self.saveData_p()
			self.data_o_count +=1
			print (data_opl)

		return id_s1

	def getDefault_px(self):
		return ["",""]

	def update_px(self, id_spl, data_opl):
		status_b = False
		if id_spl in self.data_o:
			self.data_o[id_spl] = data_opl
			self.saveData_p()
			status_b = True 
		return status_b

	def saveData_p(self):
		with codecs.open(os.path.join('data','projektmitarbeiter.json'),'w', 'utf-8') as fp_o:
			json.dump(self.data_o, fp_o)

	def delete_px(self, id_spl):
		status_b = True
		if id_spl in self.data_o:
			for i in range(int(id_spl), self.data_o_count-1):
				self.data_o[str(i)]=self.data_o[str(i+1)]
			self.data_o.pop(str(self.data_o_count-1))
			self.data_o_count -= 1
			status_b = True
			self.saveData_p();
		return status_b	


	def read_px(self, id_spl = None):

		data_o = None
		if id_spl == None:
			data_o = self.data_o
		else:
			if id_spl in self.data_o:
				data_o = self.data_o[id_spl]
		return data_o	

	def readData_p(self):
		try:
			fp_o = codecs.open(os.path.join('data', 'projektmitarbeiter.json'), 'r', 'utf-8')
		except:
			self.data_o = {}
			self.saveData_p()
		else:
			with fp_o:
				self.data_o = json.load(fp_o)
		return

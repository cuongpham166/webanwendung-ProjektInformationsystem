# coding: utf-8

import cherrypy
from .database import Database_kunden
from .view import View_kunden
from .database import Database_projekt
from .view import View_projekt
from .view import View_mitarbeiter
from .database import Database_mitarbeiter
from .view import View_homepage
from .view import View_ubersicht
from .view import View_aufwendung
from .database import  Database_aufwendung
import collections

class Application_cl(object):

	def __init__(self):
		self.db_kunden = Database_kunden()
		self.view_kunden = View_kunden ()
		self.db_projekt = Database_projekt()
		self.view_projekt = View_projekt()
		self.view_mitarbeiter = View_mitarbeiter()
		self.db_mitarbeiter = Database_mitarbeiter()
		self.view_homepage = View_homepage()
		self.view_ubersicht = View_ubersicht()
		self.view_aufwendung = View_aufwendung()
		self.db_aufwendung = Database_aufwendung()

	@cherrypy.expose
	def index(self):
		return self.view_homepage.createHomepage()

	"""
	@cherrypy.expose
	def ubersicht(self):
		data = {}
		data["projekt"]=self.db_projekt.data_o
		data["mitarbeiter"]=self.db_mitarbeiter.data_o
		print(data)
		print(data["projekt"]["0"][2])
		aufwendung=[]
		for i in self.db_projekt.data_o:
			total=0
			for j in self.db_projekt.data_o[i][6]:
				for x in range(0, len(self.db_projekt.data_o[i][6][j])):
					total = total + int(self.db_projekt.data_o[i][6][j][x])
			print(total)
			aufwendung.append(str(total))
			print(aufwendung)

		for i in data["projekt"]:
			data["projekt"][i].append(aufwendung[int(i)])
		print(data)
		#for i in data["projekt"]:
		#data["projekt"].append(totalaufwedung())
		return self.view_ubersicht.createUbersicht(data)
	"""
	"""
	@cherrypy.expose
	def totalaufwedung(self):
		aufwendung=[]
		for i in self.db_projekt.data_o:
			total = 0
			for j in self.db_projekt.data_o[i][6]:
				for x in range(0,len(self.db_projekt.data_o[i][6][j])):
					total = total + int(self.db_projekt.data_o[i][6][j][x])
			print(total)
			aufwendung.append(str(total))
			print(aufwendung)
		return aufwendung
"""
	@cherrypy.expose
	def addKunden(self):
		return self.createKundenForm_p()

	@cherrypy.expose
	def listKunden(self):
		print(self.db_kunden.data_o)
		return self.view_kunden.createKundenList(self.db_kunden.data_o)

	@cherrypy.expose
	def editKunden(self, id):
		return self.createKundenForm_p(id)
		
	@cherrypy.expose
	def saveKunden(self, **data_opl):

		id_s = data_opl["id_s"]
		
		data_o = [ data_opl["nummer_s"]
		, data_opl["bezeichnung_s"]
		, data_opl["ansprechpartner_s"]
		, data_opl["ort_s"]
		]

		print( id_s)

		if id_s != "None":
			self.db_kunden.update_px(id_s, data_o)
			print (1)
		else:
			id_s = self.db_kunden.create_px(data_o)
			print (2)
		print(data_o)
		return  self.view_kunden.createKundenList(self.db_kunden.data_o)#self.view_kunden.createKundenForm(id_s, data_o)


	@cherrypy.expose
	def deleteKunden(self, id):
		list = self.getIdProjektbyKunden(id)
		list.sort(reverse = True)
		for i in list:
			self.db_projekt.delete_px(i)
			self.db_aufwendung.delete_px(self.get_aufwendungID_by_Projekt(i))
			self.edit_projectID_in_aufwendung(i)
		for x in range(0, len(self.db_projekt.data_o)):
			if self.db_projekt.data_o[str(x)][5] > id:
				self.db_projekt.data_o[str(x)][5]=str(int(self.db_projekt.data_o[str(x)][5])-1)
		self.db_kunden.delete_px(id)
		return self.createKundenList_p()

	@cherrypy.expose
	def getIdProjektbyKunden(self, id): #id: ID Kunden
		listIdProjektByKunden = []
		for i in self.get_projektid():
			if self.db_projekt.data_o[i][5] == id:
				listIdProjektByKunden.append(i)
		return listIdProjektByKunden

	@cherrypy.expose	
	def get_projektid(self):
		listprojektid=[]
		for i in self.db_projekt.data_o:
			listprojektid.append(i)
		print (listprojektid)
		return listprojektid


	@cherrypy.expose
	def default(self, *arguments, **kwargs):
		msg_s = "unbekannte Anforderung: " + \
				str(arguments) + \
				'' + \
				str(kwargs)

		raise cherrypy.expose.HTTPError(404, msg_s)


	@cherrypy.expose
	def createKundenForm_p(self, id_spl = None):
		if id_spl != None:
			data_o = self.db_kunden.read_px(id_spl)
		else:
			data_o = self.db_kunden.getDefault_px()
		return self.view_kunden.createKundenForm(id_spl, data_o)

	@cherrypy.expose
	def createKundenList_p(self):
		data_o = self.db_kunden.read_px()
		print (data_o)
		return self.view_kunden.createKundenList(data_o)

################################################################################

#################################################################################
	@cherrypy.expose
	def addProjekt(self):
		return self.createProjektForm_p()

	@cherrypy.expose
	def listProjekt(self):
		print (self.db_projekt.data_o)
		return self.view_projekt.createProjektList(self.db_projekt.data_o)

	@cherrypy.expose
	def editProjekt(self, id):
		return self.createProjektForm_p(id)
		
	@cherrypy.expose
	def saveProjekt(self, **data_opl):
		print(data_opl)
		id_s = data_opl["id_s"]	
		
		data_o = [ data_opl["nummer_s"]
		, data_opl["bezeichnung_s"]
		, data_opl["beschreibung_s"]
		, data_opl["bearbeitungszeitraum_s"]
		, data_opl["budget_s"]
		,data_opl["kunden_s"]
		]

		"""
		data = {}
		print(id_s)
		for i in self.get_mitarbeiterlist():
			str_mit="mitarbeiter_" + i
			str_auf="aufwendung_" + i
			data_o1=[data_opl[str_mit]
					 ,data_opl[str_auf]
					 ]
			if len(data_o1[0]) == 2:
				#print(data_o1)
				data[i] = [data_opl[str_auf]]

				
		print (data)
		data_o.append(data)
		#print(data_opl)
		
		#print(data_o[5])
		#print( id_s)
		"""

		if id_s != "None":
			#self.db_projekt.update_px(id_s, data_o)
			if data_o[3] == self.db_projekt.data_o[id_s][3]:
				print(1)
				self.db_projekt.update_px(id_s, data_o)
			else:
				print(2)
				self.db_aufwendung.delete_px(self.get_aufwendungID_by_Projekt(id_s))
				self.db_projekt.update_px(id_s, data_o)
			#self.db_projektmitarbeiter.update_px(id_s,data)
		else:
			print(3)
			id_s = self.db_projekt.create_px(data_o)
			#id_s = self.db_projektmitarbeiter.create_px(data)
			#print(data)
			#print (2)
		#print (data_o1)
		#print(data_o)
		return self.view_projekt.createProjektList(self.db_projekt.data_o)


	@cherrypy.expose
	def deleteProjekt(self, id):
		self.db_projekt.delete_px(id)
		print (self.get_aufwendungID_by_Projekt(id))
		self.db_aufwendung.delete_px(self.get_aufwendungID_by_Projekt(id))
		self.edit_projectID_in_aufwendung(id)
		return self.createProjektList_p()

	@cherrypy.expose
	def default(self, *arguments, **kwargs):
		msg_s = "unbekannte Anforderung: " + \
				str(arguments) + \
				'' + \
				str(kwargs)

		raise cherrypy.expose.HTTPError(404, msg_s)

	@cherrypy.expose
	def get_kundenlist(self):
		#Dictionary von Kunden
		#db_kunden.fp_o
		listKunden =[]
		for i in self.db_kunden.data_o:
			listKunden.append(i)

		for g in listKunden:
			print(g)
			pass
		print (listKunden)
		return listKunden
		
	@cherrypy.expose
	def get_mitarbeiterlist(self):
		listMitarbeiter=[]
		for i in self.db_mitarbeiter.data_o:
			listMitarbeiter.append(i)
		print (listMitarbeiter)
		return listMitarbeiter

	@cherrypy.expose
	def createProjektForm_p(self, id_spl = None):
		data_o = {}
		data_o["kunden"] = self.get_kundenlist()
		print(data_o)
		data_o["mitarbeiter"] = {}
		for i in self.get_mitarbeiterlist():
			data_o["mitarbeiter"][i]=['0']

		if id_spl != None:
			data_o["project"] = self.db_projekt.read_px(id_spl)
			"""
			for i in  data_o["project"][6]:
				data_o["mitarbeiter"][i] = data_o["project"][6][i]
			"""
		else:
			data_o["project"] = self.db_projekt.getDefault_px()
		print (data_o)
		data_o["project"].append (id_spl)
		data_o["project"].append (self.get_kundenlist())
		print (data_o)
		return self.view_projekt.createProjektForm(data_o)
	
	

	@cherrypy.expose
	def createProjektList_p(self):
		data_o = self.db_projekt.read_px()
		return self.view_projekt.createProjektList(data_o)
#########################################################################################

	@cherrypy.expose
	def addMitarbeiter(self):
		return self.createMitarbeiterForm_p()

	@cherrypy.expose
	def listMitarbeiter(self):
		print (self.db_mitarbeiter.data_o)
		return self.view_mitarbeiter.createMitarbeiterList(self.db_mitarbeiter.data_o)
		

	@cherrypy.expose
	def editMitarbeiter(self, id):
		return self.createMitarbeiterForm_p(id)
		
	@cherrypy.expose
	def saveMitarbeiter(self, **data_opl):

		id_s = data_opl["id_s"]
		
		data_o = [ data_opl["name_s"]
		, data_opl["vorname_s"]
		, data_opl["funktion_s"]
		]

		print(id_s)

		if id_s != "None":
			self.db_mitarbeiter.update_px(id_s, data_o)
			print (1)
		else:
			id_s = self.db_mitarbeiter.create_px(data_o)
			print (2)
		print(data_o)
		return self.view_mitarbeiter.createMitarbeiterList(self.db_mitarbeiter.data_o)



	@cherrypy.expose
	def deleteMitarbeiter(self, id):
		list = self.get_aufwendungID(id)
		list.sort(reverse = True)
		print (list)
		for i in list:
			self.db_aufwendung.delete_px(i)
			print (self.db_aufwendung.data_o)
		self.db_mitarbeiter.delete_px(id)
		self.edit_mitarbeiterID_in_Aufwendung(id)
		return self.createMitarbeiterList_p()

	@cherrypy.expose
	def default(self, *arguments, **kwargs):
		msg_s = "unbekannte Anforderung: " + \
				str(arguments) + \
				'' + \
				str(kwargs)

		raise cherrypy.expose.HTTPError(404, msg_s)


	@cherrypy.expose
	def createMitarbeiterForm_p(self, id_spl = None):
		if id_spl != None:
			data_o = self.db_mitarbeiter.read_px(id_spl)
		else:
			data_o = self.db_mitarbeiter.getDefault_px()
		return self.view_mitarbeiter.createMitarbeiterForm(id_spl, data_o)

	@cherrypy.expose
	def createMitarbeiterList_p(self):
		data_o = self.db_mitarbeiter.read_px()
		print (data_o)
		return self.view_mitarbeiter.createMitarbeiterList(data_o)

	@cherrypy.expose
	def aufwendung(self):
		data_o = self.db_projektmitarbeiter.read_px()
		print (data_o)

	@cherrypy.expose
	def getProjektIDbyAufwendung(self):
		listProjektInAufwendung=[]
		for i in self.db_aufwendung.data_o:
			listProjektInAufwendung.append(i)
		return listProjektInAufwendung

	@cherrypy.expose
	def saveAufwendung(self, **data_opl):
		print(data_opl)
		projektID = data_opl["projektID"]
		id_s1 = projektID

		data_o = {"Projekt":[projektID,self.db_projekt.data_o[projektID][3]],
					"mitarbeiter":{}
					}
		#for i in self.db_aufwendung.data_o[id_s1]["mitarbeiter"]:
		for i in self.db_mitarbeiter.data_o:
			data = []
			mitarbeiter_str = "mitarbeiter_" + i
			##data.append(i)
			for j in range(0, int(self.db_projekt.data_o[projektID][3])):
				if(len(data_opl[mitarbeiter_str])==2):
					aufwendung_str = "aufwendung_" + i + "_" +str(j)
					print(aufwendung_str)
					data.append(data_opl[aufwendung_str])
					print(data)
					data_o["mitarbeiter"][i] = data

		print(data_o)

		if id_s1 in  self.get_projectID_in_Aufwendung():
			print(1)

			self.db_aufwendung.update_px(id_s1, data_o)
		else:
			print(2)
			id_s1 = self.db_aufwendung.create_px(data_o)
		print(data_o)
		print(id_s1)
		return self.view_projekt.createProjektList(self.db_projekt.data_o)

	@cherrypy.expose
	def Aufwendung(self,id_spl):
		print(id_spl)
		data = {}
		data["projekt"]=[]
		data["projekt"].append(id_spl)
		data["projekt"].append(self.db_projekt.data_o[id_spl][3])
		#if(len(self.db_aufwendung.data_o) == 0 ):
		x = self.get_aufwendungID_by_Projekt(id_spl)
		print (x)
		if x == "-1":
			data["mitarbeiter"]={}
			for i in self.get_mitarbeiterlist():
				data["mitarbeiter"][i]=[]
				for j in range(0,int(self.db_projekt.data_o[id_spl][3])):
					data["mitarbeiter"][i].append("")
			print(data)
		else:
			data["mitarbeiter"]={}
			for i in self.get_mitarbeiterlist(): #self.db_aufwendung.data_o[id_spl]["mitarbeiter"]:
				data["mitarbeiter"][i]=[]
				if i not in self.db_aufwendung.data_o[self.get_aufwendungID_by_Projekt(id_spl)]["mitarbeiter"]:
					for j in range(0,int(self.db_projekt.data_o[id_spl][3])):
						data["mitarbeiter"][i].append("")
						#data["mitarbeiter"][i].append("")
				else:
					data["mitarbeiter"][i] = self.db_aufwendung.data_o[self.get_aufwendungID_by_Projekt(id_spl)]["mitarbeiter"][i]
					print (data)

		#for i in self.get_mitarbeiterlist():
			#data["mitarbeiter"][i]=[]

		print(data)
		return self.view_aufwendung.createAufwendungForm(data)

	@cherrypy.expose
	def editAufwendung(self, id_spl):

		data = {}
		data["projekt"]=[]
		data["mitarbeiter"]=[]

		return self.view_aufwendung.createAufwendungForm(id)

	@cherrypy.expose
	def uberSicht(self):
		data = {}
		data["aufwendung"]=self.db_aufwendung.data_o

		for i in data["aufwendung"]:
			data["aufwendung"][i]["Aufwendung"]={}
			for j in range(0, int(data["aufwendung"][i]["Projekt"][1])):
				total=0
				for x in data["aufwendung"][i]["mitarbeiter"]:
					total=total + int(data["aufwendung"][i]["mitarbeiter"][x][j])
				#print(total)
				data["aufwendung"][i]["Aufwendung"][str(j)]=str(total)
		#print(data)

		thisdict={}
		for i in data["aufwendung"]:
			thisdict[i]=[]
			for j in data["aufwendung"][i]["Aufwendung"]:
				#print(data["aufwendung"][i]["Aufwendung"][j])
				thisdict[i].append(data["aufwendung"][i]["Aufwendung"][j])
			#print(thisdict)

		data["projekt"]={}

		for i in self.get_projectID_in_Aufwendung():
			data["projekt"][i]=[self.db_projekt.data_o[i][1]]
			listMitarbeiterNameByIDProjekt=[]
			for j in data["aufwendung"][self.get_aufwendungID_by_Projekt(i)]["mitarbeiter"]:
				listMitarbeiterNameByIDProjekt.append(self.db_mitarbeiter.data_o[j][0])
			newlist=sorted(listMitarbeiterNameByIDProjekt)
			#print(newlist)
			data["projekt"][i].append(newlist)
		#print(data["projekt"])

		for k in data["projekt"]:
			data["projekt"][k].append(thisdict[self.get_aufwendungID_by_Projekt(k)])
		#print(data["projekt"])

		x=collections.OrderedDict(sorted(data["projekt"].items(), key=lambda e:e[1][0]))
		data_o=dict(x)
		print(data_o) 

		return self.view_ubersicht.createUbersicht(data_o)

	def get_projectID_in_Aufwendung(self):
		data =[]
		for i in self.db_aufwendung.data_o:
			data.append(self.db_aufwendung.data_o[i]["Projekt"][0])
		return data

	def get_aufwendungID_by_Projekt(self,projektID):
		if(len(self.db_aufwendung.data_o) == 0):
			return "-1"
		for i in self.db_aufwendung.data_o:
			if self.db_aufwendung.data_o[i]["Projekt"][0] == projektID:
				return i
		else:
			return "-1"

	def get_aufwendungID(self, id):
		newList=[]
		for i in self.db_aufwendung.data_o:
			for j in self.db_aufwendung.data_o[i]["mitarbeiter"]:
				if(j == id):
					newList.append(i);
		print("list112211212121212121")
		print(newList)
		return newList


	def edit_mitarbeiterID_in_Aufwendung(self,mitarbeiterID):
		for i in self.db_aufwendung.data_o:
			data = {}
			for j in self.db_aufwendung.data_o[i]["mitarbeiter"]:
				if (int(j) > int(mitarbeiterID)):
					print(j)
					data[str(int(j)-1)] = self.db_aufwendung.data_o[i]["mitarbeiter"][j]
					#self.db_aufwendung.data_o[i]["mitarbeiter"].pop(j);
				else:
					data[j] = self.db_aufwendung.data_o[i]["mitarbeiter"][j]
			print("datasasasqsaasasasassa")
			print (data)	
			print(self.db_aufwendung.data_o[i]["mitarbeiter"])
			self.db_aufwendung.data_o[i]["mitarbeiter"] = data;

	def edit_projectID_in_aufwendung(self,projektID):
		for i in self.db_aufwendung.data_o:
			j = self.db_aufwendung.data_o[i]["Projekt"][0]
			if(int(j) > int(projektID)):
				self.db_aufwendung.data_o[i]["Projekt"][0] = str(int(j)-1)
				
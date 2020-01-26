## coding: utf-8
<!DOCTYPE html>
<html>
	<head>
		<title>Projekt-List</title>
		<meta charset="utf-8">
		<link rel="stylesheet" type="text/css" href="../content/ProjektList.css">
	</head>

	<body>
		<h1>Projekt-List</h1>
		<div id="container">
			<table id="myTable">
				<tr>
					<th>ID</th>
					<th>Kunden</th>
					<th>Nummer</th>
					<th>Bezeichnung</th>
					<th>Beschreibung</th>
					<th>Bearbeitungszeitraum (Woche)</th>	
					<th>Budget</th>
				</tr>
					% for key_s in data_o:
				<tr id = "${key_s}">
					<td>${key_s}</td>
					<td>${data_o[key_s][5]}</td>
					<td>${data_o[key_s][0]}</td>
					<td>${data_o[key_s][1]}</td>
					<td>${data_o[key_s][2]}</td>
					<td>${data_o[key_s][3]}</td>
					<td>${data_o[key_s][4]}</td>
				</tr>
					% endfor
			</table>
		</div>
		<div  class="button">
			<a href="/addProjekt">Add</a>
		</div>
		<div  class="button">
			<a href="" id="deleteprojekt">Delete</a>
		</div>
		<div  class="button">
			<a href="" id ="bearbeitenprojekt">Bearbeiten</a>
		</div>
		<div class="button">
			<a href="" id="aufwendung">Aufwendung</a>
		</div>
		<!--<div class="button">
			<a href="" id="aufwendungbearbeiten">Aufwendung Bearbeiten</a>
		</div>-->
		<div  class="button">
			<a href="/" title="Zurück zur Startseite" >Zurück zur Startseite</a>
		</div>	
		<script type="text/javascript" src="../content/List.js"></script>
	</body>
</html>

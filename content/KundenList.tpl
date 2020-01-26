## coding: utf-8
<!DOCTYPE html>
<html>
<head>
	<title>Kunden-List</title>
	<meta charset="utf-8">	
	<link rel="stylesheet" type="text/css" href="../content/style.css">
</head>
<body>
	<h1>Kunden-List</h1>
	<div id="container">
		<table id="myTable">
			<tr>
				<th>ID</th>
				<th>Nummer</th>
				<th>Bezeichnung</th>
				<th>Ansprechpartner</th>
				<th>Ort</th>
			</tr>
			% for key_s in data_o:
			<tr id = "${key_s}">
				<td>${key_s}</td>
				<td>${data_o[key_s][0]}</td>
				<td>${data_o[key_s][1]}</td>
				<td>${data_o[key_s][2]}</td>
				<td>${data_o[key_s][3]}</td>
			</tr>
			% endfor
		</table>
	</div>
	<div class="button">
		<a href="/addKunden" >Add</a>
	</div>
	<div class="button">
		<a href="" id="deletekunden">Delete</a>
	</div>
	<div class="button">
		<a href="" id ="bearbeitenkunden">Bearbeiten</a> 
	</div>
	<div class="button">
		<a href="/" title="Zurück zur Startseite">Zurück zur Startseite</a>
	</div>
	<script type="text/javascript" src="../content/KundenList.js"></script>
</body>
</html>

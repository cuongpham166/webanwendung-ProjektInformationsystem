## coding: utf-8
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Aufwendung-Mitarbeiter-Form</title>
	<link rel="stylesheet" type="text/css" href="../content/AufwendungForm.css">
</head>
<body>
	<div id="container">
	<h1>Aufwendung Form</h1>
	
	<form action="/saveAufwendung" method="POST">
		<input type="hidden" name="projektID" value="${data_o["projekt"][0]}">	
		<table id="myTable">
			<tr>
				
				<th>ID-Mitarbeiter</th>
				<th>Aufwendung je Woche</th>
			</tr>
			%for i in data_o["mitarbeiter"]:
			<tr>
				<td>${i}</td>	
				
				%for x in range(0,int(data_o["projekt"][1])):
					<td>	
					<input type="number" placeholder="Aufwendung" name="aufwendung_${i}_${x}" min="0" max="1000" step="1" value="${data_o["mitarbeiter"][i][x]}" id="aufwendung_${i}_${x}" class="input_number input_${int(i)+1}_${x+1}">	
					</td>
				%endfor
				
				<td>
					<input type="hidden"  name="mitarbeiter_${i}" value="0">
					<input type="checkbox" name="mitarbeiter_${i}" value="1" id="check_${i}">
				</td>
				
			</tr>
			%endfor
		</table>
		<input type="submit" name="Submit" class="input_submit">
		<div class="button">
				<a href="/listProjekt" class="link">Abbrechen</a>
			</div>
	</form>
	</div>
	<script type="text/javascript" src="../content/AufwendungForm.js"></script>
</body>
</html>
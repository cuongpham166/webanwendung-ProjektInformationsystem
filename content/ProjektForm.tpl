## coding: utf-8
<!DOCTYPE html>
<html>
<head>
	<title>Projekt-Form</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="../content/ProjektForm.css">
</head>
<body>
	<div id="container">
		<h1>Projekt-Form</h1>
		<form action="/saveProjekt" method="POST">
			<input type="hidden" value = "${data_o["project"][6]}" id="id_s" name="id_s" >
			<div>
				<label for="nummer_s"></label>
				<input type="number" value = "${data_o["project"][0]}" id="nummer_s" name="nummer_s"  placeholder="Nummer" class="input" min="10" max="1000"required>
			</div>

			<div>
				<label for="bezeichnung_s"></label>
				<input type="text" value="${data_o["project"][1]}" id="bezeichnung_s" name="bezeichnung_s" placeholder="Bezeichnung" class="input" required>
			</div>

			<div>
				<label for="beschreibung_s"></label>
				<input type="text" value= "${data_o["project"][2]}" id="beschreibung_s" name="beschreibung_s" placeholder="Beschreibung" class="input" required>
			</div>

			<div>
				<label for="bearbeitungszeitraum_s"></label>
				<input type="number" value ="${data_o["project"][3]}" id="bearbeitungszeitraum_s" name="bearbeitungszeitraum_s" min="1" max="50" placeholder="Bearbeitungszeitraum" class="input" required>
			</div>

			<div>
				<label for="budget_s"></label>
				<input type="number" value= "${data_o["project"][4]}" id="budget_s" name="budget_s" placeholder="Budget" class="input" min="0" max="2000" step="5" required>
			</div>

			<div>
				<select name="kunden_s" required>
					<option value="" disabled selected>Kunden-ID</option>
					%for i in data_o["kunden"]:
					<option value=${i}>${i}</option>
					%endfor
				</select>
			</div>
			<!--<div>
				<a href="#" id="create" class="link"> Create Input</a>
			</div> -->
		
			<!---
			<table id="myTable">
				<tr>
					<th class="link">ID-Mitarbeiter</th>
					<th class="link">Die Aufwendung je Woche</th>
				</tr>

				%for i in data_o["mitarbeiter"]:
				<tr>
					<td class="link" name="${i}" >${i}</td>
					<td>
						<input type="number" min="0" max="1000" step="1" placeholder="Die Aufwendung je Woche" class="input_number" name="aufwendung_${i}" value="${data_o["mitarbeiter"][i][0]}">
						<div id="contain">
					</td>
					<td>
						<input type="hidden" name="mitarbeiter_${i}" value="0">
						<input type="checkbox" name="mitarbeiter_${i}"	value="1">
					</td>
				</tr>
				%endfor
			</table>
			--->
			<div>
				<input type="submit" value="Speichern" class="input_submit">
			</div>
			<div class="button">
				<a href="/listProjekt" class="link">Abbrechen</a>
			</div>
			
		</form>
	</div>
	<script type="text/javascript" src="../content/ProjektForm.js"></script>
</body>
</html>
## coding: utf-8
<!DOCTYPE html>
<html>
<head>
	<title>Mitarbeiter-Form</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="../content/form.css">
</head>
<body>
	<div id="container">
		<h1>Mitarbeiter-Form</h1>
		<form action="/saveMitarbeiter" method="POST">
			<input type="hidden" value = "${data_o[3]}" id="id_s" name="id_s" >
			<div class="input">
				<label for="name_s"></label>
				<input type="text" value = "${data_o[0]}" id="name_s" name="name_s" placeholder="Name" required>
			</div>

			<div class="input">
				<label for="vorname_s"></label>
				<input type="text" value="${data_o[1]}" id="vorname_s" name="vorname_s" placeholder="Vorname" required>
			</div>

			<div class="input">
				<label for="funktion_s"></label>
				<input type="text" value ="${data_o[2]}" id="funktion_s" name="funktion_s" placeholder="Funktion" required>
			</div>

			<div class="input">
				<input type="submit" value="Speichern">
			</div>
			<div class="button">
				<a href="/listMitarbeiter">Abbrechen</a>
			</div>
			
	</form>
	</div>
	
</body>
</html>
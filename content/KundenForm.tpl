## coding: utf-8
<!DOCTYPE html>
<html>
<head>
	<title>Kunden-Form</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="../content/form.css">
</head>
<body>
	<div id="container">
		<h1>Kunden-Form</h1>
		<form action="/saveKunden" method="POST">
			<input type="hidden" value = "${data_o[4]}" id="id_s" name="id_s" >

			<div class="input">
				<label for="nummer_s"></label>
				<input type="number" value = "${data_o[0]}" id="nummer_s" name="nummer_s" placeholder="Nummer" min="100" max="10000" required>
			</div>

			<div class="input">
				<label for="bezeichnung_s"></label>
				<input type="text" value="${data_o[1]}" id="bezeichnung_s" name="bezeichnung_s" placeholder="Bezeichnung" required>
			</div>

			<div class="input">
				<label for="ansprechpartner_s"></label>
				<input type="text" value= "${data_o[2]}" id="ansprechpartner_s" name="ansprechpartner_s"  placeholder="Ansprechpartner" required>
			</div>

			<div class="input">
				<label for="ort_s"></label>
				<input type="text" value ="${data_o[3]}" id="ort_s" name="ort_s" placeholder="Ort" required>
			</div>

			<div>
				<input type="submit" value="Speichern">
			</div>
			
			<div  class="button">
				<a href="/listKunden">Abbrechen</a>
			</div>
			
		</form>
	</div>
	
</body>
</html>
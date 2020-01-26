## coding: utf-8
<!DOCTYPE html>
<html>
<head>
	<title>Projekt-Übersicht</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="../content/ProjektUbersicht.css">
</head>
<body>
<h1>Projekt-Übersicht</h1>
	<div class="divTable">
		<div class="divTableBody">
			<div class="divTableRow">
				<div class="divTableCell1">Projekt-ID</div>
				<div class="divTableCell1">Projekt-Bezeichnung</div>
				<div class="divTableCell1">Bearbeitungzeitraum (Woche)</div>
				<div class="divTableCell1">wöchentlicher Aufwand</div>
 				<div class="divTableCell1">Die beteiligten Mitarbeiter</div>
		</div>

			%for i in data_o:
			<div class="divTableRow">
				<div class="divTableCell"><p>${i}</p></div>
				<div class="divTableCell"><p>${data_o[i][0]}</p></div>
				<div class="divTableCell"><p>${len(data_o[i][2])}</p></div>
				<div class="divTableCell">
					%for j in range(0,len(data_o[i][2])):
						<p>${j+1}.Woche : ${data_o[i][2][j]} </p>
					%endfor
				</div>
				<div class="divTableCell">
					%for k in range(0,len(data_o[i][1])):
						<p>${data_o[i][1][k]}</p>
					%endfor
				</div>	
			</div>
			%endfor
		</div>
	</div>
		<div  class="button">
			<a href="/" title="Zurück zur Startseite">Zurück zur Startseite</a>
		</div>
</body>
</html>
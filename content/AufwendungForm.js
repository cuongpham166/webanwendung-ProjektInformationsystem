var row = document.querySelectorAll("tr");
var table = document.getElementById("myTable");
for (var i=1; i < row.length ; i++){
	for (var j=1; j < table.rows[i].cells.length-1; j++){
		if(document.getElementById("aufwendung_"+(i-1)+"_"+ (j-1)).value != ""){
			document.getElementById("check_"+ (i-1) ).checked = true;
		}
		else if (document.getElementById("aufwendung_"+(i-1)+"_"+ (j-1)).value == ""){
			document.getElementById("check_"+ (i-1) ).checked = false;
		}
	}
}
var rows = document.querySelectorAll("#myTable tr");
var deleteprojekt = document.getElementById("deleteprojekt");
var bearbeitenprojekt = document.getElementById("bearbeitenprojekt");
var aufwendung = document.getElementById("aufwendung");
//var aufwednungbearbeiten= document.getElementById("aufwendungbearbeiten");


for (var i=1; i < rows.length; i++){

	rows[i].addEventListener('click', function(){
		[].forEach.call(rows,function(el){
			//alert(rows[i]);
			el.classList.remove("highlight");
		});
		this.className += 'highlight';
	},false);
}

	bearbeitenprojekt.addEventListener("click", function(){
	var elx_o = document.querySelector(".highlight");
	if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } 
         else{
         	var d = document.getElementById("bearbeitenprojekt");
         	alert("/editProjekt/"+elx_o.id);
         	d.setAttribute("href", "/editProjekt/"+elx_o.id); 
         }
	});

	deleteprojekt.addEventListener("click",function(){
	var elx_o = document.querySelector(".highlight");
	if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } 
         else{
         	var loschen = document.getElementById("deleteprojekt");
         	alert("/deleteProjekt/"+elx_o.id);
         	loschen.setAttribute("href", "/deleteProjekt/"+elx_o.id); 
         }
});


	aufwendung.addEventListener("click", function(){
	var elx_o = document.querySelector(".highlight");
	if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } 
         else{
         	var aufwendung1 = document.getElementById("aufwendung");
         	alert("/Aufwendung/"+elx_o.id);
         	aufwendung1.setAttribute("href", "/Aufwendung/"+elx_o.id); 
         }
	});
	

   /*aufwendungbearbeiten.addEventListener("click", function(){
   var elx_o = document.querySelector(".highlight");
   if (elx_o == null) {
            alert("Bitte zuerst einen Eintrag auswählen!");
         } 
         else{
            var aufwendungbearbeiten1 = document.getElementById("aufwendungbearbeiten");
            alert("/editAufwendung/"+elx_o.id);
            aufwendungbearbeiten1.setAttribute("href", "/editAufwendung/"+elx_o.id); 
         }
   });*/
   






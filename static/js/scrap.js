$("#url_submit").on('submit',function(e){
	e.preventDefault();    

	$.ajax({
		url: $("#info").attr("href")  ,
		type: "POST",
		data:{
            "csrfmiddlewaretoken": $('#info').attr("token-id") ,
            "portal": $("#portal").val(),
            "url": $("#url").val()
		},

		dataType: 'json',

		success: function (data) { 
 			$("#news").empty();
 			$("#review").empty();
 			$("#news").append(data.message);
 			$("#review").append(" <br><br>  <input id ='ok'      type='submit' class='btn btn-success'  value='Ok' >	<input id ='notok'   type='submit' class='btn btn-danger'  value='Not Ok' > <br>	" );
		}		

	});

} );
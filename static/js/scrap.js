$("#url_submit").on('submit',function(e){
	e.preventDefault();     

	alert($("#portal").val());
	alert($("#url").val());

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
 			$("#news").append(data.message);
		}		

	});

} );
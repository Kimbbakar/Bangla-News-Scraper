var DATA = {};
var EMAIL = prompt("Please enter your email id");
var url,portal
$("#url_submit").on('submit',function(e){
	e.preventDefault();    

    portal = $("#portal").val();
    url = $("#url").val();

    if (portal == "pa"){
		var to = url.lastIndexOf('/');
		to = to == -1 ? url.length : to + 1;
		url = url.substring(0, to);
    }


	$.ajax({
		url: $("#info").attr("href")  ,
		type: "POST",
		data:{
            "csrfmiddlewaretoken": $('#info').attr("token-id") ,
            "portal": portal,
            "url": url
		},

		dataType: 'json',

		success: function (data) { 
 			$("#news").empty();
 			$("#news").append(data.message);
 			$("#review").show() ;
 			DATA = data;
		}		

	});

} );

$("#ok").on('click',function(){
	$.ajax({
		url: "postnews"  ,
		type: "POST",
		data:{
            "csrfmiddlewaretoken": $('#info').attr("token-id") ,
            "headline": DATA['headline'] ,
            "body": 	DATA['body'] ,
            "image": 	DATA['image'] , 
            "url": 		url , 
            "portal": 	portal , 
            "email":    EMAIL
		},

		dataType: 'json',

		success: function (data) { 
 			$("#news").empty();
 			$("#review").hide() ;
 			$("#url").empty(); 
 			$("#news").append("<br><br> <h2> "+ data.message + "</h2> " ); 			

		}		

	});	

} );

$("#notok").on('click',function(){
	$("#news").empty();
	$("#review").hide() ;
	$("#url").empty(); 
} );
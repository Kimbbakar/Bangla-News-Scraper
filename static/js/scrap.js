var DATA = {};
var EMAIL = "Unknown";
var url,portal;
var contribution1 = 0;
var contribution2 = 0;
// Contribution 

function prePorcess(){ 
	$.ajax({
		url: "/contribution"  ,
		type: "POST",
		data:{
	        "csrfmiddlewaretoken": $('#info').attr("token-id") ,
	        "email": EMAIL
		},

		dataType: 'json',

		success: function (data) { 
			contribution1 = data [ "contribution1" ];
			contribution2 = data [ "contribution2" ];
			update_contribution();
			EMAIL = data['email'];
			
		}		

	});	
} 



function emailInput(){
	EMAIL = prompt("Please enter your email id"); 
	prePorcess();
}


function update_contribution(){
	$("#contribution1").text(String(contribution1));
	$("#contribution2").text(String(contribution2));
}
 
 

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

 			if (data.success==true ){
	 			contribution1++;			
	 			contribution2++;
	 			update_contribution(); 				
 			}
		}		

	});	

} );

$("#notok").on('click',function(){
	$("#news").empty();
	$("#review").hide() ;
	$("#url").empty(); 
} );
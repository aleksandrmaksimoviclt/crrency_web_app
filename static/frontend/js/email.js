$(document).ready(function() {
	$('#submit').attr('disabled',true);
	    $('#email').keyup(function(){
	        if($(this).val().length !=0)
	            $('#submit').attr('disabled', false);            
	        else
	            $('#submit').attr('disabled',true);
	    })
});

    
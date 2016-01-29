$(document).ready(function() {

    /*$('#submit').attr('disabled',true);
    $('input').on('blur', function() {
        $('collect-email').validate();
        if ($('collect-email').valid()) {
            $('#submit').attr('disabled', false);  
        } else {
            $('#submit').attr('disabled', true);
        }
    });*/
    
    

    $('#collect-email').submit(function(){
            var email = $("#email").val();
            var email_data = {"email": email};
            console.log(email_data);
            $.ajax({
                data: email_data,
                type: $(this).attr('method'),
                url: $(this).attr('action'),
                success: function(response){
                    $('#message').html("Subscribed!")
                    $('#email').val('');
                    $('#submit').attr('disabled',true);
                }
            });
            return false;
       });

    $('#submit').attr('disabled',true);
            $('#email').keyup(function(){
                if($(this).val().length !=0)
                    $('#submit').attr('disabled', false);            
                else
                    $('#submit').attr('disabled',true);
            });
    
    $('#submit').click(function(){
        $('#message').fadeTo("slow" , 1, function() {
            $('#message').delay(3000).fadeTo( "slow" , 0)
            });
    });
    

});
$(document).ready(function() {
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
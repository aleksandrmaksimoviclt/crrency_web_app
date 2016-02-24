$(window).load(function(){


    $('ul.tabs').tabs('select_tab', 'timeline');
   
    

    $(window).scroll(navbardepth);
    
    $('.button-collapse').sideNav();  


   /* $(".activator").click(function() {
        setTimeout(function() {
            var myVar =  $(".story").innerHeight();
            console.log ( myVar );

        if($(".card-reveal").innerHeight() <= $(".story").innerHeight() ){
            $(".card-reveal").addClass("bottom-shadow");
        } else {
            $(".card-reveal").removeClass("bottom-shadow");
        };
        }, 1);
       
    }); */

    $(".card-reveal").bind('scroll', function() {

        if ($(this).scrollTop() > 0) {
            $(this).addClass("top-bottom-shadow");
            $(".divider").css("background-color", "red");
        } else {
            $(this).removeClass("top-bottom-shadow");
        };

        if($(this).scrollTop() + $(this).innerHeight()>=$(this)[0].scrollHeight){
            $(this).removeClass("top-bottom-shadow");
            $(this).addClass("top-shadow"); 
        } else {
            $(this).removeClass("top-shadow"); 
        };
    });


    $(".high-five-button-wrapper > .high-five").on("click",function(){
        $(this).toggleClass("clicked");
    });

});

/*whotransactsresize = function(){
    	var sender = $('#sender').height();
	    var recipient = $('#recipient').height();
	    if(sender>recipient) {
			$(".whotransacts").css("height", sender + 'px');
		} 
		else {
			$(".whotransacts").css("height", recipient + 'px');
		}
	};*/

navbardepth = function(){
    if ($(window).scrollTop() > 0){
        $('#navigation-tabs').addClass("z-depth-1");
    }
    else {
        $('#navigation-tabs').removeClass("z-depth-1");   
    }	
};

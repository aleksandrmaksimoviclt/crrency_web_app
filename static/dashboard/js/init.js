$(window).load(function(){
/*
    whotransactsresize();
    $(window).resize(whotransactsresize);
    $('#home').click(function(){
        whotransactsresize();
    });
*/
    $('ul.tabs').tabs('select_tab', 'timeline');
   
    

    $(window).scroll(navbardepth);
    
    

   
});

whotransactsresize = function(){
    	var sender = $('#sender').height();
	    var recipient = $('#recipient').height();
	    if(sender>recipient) {
			$(".whotransacts").css("height", sender + 'px');
		} 
		else {
			$(".whotransacts").css("height", recipient + 'px');
		}
	};

navbardepth = function(){
    if ($(window).scrollTop() > 0){
        $('#navigation-tabs').addClass("z-depth-3");
    }
    else {
        $('#navigation-tabs').removeClass("z-depth-3");   
    }	
};
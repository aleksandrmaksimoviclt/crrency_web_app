$(window).load(function(){
    $('ul.tabs').tabs('select_tab', 'timeline');
   	whotransactsresize();
    $(window).resize(whotransactsresize);
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
        $('#navigation-tabs').addClass("z-depth-2");

        
    }
    else {
        $('#navigation-tabs').removeClass("z-depth-2");
        
    }
    	
};
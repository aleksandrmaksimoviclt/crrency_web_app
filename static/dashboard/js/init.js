$(window).load(function(){

    $('ul.tabs').tabs('select_tab', 'timeline');
   
    

    $(window).scroll(navbardepth);
    
    $(".button-collapse").sideNav();
   
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

/* TODO Do action while scroll */
/*

$(function() {

    var timer, el = $('body'),
        flag = false;
    $(window).scroll(function() {
        if (!flag) {
            flag = true;
            el.addClass('scrolling');
        }
        clearTimeout(timer);
        timer = setTimeout(function() {
            el.removeClass('scrolling');
            flag = false;
        }, 200);
    });

});

*/

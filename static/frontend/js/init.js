$(window).load(function(){
	$("#preloader").addClass("hide");
	$("#view").removeClass("hide");
	$(".button-collapse").sideNav();
	$(window).scroll(function(){
        if ($(window).scrollTop() > 0){
            $('#navbar').addClass("blue");
            $('#navbar').removeClass("transparent");
            
        }
        else {
            $('#navbar').removeClass("blue");
            $('#navbar').addClass("transparent");
            
        }
    });	
});
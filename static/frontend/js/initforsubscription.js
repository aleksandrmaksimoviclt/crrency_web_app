$(window).load(function(){
	$("#preloader").addClass("hide");
	$("#view").removeClass("hide");

	$('#collect-email').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});

});

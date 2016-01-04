(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $('.slider').slider({full_width: true});
    $('.tab-demo').show().tabs();
    $('.modal-trigger').leanModal();
    $('.scrollspy').scrollSpy();
    $('.datepicker').pickadate({selectYears: 20});
    $('select').not('.disabled').material_select();
	
  }); // end of document ready
})(jQuery); // end of jQuery name space

/* $(document).ready(function(){
	var vid = document.getElementById("bgvid");
	var pauseButton = document.querySelector("#playpause button");

	function vidFade() {
	  vid.classList.add("stopfade");
	}

	vid.addEventListener('ended', function()
	{
	// only functional if "loop" is removed 
	vid.pause();
	// to capture IE10
	vidFade();
	}); 


	pauseButton.addEventListener("click", function() {
	  vid.classList.toggle("stopfade");
	  if (vid.paused) {
		vid.play();
		pauseButton.innerHTML = "Pause";
	  } else {
		vid.pause();
		pauseButton.innerHTML = "Paused";
	  }
	})


})

*/

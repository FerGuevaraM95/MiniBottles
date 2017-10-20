$(function(){
	var button = $('#btn-menu');
	var background_link = $('#background-link');

	button.on('click', function(e){
		background_link.toggleClass('active');
		$('#left-sidebar').toggleClass('active');
		e.preventDefault();
	});

	background_link.on('click', function(e){
		background_link.toggleClass('active');
		$('#left-sidebar').toggleClass('active');
		e.preventDefault();
	});
}())
//size cells
$(document).ready(function(){
	var size = $('td').width();
	$('td').height(size);
});

//toggle cell color
$(document).ready(function(){
	$('.cell').mousedown(function(){
		$(this).toggleClass('hit');
	});
});

//send JSON to add cell to Flask
$(document).ready(function(){
	$('.cell').bind('click', function(){
		var r = $(this).closest('td').index();
		var c = $(this).closest('tr').index();
		if($(this).attr('hit')){
			$.getJSON($SCRIPT_ROOT + '/add_point', {
				row: $(this).closest('td').index(),
				col: $(this).closest('tr').index()
			}, function(data){
				console.log(data.result);
			});
		else{
			$.getJSON($SCRIPT_ROOT + '/delete_point', {
				row: $(this)
			});
		}
	});
});

//temp canvas modifier
$(document).ready(function(){
	var context = $('#grid-canvas')[0].getContext('2d');
	context.beginPath();
	context.moveTo(100, 150);
	context.lineTo(450, 50);
	context.stroke();
});
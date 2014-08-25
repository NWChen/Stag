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
		$.getJSON($SCRIPT_ROOT + '/add_point', {
			row: $(this).closest('td').index(),
			col: $(this).closest('tr').index()
		});
		//return false;
	});
});
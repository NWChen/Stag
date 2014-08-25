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

//add cell whenever hit; remove cell whenever un-hit
$(document).ready(function(){
	$('.cell').bind('click', function(){
		var r = $(this).closest('td').index();
		var c = $(this).closest('tr').index();
		var thisClass = $(this).attr('class');
		if(thisClass==='cell hit') $.getJSON($SCRIPT_ROOT + '/add_point', {row: r, col: c}, 
			function(data){
				console.log(data.result);
			});
		else $.getJSON($SCRIPT_ROOT + '/remove_point', {row: r, col: c},
			function(data){
				console.log(data.result);
			});
	});
});

//illustrate lines between cells
$(document).ready(function(){
	var segments = []
	$.getJSON($SCRIPT_ROOT + '/get_segments', {}, function(data){
		segments = 
	});
});

function draw(fromCell, toCell){
	var context = $('.grid-canvas')[0].getContext('2d');
	context.beginPath();
	context.moveTo($(fromCell).parent().children().index($(fromCell)), $(fromCell).parent().parent().children().index($(fromCell).parent()));
	context.lineTo($(toCell).parent().children().index($(toCell)), $(toCell).parent().parent().children().index($(toCell).parent()));
	context.stroke();
}
function draw(fromCell, toCell){
	var context = $('.grid-canvas')[0].getContext('2d');
	context.beginPath();
	context.moveTo($(fromCell).parent().children().index($(fromCell)), $(fromCell).parent().parent().children().index($(fromCell).parent()));
	context.lineTo($(toCell).parent().children().index($(toCell)), $(toCell).parent().parent().children().index($(toCell).parent()));
	context.stroke();
}

//size cells
$(document).ready(function(){
	var size = $('td').width();
	$('td').height(size);
});

//illustrate lines between cells
function redraw(){
	var points = [];
	$.getJSON($SCRIPT_ROOT + '/get_point_sequence', {pass: 0}, function(data){
		points = data.result; 
	});
	console.log(points.length)
	for(i=0; i<points.length-1; i++){
		console.log('drawing shit mother fucker ' + i);
		x1 = points[i].substring(1, points[i].indexOf(","));
		y1 = points[i].substring(points[i].indexOf(",")+2, points[i].indexOf(")"));
		x2 = points[i+1].substring(1, points[i+1].indexOf(","));
		y2 = points[i+1].substring(points[i].indexOf(",")+2, points[i].indexOf(")"));
		fromCell = $('#grid').rows[x1].cells[y1];
		toCell = $('#grid').rows[x2].cells[y2];
		draw(fromCell, toCell);
	}
}

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
				redraw();
			});
		else $.getJSON($SCRIPT_ROOT + '/remove_point', {row: r, col: c},
			function(data){
				console.log(data.result);
				redraw();
			});
	});
});


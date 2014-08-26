function draw(x1, y1, x2, y2){
	context = $('#overlay')[0].getContext('2d');
	context.beginPath();
	context.moveTo(x1, y1);
	context.lineTo(x2, y2);
	context.stroke();
}

//illustrate lines between cells
//makeshift code since passing a Python list to a Javascript array is weird
function redraw(){
	$.getJSON($SCRIPT_ROOT + '/get_point_sequence', {pass: 0}, function(data){
		var points = data.result.split(' ');
		for(i=0; i<points.length-1; i++){
			x1 = parseInt(points[i].substring(1, points[i].indexOf(",")));
			y1 = parseInt(points[i].substring(points[i].indexOf(",")+1, points[i].indexOf(")")));
			x2 = parseInt(points[i+1].substring(1, points[i+1].indexOf(",")));
			y2 = parseInt(points[i+1].substring(points[i+1].indexOf(",")+1, points[i+1].indexOf(")")));
			fromCell = document.getElementById('grid').rows[x1].cells[y1];
			toCell = document.getElementById('grid').rows[x2].cells[y2];
			fromRect = fromCell.getBoundingClientRect();
			toRect = toCell.getBoundingClientRect();
			console.log(fromRect.top, fromRect.left, toRect.top, toRect.left);
			draw((fromRect.top/4)-14, (fromRect.left/7)-2, (toRect.top/4)-14, (toRect.left/7)-2);
		}
	});
}

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
				redraw();
			});
		else $.getJSON($SCRIPT_ROOT + '/remove_point', {row: r, col: c},
			function(data){
				console.log(data.result);
				redraw();
			});
	});
});


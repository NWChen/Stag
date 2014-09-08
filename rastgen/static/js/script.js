$(document).ready(function(){

var waypts = [];
var canvas = $('canvas'), ctx;
canvas = canvas[0];
canvas.height = 600;
canvas.width = $('canvas').parent().width();
ctx = canvas.getContext('2d');

function plotPoint(point, radius, color){
	ctx.strokeStyle = color;
	ctx.fillStyle = color;
	ctx.beginPath();
	ctx.moveTo(point.x, point.y);
	ctx.arc(point.x, point.y, radius, 2*Math.PI, false);
	ctx.closePath();
	ctx.fill();
	ctx.stroke();
}

function plotTriangle(point, side, color){
	ctx.strokeStyle = color;
}

function plotLine(p1, p2, color){
	ctx.strokeStyle = color;
	ctx.fillStyle = color;
	ctx.beginPath();
	ctx.moveTo(p1.x, p1.y);
	ctx.lineTo(p2.x, p2.y);
	ctx.stroke();
}



//conflicts with click function. move that shit
function findControlPoints(p1, p2, p3){
	plotLine(p1, p2, 'gray');
	plotLine(p2, p3, 'gray');
	plotPoint(p1, 2, 'black'); //should this be part of the click event?
	plotPoint(p2, 2, 'black');
	plotPoint(p3, 2, 'black');

	m1 = {x:(p1.x+p2.x)/2, y:(p1.y+p2.y)/2};
	m2 = {x:(p2.x+p3.x)/2, y:(p2.y+p3.y)/2};
	l12 = Math.sqrt(Math.pow(p2.x-p1.x, 2)+Math.pow(p2.y-p1.y), 2);
	l23 = Math.sqrt(Math.pow(p3.x-p2.x, 2)+Math.pow(p3.y-p2.y), 2);
	m1q/qm2 = l12/l23
	

}

$('canvas').click(function(e){
	var offset = $(this).offset();
	var point = {x:e.pageX-offset.left, y:e.pageY-offset.top};
	plotPoint(point, 2, 'black');
	waypts.push(point);
	if(waypts.length>1){
		plotLine(waypts[drawn], waypts[drawn+1]);
		var m = findMidpoint(waypts[drawn], waypts[++drawn]);
		plotPoint(m, 2, 'gray')
		mids.push(m);
	}
	if(mids.length>1) plotLine(mids[mid_drawn], mids[++mid_drawn], 'blue');
});

});
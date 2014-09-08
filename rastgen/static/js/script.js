$(document).ready(function(){

var mid_drawn = 0;
var drawn = 0;
var pts = [];
var mids = [];
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

function findMidpoint(p1, p2){
	m = {x:(p1.x+p2.x)/2, y:(p1.y+p2.y)/2};
	console.log(m);
	return m;
}

//conflicts with click function. move that shit
function findControlPoints(p1, p2, p3){
	
}

$('canvas').click(function(e){
	var offset = $(this).offset();
	var point = {x:e.pageX-offset.left, y:e.pageY-offset.top};
	plotPoint(point, 2, 'black');
	pts.push(point);
	if(pts.length>1){
		plotLine(pts[drawn], pts[drawn+1]);
		var m = findMidpoint(pts[drawn], pts[++drawn]);
		plotPoint(m, 2, 'gray')
		mids.push(m);
	}
	if(mids.length>1) plotLine(mids[mid_drawn], mids[++mid_drawn], 'blue');
});

});
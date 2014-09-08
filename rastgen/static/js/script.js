$(document).ready(function(){

var pts = [];
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

}

$('canvas').click(function(e){
	var offset = $(this).offset();
	var point = {x:e.pageX-offset.left, y:e.pageY-offset.top};
	plotPoint(point, 2, 'black');
	pts.push(point);
	if(pts.length > 1){
		for(i=0; i<pts.length-1; i++){
			plotLine(pts[i], pts[i+1], 'gray');
		}
	}
});

});
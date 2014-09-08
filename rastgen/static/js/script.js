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

function distance(p1, p2){
	return Math.sqrt(Math.pow(p2.x-p1.x, 2)+Math.pow(p2.y-p1.y), 2)
}

//conflicts with click function. move that shit
function findControlPoints(p1, p2, p3){
	plotLine(p1, p2, 'gray');
	plotLine(p2, p3, 'gray');
	plotPoint(p1, 2, 'black'); //should this be part of the click event?
	plotPoint(p2, 2, 'black');
	plotPoint(p3, 2, 'black');

	m1 = {x:(p1.x+p2.x)/2, y:(p1.y+p2.y)/2}; //midpoint of p1, p2
	m2 = {x:(p2.x+p3.x)/2, y:(p2.y+p3.y)/2}; //midpoint of p2, p3
	l12 = distance(p1, p2); //distance between p1 and p2
	l23 = distance(p2, p3); //distance between p2 and p3
	k = l12/l23 //ratio of p1, p2 to p2, p3
	m1q = k*distance(m1, m2); //distance from m1 to q
	m2q = (1-k)*distance(m1, m2); //distance from q to m2
	dxq2 = (m2q*(m2.x-m1.x))/(m1q+m2q); //distance from q to m2 in the x-axis
	dyq2 = (m2q*(m1.y-m2.y))/(m1q+m2q); //distance from q to m2 in the y-axis
	dxq1 = (m2.x-m1.x)-dxq2;
	dyq1 = (m2.y-m1.y)-dyq2;
	//q = {x:(m2.x-dxq2), y:(m2.y-dyq2)};
	c1 = {x:p2.x-dxq1, y:p2.y-dyq1};
	c2 = {x:p2.x+dxq2, y:p2.y+dxq2};
	return {c1:c1, c2:c2, l1:l1, l2:l2};
}

$('canvas')

/*
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
*/

});
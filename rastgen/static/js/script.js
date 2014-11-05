$(document).ready(function(){

var scan = 0;
var waypts = [];
var canvas = $('canvas'), ctx;
canvas = canvas[0];
canvas.height = 600;
canvas.width = $('canvas').parent().width();
ctx = canvas.getContext('2d');

function plotPoint(point, radius, color){
	ctx.strokeStyle = color;
	ctx.fillStyle = color;
	ctx.beginPath();s
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
	return Math.sqrt(Math.pow(p2.x-p1.x, 2.0)+Math.pow(p2.y-p1.y, 2.0));
}

//conflicts with click function. move that shit
function findControlPoints(p1, p2, p3){
	plotLine(p1, p2, 'gray');
	plotLine(p2, p3, 'gray');

	m1 = {x:(p1.x+p2.x)/2.0, y:(p1.y+p2.y)/2.0}; //midpoint of p1, p2
	m2 = {x:(p2.x+p3.x)/2.0, y:(p2.y+p3.y)/2.0}; //midpoint of p2, p3
	
	//toss all this...
	l12 = distance(p1, p2); //distance between p1 and p2
	l23 = distance(p2, p3); //distance between p2 and p3
	k = l12/l23 //ratio of p1, p2 to p2, p3
	m1q = k*distance(m1, m2); //distance from m1 to q
	m2q = (1.0-k)*distance(m1, m2); //distance from q to m2
	dxq2 = (m2q*(m2.x-m1.x))/(m1q+m2q); //distance from q to m2 in the x-axis
	dyq2 = (m2q*(m1.y-m2.y))/(m1q+m2q); //distance from q to m2 in the y-axis
	dxq1 = (m2.x-m1.x)-dxq2;
	dyq1 = (m2.y-m1.y)-dyq2;
	//q = {x:(m2.x-dxq2), y:(m2.y-dyq2)};

	var dx1 = p1.x-p2.x, dy1 = p1.y-p2.y, 
		dx2 = p2.x-p3.x, dy2 = p2.y-p3.y;

	var l1 = Math.sqrt(dx1*dx1 + dy1*dy1),
		l2 = Math.sqrt(dx2*dx2 + dy2*dy2);

	var m1 = {x:(p1.x+p2.x)/2, y:(p1.y+p2.y)/2},
		m2 = {x:(p2.x+p3.x)/2, y:(p2.y+p3.y)/2};

	var dxm = (m1.x-m2.x),
		dym = (m1.y-m2.y);
 
 	var q = l1/(l1+l2), 


	c1 = {x:p1.x+tx, y:p1.y+ty};
	c2 = {x:p2.x+tx, y:p2.y+ty};
	console.log(l12);
	return {c1:c1, c2:c2, l1:l12, l2:l23};
}

$('canvas').click(function(e){
	var offset = $(this).offset();
	point = {x:e.pageX-offset.left, y:e.pageY-offset.top};
	waypts.push(point);
	plotPoint(point, 2, 'black');
	if(waypts.length>2){
		var S = findControlPoints(waypts[scan], waypts[scan+1], waypts[scan+2]);
		scan++;
		console.log(S);
		plotPoint(S.c1, 2, 'blue');
		plotPoint(S.c2, 2, 'blue');
	}
});


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
#include<iostream.h>
#include<graphics.h>
#include<conio.h>
#include<stdio.h>
 
struct point
{
int x,y;
};
 
void hermite(point p1,point p4,double r1,double r4)
{
	float x,y,t;
	for(t=0.0;t<=1.0;t+=.001)
	{
		x=(2*t*t*t-3*t*t+1)*p1.x+(-2*t*t*t+3*t*t)*p4.x+(t*t*t-2*t*t+t)*r1+(t*t*t-t*t)*r4;
		y=(2*t*t*t-3*t*t+1)*p1.y+(-2*t*t*t+3*t*t)*p4.y+(t*t*t-2*t*t+1)*r1+(t*t*t-t*t)*r4;
		putpixel(x,y,YELLOW);
	 }
}
 
int main()
{
	int gd=DETECT,gm;
	double r1,r4;
	initgraph(&gd,&gm,"..//BGI");
	point p1,p2;
	printf("Enter 2 hermite points:\n");
	scanf("%d%d%d%d",&p1.x,&p1.y,&p2.x,&p2.y);
	printf("Enter the tangents at p1,p4");
	scanf("%d%d",&r1,&r4);
	cleardevice();
	hermite(p1,p2,r1,r4);
	putpixel(x1,y1,WHITE);
	putpixel(x2,y2,WHITE);
	getch();
	closegraph();
	return 0;
}
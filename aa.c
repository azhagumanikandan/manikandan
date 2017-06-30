#include<stdio.h>
#include<conio.h>
void main()
{
char a,e,i,o,u,temp;
clrscr();
printf("enter the details");
scanf("%c",&temp);
if(temp=='a'||temp=='e'||temp=='i'||temp=='o'||temp=='u')
{
printf("the %c is vowlel");
}
else
{
printf("the %c is consonant");
}
getch();
}



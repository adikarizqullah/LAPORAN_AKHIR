#include <stdio.h>

int main (void){
 int a,i;
 char c;
 scanf("%d %c",&a, &c);

 for ( i = 1; i < 51; i++)
 {
 if (i%a==0){
 printf("%c ",c);
 }
 else{
 printf("%d ",i);
 }

}
}

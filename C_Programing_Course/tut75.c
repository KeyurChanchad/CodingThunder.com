#include <stdio.h>
#include <stdlib.h>
int main()
{
    int i=0;     
    int *k;
    while (i<4552)
    {
        printf("Hello code with keyur:\n");
        k= malloc(50* sizeof(int));
        if (i%100==0)
        {
            getchar();
        }
        i++;
    free(k); // if programmer can't free memory that heap is going full that is memory leak
      // run programe .exe wite and click on taskbar and open task manager.
    }
    return 0;
}
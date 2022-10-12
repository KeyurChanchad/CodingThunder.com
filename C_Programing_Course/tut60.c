#include <stdio.h>
int main()
{
    printf("Current File name is %s\n",__FILE__); // __ double under soure
    printf("Current time is %s\n",__TIME__);
    printf("Today's date is %s\n",__DATE__);
    printf("Line NO is %d\n",__LINE__);
    printf("ANSI is %d\n",__STDC__); // ANSI is you compile the program
    return 0;
}
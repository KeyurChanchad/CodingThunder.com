#include <stdio.h>
#include <time.h>
int genraterandomnumber(n)
{
  srand(time(NULL));
  return rand() % n;
}
int greater(char1, char2)
{
  // return 1 if char1>char2 and 0 otherwise. if char1==char2 will return-1
  if ((char1 == 'R') && (char2 == 'S'))
  {
    return 1;
  }
  else if ((char2 == 'R') && (char1 == 'S'))
  {
    return 0;
  }
  else if ((char1 == 'S') && (char2 == 'P'))
  {
    return 1;
  }
  else if ((char2 == 'S') && (char1 == 'P'))
  {
    return 0;
  }
  else if ((char1 == 'p') && (char2 == 'R'))
  {
    return 1;
  }
  else if ((char2 == 'P') && (char1 == 'R'))
  {
    return 0;
  }
  else if ((char1 == char2))
  {
    return -1;
  }
}
int main()
{
  char playerchar, compchar;
  char dict[] = {'R', 'P', 'S'};
  int playerscore = 0, compscore = 0, tmp, i;
  printf("Welcome to the Rock, Paper, scissor:");
  for (i = 0; i < 3; i++)
  {
    printf("\nPlayer's turn:\n");
    printf("Enter 1.Rock, 2.Paper, 3.Scissor\n");
    scanf("%d", &tmp);
    getchar();
    playerchar = dict[tmp - 1];
    printf("You choose:%c\n\n", playerchar);

    printf("computer's turn:\n");
    tmp = genraterandomnumber(3) + 1;
    compchar = dict[tmp - 1];
    printf("CPU choose:%c\n\n", compchar);

    // compaire
    if (greater(playerchar, compchar) == 1) // player is grater means it win
    {
      playerscore += 1;
      printf("You got it:\n");
    }
    else if (greater(playerchar, compchar) == -1) // it draw
    {
      compscore += 1;
      playerchar += 1;
      printf("it's Draw:\n");
    }
    else if (greater(playerchar, compchar) == 0) // computer win
    {
      compchar += 1;
      printf("Computer got it:\n");
    }
  }
  printf("Your score:%d\n Computer:%d", playerscore, compscore);
  if (playerscore > compscore)
  {
    printf("\n****You Win****");
  }
  else if (compscore > playerscore)
  {
    printf("\n***Computer Win***");
  }
  else if (playerscore == compscore)
  {
    printf("\n***It's draw***");
  }
}
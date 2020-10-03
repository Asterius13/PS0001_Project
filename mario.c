#include <stdio.h>
#include <cs50.h>

int main (void)
{ int height;
  do
  {
     height=get_int("Height?\n");
  }
  while (height<1 || height>8);
  {
      for (int row=1; row<=height; row++)
      {
          //print spaces
          for (int space= height-row; space>0; space--)
              {
                   printf(" ");
               }
          //print hashes
          for (int hash=1; hash<=row; hash++)
              {
                   printf("#");
              }
          //print new line
              printf("\n");
      }
  }
}

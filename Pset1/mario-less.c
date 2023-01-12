#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;

    //prompt user for height
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    //print pyramid
    for (int row = 0; row < height; row++) //print new line as row
    {
        for (int space = height - row -1; space > 0; space--)
        {
            printf(" ");
        }
        for (int hash = 0; hash < row + 1; hash++)
        {
            printf("#");
        }
        printf("\n");
    }
}

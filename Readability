#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int main(void)
{
    string text = get_string("Text: \n");

    int letters = 0;
    int words = 1;
    int sentences = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }

        else if (text[i] == ' ')
        {
            words++;
        }

        else if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
    }

    float L = (float) letters / (float) words * 100;
    float S = (float) sentences / (float) words * 100;

    int index = round(0.0588 * L - 0.296 * S - 15.8);//using round to round up and not have decimals

    if (index < 1)
    {
        printf("Before Grade 1\n");//identifies grade level 1
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");//identifies grade level 16+
    }
    else
    {
        printf("Grade %i\n", index);//identifies all other grade levels
    }


}

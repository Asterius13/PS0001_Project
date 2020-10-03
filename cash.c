#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float change;
    int cents;

    do
    {
        change = get_float("Change owed:");
        //convert change in dollar to cents
        cents = round(change * 100);
    }
    //reject all non-positive values
    while (change <= 0);

    //find number of quarters used
    int quarters = cents / 25;

    //find number of dimes used via remainder of change after using 25c
    int dimes = (cents % 25) / 10;

    //find number of nickels used via remainder of change after using 25c,10c
    int nickels = (cents % 25) % 10 / 5;

    //find number of pennies used via remainder of change after using 25c,10,5c
    int pennies = ((cents % 25) % 10) % 5;

    int coins_given = quarters + dimes + nickels + pennies;

    printf("%i coins\n", coins_given);

}
/*Odd numbers are NOT divisible by 2. 

Write a Javascript program that prints out all the odd numbers between 1 and 20. Your code must use a for-loop.
*/


for ( let number = 1; number <=20; number = number+1 ) {
    if (number % 2 !== 0) {
        // console.log(number);
        console.log(number,'This is an odd number');
    
    }
}
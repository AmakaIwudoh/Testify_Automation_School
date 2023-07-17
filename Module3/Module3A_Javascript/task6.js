/*Odd or even?
Write a Javascript program that checks if a given number, number is odd or even. 

If the number is odd, print to the console: number is odd. If  the number is even, print to the console: number is even */


for ( let number = 1; number <=20; number = number+1 ) {
    if (number % 2 !== 0) {
        // console.log(number);
        console.log(number,'This is an odd number');
    } else {
        console.log(number,'This is an even number');
    }
}
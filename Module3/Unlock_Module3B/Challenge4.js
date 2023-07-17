//jsc4 Print a table containing multiplication table

// take input from the user
const number = parseInt(5);

//creating a multiplication table
for(let i = 1; i <= 10; i++) {

    // multiply number with i
    const result = number * i;

    // display the result
    console.log(`${number} * ${i} = ${result}`);
   
}
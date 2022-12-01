//1 Sum of numbers in an array

const ages = [3, 6, 7, 20];

const sum = ages.reduce((a, b) => a + b, 0);
console.log(sum) //36


//2 Length Converter|| Converting centimeter to meter

function lengthConverter(centiMeter){
    const meter = centiMeter / 100;
    return meter;
     }
    
    const meterValue = lengthConverter(250);
    console.log(meterValue + ' meter')

 //3 Print all even numbers from 0-10
for(let number = 0; number <=10; number = number + 1){
     if(number % 2 === 0){
     console.log(number)
    }

   }

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

//jsc5 Create a function that reverses an array

const namess = ['Rukky', 'Amaka', 'Biola', 'Festus']
namess.reverse()
console.log(namess) //Festus, Biola, Amaka, Rukky


//jsc6 Sort an array of strings in alphabetical order

const names = ['Rukky', 'Amaka', 'Biola', 'Ada', 'Festus']
names.sort()
console.log(names) //Ada,Amaka, Biola, Festus, Rukky


//JSC 7 Sort an array of numbers in descending order

const numbers = [3,7,8,4,1,6]
numbers.sort((a,b)=> b-a)
console.log(numbers) //[8,7,6,4,3,1]

//JSC 8 Return a Boolean if a number is divisible by 10
checkNumber  = function(numberToCheck){
	for(let number = 1; number <= numberToCheck; number++){
		
		if(number % 10 === 0){
			return true;
		}
	}	

}

result = checkNumber(20);

console.log('result is ==> ' + result);

//jsc9 Return the number of vowels in a string

// defining vowels
const vowels = ["a", "e", "i", "o", "u"]

function countVowel(str) {
    // initialize count
    let count = 0;

    // loop through string to test if each character is a vowel
    for (let letter of str.toLowerCase()) {
    if (vowels.includes(letter)) {
    count++;
        }
    }

    // return number of vowels
    return count
}
// take input
const string = ('FestusAMAKA');

const result = countVowel(string);

console.log(result); //5


// jsc10 Create a function that filters out negative numbers

var array = [18, -42, 21, 6, -60, -10, -5];
negatives = array.filter(x => x < 0);
console.log(negatives); // [-42, -60, -10, -5]


//option 2

// var array = [18, -42, 21, 6, -50];
// array = array.filter(function(x) { return x < 0; });
// console.log(array); // [-42, -50,]




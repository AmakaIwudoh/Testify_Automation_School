// jsc10 Create a function that filters out negative numbers

var array = [18, -42, 21, 6, -60, -10, -5];
negatives = array.filter(x => x < 0);
console.log(negatives); // [-42, -60, -10, -5]


//option 2

// var array = [18, -42, 21, 6, -50];
// array = array.filter(function(x) { return x < 0; });
// console.log(array); // [-42, -50,]

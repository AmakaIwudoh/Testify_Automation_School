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

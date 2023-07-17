//My Personal Library2

/*
    Add a toggleReadingStatus method to your books objects. 
    The method should update the value of the reading property of the book object.
*/

const books = {

    title: 'Animal Farm',
    description: 'Story of group of animals',
    numberOfPages: 160,
    author: 'George Orwell',
    reading: false,
    toggleReadingStatus: function(){
        if(books.reading === true){
            books.reading = false
        }else {
            books.reading = true
        }
    }
}
books.toggleReadingStatus();
console.log(books.reading);
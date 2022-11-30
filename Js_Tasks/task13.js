//My Personal Library2

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
books.toggleReadingStatus()
console.log(books.reading)
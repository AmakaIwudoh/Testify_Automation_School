//My Personal Library3

/*
    Create a books array. 

    Each element of this array will be a book object. 

    Each book object will have the following properties

    title (string)

    description (string)

    numberOfPages (number)

    authour (string)

    reading (boolean)
*/

const books = [
    {

        title: 'Animal Farm',
        description: 'Story of group of animals',
        numberOfPages: 160,
        author: 'George Orwell',
        reading: true
    },

    {

        title: 'Things Fall Apart',
        description: 'Story of about Village Settings',
        numberOfPages: 350,
        author: 'Chinua Achebe',
        reading: true
    },
    {

        title: 'Half of a Yellow Sun',
        description: 'Story of about Biafran War',
        numberOfPages: 450,
        author: 'Chimamanda Adichie',
        reading: true
    },
    {

        title: 'Purple Hisbiscus',
        description: 'Story of about Freedom',
        numberOfPages: 400,
        author: 'Chimamanda Adichie',
        reading: false
    }
]

for (let i = 0; i < books.length; i++){
    if (books[i].reading === true)
    console.log(books[i])   
}
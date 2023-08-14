class Book {
    constructor(title, author) {
        this.title = title;
        this.author = author;
    }
}
var book1 = new Book("On Liberty", "Mill");
book1.author = "John Stuart Mill";
console.log(book1.title);
console.log(book1.author);
var book2 = new Book("The Last Casualty", "Ben Elton");
book2.title = "The First Casualty";
console.log(book2.title);
console.log(book2.author);
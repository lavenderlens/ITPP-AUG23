class Book {
    String title;
    String author;
    Book(String title, String author) {
        this.title = title;
        this.author = author;
    }
}
Book book1 = new Book("On Liberty", "Mill");
book1.author = "John Stuart Mill";
System.out.println(book1.title);
System.out.println(book1.author);
Book book2 = new Book("The Last Casualty", "Ben Elton");
book2.title = "The First Casualty";
System.out.println(book2.title);
System.out.println(book2.author);
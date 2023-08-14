class Address {
    String buildingAndStreet;
    String townOrCity;
    String postcode;
    Address() {
        this.buildingAndStreet = "";
        this.townOrCity = "";
        this.postcode = "";
    }
}
class Scientist {
    String name;
    int yearOfBirth;
    boolean married;
    Address address;
    Scientist(String name) {
        this.name = name;
        this.yearOfBirth = 0;
        this.married = false;
        this.address = new Address();
    }
    void printToScreen() {
        System.out.println("Name: " + this.name);
        System.out.println("Year of birth: " + this.yearOfBirth);
        System.out.println("Married: " + this.married);
        System.out.println("Address: " + 
            this.address.buildingAndStreet + ", " +
            this.address.townOrCity + ", " + 
            this.address.postcode);
    }
}
Scientist curie = new Scientist("Marie Curie");
curie.yearOfBirth = 1867;
curie.married = true;
curie.address.buildingAndStreet = "Freta 16";
curie.address.townOrCity = "Warsaw";
curie.address.postcode = "00-227";
curie.printToScreen();
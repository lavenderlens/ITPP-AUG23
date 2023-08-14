function Address() {
        this.buildingAndStreet = "";
        this.townOrCity = "";
        this.postcode = "";
    }
function Scientist(name, ...fields) {
        this.name = name;
        this.yearOfBirth = 0;
        this.married = false;
        this.fields = [...fields];
        this.address = new Address();
}
    Scientist.prototype.printToScreen = function () {
        console.log("Name: " + this.name);
        console.log("Year of birth: " + this.yearOfBirth);
        console.log("Married: " + this.married);
        console.log("Fields: ");
        for(var field of this.fields) {
            console.log("- " + field);
        }
        // console.log("Address: " + 
        //     this.address.buildingAndStreet + ", " +
        //     this.address.townOrCity + ", " + 
        //     this.address.postcode);
        console.log(`Address: 
        ${this.address.buildingAndStreet},
        ${this.address.townOrCity},
        ${this.address.postcode}`);
    }
var curie = new Scientist("Marie Curie", "Phys", "Chem", "Bio");
curie.yearOfBirth = 1867;
curie.married = true;
// curie.fields.push("Physics");
// curie.fields.push("Chemistry");
// curie.fields.push("Radioactivity");
curie.address.buildingAndStreet = "Freta 16";
curie.address.townOrCity = "Warsaw";
curie.address.postcode = "00-227";
curie.printToScreen();

var crick = new Scientist("Marie Curie", "Phys", "Chem", "Bio");
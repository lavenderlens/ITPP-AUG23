package changeit;

public class ChangeIt {

	public static void main(String[] args) {

		int x = 1;
		changeIt(x);
		System.out.println(x);//no change
		
		Person p = new Person("Dua Lipa", 24);
		changeIt(p);
		System.out.println(p.name);//changed
	}//end main
	
	//static method
	//changes copy of primitive reference
	static int changeIt(int number) {
	    number += 1;
	    return number;
	}
	
	//object method
	//changes object reference
    static Person changeIt(Person person) {
		person.name = "Bruce Springsteen";
		return person;
    }
    
}//end class

const bank = new Bankpackage bankingappapart3;

public class BankTester {

	public static void main(String[] args) {
		Bank bankOfIreland = new Bank("Bank of Ireland");
		
		bankOfIreland.add(new Account("alan", 1234));
		bankOfIreland.add(new Account("bruce", 1235));
		bankOfIreland.add(new Account("patti", 1236));
		
		Account bruce = bankOfIreland.find("bruce");
		bruce.deposit(250_000);
		System.out.println(bruce.balance);
		System.out.println(bruce);
		
		// this account is instantiated but not added to Bank
		// It is in an aggregate relationship with Bank-
		// it may exist outside of Bank
		Account bruce_touring = new Account("bruce", 1235);
		bruce_touring.deposit(250_000);
		System.out.println(bruce_touring.equals(bruce));
	
	}

}

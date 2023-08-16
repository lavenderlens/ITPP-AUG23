package bankingappapart3;

import java.util.ArrayList;
import java.util.List;

public class Bank {
	
	String name;
	List<Account> accounts;
	
	public Bank(String name) {
		this.name = name;
		this.accounts = new ArrayList<Account>();
	}
	
	void add(Account account) {
		this.accounts.add(account);
	}
	
	Account find(String name) {
		for(Account acc : this.accounts) {
			if(name.equalsIgnoreCase(acc.name)) {
				return acc;
			}
		}
		return null;
	}



}

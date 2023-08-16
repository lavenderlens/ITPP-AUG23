package bankingappapart3;

public class Account {
	String name;
	int num;
	double balance;

	public Account(String name, int num) {
		this.name = name;
		this.num = num;
		balance = 0;
	}

	public void deposit(double amount) {
		this.balance += amount;	
	}

	@Override
	public String toString() {
		return "Account [name=" + name + ", num=" + num + ", balance=" + balance + "]";
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		long temp;
		temp = Double.doubleToLongBits(balance);
		result = prime * result + (int) (temp ^ (temp >>> 32));
		result = prime * result + num;
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Account other = (Account) obj;
		if (Double.doubleToLongBits(balance) != Double.doubleToLongBits(other.balance))
			return false;
		if (num != other.num)
			return false;
		return true;
	}
	
	

}

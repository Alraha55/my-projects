import java.util.Scanner;

class Person {
    protected String name;
    protected int id;

    public Person(String name, int id) {
        this.name = name;
        this.id = id;
    }

    // polymorphism (can be overridden)
    public void displayInfo() {
        System.out.println("Person: " + name + " | ID: " + id);
    }
}

class Account {

    private int accountNumber;
    private double balance;

    public Account(int accountNumber, double balance) {
        this.accountNumber = accountNumber;
        this.balance = balance;
    }

    // getters / setters (encapsulation)
    public int getAccountNumber() {
        return accountNumber;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }
}

interface ATMOperations {
    void viewBalance(Account acc);
    void withdraw(Account acc, double amount);
    void deposit(Account acc, double amount);
}

class ATMMachine extends Person implements ATMOperations {

    public ATMMachine(String name, int id) {
        super(name, id);
    }

    @Override
    public void displayInfo() {
        System.out.println("ATM Machine Handled By: " + name + " | ID: " + id);
    }

    @Override
    public void viewBalance(Account acc) {
        System.out.println("Balance: " + acc.getBalance());
    }

    @Override
    public void withdraw(Account acc, double amount) {
        if (amount <= acc.getBalance()) {
            acc.setBalance(acc.getBalance() - amount);
            System.out.println("Withdrawn: " + amount);
        } else {
            System.out.println("Insufficient Balance!");
        }
    }

    @Override
    public void deposit(Account acc, double amount) {
        acc.setBalance(acc.getBalance() + amount);
        System.out.println("Deposited: " + amount);
    }
}

public class Main {
    public static void main(String[] args) {

        Account acc = new Account(12345, 2000);

        // Polymorphism
        ATMOperations atm = new ATMMachine("Manar", 101);

        Scanner in = new Scanner(System.in);

        OUTER:
        while (true) {
            System.out.println("\n1. View Balance\n2. Withdraw\n3. Deposit\n4. Exit");
            System.out.print("Enter Choice: ");
            int ch = in.nextInt();
            switch (ch) {
                case 1:
                    atm.viewBalance(acc);
                    break;
                case 2:
                    System.out.print("Withdraw Amount: ");
                    atm.withdraw(acc, in.nextDouble());
                    break;
                case 3:
                    System.out.print("Deposit Amount: ");
                    atm.deposit(acc, in.nextDouble());
                    break;
                case 4:
                    System.out.println("Thank you for using ATM!");
                    break OUTER;
                default:
                    break;
            }
        }
    }
}

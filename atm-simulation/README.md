# ATM Simulation System

A console ATM simulation written in **Java** that demonstrates the four core Object-Oriented Programming principles through a small banking application. The user picks an operation from a menu: view balance, withdraw, deposit, or exit.

Team project for an Object-Oriented Programming course (4 students).

## Features

- Interactive menu loop that runs until the user exits
- View balance, withdraw and deposit
- Withdrawal check: rejects amounts above the balance with `Insufficient Balance!`

## OOP concepts

| Concept | Where it is used |
|---|---|
| **Encapsulation** | `Account` keeps `accountNumber` and `balance` private and exposes them through getters and a setter |
| **Abstraction** | The `ATMOperations` interface defines `viewBalance`, `withdraw` and `deposit` without implementing them |
| **Inheritance** | `ATMMachine` extends `Person` and inherits `name`, `id` and `displayInfo()` |
| **Polymorphism** | `ATMMachine` overrides `displayInfo()`, and the machine is used through the `ATMOperations` type: `ATMOperations atm = new ATMMachine("Manar", 101);` |

## Class structure

```
Person            (name, id, displayInfo())
  └── ATMMachine  implements ATMOperations
Account           (accountNumber, balance, getters/setter)
ATMOperations     (interface: viewBalance, withdraw, deposit)
Main              (menu loop, entry point)
```

## Run it

Requires Java 8 or later.

```bash
cd src
javac Main.java
java Main
```

Example session:

```
1. View Balance
2. Withdraw
3. Deposit
4. Exit
Enter Choice: 1
Balance: 2000.0

1. View Balance
2. Withdraw
3. Deposit
4. Exit
Enter Choice: 4
Thank you for using ATM!
```

The demo account starts with a balance of 2000.

## Files

```
├── src/Main.java                              # all classes
├── docs/
│   ├── console-output.jpg                     # run output
│   └── ATM-Simulation-Presentation.pdf        # project presentation
└── README.md
```

## Team

Almaha Abdulrahman Alzubaidi, Alraha Abdullah Alzubaidi, Manar Laheq Alzubaidi, Sarah Ali Alamri

## Skills demonstrated

Java, object-oriented programming (encapsulation, abstraction, inheritance, polymorphism), interfaces, console I/O, Maven.

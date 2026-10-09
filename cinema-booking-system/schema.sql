DROP DATABASE IF EXISTS HomeTheater;
CREATE DATABASE HomeTheater;
USE HomeTheater;

CREATE TABLE Movie (
    MovieID INT PRIMARY KEY,
    Title VARCHAR(100),
    Genre VARCHAR(100),
    Duration INT
);

ALTER TABLE Movie
ADD Rating VARCHAR(20);

INSERT INTO Movie VALUES
 (1,'Avengers Endgame','Action',180,'PG-13'),
 (2,'Frozen 2','Animation',120,'PG'),
 (3,'Joker','Drama',122,'R'),
 (4,'Inception','Sci-Fi',148,'PG-13'),
 (5,'Titanic','Romance',195,'PG-13'),
 (6,'Interstellar','Sci-Fi',169,'PG-13'),
(7,'The Batman','Action',176,'PG-13'),
(8,'Coco','Animation',105,'PG'),
(9,'Avatar','Fantasy',162,'PG-13'),
(10,'Moana','Adventure',107,'PG');

CREATE TABLE Hall (
    HallID INT PRIMARY KEY,
    HallName VARCHAR(100),
    Capacity INT,
    Type VARCHAR(50)
);

ALTER TABLE Hall
ADD Location VARCHAR(100);

INSERT INTO Hall VALUES
 (1,'Hall A',100,'VIP','First Floor'),
 (2,'Hall B',150,'Standard','Second Floor'),
 (3,'Hall C',120,'VIP','First Floor'),
 (4,'Hall D',200,'IMAX','Ground Floor'),
 (5,'Hall E',90,'Standard','Second Floor'),
 (6,'Hall F',110,'VIP','Third Floor'),
 (7,'Hall G',130,'IMAX','Ground Floor'),
 (8,'Hall H',140,'Standard','Second Floor'),
 (9,'Hall I',160,'VIP','Third Floor'),
 (10,'Hall J',180,'IMAX','Ground Floor');

CREATE TABLE Shows (
    ShowID INT PRIMARY KEY,
    Date DATE,
    MovieID INT,
    HallID INT,
    FOREIGN KEY (MovieID) REFERENCES Movie(MovieID),
    FOREIGN KEY (HallID) REFERENCES Hall(HallID)
);

ALTER TABLE Shows
ADD Time TIME;

INSERT INTO Shows VALUES
(1,'2025-05-01',1,1,'18:00:00'),
 (2,'2025-05-02',2,2,'20:00:00'),
 (3,'2025-05-03',3,3,'16:30:00'),
 (4,'2025-05-04',4,4,'19:00:00'),
 (5,'2025-05-05',5,5,'21:00:00'),
 (6,'2025-05-06',6,6,'17:00:00'),
 (7,'2025-05-07',7,7,'22:00:00'),
 (8,'2025-05-08',8,8,'15:00:00'),
 (9,'2025-05-09',9,9,'18:30:00'),
 (10,'2025-05-10',10,10,'20:30:00');

CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(100),
    PhoneNumber VARCHAR(15),
    Email VARCHAR(100)
);

ALTER TABLE Customer
ADD Age INT;

INSERT INTO Customer VALUES
 (1,'Ahmed Ali','0551234567','ahmed@gmail.com',22),
 (2,'Sara Khalid','0569876543','sara@gmail.com',25),
 (3,'Omar Hassan','0543210987','omar@gmail.com',30),
 (4,'Laila Ahmed','0555678901','laila@gmail.com',27),
 (5,'Fahad Ali','0581239876','fahad@gmail.com',35),
(6,'Noura Saleh','0568745123','noura@gmail.com',28),
(7,'Hassan Mohammed','0531236547','hassan@gmail.com',40),
 (8,'Reem Abdullah','0598765432','reem@gmail.com',24),
 (9,'Yousef Ibrahim','0547893216','yousef@gmail.com',31),
 (10,'Mona Saud','0565432198','mona@gmail.com',29);

CREATE TABLE Booking (
    BookingID INT PRIMARY KEY,
    PaymentStatus VARCHAR(50),
    SeatNumber INT,
    ShowID INT,
    CustomerID INT,
    FOREIGN KEY (ShowID) REFERENCES Shows(ShowID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

INSERT INTO Booking VALUES
 (1,'Paid',15,1,1),
 (2,'Pending',22,2,2),
 (3,'Paid',10,3,3),
 (4,'Cancelled',5,4,4),
 (5,'Paid',18,5,5),
 (6,'Pending',25,6,6),
 (7,'Paid',12,7,7),
 (8,'Paid',8,8,8),
 (9,'Cancelled',30,9,9),
 (10,'Paid',14,10,10);

-- Data manipulation
UPDATE Customer
SET Age = 26
WHERE CustomerID = 2;

UPDATE Booking
SET PaymentStatus = 'Paid'
WHERE BookingID = 2;

DELETE FROM Booking
WHERE BookingID = 9;

-- Queries
SELECT Customer.Name, Movie.Title, Shows.Date, Booking.SeatNumber
FROM Booking
JOIN Customer
ON Booking.CustomerID = Customer.CustomerID
JOIN Shows
ON Booking.ShowID = Shows.ShowID
JOIN Movie
ON Shows.MovieID = Movie.MovieID;

SELECT PaymentStatus, COUNT(BookingID) AS TotalBookings
FROM Booking
GROUP BY PaymentStatus;

SELECT * FROM movie
ORDER BY Duration DESC;

SELECT Hall.Type, COUNT(Shows.ShowID) AS NumberOfShows
FROM Shows
JOIN Hall
ON Shows.HallID = Hall.HallID
GROUP BY Hall.Type;

SELECT Movie.Title, Hall.HallName, Shows.Time
FROM Shows
JOIN Movie
ON Shows.MovieID = Movie.MovieID
JOIN Hall
ON Shows.HallID = Hall.HallID;

SELECT Customer.Name, Booking.PaymentStatus
FROM Booking
JOIN Customer ON Booking.CustomerID = Customer.CustomerID
WHERE PaymentStatus = 'Paid';

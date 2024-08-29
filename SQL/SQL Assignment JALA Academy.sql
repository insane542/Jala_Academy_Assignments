/*Create Table SALESPEOPLE:*/
CREATE TABLE SALESPEOPLE (
  SNUM NUMBER(5) PRIMARY KEY,
  SNAME CHAR(10),
  CITY CHAR(20),
  COMM DECIMAL(8,3));

/*Insert Values in SALESPEOPLE Table*/
INSERT INTO SALESPEOPLE VALUES (1001, 'Peel', 'London',0.12); 
INSERT INTO SALESPEOPLE VALUES(1002, 'Serres','San Jose',0.13);
INSERT INTO SALESPEOPLE VALUES(1004, 'Motika','London',0.11);
INSERT INTO SALESPEOPLE VALUES(1007, 'Rafkin','Barcelona',0.15);
INSERT INTO SALESPEOPLE VALUES(1003, 'Axelrod','New York',0.1);

/*Create Table CUST:*/
CREATE TABLE CUST (
  CNUM NUMBER(5) PRIMARY KEY,
  CNAME CHAR(20),
  CITY CHAR(20),
  RATING NUMBER(3),
  SNUM NUMBER(4));

/*Insert values in CUST Table:*/
INSERT INTO CUST VALUES (2001, 'Hoffman', 'London',100,1001); 
INSERT INTO CUST VALUES (2002, 'Giovanne', 'Rome',200,1003);
INSERT INTO CUST VALUES (2003, 'Liu', 'San Jose',300,1002);
INSERT INTO CUST VALUES (2004, 'Grass', 'Brelin',100,1002);
INSERT INTO CUST VALUES (2006, 'Clemens', 'London',300,1007);
INSERT INTO CUST VALUES (2007, 'Pereia', 'Rome',100,1004);

/*Create Table ORDERS:*/
CREATE TABLE ORDERS (
  ONUM NUMBER(5) PRIMARY KEY,
  AMT DECIMAL(7,2),
  ODATE DATE,
  CNUM NUMBER(4),
  SNUM NUMBER(4));

/*Insert values in ORDERS Table:*/
INSERT INTO ORDERS VALUES (3001,18.69,'03-OCT-94',2008,1007);
INSERT INTO ORDERS VALUES (3003,767.19,'03-OCT-94',2001,1001);
INSERT INTO ORDERS VALUES (3002,1900.10,'03-OCT-94',2007,1004);
INSERT INTO ORDERS VALUES (3005,5160.45,'03-OCT-94',2003,1002);
INSERT INTO ORDERS VALUES (3006,1098.16,'04-OCT-94',2008,1007);
INSERT INTO ORDERS VALUES (3009,1713.23,'04-OCT-94',2002,1003);
INSERT INTO ORDERS VALUES (3007,75.75,'05-OCT-94',2006,1002);
INSERT INTO ORDERS VALUES (3008,4723.00,'05-OCT-94',2006,1001);
INSERT INTO ORDERS VALUES (3010,1309.95,'06-OCT-94',2004,1002);
INSERT INTO ORDERS VALUES (3011,9891.88,'06-OCT-94',2006,1001);

/*Display snum, sname, city and comm of all salespeople.*/
SELECT snum, sname, city, comm FROM SALESPEOPLE;

/*Display all snum without duplicates from all orders.*/
SELECT DISTINCT snum FROM ORDERS;

/*Display names and commissions of all salespeople in London.*/
SELECT sname, comm FROM SALESPEOPLE WHERE city = 'London';

/*All customers with rating of 100.*/
SELECT cname FROM CUST WHERE rating = 100;

/*Produce orderno, amount and date form all rows in the order table.*/
SELECT onum, amt, odate FROM ORDERS;

/*All customers in San Jose, who have rating more than 200.*/
Select cname from cust where rating > 200;

/*All customers who were either located in San Jose or had a rating above 200.*/
SELECT * FROM CUST WHERE city = 'San Jose' OR rating > 200;

/*All orders for more than $1000.*/
SELECT * FROM ORDERS WHERE amt > 1000;

/*Names and citires of all salespeople in london with commission above 0.10.*/
SELECT sname, city from SALESPEOPLE WHERE city = 'London' and comm > 0.10;

/*All customers excluding those with rating < = 100 unless they are located in Rome.*/
SELECT cname FROM CUST WHERE rating <= 100 OR city = 'Rome'; 

/*All salespeople either in Barcelona or in london.*/
SELECT sname, city FROM SALESPEOPLE WHERE city in ('Barcelona', 'London');

/*All salespeople with commission between 0.10 and 0.12. (Boundary values should be excluded)*/
SELECT sname, comm FROM SALESPEOPLE WHERE comm > 0.10 AND comm < 0.12;

/*All customers with NULL values in city column.*/
SELECT * FROM CUST WHERE city IS NULL;

/*All orders taken on Oct 3Rd and Oct 4th 1994.*/
SELECT * FROM ORDERS WHERE ODATE IN ('03-OCT-94', '04-OCT-94')

/*All customers serviced by peel or Motika.*/
SELECT DISTINCT cname from CUST JOIN ORDERS on ORDERS.CNUM = CUST.CNUM WHERE ORDERS.SNUM IN (SELECT snum FROM SALESPEOPLE WHERE sname IN ('Peel','Motika'));

/*All customers whose names begin with a letter from A to B.*/
SELECT cname FROM CUST WHERE cname LIKE 'A%' OR cname LIKE 'B%';

/*All orders except those with 0 or NULL value in amt field.*/
SELECT onum, amt FROM ORDERS WHERE amt IS NOT NULL AND amt != 0;

/*Count the number of salespeople currently listing orders in the order table.*/
SELECT COUNT(DISTINCT snum) AS 'NUMBER OF SALESPEOPLE' FROM ORDERS;

/*Largest order taken by each salesperson, datewise.*/
SELECT odate, snum, max(amt) FROM ORDERS GROUP BY odate, snum ORDER BY odate, snum;

/*Largest order taken by each salesperson with order value more than $3000.*/
SELECTT odate, snum, max(amt) FROM ORDERS where amt > 3000 GROUP BY odate, snum ORDER BY odate, snum;

/*Largest order taken by each salesperson with order value more than $3000.*/
SELECT odate, snum, MAX(amt) FROM ORDERS WHERE amt > 3000 GROUP BY odate, snum;

/*Which day had the hightest total amount ordered.*/
SELECT odate, amt, snum, cnum FROM ORDERS WHERE amt = (SELECT MAX(amt) FROM ORDERS)

/*count all orders for Oct 3rd.*/
SELECT COUNT(odate) FROM ORDERS WHERE odate = '03-OCT-94'

/*Count the number of different non NULL city values in customers table.*/
SELECT COUNT(DISTINCT city) FROM CUST;

/*Select each customer’s smallest order.*/
SELECT cnum, MIN(amt) FROM ORDERS GROUP BY cnum;

/*First customer in alphabetical order whose name begins with G.*/
SELECT cname FROM CUST WHERE cname LIKE 'G%' ORDER BY cname ASC LIMIT 1;

/*Get the output like "For dd/mm/yy there are_orders.*/
SELECT 'For ' || to_char(odate,'dd/mm/yy') || ' there are '||  count(*) || ' Orders' FROM ORDERS GROUP BY odate;

/*Assume that each salesperson has a 12% commission. Produce order no., salesperson no., and amount of salesperson’s commission for that order.*/
SELECT onum, snum, amt, amt * 0.12 FROM ORDERS ORDER BY snum;

/*Find highest rating in each city. Put the output in this form. For the city (city), the highest rating is : (rating).*/
SELECT 'For the city (' || city || '), the highest rating is: ' || MAX(rating) FROM CUST GROUP BY city;

/*All combinations of salespeople and customers who shared a city. (ie same city)*/
SELECT C.CNAME, S.SNAME, C.CITY FROM CUST C JOIN SALESPEOPLE S ON C.CITY = S.CITY;

/*Name of all customers matched with the salespeople serving them.*/
SELECT C.CNAME AS Customer_Name, S.SNAME AS Salesperson_Name FROM CUST C JOIN SALESPEOPLE S ON C.SNUM = S.SNUM;

/*Name of all customers matched with the salespeople serving them.*/
SELECT C.CNAME, S.SNAME FROM CUST C JOIN SALESPEOPLE S ON C.SNUM = S.SNUM;

/*List each order number followed by the name of the customer who made the order.*/
SELECT O.ONUM, C.CNAME FROM CUST C JOIN ORDERS O ON C.CNUM = O.CNUM;

/*Names of salesperson and customer for each order after the order number.*/
SELECT O.onum, C.cname, S.sname from ORDERS O JOIN CUST C ON O.CNUM = C.CNUM JOIN SALESPEOPLE S ON O.SNUM = S.SNUM;

/*Produce all customer serviced by salespeople with a commission above 12%.*/
SELECT C.CNAME, S.SNAME, S.COMM FROM CUST C JOIN ORDERS O ON C.CNUM = O.CNUM JOIN SALESPEOPLE S ON O.SNUM = S.SNUM WHERE S.comm > 0.12;

/*Calculate the amount of the salesperson’s commission on each order with a rating above 100.*/
SELECT O.onum, C.cname, C.rating, S.sname, O.amt, (O.amt * S.comm) FROM ORDERS O JOIN SALESPEOPLE S ON O.SNUM = S.SNUM JOIN CUST C ON O.CNUM = C.CNUM WHERE C.RATING > 100;

/*Find all pairs of customers having the same rating.*/
SELECT C1.cname, C2.cname, C1.RATING from CUST C1 JOIN CUST C2 ON C1.RATING = C2.RATING WHERE C1.CNUM < C2.CNUM;

/*Policy is to assign three salesperson to each customers. Display all such combinations.*/
SELECT C1.cname, C2cname, C1.rating FROM CUST C1, CUST C2 WHERE C1.rating = C2.RATING AND C1.CNUM != C2.CNUM and C1.CNUM ≶ C2.CNUM;

/*Display all customers located in cities where salesman serres has customer.*/
SELECT C.CNAME, C.CITY FROM CUST C WHERE C.CITY IN (SELECT DISTINCT C.CITY FROM CUST C JOIN SALESPEOPLE S ON C.SNUM = S.SNUM WHERE S.SNAME = 'Serres');

/*Find all pairs of customers served by single salesperson.*/
SELECT C1.CNAME, C2.CNAME, C1.SNUM FROM CUST C1 JOIN CUST C2 ON C1.SNUM = C2.SNUM WHERE C1.CNUM <> C2.CNUM ORDER BY C1.SNUM, C1.CNAME, C2.CNAME;

/*Produce all pairs of salespeople which are living in the same city. Exclude combinations of salespeople with themselves as well as duplicates with the order reversed.*/
SELECT S1.SNAME, S2.SNAME, S1.CITY FROM SALESPEOPLE S1 JOIN SALESPEOPLE S2 ON S1.CITY = S2.CITY WHERE S1.SNUM < S2.SNUM ORDER BY S1.CITY, S1.SNAME, S2.SNAME;

/*Produce names and cities of all customers with the same rating as Hoffman.*/
SELECT cname, city FROM CUST WHERE rating = (SELECT rating FROM CUST WHERE cname = 'Hoffman');

/*Extract all the orders of Motika.*/
SELECT O.* FROM ORDERS O JOIN SALESPEOPLE S ON O.SNUM = S.SNUM WHERE S.SNAME = 'Motika';

/*All orders credited to the same salesperson who services Hoffman.*/
SELECT O.ONUM, S.SNAME, C.CNAME, O.AMT FROM ORDERS O JOIN SALESPEOPLE S ON O.SNUM = S.SNUM JOIN CUST C ON O.CNUM = C.CNUM WHERE O.SNUM = (SELECT S.SNUM FROM SALESPEOPLE S JOIN CUST C ON S.SNUM = C.SNUM WHERE C.CNAME = 'Hoffman');

/*All orders that are greater than the average for Oct 4.*/
SELECT * FROM ORDERS WHERE ODATE > '04-OCT-94' AND AMT > (SELECT AVG(AMT) FROM ORDERS WHERE ODATE = '04-OCT-94');

/*Find average commission of salespeople in london.*/
SELECT AVG(comm) FROM SALESPEOPLE WHERE city = 'London';

/*Find all orders attributed to salespeople servicing customers in london.*/
SELECT O.* FROM ORDERS O JOIN CUST C ON O.CNUM = C.CNUM JOIN SALESPEOPLE S ON O.SNUM = S.SNUM WHERE C.CITY = 'London';

/*Extract commissions of all salespeople servicing customers in London.*/
SELECT S.comm, C.city FROM SALESPEOPLE S Join CUST C ON S.SNUM = C.SNUM WHERE C.CITY = 'London';

/*Find all customers whose cnum is 1000 above the snum of serres.*/
SELECT * FROM CUST WHERE cnum = (SELECT snum + 1000 FROM SALESPEOPLE WHERE sname = 'Serres');

/*Count the customers with rating above San Jose’s average.*/
SELECT COUNT(rating) FROM CUST WHERE rating > (SELECT AVG(rating) FROM CUST WHERE city = 'San Jose')
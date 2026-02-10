SELECT Category, SUM(TransactionAmount)
FROM transactions
GROUP BY Category;

SELECT * FROM transactions
WHERE TransactionAmount > 20000;

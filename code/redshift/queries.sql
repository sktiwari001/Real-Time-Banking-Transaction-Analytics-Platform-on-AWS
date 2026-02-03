1.CREATE DATABASE banking_analytics;
SELECT channel, COUNT(*) AS total_txns, SUM(amount) AS total_amount
FROM transactions_gold
GROUP BY channel;
SELECT branch, SUM(amount) AS branch_revenue
FROM transactions_gold
GROUP BY branch
ORDER BY branch_revenue DESC;

2.CREATE TABLE banking_transactions (
    txn_id VARCHAR(100),
    account_id VARCHAR(50),
    customer_name VARCHAR(100),
    amount INT,
    channel VARCHAR(20),
    branch VARCHAR(50),
    txn_time TIMESTAMP,
    is_suspicious VARCHAR(5)
);

3.INSERT INTO banking_transactions
SELECT
    txn_id,
    account_id,
    customer_name,
    CAST(amount AS INT),
    channel,
    branch,
    CAST(txn_time AS TIMESTAMP),
    is_suspicious
FROM
    awsdatabasecatalog.banking_analytics_new.transactions_gold;

4.SELECT * FROM banking_transactions LIMIT 5;

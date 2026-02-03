1.SELECT *
FROM banking_raw_ext.transactions_gold
LIMIT 5;


2.SELECT *
FROM awsdatabasecatalog.banking_analytics_db.transactions_gold
LIMIT 5;

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
 awsdatacatalog.banking_analytics_new.transactions_gold;
 

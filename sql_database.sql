-- ===== HEAT EXCHANGER SQL DATABASE =====

CREATE DATABASE heat_exchanger_db;
USE heat_exchanger_db;

CREATE TABLE exchanger_data (
  id INT PRIMARY KEY AUTO_INCREMENT,
  date DATE,
  Th_in FLOAT, Tc_in FLOAT,
  m_hot FLOAT, m_cold FLOAT,
  Area FLOAT, U FLOAT, Q FLOAT,
  fouling_pct FLOAT, saving_usd FLOAT,
  status VARCHAR(30)
);

-- 1. Total Records
SELECT COUNT(*) FROM exchanger_data;

-- 2. Avg U
SELECT AVG(U) as avg_U FROM exchanger_data;

-- 3. Top 10 Best U
SELECT * FROM exchanger_data ORDER BY U DESC LIMIT 10;

-- 4. Fouling Alert
SELECT * FROM exchanger_data WHERE fouling_pct > 5;

-- 5. Monthly Saving - Power BI / Tableau layi
SELECT Month, SUM(saving_usd) as total_saving FROM exchanger_data GROUP BY Month;

-- 6. Healthy vs Cleaning Count
SELECT status, COUNT(*) FROM exchanger_data GROUP BY status;

-- 7. Avg Q by Area Group
SELECT CASE WHEN Area < 2 THEN 'Small' WHEN Area < 4 THEN 'Medium' ELSE 'Large' END as size, AVG(Q) FROM exchanger_data GROUP BY size;

-- 8. Max Saving Day
SELECT date, saving_usd FROM exchanger_data ORDER BY saving_usd DESC LIMIT 1;

-- 9. Join Example - Exchanger + Maintenance Table
SELECT e.*, m.last_cleaning FROM exchanger_data e LEFT JOIN maintenance m ON e.id = m.exchanger_id;

-- 10. Window Function - Running Total Saving
SELECT date, saving_usd, SUM(saving_usd) OVER (ORDER BY date) as running_total FROM exchanger_data;

-- 11. Cleaning Required - Last 30 Days
SELECT * FROM exchanger_data WHERE fouling_pct > 5 AND date >= CURDATE() - INTERVAL 30 DAY;

-- 12. Efficiency Drop
SELECT AVG(U) as avg_U, MAX(U)-MIN(U) as U_range FROM exchanger_data;

-- 13. Update Status
UPDATE exchanger_data SET status='CLEANING REQUIRED' WHERE fouling_pct > 5;

-- 14. Delete Dirty Data
DELETE FROM exchanger_data WHERE U IS NULL OR U > 5000;

-- 15. Create View for Power BI
CREATE VIEW vw_dashboard AS SELECT Month, AVG(U) as avg_U, SUM(saving_usd) as saving, AVG(fouling_pct) as fouling FROM exchanger_data GROUP BY Month;

-- Vendor Issue/Risk Performance Summary
SELECT 
    r.Project_ID,
    p.Project_Name,
    r.Type,
    r.Description,
    r.Severity,
    r.Status,
    r.Owner
FROM raid_log r
JOIN projects p
    ON r.Project_ID = p.Project_ID
WHERE r.Status = 'Open'
ORDER BY r.Severity DESC;

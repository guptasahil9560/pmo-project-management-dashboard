-- Delayed Tasks Across All Projects
SELECT 
    t.Task_ID,
    t.Task_Name,
    t.Project_ID,
    p.Project_Name,
    t.Owner,
    t.Due_Date,
    t.Status,
    t.Completion_Percent
FROM tasks t
JOIN projects p
    ON t.Project_ID = p.Project_ID
WHERE t.Status = 'Delayed'
ORDER BY t.Due_Date ASC;

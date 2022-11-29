

USE foreclose;

SELECT COUNT(P_Type) AS Property1
FROM foreclose
WHERE P_Type = "Multi-Family";

SELECT COUNT(P_Type) AS Property2
FROM foreclose
WHERE P_Type = "Single Family";

SELECT COUNT(P_Type) AS Property2
FROM foreclose
WHERE P_Type = "Vacant Residential";

SELECT COUNT(P_Type) AS Property2
FROM foreclose
WHERE P_Type = "Non-Residential";
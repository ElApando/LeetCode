WITH client AS
(
	SELECT  users_id AS client
	       ,banned   AS cli_b
	FROM Users
	WHERE role = 'client'
	AND banned != "Yes"
), driver AS
(
	SELECT  users_id AS driver
	       ,banned   AS dri_b
	FROM Users
	WHERE role = 'driver'
	AND banned != "Yes"
), _all_ AS
(
	SELECT  *
	FROM Trips a
	JOIN client b
	ON a.client_id = b.client
	JOIN driver c
	ON a.driver_id = c.driver
)
SELECT  request_at                                                                                                                AS 'Day'
       ,ROUND(COUNT(CASE WHEN status = 'cancelled_by_client' OR status = 'cancelled_by_driver' THEN 1 END) / COUNT(request_at),2) AS 'Cancellation Rate'
FROM _all_
WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY  request_at
ORDER BY  request_at
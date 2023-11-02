WITH LatestData AS (
SELECT
propertyid,
unitid,
MAX(timestamp) AS latest_timestamp
FROM
takehome.raw_rent_roll_history
WHERE
timestamp <= '2023-06-04' --- Updated the desired timestamp here
GROUP BY
propertyid, unitid
)
SELECT
R.propertyid,
R.unitid,
R.status,
R.total,
R.pastdue,
R.timestamp
FROM
LatestData AS L
LEFT JOIN takehome.raw_rent_roll_history AS R
ON L.propertyid = R.propertyid
AND L.unitid = R.unitid
AND L.latest_timestamp = R.timestamp
ORDER BY
R.propertyid, R.unitid;

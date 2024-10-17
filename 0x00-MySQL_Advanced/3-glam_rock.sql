-- SQL script to list all bands with Glam rock as their main style,
-- ranked by their longevity (in years until 2022)

SELECT
    band_name,
    CASE
        -- If the band is still active (i.e., split is NULL), calculate lifespan until 2022
        WHEN split IS NULL THEN 2022 - formed
        -- If the band has split, calculate lifespan based on the split year
        ELSE split - formed
    END AS lifespan
FROM
    metal_bands
WHERE
    style = 'Glam rock'
ORDER BY
    lifespan DESC;

#Making a database of the information of the movies 
CREATE DATABASE IF NOT EXISTS movies_data;
USE  movies_data;


# Tables for data of movies, csv will be charge from Python to the next tables

CREATE TABLE IF NOT EXISTS Amazon_prime_titles(
show_id varchar(200),
type_ VARCHAR(300),
title VARCHAR(300),
director VARCHAR(3000),
cast VARCHAR(3000),
country VARCHAR(300),
date_added VARCHAR(300),
release_year VARCHAR(300),
rating VARCHAR(300),
duration VARCHAR(300),
listed_in VARCHAR(300),
description_ VARCHAR(5000)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE IF NOT EXISTS disney_plus_titles(
show_id varchar(200) ,
type_ VARCHAR(300),
title VARCHAR(300),
director VARCHAR(3000),
cast VARCHAR(3000),
country VARCHAR(300),
date_added VARCHAR(300),
release_year VARCHAR(300),
rating VARCHAR(300),
duration VARCHAR(300),
listed_in VARCHAR(300),
description_ VARCHAR(5000)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE IF NOT EXISTS hulu_titles(
show_id varchar(200) ,
type_ VARCHAR(300),
title VARCHAR(300),
director VARCHAR(3000),
cast VARCHAR(3000),
country VARCHAR(300),
date_added VARCHAR(300),
release_year VARCHAR(300),
rating VARCHAR(300),
duration VARCHAR(300),
listed_in VARCHAR(300),
description_ VARCHAR(5000)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE IF NOT EXISTS netflix_titles(
show_id varchar(200) ,
type_ VARCHAR(300),
title VARCHAR(300),
director VARCHAR(3000),
cast VARCHAR(3000),
country VARCHAR(300),
date_added VARCHAR(300),
release_year VARCHAR(300),
rating VARCHAR(300),
duration VARCHAR(300),
listed_in VARCHAR(300),
description_ VARCHAR(5000)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

#The data is charging from python

#transfroming the data of amazon

#generating a new id that is the combination of the first letter of the platform plus the show_id
ALTER TABLE amazon_prime_titles
ADD COLUMN id VARCHAR(50) NOT NULL FIRST;

UPDATE amazon_prime_titles
SET id =concat('a',show_id) 
WHERE id IS NULL OR ID LIKE '';

#The null values in rating column set as G (for all people)

UPDATE amazon_prime_titles
SET rating= 
	CASE 
		WHEN rating IS NULL OR rating like 'NULL' THEN 'g'
        ELSE rating
        END;

#ALL FIELDS IN LOWER CASE

UPDATE amazon_prime_titles
SET
	type_=LOWER(type_),
    title=LOWER(title),
    director=LOWER(director),
    cast=LOWER(cast),
    country=LOWER(country),
    rating=LOWER(rating),
    duration=LOWER(duration),
    listed_in=LOWER(listed_in),
    description_=LOWER(description_),
	date_added=LOWER(date_added);
    
    
#Date  in format year-month-day

UPDATE amazon_prime_titles
SET date_added=
	CASE 
		WHEN date_added IS NULL OR date_added LIKE 'NULL' THEN date_added
        ELSE CONCAT(SUBSTRING_INDEX(date_added, ',', -1),SUBSTRING_INDEX(date_added, ',', 1))
        END; 


#Convert duration to Int_value  and string_value

ALTER TABLE amazon_prime_titles
ADD COLUMN duration_int INT AFTER duration,
ADD COLUMN   duration_type VARCHAR(20) AFTER duration_int;

UPDATE amazon_prime_titles
SET duration_int=CAST(SUBSTRING_INDEX(duration, ' ', 1) AS UNSIGNED),
 duration_type= SUBSTRING_INDEX(duration, ' ', -1);

SELECT * FROM amazon_prime_titles;


#_______________________________________________________________________________________________________________________________________________________________________
#Now Transform data of Disney Plus
#generating a new id that is the combination of the first letter of the platform plus the show_id
ALTER TABLE disney_plus_titles
ADD COLUMN id VARCHAR(50) NOT NULL FIRST;

UPDATE disney_plus_titles
SET id =concat('d',show_id) 
WHERE id IS NULL OR id LIKE '';

#The null values in rating column set as G (for all people)

UPDATE disney_plus_titles
SET rating= 
	CASE 
		WHEN rating IS NULL OR rating like 'NULL' THEN 'g'
        ELSE rating
        END;

#ALL FIELDS IN LOWER CASE

UPDATE disney_plus_titles
SET
	type_=LOWER(type_),
    title=LOWER(title),
    director=LOWER(director),
    cast=LOWER(cast),
    country=LOWER(country),
    rating=LOWER(rating),
    duration=LOWER(duration),
    listed_in=LOWER(listed_in),
    description_=LOWER(description_),
	date_added=LOWER(date_added);
    
#Date  in format year-month-day

update disney_plus_titles
set date_added=
	CASE 
		WHEN date_added IS NULL OR date_added like 'NULL' THEN date_added
        ELSE CONCAT(SUBSTRING_INDEX(date_added, ',', -1),SUBSTRING_INDEX(date_added, ',', 1))
        END; 


#Convert duration to Int_value  and string_value

alter table disney_plus_titles
ADD COLUMN duration_int INT AFTER duration,
ADD COLUMN   duration_type VARCHAR(20) AFTER duration_int;

UPDATE disney_plus_titles
SET duration_int=CAST(SUBSTRING_INDEX(duration, ' ', 1) AS UNSIGNED),
 duration_type= SUBSTRING_INDEX(duration, ' ', -1);

SELECT * FROM disney_plus_titles;

#_______________________________________________________________________________________________________________________________________________________________________
#Now Transform data of hulu

#generating a new id that is the combination of the first letter of the platform plus the show_id

ALTER TABLE hulu_titles
ADD COLUMN id VARCHAR(50) NOT NULL FIRST;

UPDATE hulu_titles
SET id =concat('h',show_id) 
WHERE id IS NULL OR id LIKE '';

#The null values in rating column set as G (for all people)

UPDATE hulu_titles
SET rating= 
	CASE 
		WHEN rating IS NULL OR rating like 'NULL' THEN 'g'
        ELSE rating
        END;

#ALL FIELDS IN LOWER CASE

UPDATE hulu_titles
SET
	type_=LOWER(type_),
    title=LOWER(title),
    director=LOWER(director),
    cast=LOWER(cast),
    country=LOWER(country),
    rating=LOWER(rating),
    duration=LOWER(duration),
    listed_in=LOWER(listed_in),
    description_=LOWER(description_),
	date_added=LOWER(date_added);
    
#Date  in format year-month-day

update hulu_titles
set date_added=
	CASE 
		WHEN date_added IS NULL OR date_added LIKE 'NULL' THEN date_added
        ELSE CONCAT(SUBSTRING_INDEX(date_added, ',', -1),SUBSTRING_INDEX(date_added, ',', 1))
        END; 


#Convert duration to Int_value  and string_value

ALTER TABLE hulu_titles
ADD COLUMN duration_int VARCHAR(20) AFTER duration,
ADD COLUMN   duration_type VARCHAR(20) AFTER duration_int;

UPDATE hulu_titles
SET duration_int=
	CASE
    WHEN duration IS NULL OR LOWER(duration) LIKE 'null' THEN duration
    ELSE SUBSTRING_INDEX(duration, ' ', 1) 
    END,
duration_type=
 CASE
    WHEN duration IS NULL OR LOWER(duration) LIKE 'null' THEN duration
    ELSE SUBSTRING_INDEX(duration, ' ', -1)
    END;

SELECT * FROM hulu_titles;

#_______________________________________________________________________________________________________________________________________________________________________
#Now Transform data of Netflix
#generating a new id that is the combination of the first letter of the platform plus the show_id
ALTER TABLE netflix_titles
ADD COLUMN id VARCHAR(50) NOT NULL FIRST;

UPDATE netflix_titles
SET id =concat('n',show_id) 
WHERE id IS NULL OR id LIKE '';

#The null values in rating column set as G (for all people)

UPDATE netflix_titles
SET rating= 
	CASE 
		WHEN rating IS NULL OR rating LIKE 'NULL' THEN 'g'
        ELSE rating
        END;

#ALL FIELDS IN LOWER CASE

UPDATE netflix_titles
SET
	type_=LOWER(type_),
    title=LOWER(title),
    director=LOWER(director),
    cast=LOWER(cast),
    country=LOWER(country),
    rating=LOWER(rating),
    duration=LOWER(duration),
    listed_in=LOWER(listed_in),
    description_=LOWER(description_),
	date_added=LOWER(date_added);
    
#Date  in format year-month-day

update netflix_titles
SET date_added=
	CASE 
		WHEN date_added IS NULL OR date_added LIKE 'NULL' THEN date_added
        ELSE CONCAT(SUBSTRING_INDEX(date_added, ',', -1),SUBSTRING_INDEX(date_added, ',', 1))
        END; 


#Convert duration to Int_value  and string_value

ALTER TABLE netflix_titles
ADD COLUMN duration_int VARCHAR(20) AFTER duration,
ADD COLUMN   duration_type VARCHAR(20) AFTER duration_int;

UPDATE netflix_titles
SET duration_int=
	CASE
    WHEN duration IS NULL OR LOWER(duration) LIKE 'null' THEN duration
    ELSE SUBSTRING_INDEX(duration, ' ', 1) 
    END,
duration_type=
 CASE
    WHEN duration IS NULL OR LOWER(duration) LIKE 'null' THEN duration
    ELSE SUBSTRING_INDEX(duration, ' ', -1)
    END;
    
SELECT * FROM netflix_titles;
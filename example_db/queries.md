## Datatypes

- INT
- DECIMAL (M,N)
- VARCHAR(N)
- BLOB
- DATE         "YYYY-MM-DD"
- TIMESTAMP    "YYYY-MM-DD HH:MM:SS"

## Keywords

    NOT NULL,
    DEFAULT 'blah',
    UNIQUE,
    AUTO_INCREMENT for primary key

## Create tables

    CREATE TABLE name_of_table (
        student_id INT PRIMARY KEY,
        name VARCHAR(20) NOT NULL,
        major VARCHAR(10) UNIQUE,
        PRIMARY KEY(student_id)
    );

#### Describe tables

    DESCRIBE name_of_table;

#### Delete table

    DROP TABLE name_of_table;

#### Modify table

    ALTER TABLE name_of_table ADD gpa DECIMAL(3,2);
    ALTER TABLE name_of_table DROP COLUMN gpa;

#### Inserting data into table

    INSERT INTO name_of_table VALUES (
        1, 'Jack', 'Biology'
    );
    INSERT INTO name_of_table VALUES (
        2, 'Kate', 'Sociology'
    );

    INSERT INTO name_of_table(student_id, name) VALUES (
        3, 'Claire',
    );
    INSERT INTO name_of_table VALUES (
        4, 'Mike', 'Computer Science'
    );

#### Update or deleting

    UPDATE name_of_table
    SET major = 'Biochemistry', name = 'blah'
    WHERE major = 'Biology' OR major = 'Chemistry';


    DELETE FROM name_of_table
    WHERE student_id = 5;

    DELETE FROM name_of_table; will delete all the rows

#### Selecting data from table

    SELECT * FROM name_of_table;

    SELECT * from name_of_table ORDER BY column_name DESC;

    SELECT * FROM name_of_table ORDER BY first_col, second_col;

    SELECT * FROM name_of_table LIMIT 5;

    SELECT first_col, second_col FROM name_of_table;

    SELECT first_col AS something, second_col AS something FROM name_of_table;

    SELECT DISTINCT first_col FROM name_of_table;

    SELECT COUNT(emp_id) FROM name_of_table;

    SELECT COUNT(emp_id) FROM name_of_table WHERE sex = 'F' AND birth_date > '1970-01-01';

    SELECT AVG(salary) FROM name_of_table;
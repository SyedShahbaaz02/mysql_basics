import mysql.connector

# Establish a connection to the MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password"
)

cursor = mydb.cursor()

# Create the database
cursor.execute('CREATE DATABASE IF NOT EXISTS ds_blogs')

# Switch to the ds_blogs database
mydb = mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password",
    database="ds_blogs"
)

cursor = mydb.cursor()

# Create the posts table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        post_id INT PRIMARY KEY,
        author_id INT,
        post_first_published_on DATE,
        num_likes INT,
        num_dislikes INT,
        num_comments INT
    )
''')

# Insert data into the posts table
cursor.execute('''
    INSERT INTO posts (post_id, author_id, post_first_published_on, num_likes, num_dislikes, num_comments)
    VALUES
        (1, 1, '2023-06-01', 10, 2, 5),
        (2, 2, '2023-06-02', 8, 1, 3),
        (3, 3, '2023-06-03', 12, 0, 7),
        (4, 1, '2023-06-04', 15, 3, 10),
        (5, 2, '2023-06-05', 6, 2, 2),
        (6, 4, '2023-06-06', 20, 1, 8),
        (7, 5, '2023-06-07', 14, 0, 6),
        (8, 3, '2023-06-08', 9, 2, 4),
        (9, 6, '2023-06-09', 18, 1, 7),
        (10, 1, '2023-06-10', 11, 0, 5),
        (11, 2, '2023-06-11', 7, 1, 3),
        (12, 7, '2023-06-12', 13, 3, 9),
        (13, 8, '2023-06-13', 16, 2, 6),
        (14, 3, '2023-06-14', 10, 1, 4),
        (15, 9, '2023-06-15', 12, 0, 5),
        (16, 1, '2023-06-16', 9, 2, 3),
        (17, 4, '2023-06-17', 15, 1, 7),
        (18, 5, '2023-06-18', 8, 0, 4),
        (19, 2, '2023-06-19', 11, 1, 6),
        (20, 6, '2023-06-20', 13, 2, 8)
''')

# Create the writers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS writers (
        author_id INT PRIMARY KEY,
        author_first_enroldate DATE,
        num_posts_written INT,
        total_num_likes INT,
        total_num_dislikes INT,
        total_num_comments INT
    )
''')

# Insert data into the writers table
cursor.execute('''
    INSERT INTO writers (author_id, author_first_enroldate, num_posts_written, total_num_likes, total_num_dislikes, total_num_comments)
    VALUES
        (1, '2022-01-01', 5, 40, 8, 25),
        (2, '2022-02-01', 8, 60, 10, 30),
        (3, '2022-03-01', 7, 50, 5, 20),
        (4, '2022-04-01', 5, 30, 2, 15),
        (5, '2022-05-01', 3, 20, 3, 10),
        (6, '2022-06-01', 4, 35, 6, 18),
        (7, '2022-07-01', 6, 45, 4, 22),
        (8, '2022-08-01', 2, 15, 1, 8),
        (9, '2022-09-01', 7, 55, 7, 28),
        (10, '2022-10-01', 3, 25, 2, 12)
''')

# Commit the changes
mydb.commit()

# Close the cursor and connection
cursor.close()
mydb.close()



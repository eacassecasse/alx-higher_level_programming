-- Creates a new user ``user_0d_1`` only if it doesn't exist
-- with the password ``user_0d_1_pwd``
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
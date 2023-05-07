-- Database: db_sunny_web

-- DROP DATABASE IF EXISTS db_sunny_web;

CREATE DATABASE db_sunny_web
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

ALTER ROLE postgres IN DATABASE db_sunny_web
    SET "TimeZone" TO 'Europe/Berlin';
/*

create the database :
    create database superMarket;

create table products :
    create table products (id int primary key, name varchar(100), price int, quantity int);

*/

#include <mysql.h>
#include "h/color.h"
#include <iostream>
#include <cstdio>

int main() {
    color color;

    MYSQL *conn;
    MYSQL_RES *res;
    MYSQL_ROW row;

    char const *server = "127.0.0.1";
    char const *user = "root";
    char const *password = "12305123";
    char const *database = "superMarket";
    
    conn = mysql_init(NULL);

    if (!mysql_real_connect(conn, server, user, password, database, 0, NULL, 0)) {
        std::cout << stderr << "\n" << mysql_errno(conn);
        return -1;
    }

    if (!mysql_query(conn, "select * from products")) {
        std::cout << stderr << "\n" << mysql_errno(conn);
        return -1;
    }
    
}
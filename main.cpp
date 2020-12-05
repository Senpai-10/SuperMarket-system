#include <iostream>
#include <string>
#include <Windows.h>
#include "h/color.h"
#include <fstream>
#include <filesystem>

HANDLE color = GetStdHandle(STD_OUTPUT_HANDLE);


void print(std::string msg) {std::cout << msg;}
void menuItem(std::string number, std::string msg) { Gray; print(">> "); White; print(number); print(". "); print(msg + "\n");}

bool exists(const char * FileName) {
    FILE *file;
    if (file = fopen(FileName, "r")) {
        fclose(file);
        return true;
        
    } else {
        return false;
    }
}


class config {
    // configuration class 
    public:
        const std::string DatabaseName = "db";
        
        // create new Product folder
        void CreateProduct(std::string name) {
            if (name == "") {print("invalid Product Name");}
            
            // WinExec(("mkdir " + DatabaseName).c_str(), SW_HIDE);
            system(("mkdir " + DatabaseName).c_str());
            system(("cd " + DatabaseName + " && mkdir \"" + name + "\"").c_str());
            
        }

        void write(std::string ProductName, std::string key, std::string value) {
            std::ofstream write;
            write.open((DatabaseName + "/" + ProductName + "/" + key + ".txt").c_str());
            write << value;
            write.close();
        }

        std::string read(std::string ProductName, std::string key) {
            std::string line;
            std::ifstream read;
            read.open((DatabaseName + "/" + ProductName + "/" + key + ".txt").c_str());
            read >> line;
            return line;
        }

        void pop(std::string ProductName) {
            system(("cd \"" + DatabaseName + "/" + ProductName + "\"" + " && del * /S /Q").c_str());
            system(("cd \"" + DatabaseName + "\"" + " && rmdir " + ProductName).c_str());

        }

        void clear() {
            system(("rd /s /q \"" + DatabaseName + "\"").c_str());
        }
};


class product {
    public:
        config Config;
        std::string ProductName;
        std::string ProductPrice;
        std::string ProductAmount;

        // add product to the stock
        void add() {

            print("\n# YOU CAN'T USE SPACE\n");

            print("Product name: ");
            std::cin>>ProductName;
    
            print("Product price: ");
            std::cin>>ProductPrice;
            
            print("Product amount: ");
            std::cin>>ProductAmount;

            Config.CreateProduct(ProductName);
            Config.write(ProductName, "price", "$" + ProductPrice);
            Config.write(ProductName, "amount", ProductAmount);

            print("\n------------------------------------------\n");
            print(" New                :    \n");
            print("------------------------------------------\n");
            print(" Product name       :    " + ProductName + "\n");
            print(" Product price      :    " + ProductPrice + "\n");
            print(" Product amount     :    " + ProductAmount + "\n");
            print("------------------------------------------\n");
        }
        // remove product from the stock
        void remove() {
            print("Product name: ");
            std::cin>>ProductName;

            Config.pop(ProductName);
        }
        // change product price
        void changePrice() {
            print("Product name: ");
            std::cin>>ProductName;

            print(("Product price: " + Config.read(ProductName, "price")).c_str());

            print("new Product price: ");
            std::cin>>ProductPrice;

            print(("new Product price: " + Config.read(ProductName, "price")).c_str());
        }
        // get all products in stock
        void stock() {
            LGreen;
            print("\nStock:\n");
            Gray;
            print("--------------\n\n");
            White;
            system(("cd "+ Config.DatabaseName +" && dir /b").c_str());
            print("\n--------------\n\n");
        }
        // search for specific product and get remaining number in stock + price
        void search() {
            print("Product name: ");
            std::cin>>ProductName;
            


            print("\n------------------------------------------\n");
            print(" Search             :    \n");
            print("------------------------------------------\n");
            print(" Product name       :    " + ProductName + "\n");
            print(" Product price      :    " + Config.read(ProductName, "price") + "\n");
            print(" Product amount     :    " + Config.read(ProductName, "amount") + "\n");
            print("------------------------------------------\n");
        }
        // clearing all stored data
        void clearData() {
            Config.clear();
        }
};



// main menu function
void menu() {
    print(R"(
   _____                       __  ___           __        __ 
  / ___/__  ______  ___  _____/  |/  /___ ______/ /_____  / /_
  \__ \/ / / / __ \/ _ \/ ___/ /|_/ / __ `/ ___/ //_/ _ \/ __/
 ___/ / /_/ / /_/ /  __/ /  / /  / / /_/ / /  / ,< /  __/ /_  
/____/\__,_/ .___/\___/_/  /_/  /_/\__,_/_/  /_/|_|\___/\__/  
          /_/                                                 
    )");
    print("\n");

    menuItem("1", "add product");
    menuItem("2", "remove product");
    menuItem("3", "change Price");
    menuItem("4", "see stock");
    menuItem("5", "search");
    menuItem("6", "clear Data");

}



int main() {
    int choice;
    product Product;
    config Config;


    
    system("cls");
    menu();
    
    print("\nYour choice number: ");
    std::cin>>choice;

    print("\n------------------------------------------\n");
    

    
    switch (choice)
    {
        case 1:
            // add product
            Product.add();
            break;
        
        case 2:
            // remove product
            Product.remove();
            break;
        
        case 3:
            // change price
            Product.changePrice();
            break;
        
        case 4:
            // see stock
            Product.stock();
            break;
        
        case 5:
            // search
            Product.search();
            break;
        
        case 6:
            // clear Data
            Product.clearData();
            break;
        
        default:
            print("error");
            break;
    }

    

}
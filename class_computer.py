'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
'''

import sqlite3


class Computer:
    """AI is creating summary for
    """
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.hdd = None
        self.hdd_type = None
        self.conn = sqlite3.connect('/home/admin97/myprojects/OOP/Data.db')
        self.create_table()
# Create the computers table if it doesn't exist

    def create_table(self):
        """AI is creating summary for create_table
        """
        sql = '''
        CREATE TABLE IF NOT EXISTS computers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cpu TEXT,
            ram INTEGER,
            hdd INTEGER,
            hdd_type TEXT
        )
        '''
        self.conn.execute(sql)
        self.conn.commit()

    def get_user_input(self):
        """AI is creating summary for get_user_input
        """
        cpu_options = {
            1: "Intel Core i5",
            2: "Intel Core i7",
            3: "AMD Ryzen 5",
            4: "AMD Ryzen 7"
        }
        print("Available processor models:")
        for option, model in cpu_options.items():
            print(f"{option}: {model}")
        cpu_choice = int(input("Select the processor model (enter the number): "))
        self.cpu = cpu_options.get(cpu_choice)
        # Prompt the user to enter the amount of RAM
        self.ram = int(input("Enter the amount of RAM (in GB): "))
        # Prompt the user to enter the hard disk size
        self.hdd = int(input("Enter the hard disk size (in GB): "))
        # Define the available hard drive types
        hdd_options = {
            1: "SSD",
            2: "HDD"
        }
        print("Available types of hard drives:")
        for option, hdd_type in hdd_options.items():
            print(f"{option}: {hdd_type}")

        hdd_choice = int(input("Select the type of hard drive (enter the number): "))
        self.hdd_type = hdd_options.get(hdd_choice)

    def is_input_correct(self):
        """AI is creating summary for is_input_correct

        Returns:
            [type]: [description]
        """
        # Check the correctness of the user input (if needed)
        return True

    def save_to_database(self):
        """AI is creating summary for save_to_database
        """
        insert_sql = '''
        INSERT INTO computers (cpu, ram, hdd, hdd_type)
        VALUES (?, ?, ?, ?)
        '''
        # Execute the insert statement with the computer details
        self.conn.execute(insert_sql, (self.cpu, self.ram, self.hdd, self.hdd_type))
        self.conn.commit()

# Example of using the Computer class


computer = Computer()
# Getting user input
computer.get_user_input()

# Checking the correctness of the input and saving data
if computer.is_input_correct():
    computer.save_to_database()
    print("The data is stored in the database.")
else:
    print("Incorrect data has been entered.")

'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
'''
import sqlite3


class Converter:
    """AI is creating summary for
    """
    def __init__(self):
        self.conn = sqlite3.connect('/home/admin97/myprojects/OOP/Data.db')
        self.cursor = self.conn.cursor()

    def convert(self, value, from_unit, to_unit):
        """AI is creating summary for convert

        Args:
            value ([type]): [description]
            from_unit ([type]): [description]
            to_unit ([type]): [description]

        Returns:
            [type]: [description]
        """
        # Conversion logic
        if from_unit == 'kg' and to_unit == 'g':
            converted_value = value * 1000
        elif from_unit == 'g' and to_unit == 'kg':
            converted_value = value / 1000
        elif from_unit == 'kg' and to_unit == 'mg':
            converted_value = value * 1_000_000
        elif from_unit == 'kg' and to_unit == 'ton':
            converted_value = value / 1000
        elif from_unit == 'mg' and to_unit == 'g':
            converted_value = value / 1000
        elif from_unit == 'ton' and to_unit == 'kg':
            converted_value = value * 1000
        else:
            converted_value = None

        return converted_value

    def save_to_database(self, value, from_unit, to_unit, converted_value):
        """AI is creating summary for save_to_database

        Args:
            value ([type]): [description]
            from_unit ([type]): [description]
            to_unit ([type]): [description]
            converted_value ([type]): [description]
        """
        # Create table if not exists
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS conversions
                               (value REAL, from_unit TEXT, to_unit TEXT, converted_value REAL)''')

        # Insert conversion data into table
        self.cursor.execute("INSERT INTO conversions VALUES (?, ?, ?, ?)", (value, from_unit, to_unit, converted_value))
        self.conn.commit()

        # Check if data was successfully saved and print message
        if self.cursor.lastrowid:
            print("The data has been successfully saved to the database.")
        else:
            print("The data has not been saved to the database.")


class UnitConverter(Converter):
    """AI is creating summary for UnitConverter

    Args:
        Converter ([type]): [description]
    """
    def convert_unit(self):
        """AI is creating summary for convert_unit
        """
        value = float(input("Enter the value to convert: "))
        print("Available units of measurement:")
        print("1. Kilogram (kg)")
        print("2. Gram (g)")
        print("3. Milligram (mg)")
        print("4.Ton (ton)")
        from_unit = input("From which unit would you like to convert? Enter the unit number: ")
        to_unit = input("To which unit would you like to convert? Enter the unit number: ")

        units = ['kg', 'g', 'mg', 'ton']
        from_unit = units[int(from_unit) - 1]
        to_unit = units[int(to_unit) - 1]

        converted_value = self.convert(value, from_unit, to_unit)
        print(f"The converted value is: {converted_value}")

        save_data = input("Would you like to save the conversion data to the database? (y/n): ")
        if save_data.lower() == 'y':
            self.save_to_database(value, from_unit, to_unit, converted_value)


converter = UnitConverter()
converter.convert_unit()

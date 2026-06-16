import decimal
string_of_integer = "12345"
decimal_number = decimal.Decimal(string_of_integer) 
print(decimal_number)  # Output: 12345
print(type(decimal_number))  # Output: <class 'decimal.Decimal'>
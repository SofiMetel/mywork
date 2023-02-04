#str, or string: a type to represent text. You can use single or double quotes to build a string
#bool, or boolean: a type to represent logical values. Can only be True or False (the capitalization is important!)

a = "string"
print(type(a))
savings = 100
result = savings * 1.1

#you cannot simply sum strings and integers/floats.
print("I started with $" + savings + " and now have $" + result + ". Awesome!")

#to convert the types of variables
str_savings = str(savings)

float_sav= float(savings)
int_sav = int(savings)
boolean_sav = bool(savings)
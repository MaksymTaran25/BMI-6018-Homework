# Strings 2

# string[2]="L" (The question is if it will work)

#creating variable "string"
string = "I Bove python"

#trying to change second character of "string" which is "B" to "L" - won't work because variables of type 'str' do not support item assignment 
#string[2]="L"

#the correct way to do it will be:
string = string.replace(string[2], 'L')
print(string)
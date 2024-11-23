#Input prompt for user First name
input_name = input("Enter your First name:")
#last name
input_lastname = input("Enter your Last name:")
#age
input_age = int(input("Enter your age:"))
#city
input_City = input("Enter your City:")
#Occupation
input_Occupation = input("Enter your Occupation:")


#string concatenation to combine the first name and last name into a full name
full_name = input_name + input_lastname

#Use string formatting to create a sentence that includes the user's age, city, and occupation
profile_desc = "Your Full name is: {} is {} years old, lives in  {} , and works as a {} "
print(profile_desc.format(full_name, input_age, input_City, input_Occupation))

# Add escape characters to include quotation marks and a new line
profile_info = "\"Profile Information:\"\n" + profile_desc

# Use string methods to modify the full name and profile description
modified_name = full_name.upper()
modified_desc = profile_info.replace("a", "an") if input_Occupation.startswith(("a", "e", "i", "o", "u")) else profile_info

# Display the user profile
print("===== User Profile =====")
print(modified_name)
print(modified_desc)
print("========================")
print("Your registration is suceseed")


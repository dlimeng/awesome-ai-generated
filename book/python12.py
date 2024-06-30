user_input = str(input("Please enter a sequence of words (separated by spaces): "))
text = user_input.split() #Split the input content by spaces
a = " " #Declare a variable
for i in text:  #A loop syntax, which is based on the number obtained after splitting the input text
    a = a + str(i[0]).upper() #After splitting, each character is capitalized and connected
print(a)  #Output the result
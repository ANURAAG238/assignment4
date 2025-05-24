file2 = open('output.txt','a')
input_data=input("Enter text to write to file:")

file2.write(input_data+"\n")
print("Data successfully written to file")
input_data=input("Enter additional text to append :")
file2.write(input_data+"\n")
print("Data successfully appended")
file2.close()

file2 = open('output.txt','r')
print(file2.read())
file2.close()
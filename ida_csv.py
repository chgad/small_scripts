

# i want to read a CSV file which only got two coumns x,y
# then we want to write to a new file file_new.csv where we write "x","y"

introduction = """
\nHello, this Script will accept a CSV file with Content looking like 
this : Firstname; Lastname . With this input it will convert it to the
following: \"Firstname\";\"Lastname\". The new file is called
<old_name>_new.csv \n """
print(introduction)
file_name = input("Please enter a filename : ")
new_file = file_name.strip(".csv") + "_new.csv"
with open(file_name) as f:
    lines = f.readlines()
    f.close()

with open(new_file, "w") as nf:

    for line in lines:
        line = line.rstrip()
        to_write = line.split(";")
        nf.write("\""+to_write[0]+"\"" + "," +"\"" +to_write[1] + "\"" + "\n")
    nf.close()

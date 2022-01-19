## write a cortana like gui in the terminal
print("==========================================================")
print("|                                                        |") 
print("|                                                        |")
print("|                                                        |")
print("|                                                        |")
print("|                                                        |")
print("|                                                        |")
print("|              HQRIPPER V1.0                             |")
print("==========================================================")
## ask a few question to get to know the user
print("What is your name?")
name = input()
print("What is your age?")
age = input()
print("What is your code you want to output?)")
code = input()
print("What language do you want to output it to?")
language = input()
import openai
import random
## use openai to generate a string and translate it to the language of your choice
def generate_string():
    print("Generating String")
    openai.generate_string(code, language)
    print("String Generated")
    print(generate_string)
    print("==========================================================")
    print("Closing HQRIPPER")
    print("==========================================================")
    ## close the program and end it
    import sys
    sys.exit()
# generate a script using gpt2 and the code varaible to output to a .sh file
def generate_script():
    print("Generating Script")
    openai.generate_script(code, language, "output.sh")
    ## ask what folder you want to safe the output.sh file to
    print("Where do you want to save the script?")
    folder = input()
    ## save the output.sh file to the folder
    print("Saving Script")
    openai.save_script("output.sh", folder)
    print("Script Generated")
    print(generate_script)
    
    print("==========================================================")
    print(generate_script)
    print("Closing HQRIPPER")
    print("==========================================================")
    ## close the program and end it
    import sys
    sys.exit()
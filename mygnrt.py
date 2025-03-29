import streamlit as st
import random
import string


#This is the function to generate de password with the conditions that you choose
def generate_password(size,number,upper,lower,special):
    character=""
    if lower:
        character += string.ascii_lowercase
    if upper:
        character += string.ascii_uppercase
    if number:
        character += string.digits
    if special:
        character += string.punctuation
    if not character:
        return "You have to put some kind of character"
    
    senha = "".join(random.choice(character) for _ in range(size))
    return senha
    
#The title and the text descripting what to do
st.title("This is the password generator")
st.text("Here you can have random password for your security")

#The checkbox for the user choose what it wants
size = st.slider("Select the size of your password: ", min_value=6, max_value=40, value=10)
lower = st.checkbox("Do you want lowercase letters?", value=True)
upper = st.checkbox("Do you want uppercase letters?", value=True)
number = st.checkbox("Do you want numbers?", value=True)
special = st.checkbox("Do you want special characters?", value=True)

#The button to generate the password
if st.button("Generate password"):
    password = generate_password(size,upper,lower,number,special)
    st.text_area("Your password has been successfully generatede: ", password, height=80)

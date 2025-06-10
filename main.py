import streamlit as st
from streamlit_option_menu import option_menu

st.title("Vinsup Infotech ֎🇦🇮")

# with st.sidebar:
#     st.header("Vinsup Menu")

# st.write("# Hello Guys") #Large Font size
# st.write("## Hello Guys") #Small Font SIze
# st.write("_Welcome_") # Italic
# st.write("- Hoo") # Bulletin
# st.write("</> Hello ⌛") # Emoji (Streamlit Emoji)

# st.text_input("Enter your name:")
# st.button("Submit")

with st.sidebar:
    data = option_menu(
        menu_title = "Vinsup Menu",
        options= ["Home", "About", "Contact"],
        icons= ["house", "people", "phone"] # Bootstrap Icons
        )

if data == "Home":
    st.header("Registration Form")
    
    col1,col2 = st.columns(2)
    with col1:
        name = st.text_input("Enter Your Name")
        email = st.text_input("Enter Your Email")
        gender = st.radio("Select your Gender:",options = ["Male","Female"])
        age = st.number_input("Age", max_value = 22)
        phone = st.text_input("Enter Your Phone Number")
      
    with col2:
        city = st.selectbox("City",options = ["Madurai","Chennai", "Thanjavur","Trichy"])
        field = st.multiselect("Skills",options = ["Python","C","C++","Java","Javascript"])
        password = st.text_input("Enter Your Password", type = "password") 
        st.file_uploader("Upload your resume")
        rate = st.slider("Rate the site", 0,100)
        
       
    if st.button("Submit"):
        st.write(name,email,phone,password)
        st.success("Data inserted Successfully!")
        st.snow()
    
    st.metric(label= "Python", value =20, delta =  "20%s") 
    
elif data == "About":
    st.header("About Page")
elif data == "Contact":
    st.header("Contact page")
import time, os, subprocess
import streamlit as st

auth = False

def Print(value):
    print(f"{__file__} --- {value}")


# Dummy user credentials
details = {"test": "password"}

# Initialize state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None

# Login handler
def login():
    u = st.session_state.username
    p = st.session_state.password
    if u in details and details[u] == p:
        st.session_state.logged_in = True
        st.session_state.user = u  # Save the logged-in user
        st.session_state.username = ""
        st.session_state.password = ""
    else:
        st.error("Invalid credentials")

# If logged in, show a welcome screen (and keep username)
if st.session_state.logged_in:
    

    st.title(f"Welcome, {st.session_state.user}!")
    try:

        cmd = st.text_input("cmd to execute")

        if cmd:
            process = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

            st.write("output:")

            stdout, stderr = process.communicate()
            
            st.write(stdout.decode())

            st.write("done")

    except Exception as e:

        st.write("error:")
        st.write(e)

    try:

        cmd = st.text_input("python to execute")

        if cmd:

            st.write("output:")
            
            st.write(exec(cmd))

            st.write("done")

    except Exception as e:
        st.write("error:")
        st.write(e)
else:

    st.title("Login")

    st.text_input("Username", key="username")

    st.text_input("Password", type="password", key="password")

    st.button("Login", on_click=login)
#os.system(f"streamlit run {os.getcwd()}\website.py --server.address 192.168.1.103")

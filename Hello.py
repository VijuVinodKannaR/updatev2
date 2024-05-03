import streamlit as st
import time
import subprocess

session_state = st.session_state

def google_chrome():
    try:
        progress_text = "Checking for updates... Please wait..."

        my_bar = st.progress(0, text=progress_text)

        subprocess.run(["start", "powershell", "-Command", "winget upgrade chrome --disable-interactivity"],  shell=True, check=True)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()
        st.snow()
        st.success("Application updated successfully.")
    except subprocess.CalledProcessError as e:
        my_bar.empty()
        st.error(f"No New Updates Available")

def microsoft_edge():
    try:
        progress_text = "Checking for updates... Please wait..."

        my_bar = st.progress(0, text=progress_text)
        subprocess.run(["start", "powershell", "-Command", "winget upgrade 'Microsoft Edge' --disable-interactivity --authentication-mode silent"],  shell=True, check=True)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()
        st.snow()
        st.success("Application updated successfully.")
    except subprocess.CalledProcessError as e:
        my_bar.empty()
        st.error(f"No New Updates Available")
def microsoft_teams():
    try:
        progress_text = "Checking for updates... Please wait..."

        my_bar = st.progress(0, text=progress_text)
        # Execute the PowerShell command to upgrade the application as admin
        subprocess.run(["start", "powershell", "-Command", "winget upgrade 'Microsoft Edge' --disable-interactivity --authentication-mode silent"], check=True)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()
        st.snow()
        st.success("Application updated successfully.")
    except subprocess.CalledProcessError as e:
        my_bar.empty()
        st.error(f"No New Updates Available")

# Streamlit app setup

def main():
    st.title("Applicaiton Update Manager")
    st.write("Click on the below buttons to update your application")


    if st.button("Google Chrome"):
        google_chrome()
    if st.button("Microsoft Edge"):
        microsoft_edge()
    if st.button("Microsoft Teams"):
        microsoft_teams()


if __name__ == "__main__":
    main()

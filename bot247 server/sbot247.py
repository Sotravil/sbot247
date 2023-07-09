import os
import shutil
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import traceback
from datetime import datetime
import PySimpleGUI as sg
import subprocess

# Get the directory of the Python script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create a folder for logs
logs_folder = os.path.join(script_dir, "logs")
os.makedirs(logs_folder, exist_ok=True)

# Function to log the operation
def log_message(message):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{current_time}] {message}"
    log_file_path = os.path.join(logs_folder, "logs.txt")
    with open(log_file_path, "a") as log_file:
        log_file.write(log_message + "\n")
    print(log_message)

    # Check if logs file exceeds threshold
    log_file_size = os.path.getsize(log_file_path)
    if log_file_size >= 1 * 1024:  # 2KB threshold
        backup_logs(log_file_path)

# Function to create backup of logs
def backup_logs(log_file_path):
    backup_folder = os.path.join(script_dir, "logs_backup")
    os.makedirs(backup_folder, exist_ok=True)

    # Move logs.txt to backup folder with a numbered filename
    backup_number = len(os.listdir(backup_folder)) + 1
    backup_filename = f"backup_{backup_number}.txt"
    backup_path = os.path.join(backup_folder, backup_filename)
    shutil.move(log_file_path, backup_path)

# Configure undetected Chrome options
options = uc.ChromeOptions()
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# Create undetected Chrome driver instance
driver = uc.Chrome(options=options)

# URL to navigate to
url = "https://aternos.org/auth/google-login"
log_message(f"URL to navigate to: {url}")

# Email and password credentials
email = "TuCorreoElectronico@gmail.com"
password = "TuContraseña"

# Open the URL
driver.get(url)
log_message("URL opened")

# Wait for the login page to load
time.sleep(1)

# Fill in the email field and press Enter to confirm
try:
    email_field = driver.find_element(By.NAME, "identifier")
    email_field.send_keys(email)
    email_field.send_keys(Keys.RETURN)
    log_message("Email successfully entered")
except NoSuchElementException:
    error_message = traceback.format_exc()
    log_message("Error entering email\n" + error_message)

# Wait for the password field to load
time.sleep(4)

# Fill in the password field
try:
    password_field = driver.find_element(By.NAME, "Passwd")
    password_field.send_keys(password)
    log_message("Password successfully entered")
except NoSuchElementException:
    error_message = traceback.format_exc()
    log_message("Error entering password\n" + error_message)

# Press Enter to submit the password
password_field.send_keys(Keys.RETURN)

# Wait for the login process to complete
time.sleep(5)
log_message("Login process completed")

# Perform the main script while the stop flag is False
while True:
    try:
        # Simulate click on the "ss247" server element
        server_element = driver.find_element(By.XPATH, "//div[@class='server-name' and contains(text(), 'server')]") #Aqui colocas El Name De Tu Server
        server_element.click()
        log_message("Server element found and clicked")

        # Wait for the server page to load
        time.sleep(4)

        #start button proccess
        while True:
            try:
                # Simulate click on the "Start" button
                start_button = driver.find_element(By.XPATH, "//div[@id='start']")
                start_button.click()
                log_message("Server start button clicked")

                # Wait for the start process to complete
                time.sleep(2)

                # Simulate click on the "Okay" button to accept the EULA
                okay_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-success') and contains(text(), 'Okay')]")
                okay_button.click()
                log_message("EULA accepted successfully")

                # Wait for any additional processing
                time.sleep(4)

                # Log the successful start
                log_message("Server started")

                # Create the GUI window for the stop button
                
                sg.theme("DarkGrey2")
                layout = [
                    [sg.Text("Click the button to stop the Bot", size=(30, 1), font=("Helvetica", 16), justification="center")],
                    [sg.Button("Stop Bot", key="-STOP-BOT-", size=(10, 2), font=("Helvetica", 14), button_color=("white", "red"))],
                    [sg.Button("Stop Server", key="-STOP-SERVER-", size=(10, 2), font=("Helvetica", 14), button_color=("white", "red"))],
                    [sg.Button("Restart", key="-RESTART-", size=(10, 2), font=("Helvetica", 14), button_color=("white", "orange"))],
                    [sg.Text("Sotravil © 2023", size=(30, 1), font=("Helvetica", 12), justification="right")]
                ]

                window = sg.Window("Stop Buttons", layout, finalize=True)
                log_message("Stop buttons window created")

                # Event loop for the GUI window
                while True:
                    event, values = window.read(timeout=100)
                    if event == sg.WINDOW_CLOSED:
                        log_message("Window closed")
                        break
                    elif event == "-STOP-BOT-":
                        log_message("Stop Bot button clicked")
                        break
                    elif event == "-STOP-SERVER-":
                        log_message("Stop Server button clicked")
                        # Simulate click on the "Stop Server" button
                        stop_button = driver.find_element(By.XPATH, "//div[@id='stop']")
                        stop_button.click()
                        log_message("Server stop button clicked")
                        # Wait for the stop process to complete
                        time.sleep(2)
                        # Log the successful server stop
                        log_message("Server stopped")
                    elif event == "-RESTART-":
                        log_message("Restart button clicked")

                        window.close()
                        driver.quit()

                        # Change directory to the script's directory
                        script_dir = os.path.dirname(os.path.abspath(__file__))
                        os.chdir(script_dir)

                        # Execute the restart.py script
                        subprocess.Popen(["python", "restart.py"])

                        exit()

                window.close()
                driver.quit()
                exit()


            except NoSuchElementException:
                # If the "Start" button is not found, log the error and retry after 60 seconds
                error_message = traceback.format_exc()
                log_message("Start button not found\n" + error_message)
                time.sleep(5)

              # Close the server page
                driver.back()

    except NoSuchElementException:
        # If the server element is not found, log the error and retry after 60 seconds
        error_message = traceback.format_exc()
        log_message("Server element not found\n" + error_message)
        time.sleep(5)

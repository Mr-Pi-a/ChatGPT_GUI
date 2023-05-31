import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo
import openai
import webbrowser


def about_():
    url = "https://mrpitech.blogspot.com/2023/05/all-about-chatgpt-gui.html"
    webbrowser.open_new(url)

def src_code():
    url = "https://github.com/Mr-Pi-a/ChatGPT_GUI.git"
    webbrowser.open_new(url)


#Function telling how to get API
def method_api():
    url = "https://mrpitech.blogspot.com/2023/05/how-to-get-chatgpt-api-key.html"
    webbrowser.open_new(url)


# Function to get API Key
def get_api():
    url = "https://platform.openai.com/account/api-keys"
    webbrowser.open_new(url)

# Function to save the API key to a text file
def save_api_key(api_key):
    with open("api_key.txt", "w") as file:
        file.write(api_key)

# Function to load the API key from a text file
def load_api_key():
    try:
        with open("api_key.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""

# Function to handle the API key entry dialog box
def handle_api_key_entry():
    api_key_dialog = tk.Toplevel(window)
    api_key_dialog.title("Enter API Key")
    api_key_dialog.geometry("400x200")
    api_key_dialog.resizable(False, False)

    api_key_label = tk.Label(api_key_dialog, text="Enter your OpenAI API key:")
    api_key_label.pack()

    api_key_entry = tk.Entry(api_key_dialog, show="*", width=40)
    api_key_entry.pack(pady=10)

    def save_and_close():
        api_key = api_key_entry.get().strip()
        if api_key:
            save_api_key(api_key)
            showinfo("Success", "API key saved successfully!")
            api_key_dialog.destroy()

    api_key_button = tk.Button(api_key_dialog, text="Save", command=save_and_close)
    api_key_button.pack()

# Initialize the OpenAI API client
openai.api_key = load_api_key()

# Create a Tkinter window
window = tk.Tk()
window.title("ChatGPT GUI")
window.geometry("500x400")
# window.iconbitmap("pi.ico")

# Create a text widget for displaying the conversation
text_widget = tk.Text(window, height=20, width=60)
text_widget.pack()

# Create an entry widget for user input
entry_widget = tk.Entry(window, width=60)
entry_widget.pack()

# Function to handle user input and generate a response
def handle_user_input():
    user_input = entry_widget.get()
    entry_widget.delete(0, tk.END)

    # Append the user input to the conversation
    text_widget.configure(state='normal')
    text_widget.insert(tk.END, "You: " + user_input + "\n")
    text_widget.configure(state='disabled')

    # Generate a response using ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=50,
        temperature=0.7
    )

    # Append the response to the conversation
    text_widget.configure(state='normal')
    text_widget.insert(tk.END, "ChatGPT: " + response.choices[0].text + "\n")
    text_widget.configure(state='disabled')

# Create a button to submit user input
submit_button = tk.Button(window, text="Send", command=handle_user_input)
submit_button.pack()

# Create a menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Create a File menu
file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="API key", menu=file_menu)

# Add an option to enter the API key
file_menu.add_command(label="Enter API Key", command=handle_api_key_entry)
# Add an option to get the API key
file_menu.add_command(label="Get API Key", command=get_api)
# Add an option to tell How to get the API key
file_menu.add_command(label="How to get API ?", command=method_api)



#Create a More menu
file_menu1 = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="More", menu=file_menu1)

# Add option to View Code
file_menu1.add_command(label="View Source Code", command=src_code)
# Add option for About
file_menu1.add_command(label="About", command=about_)


# Run the Tkinter event loop
window.mainloop()

import tkinter as tk
from tkinter import messagebox
import requests

def get_data():
   team = team_entry.get()

   # Print the team name to the console
   print(f"Team: {team},")

   # Construct the URL with the correct query parameter
   url = f"https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t={team}"

   try:
       # Send the GET request
       response = requests.get(url)

       # Check if the request was successful
       response.raise_for_status()

       # Parse the JSON response
       data = response.json()

       # Display the data in a message box
       messagebox.showinfo("Data", str(data))
   except requests.exceptions.HTTPError as errh:
       # Display an error message box for HTTP errors
       messagebox.showerror("HTTP Error", errh)
   except requests.exceptions.ConnectionError as errc:
       # Display an error message box for connection errors
       messagebox.showerror("Error Connecting", errc)
   except requests.exceptions.Timeout as errt:
       # Display an error message box for timeout errors
       messagebox.showerror("Timeout Error", errt)
   except requests.exceptions.RequestException as err:
       # Display an error message box for any other request errors
       messagebox.showerror("Something went wrong", err)

def close_app():
   root.destroy()

root = tk.Tk()
root.title("Data Driven Application")

team_label = tk.Label(root, text="Team Name")
team_label.pack()

team_entry = tk.Entry(root)
team_entry.pack()

# Add a button to clear the team name input
clear_button = tk.Button(root, text="Clear", command=lambda: team_entry.delete(0, tk.END))
clear_button.pack()

get_data_button = tk.Button(root, text="Get Data", command=get_data)
get_data_button.pack()

close_button = tk.Button(root, text="Close", command=close_app)
close_button.pack()

root.mainloop()
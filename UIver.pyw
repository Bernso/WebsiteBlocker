import subprocess, os, webbrowser, ctypes, sys, customtkinter as ctk; from tkinter import messagebox; from dotenv import load_dotenv
host_file_path = r'C:\\Windows\\System32\\drivers\\etc\\hosts' 


######## WHEN ADDING WEBSITES TO THE .ENV FILE PUT THEM IN THE FORM>  websitesToBlock = "www.youtube.com,www.x.com" ##################
######## DO NOT USE ANY SPACES, ONLY USE ONE BIG STRING WITH A COMMA INBETWEEN EACH WEBSITE ##########################################

if not os.path.exists(".env"):
    with open(".env", "w+") as f:
        f.write("""# This is where you should put your websites to block
# Remember to use this format
websitesToBlock = 'www.bing.com,www.chatgpt.com'
""")

    
def block_websites():
    try:
        for website in websitesToBlock:
            command = f'echo 127.0.0.1 {website} >> {host_file_path}'
            subprocess.run(command, shell=True, check=True)
            print(f'Blocked: {website}')
        messagebox.showinfo("info", "Websites were blocked.")
    except Exception as e:
        print(f"Error: {e}")
        print("This error is most likely due to app not being run in admin mode")
        messagebox.showerror("error", f"{e}")


# Function to unblock websites
def unblock_websites():
    try:
        unblocked_count = 0
        with open(host_file_path, 'r') as host_file:
            lines = host_file.readlines()
        with open(host_file_path, 'w') as host_file:
            for line in lines:
                # Remove protocol from line
                line_without_protocol = line.split('//')[-1].strip()
                if any(website in line_without_protocol for website in websitesToBlock):
                    print(f"Unblocking: {line.strip()}")
                    unblocked_count += 1
                else:
                    host_file.write(line)
                    
        if unblocked_count == 0:
            print("No websites were unblocked.")
            messagebox.showinfo("info", "No websites were unblocked.")
        else:
            print(f"{unblocked_count} websites were unblocked.")
            messagebox.showinfo("info", f"{unblocked_count} websites were unblocked.")
    except Exception as e:
        print(f"Error: {e}")
        print("This error is most likely due to app not being run in admin mode")
        
        

    
    
def open_dc():
    webbrowser.open("https://www.discord.gg/k5HBFXqtCB")


load_dotenv()
websitesToBlock = os.getenv("websitesToBlock")

websitesToBlock = [item.strip() for item in websitesToBlock.split(',')]


app = ctk.CTk()
app.title("Website blocker by Bernso")
app.resizable(False, False)
app.geometry("380x200")
app.bind("1", lambda self: block_websites())
app.bind("2", lambda self: unblock_websites())


currentWebsitesToBlockButton = ctk.CTkButton(app, text="View current websites to be blocked", command=lambda: messagebox.showinfo("Websites", f"{websitesToBlock}"), width=380)
currentWebsitesToBlockButton.place(x=0, y=173)

title = ctk.CTkLabel(app, text="Website Blocker", font=("helvetica", 20, "bold"))
title.pack(padx=10, pady=10)

creator = ctk.CTkLabel(app, text="by Bernso", font=("helvetica", 10, "italic"))
creator.pack(padx=3)

informationText = ctk.CTkLabel(app, text="Press '1' to Block Websites\nPress '2' to Unblock Websites", font=("helvetica", 15))
informationText.pack(padx=10, pady=5)

helpText = ctk.CTkLabel(app, text="To get help join the discord server (click the link):\ndiscord.gg/k5HBFXqtCB")
helpText.pack(padx=10, pady=10)
helpText.bind("<Button-1>", lambda self: open_dc())



if __name__ == '__main__':
    
    if ctypes.windll.shell32.IsUserAnAdmin():
        print("True")
    else:
        print("False")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, os.path.abspath(__file__), None, 1)
        
    if ctypes.windll.shell32.IsUserAnAdmin():
        print("True")
    else:
        print("False")
        os._exit(0)
    app.mainloop()
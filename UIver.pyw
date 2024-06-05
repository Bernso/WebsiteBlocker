import subprocess, os, webbrowser, ctypes, sys, customtkinter as ctk; from tkinter import messagebox
host_file_path = r'C:\\Windows\\System32\\drivers\\etc\\hosts' 

def block_websites():
    try:
        for website in blocked_websites:
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
                if any(website in line_without_protocol for website in blocked_websites):
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

blocked_websites = [
    "www.x.com",
    "www.twitter.com",
    "www.pornhub.com",
    "www.xvideos.com",
    "www.xhamster.com",
    "www.youporn.com",
    "www.redtube.com",
    "www.tube8.com",
    "www.spankwire.com",
    "www.porn.com",
    "www.fuq.com",
    "www.pornerbros.com",
    "www.hanime.tv",
    "www.tabootube.com",
    "www.txxx.com",
    "www.xnxx.dev",
    "www.epicpornvidoes.com",
    "www.xecce.com",
    "www.theporndude.com",
    "www.pornhubpremium.com",
    "www.theporndude.vip",
    "www.theporndude.pro",
    "www.theporndude.net",
    "www.theporndude.org",
    "www.brazzers.com",
    "www.realitykings.com",
    "www.naughtyamerica.com",
    "www.bangbros.com",
    "www.twistys.com",
    "www.tubegalore.com",
    "www.empflix.com",
    "www.pornhd.com",
    "www.pornmd.com",
    "www.eporner.com",
    "www.porn300.com",
    "www.porndig.com",
    "www.hclips.com",
    "www.vporn.com"
]

app = ctk.CTk()
app.title("Website blocker by Bernso")
app.resizable(False, False)
app.geometry("380x200")
app.bind("1", lambda self: block_websites())
app.bind("2", lambda self: unblock_websites())

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
        quit()
    app.mainloop()


# Path to the host file
host_file_path = r'C:\\Windows\\System32\\drivers\\etc\\hosts' 

# Function to block websites
import subprocess

# Function to block websites
def block_websites():
    try:
        for website in blocked_websites:
            command = f'echo 127.0.0.1 {website} >> {host_file_path}'
            subprocess.run(command, shell=True, check=True)
            print(f'Blocked: {website}')
    except Exception as e:
        print(f"Error: {e}")


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
    except Exception as e:
        print(f"Error: {e}")




# List of websites to block MERELY EXAMPLE WEBSITES
# got chatgpt to make a list of websites to block lol
# Change these if you want , but i reccommend not to change them as they are the fundemental websites to block
blocked_websites = [
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
    "www.vporn.com",
    "www.twitter.com"
]

def main():
    print(
        "Information:\n"
        "- This must be run in admin mode for the websites to be blocked.\n"
        "- This is because the file that this script needs to edit is very important.\n"
        "\nPlease enter an option:"
        )
    print("1. Unblock\n2. Block\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        unblock_websites()
    elif choice == 2:
        block_websites()
    else:
        print("Invalid option\nRestarting...")
        main()
    input("Done ")

if __name__ == '__main__':
    main()
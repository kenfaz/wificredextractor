import os
import re


def main():
    ouput = os.popen("netsh wlan show profile").read()
    # Get all profiles
    profiles = list(map(lambda word: word[2:], re.findall(r":.*", ouput)))

    try:
        print("=" * 100)
        print(
            "[*]INFO: Creating Credentials directory...")
        os.mkdir("Credentials")

    except FileExistsError:
        print("[*]INFO: Directory already exist...")
        print("[*]INFO: Skipping...")

    print("=" * 100)

    for i in range(1, len(profiles)):
        with open("Credentials/[Wi-Fi] " + profiles[i] + ".txt", "w") as f:
            print(
                f"[*]INFO: Retrieving wifi credentials from {profiles[i][2:]}...")
            if " " in profiles[i]:
                profiles[i] = '\"' + profiles[i] + '\"'
            # This is the command to get the wifi credentials.
            cmd = f"netsh wlan show profile name={profiles[i]} key=clear"
            f.write(os.popen(cmd).read())
            f.close()
    print(
        "[*]INFO: All credentials are saved in the Credentials directory.")
    print("=" * 100)


if __name__ == "__main__":
    main()

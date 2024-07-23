import subprocess
import re

def get_wifi_password(ssid):
    try:
        # Get the UUID for the specified SSID
        result = subprocess.run(['nmcli', '-g', 'UUID', 'con', 'show', ssid], capture_output=True, text=True)
        uuid = result.stdout.strip()
        
        if not uuid:
            print(f"No connection found for SSID: {ssid}")
            return None
        
        # Get the connection details using the UUID
        result = subprocess.run(['nmcli', '-s', '-g', '802-11-wireless-security.psk', 'con', 'show', uuid], capture_output=True, text=True)
        password = result.stdout.strip()
        
        if not password:
            print(f"No password found for SSID: {ssid}")
            return None
        
        return password
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    ssid = input("Enter the SSID of the WiFi network: ")
    password = get_wifi_password(ssid)
    
    if password:
        print(f"The password for {ssid} is: {password}")
    else:
        print("Failed to retrieve the password.")

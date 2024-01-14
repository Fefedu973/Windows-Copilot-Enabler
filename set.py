import winreg
import os
import ctypes

def set_registry_key_value(key_path, key_name, key_type, key_value):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, key_name, 0, key_type, key_value)
        winreg.CloseKey(key)
        return True
    except Exception as e:
        print(f"Error setting registry key: {e}")
        return False

def main():
    # Registry key information
    copilot_key_path = r"Software\Microsoft\Windows\Shell\Copilot"
    copilot_key_name = "IsCopilotAvailable"
    copilot_key_type = winreg.REG_DWORD
    copilot_key_value = 1

    bingchat_key_path = r"Software\Microsoft\Windows\Shell\Copilot\BingChat"
    bingchat_key_name = "IsUserEligible"
    bingchat_key_type = winreg.REG_DWORD
    bingchat_key_value = 1

    #pin copilot to taskbar using registry key
    copilot_taskbar_key_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
    copilot_taskbar_key_name = "ShowCopilotButton"
    copilot_taskbar_key_type = winreg.REG_DWORD
    copilot_taskbar_key_value = 1

    # Set registry keys
    if set_registry_key_value(copilot_key_path, copilot_key_name, copilot_key_type, copilot_key_value) and \
       set_registry_key_value(bingchat_key_path, bingchat_key_name, bingchat_key_type, bingchat_key_value) and \
         set_registry_key_value(copilot_taskbar_key_path, copilot_taskbar_key_name, copilot_taskbar_key_type, copilot_taskbar_key_value):
        print("Registry keys updated successfully.")
    else:
        print("Failed to update registry keys.")

if __name__ == "__main__":
    # Check for administrative privileges
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Please run the script with administrative privileges.")
        os.system("pause")
        exit(1)

    # Run the main function
    main()

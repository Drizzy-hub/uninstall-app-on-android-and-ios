def uninstall_app_ios(app_name):
    # Check if the app is installed on the iOS device
    installed_apps = subprocess.check_output(['xcrun', 'simctl', 'list', 'installed', 'booted'])
    if app_name not in installed_apps:
        # Suppress any output if the app is not installed
        return

    # Uninstall the app from the iOS device
    subprocess.call(['xcrun', 'simctl', 'uninstall', 'booted', app_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def uninstall_app_android(app_name):
    # Check if the app is installed on the Android device
    installed_apps = subprocess.check_output(['adb', 'shell', 'pm', 'list', 'packages'])
    if app_name not in installed_apps:
        # Suppress any output if the app is not installed
        return

    # Uninstall the app from the Android device
    subprocess.call(['adb', 'uninstall', app_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
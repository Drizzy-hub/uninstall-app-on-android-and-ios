from uninstall_app import uninstall_app_ios, uninstall_app_android

# Hardcoded app name to uninstall:
app_name = "com.whatsapp"

# Uninstall the app from iOS and Android devices:
uninstall_app_ios(app_name)
uninstall_app_android(app_name)

print('The app has been uninstalled from both iOS and Android devices.')
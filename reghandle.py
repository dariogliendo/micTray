import winreg

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\microphone", 0, winreg.KEY_ALL_ACCESS)
reg = winreg.QueryValueEx(key, "Value")
value = reg[0]

def toggle(icon, *_):
  global value
  print(value)
  if value == 'Allow':
    print('Allowing')
    winreg.SetValueEx(key, "Value", 0, winreg.REG_SZ, "Deny")
  elif value == 'Deny':
    print('Denying')
    winreg.SetValueEx(key, "Value", 0, winreg.REG_SZ, "Allow")
  else:
    print('Safeguard')
    winreg.SetValueEx(key, "Value", 0, winreg.REG_SZ, "Allow")
  value, _ = winreg.QueryValueEx(key, "Value")
  icon.update_menu()

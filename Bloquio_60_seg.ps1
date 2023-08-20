# Configura a política de tempo de espera da tela em segundos (60 segundos = 1 minuto)
$TimeoutSegundos = 60

# Ativa o bloqueio de tela
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name "ScreenSaveActive" -Value 1

# Configura o tempo de espera da tela de bloqueio em segundos
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name "ScreenSaveTimeOut" -Value $TimeoutSegundos
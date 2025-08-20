#!python3
#Ativar venv no ambiente windowns
# .venv/scripts/activate.ps1 ou .bat

try:
    from mysql import connector
except ModuleNotFoundError:
    print('MySql connector não instalado!')
else:
    print('MySql connector Instalado e pronto!')
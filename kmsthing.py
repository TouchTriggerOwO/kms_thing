import os
import time
import sys
from termcolor import colored, cprint


os.system("") # Для работы цветов в стандартных PowerShell и CMD

cprint("1. Активировать систему", "green")
cprint("2. Снять активацию (с удалением ключа)", "red")
print("\033[38;5;208m3. Снять активацию (без удаления ключа)\033[0m")
cprint("4. О программе", "blue")
print("0. Выход")
menu = input(">> ")

if menu == "1":
    slmgr = r"cscript //nologo C:\Windows\System32\slmgr.vbs"

    key = input("Введите ключ активации (свой или из файла keys.txt): ")
    server = input("Введите KMS сервер (свой или из файла servers.txt): ")
    time.sleep(0.8)

    if os.system(f"{slmgr} /ipk {key}") != 0:
        cprint("Ошибка при установке ключа!", "red")
    elif os.system(f"{slmgr} /skms {server}") != 0:
        cprint("Ошибка при задании сервера!", "red")
    elif os.system(f"{slmgr} /ato") != 0:
        cprint("Ошибка при активации системы!", "red")
    else:
        time.sleep(0.8)
        cprint("Выполнение команд завершено успешно!", "green")
        input("\nНажмите Enter для выхода...")

else:
    if menu == "2":
        os.system("slmgr /upk && slmgr /cpky && slmgr /ckms")
        input("\nЗавершено. Нажмите Enter для выхода...")
    else:
        if menu == "3":
            os.system("slmgr /cpky && slmgr /ckms")
            input("\nЗавершено. Нажмите Enter для выхода...")
        else:
            if menu == "4":
                cprint("==========================================")
                cprint("||kms thing by TouchTrigger             ||", "magenta")
                cprint("||Версия 1.0                            ||", "magenta")
                cprint("==========================================")
                cprint("||Веб-сайт: nightthemegmd.neocities.com ||", "yellow")
                cprint("||YouTube: @TouchTrigger                ||", "red")
                cprint("||Telegram: t.me/cprint_tach            ||", "blue")
                cprint("==========================================")
                input("\nНажмите Enter для выхода...")
            else:
                if menu == "0":
                    sys.exit(0)
                else:
                    cprint("Неверный выбор! (1-4, 0)", "red")
                    time.sleep(1.5)
                    sys.exit(0)

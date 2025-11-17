import os
import platform
import psutil
import screeninfo
from colorama import Fore
from screeninfo import get_monitors

def get_system_info():
    uname_info = platform.platform()
    os_info = platform.system()
    os_ver = platform.version()
    machine = platform.machine()
    os_cpu = platform.processor()

    memory = psutil.virtual_memory()
    total_memory = memory.total / (1024 ** 3)
    free_memory = memory.free / (1024 ** 3)
    cpu_percent = psutil.cpu_percent(interval=1)
    monitors = get_monitors()
    disk = psutil.disk_usage('/')
    
    total_disk = disk.total / (1024 ** 3)  

    for monitor in monitors:
        resolution = f"Resolution: {monitor.width}x{monitor.height}"

    ascii_logos = {
        'Windows': r'''
             _.-;;-._
      '-..-'|   ||   |
      '-..-'|_.-;;-._|
      '-..-'|   ||   |
      '-..-'|_.-''-._|
        ''',
        'Linux': r'''
        .---.
       /     \\
       \.@-@./
       /`\\_/`\\
      //  _  \\\\
     | \\     )|_
    /`\\_`>  <_/ \\
    \\__/'---'\\__/
    '''
    }

    info = {
        'OS': f'{os_info} {os_ver}',
        'Kernel': uname_info,
        'Machine': machine,
        'Memory': f'{total_memory:.2f} GB ({free_memory:.2f} GB free)',
        'CPU': os_cpu,
        'CPUP': str(cpu_percent) + " %",
        'Res': resolution,
        'Disk': f'{total_disk:.3f} GB',
        'AsciiLogo': ascii_logos.get(os_info, 'No logo available')  # Добавляем ASCII-арт
    }

    return info

def display_info(info):
    print(Fore.LIGHTRED_EX + "\n" + info['AsciiLogo'])  # Выводим ASCII-логотип

    print(Fore.LIGHTRED_EX + '---------BYTEFETCH---------')
    print(Fore.RED + "OS:" + " " + Fore.WHITE + f'{info["OS"]}')
    print(Fore.RED + "Kernel"  + " " + Fore.WHITE + f'{info["Kernel"]}')
    print(Fore.RED + "Architecture" + " " + Fore.WHITE + f'{info["Machine"]}')
    print(Fore.RED + "Memory" + " " + Fore.WHITE + f'{info["Memory"]}')
    print(Fore.RED + "CPU" + " " + Fore.WHITE + f'{info["CPU"]}')
    print(Fore.RED + "CPU Percent" + " " + Fore.WHITE + f'{info["CPUP"]}')
    print(Fore.RED + "Resolution" + " " + Fore.WHITE + f'{info["Res"]}')
    print(Fore.RED + "Disk" + " " + Fore.WHITE + f'{info["Disk"]}')  
    
    print(Fore.LIGHTRED_EX + '------------END-------------')

if __name__ == "__main__":
    system_info = get_system_info()
    display_info(system_info)  

import subprocess
import psutil
from datetime import datetime

# Get system date and time
current_time = datetime.now().strftime('%y-%m-%d %H:%M:%S')

# Get system uptime
uptime = subprocess.check_output('cat /proc/uptime', shell=True).decode('utf-8').split()[0]
epoch_time = float(uptime)

# Get GPU temperature
gpu_temp = subprocess.check_output('vcgencmd measure_temp', shell=True).decode('utf-8').strip()
gpu_temp = gpu_temp.replace('temp=', '').replace('\'C', '')

# Get CPU temperature
cpu_temp = subprocess.check_output('cat /sys/class/thermal/thermal_zone0/temp', shell=True).decode('utf-8').strip()
cpu_temp = round(float(cpu_temp) / 1000.00, 2)

# Get CPU usage
cpu_usage = psutil.cpu_percent(interval=1)

# Get RAM usage
ram_usage = psutil.virtual_memory().percent

# Get Swap usage
swap_usage = psutil.swap_memory().percent

# Hostname
hostname = subprocess.check_output('hostname', shell=True).decode('utf-8').strip()

# Format the result
result = f'Timestamp: {current_time}\n'
result += f'Epoch Time: {epoch_time}\n'
result += f'GPU Temperature: {gpu_temp}˚C\n'
result += f'CPU Temperature: {cpu_temp}\n'
result += f'CPU Usage: {cpu_usage}\n'
result += f'RAM Usage: {ram_usage}\n'
result += f'Swap Usage: {swap_usage}\n'
result += f'Raspberry Pi Hostname: {hostname}'

print(result)
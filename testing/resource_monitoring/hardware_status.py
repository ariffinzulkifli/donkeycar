import subprocess
import psutil
from datetime import datetime, timedelta

# Get system date and time
current_time = datetime.now().strftime('%y-%m-%d %H:%M:%S')

# Get system uptime as a string
uptime_str = subprocess.check_output('cat /proc/uptime', shell=True).decode('utf-8').split()[0]

# Convert uptime string to a float
uptime_seconds = float(uptime_str)

# Convert uptime to a human-readable format
uptime_timedelta = timedelta(seconds=uptime_seconds)
uptime_readable = str(uptime_timedelta)

# Extract days, hours, and minutes from the timedelta
days = uptime_timedelta.days
hours, remainder = divmod(uptime_timedelta.seconds, 3600)
minutes = remainder // 60

# Format the uptime as "3 days 2 hours 13 minutes"
uptime_readable = f"{days} days {hours} hours {minutes} minutes"

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
result = f'Raspberry Pi Hostname: {hostname}\n'
result += f'Uptime: {uptime_readable}\n'
result += f'GPU Temperature: {gpu_temp} ˚C\n'
result += f'CPU Temperature: {cpu_temp} ˚C\n'
result += f'CPU Usage: {cpu_usage} %\n'
result += f'RAM Usage: {ram_usage} %\n'
result += f'Swap Usage: {swap_usage} %'

print(result)
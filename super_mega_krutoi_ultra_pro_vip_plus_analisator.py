import psutil
import time

# тут информация о процессах
physical_cores = psutil.cpu_count(logical=False)
total_cores = psutil.cpu_count(logical=True)

print(f"физических ядра: {physical_cores}")
print(f"логические потоки: {total_cores}")

# измеряем давление (нагрузку процессора)
cpu_usage = psutil.cpu_percent(interval=1)
print(f"нагрузка процессора: {cpu_usage}%")

# измеряем пульс (оперативку)
# чтобы ваши глаза не взорвались, мы из байтов переводим в мегабайты
ram = psutil.virtual_memory()

print(f"всего: {ram.total // (1024**2)} MB")
print(f"использовано: {ram.used // (1024**2)} MB ({ram.percent}%)")
print(f"свободно: {ram.available // (1024**2)} MB")

# измеряем уровень кислорода (диск) здесь делаем красиво в гигабайтах
disk = psutil.disk_usage('/')

print(f"всего на диске: {disk.total // (1024**3)} GB")
print(f"использовано: {disk.used // (1024**3)} GB ({disk.percent}%)")
print(f"свободно: {disk.free // (1024**3)} GB")

# запускаемся в космос (что запущено)
pids = psutil.pids()
print(f"запущенные процессы: {len(pids)}")

# рыболовная сеть (сеть) 
net = psutil.net_io_counters()

print(f"отправлено данных: {net.bytes_sent // (1024**2)} MB")
print(f"получено данных: {net.bytes_recv // (1024**2)} MB")
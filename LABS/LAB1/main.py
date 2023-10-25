import time
import psutil
import csv
import matplotlib.pyplot as plt

# Configuración de parámetros
sample_frequency = 5  # Frecuencia de muestreo en segundos
sampling_time = 300  # Tiempo total de muestreo en segundos (5 minutos)

# Inicializar listas para almacenar los datos
timestamps = []
idle_times = []
memory_usages = []
network_bytes_sent = []
network_bytes_received = []

# Tiempo de inicio del experimento
start_time = time.time()

# Bucle de adquisición de datos
while time.time() - start_time < sampling_time:
    timestamp = time.time()
    
    # Capturar datos del CPU
    idle_time = psutil.cpu_times().idle
    idle_times.append(idle_time)
    
    # Capturar datos de la memoria RAM
    memory_usage = psutil.virtual_memory().percent
    memory_usages.append(memory_usage)
    
    # Capturar datos de la actividad de red
    network_stats = psutil.net_io_counters()
    network_bytes_sent.append(network_stats.bytes_sent)
    network_bytes_received.append(network_stats.bytes_recv)
    
    timestamps.append(timestamp)
    time.sleep(sample_frequency)

# Almacenar los datos en un archivo CSV
with open('datos_experimento.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Timestamp', 'Idle Time', 'Memory Usage', 'Bytes Sent', 'Bytes Received'])
    for i in range(len(timestamps)):
        csv_writer.writerow([timestamps[i], idle_times[i], memory_usages[i], network_bytes_sent[i], network_bytes_received[i]])

# Calcular estadísticas
mean_idle_time = sum(idle_times) / len(idle_times)
mean_memory_usage = sum(memory_usages) / len(memory_usages)
mean_network_bytes_sent = sum(network_bytes_sent) / len(network_bytes_sent)
mean_network_bytes_received = sum(network_bytes_received) / len(network_bytes_received)

# Crear gráficos
plt.subplot(3, 1, 1)
plt.plot(timestamps, idle_times)
plt.ylabel('Tiempo de Ocio del CPU')

plt.subplot(3, 1, 2)
plt.plot(timestamps, memory_usages, color='orange')
plt.ylabel('Uso de Memoria (%)')

plt.subplot(3, 1, 3)
plt.plot(timestamps, network_bytes_sent, label='Enviados')
plt.plot(timestamps, network_bytes_received, label='Recibidos')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Bytes de Red')
plt.legend()

plt.tight_layout()
plt.show()

# Imprimir estadísticas
print(f"Media Tiempo de Ocio: {mean_idle_time}")
print(f"Media Uso de Memoria: {mean_memory_usage}")
print(f"Media Bytes Enviados: {mean_network_bytes_sent}")
print(f"Media Bytes Recibidos: {mean_network_bytes_received}")

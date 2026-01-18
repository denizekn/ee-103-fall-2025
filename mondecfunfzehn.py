import numpy as np
import matplotlib.pyplot as plt

# 1. Veri Oluşturma (Rezonans Eğrileri)
freq = np.linspace(2.35, 2.55, 500)  # 2.35 - 2.55 GHz arası

# Dry Air (Kuru Hava) - Merkez: 2.48 GHz
dry_response = -20 * np.exp(-((freq - 2.48)**2) / (2 * 0.005**2)) 

# Humid Air (Nemli Hava) - Merkez: 2.43 GHz (Sola kaymış)
humid_response = -20 * np.exp(-((freq - 2.43)**2) / (2 * 0.005**2))

# 2. Grafiği Çizme
plt.figure(figsize=(8, 5))
plt.plot(freq, dry_response, label='Dry Air (Low Permittivity)', color='blue', linewidth=2)
plt.plot(freq, humid_response, label='Humid Air (High Permittivity)', color='red', linestyle='--', linewidth=2)

# 3. Süslemeler ve Ok İşareti
plt.title("Resonant Frequency Shift Due to Humidity", fontsize=14)
plt.xlabel("Frequency (GHz)", fontsize=12)
plt.ylabel("Reflection Coefficient (dB)", fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# Ok işareti (Shift'i göstermek için)
plt.annotate('', xy=(2.43, -20), xytext=(2.48, -20),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.text(2.44, -15, "Frequency Shift\n(Due to Humidity)", horizontalalignment='center')

# 4. Kaydetme
plt.ylim(-25, 1)
plt.tight_layout()
plt.savefig("Sensor_Graph.png", dpi=300)
plt.show()
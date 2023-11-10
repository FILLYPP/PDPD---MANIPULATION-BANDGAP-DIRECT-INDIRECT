import matplotlib.pyplot as plt

# Multiplicar as energias de ionização teóricas por -1
combined_data['Energia de Ionização Teórico'] *= -1

# Gráfico de linhas para mostrar energias teóricas e experimentais
plt.figure(figsize=(10, 6))

# Energias teóricas
plt.plot(combined_data['Átomo'], combined_data['Energia de Ionização Teórico'], marker='o', label='Teórico', color='b', linewidth=2, markersize=8)

# Energias experimentais
plt.plot(combined_data['Átomo'], combined_data['Energia de Ionização Experimental (eV)'], marker='o', label='Experimental', color='g', linewidth=2, markersize=8)

plt.xlabel('Átomo')
plt.ylabel('Energia de Ionização (eV)')
plt.title('Energias de Ionização Teóricas e Experimentais')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

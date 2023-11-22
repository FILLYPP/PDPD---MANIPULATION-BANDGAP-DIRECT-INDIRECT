from pyscf import gto, dft

atoms = {
    'Li': {'charge': 0, 'spin': +1},
    'Be': {'charge': 0, 'spin': 0},
    'B':  {'charge': 0, 'spin': +1},
    'C':  {'charge': 0, 'spin': +2},
    'N':  {'charge': 0, 'spin': +3},
    'O':  {'charge': 0, 'spin': +2},
    'F':  {'charge': 0, 'spin': +1},
    'Ne': {'charge': 0, 'spin': 0},
    'Li_1': {'charge': 1, 'spin': 0},
    'Be_1': {'charge': 1, 'spin': +1},
    'B_1':  {'charge': 1, 'spin': 0},
    'C_1':  {'charge': 1, 'spin': +1},
    'N_1':  {'charge': 1, 'spin': +2},
    'O_1':  {'charge': 1, 'spin': +3},
    'F_1':  {'charge': 1, 'spin': +2},
    'Ne_1': {'charge': 1, 'spin': +1},
}

hartree_to_ev = -27.2114  # Fator de conversão de Hartree para eV

energies = {}  # Dicionário para armazenar as energias de cada átomo

for atom, properties in atoms.items():
    charge = properties['charge']
    spin = properties['spin']
    
    mol = gto.M(atom=f'{atom.split("_")[0]} 0 0 0;', basis='ccpvdz', charge=charge, spin=spin)
    rks = dft.RKS(mol)
    rks.xc = 'b3lyp'
    rks.verbose = 0
    total_energy = rks.kernel()

    total_energy_ev = total_energy * hartree_to_ev  # Convertendo para eV
    energies[atom] = total_energy_ev  # Armazenando a energia no dicionário
    print(f'\nThe RKS ground state total energy (in eV) of an isolated {atom} atom is {total_energy_ev}')

for element in ['Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']:
    neutral_energy = energies[f'{element}']
    charged_energy = energies[f'{element}_1']
    energy_difference = neutral_energy - charged_energy
    print(f'\nEnergy difference (in eV) between {element} and {element}_1 is {energy_difference}')


import matplotlib.pyplot as plt

# Valores teóricos e experimentais das energias em eV
atomos = ['Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
teorico = [5.39172, 9.32263, 8.29803, 11.2603, 15.581, 12.0697, 17.42282, 21.56454]
experimental = [5.613747332741696, 9.160976191281406, 8.725568145051852, 11.518296856499546,
                14.5876905848952, 13.912786585243111, 17.46351506616611, 21.357354457192287]

# Calculando a diferença entre os valores teóricos e experimentais
diferenca = [exp - teo for exp, teo in zip(experimental, teorico)]

# Determinando os limites do eixo y em intervalos de 0.2
limite_inferior = min(diferenca) - (min(diferenca) % 0.2)  # Arredonda para baixo
limite_superior = max(diferenca) + 0.2 - (max(diferenca) % 0.2)  # Arredonda para cima

# Criando o gráfico de barras com os limites de intervalos de 0.2
plt.figure(figsize=(10, 6))
plt.bar(atomos, diferenca, color='skyblue')
plt.xlabel('Átomos')
plt.ylabel('Diferença (eV)')
plt.title('Diferença entre Valores Teóricos e Experimentais das Energias dos Átomos')
plt.xticks(rotation=45)
plt.yticks([i * 0.2 for i in range(int(limite_inferior * 5), int(limite_superior * 5) + 1)], [i * 0.2 for i in range(int(limite_inferior * 5), int(limite_superior * 5) + 1)])
plt.grid(axis='y')

# Mostrando o gráfico
plt.tight_layout()
plt.show()

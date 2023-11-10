import sys
print(sys.path)

import pandas as pd
import matplotlib.pyplot as plt
import pyscf
from pyscf import gto, scf

atomos = ['B', 'C', 'N', 'O', 'F']
numeros_atomicos = [5, 6, 7, 8, 9]

basis={'minao':1,'ccpvdz':2,'ccpvtz':3,'ccpvqz':4,'ccpv5z':5}

resultados = []

for atom, Z in zip(atomos, numeros_atomicos):
    for basis_set in basis:
        for charge in range(-1, 2):
            num_eletrons = Z - charge
            if num_eletrons < 0:
                continue 
            
            if num_eletrons % 2 == 0:
                spin = 0
            else:
                spin = 1

            mol = gto.M(atom=f'{atom} 0 0 0', basis=basis_set, charge=charge, spin=spin)

            mf = scf.RHF(mol)
            energy = mf.kernel()
            
            resultados.append([atom, basis_set, charge, energy])

df = pd.DataFrame(resultados, columns=['Átomo', 'Base', 'Carga', 'Energia'])

df.to_csv('resultados.csv', index=False)

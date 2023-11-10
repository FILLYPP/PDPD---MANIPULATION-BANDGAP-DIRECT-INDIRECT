from pandas import read_csv
from seaborn import scatterplot
from matplotlib.pyplot import subplots, tight_layout, savefig

df = read_csv('resultados.csv')
atoms=list(set(df['Átomo'].tolist()))

fig, ax = subplots(1,len(atoms),sharex=True,figsize=(12, 3))

for i,atom in enumerate(atoms):
    scatterplot(data=df[df.Átomo==atom],x='Base',y='Energia',hue='Carga',ax=ax[i])
    ax[i].set_title(f'Species: {atom}')
    for item in ax[i].get_xticklabels():
        item.set_rotation(45)
    
tight_layout()
savefig('Eion_plots.png')

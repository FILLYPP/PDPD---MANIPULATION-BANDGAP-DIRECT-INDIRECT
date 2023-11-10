from pandas import read_csv
from seaborn import scatterplot
from matplotlib.pyplot import subplots, tight_layout, savefig
from scipy.optimize import curve_fit
from scipy.stats import chisquare
from numpy import exp, arange, diag, sqrt, log

def func(x,a,b,c):
    return a*exp(-b*x) + c

df = read_csv('resultados.csv')
atoms=list(set(df['Átomo'].tolist()))

basis_size={'minao':1,'ccpvdz':2,'ccpvtz':3,'ccpvqz':4,'ccpv5z':5}
df['Basis_size'] = df['Base'].apply(lambda x:basis_size[x])

print(df)

atom='F'
charge=-1

xdata=df[ (df.Átomo==atom) & (df.Carga==charge) ]['Basis_size'].to_numpy()
ydata=df[ (df.Átomo==atom) & (df.Carga==charge) ]['Energia'].to_numpy()

popt, pcov = curve_fit(func,xdata,ydata)
chisq = chisquare(ydata,func(xdata,*popt))
print(f'Goodness of fit: chi^2={chisq[0]}; pvalue={chisq[1]};')
print(f'Etot(cbs)={popt[2]};')

fig, ax = subplots(1,1)
scatterplot(data=df[df.Átomo==atom],x='Basis_size',y='Energia',hue='Carga',ax=ax) # DFT data points
# Fit
new_xdata=arange(0.5,5.5,0.1)
ax.plot(new_xdata,func(new_xdata,*popt),color='gray')
# Line indicating Etot at the Complete Basis Set limit (i.e. parameter c of func)
ax.plot([0.5,5.5],[popt[2]]*2,'--',color='gray')

tight_layout()
savefig('Eion_fit.png')

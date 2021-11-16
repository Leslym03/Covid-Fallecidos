import matplotlib.pyplot as plt

def sexo_hos(path, data):
    tabla = data.groupby('flag_hospitalizado')['dpt_cdc'].value_counts()
    print(tabla)

    positivos = data.groupby(['flag_hospitalizado','sexo']).size().unstack()
    positivos.plot(kind='bar', stacked=True)
    plt.ylabel('Numero de personas')
    plt.xlabel('Hospitalizados por covid')
    plt.title('Cantidad de personas hospitalizadas segun su sexo')
    plt.savefig(path)
    plt.show()
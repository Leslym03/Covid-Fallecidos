import matplotlib.pyplot as plt

def sexo_pos(path, data):
    tabla = data.groupby('cdc_positividad')['dpt_cdc'].value_counts()
    print(tabla)

    positivos = data.groupby(['cdc_positividad','sexo']).size().unstack()
    positivos.plot(kind='bar', stacked=True)
    plt.ylabel('Numero de personas')
    plt.xlabel('Positividad a covid')
    plt.title('Cantidad de personas positivas y negativas a covid segun su sexo')
    plt.savefig(path)
    plt.show()
import matplotlib.pyplot as plt

def criterio_fallecidos_bar(path, data):
    #x_values = data['criterio_fallecido'].unique()
    x_values = ['Enero', 'Febrero','Inv. Ep.', 'Serologico','Clinico', 'Radiologico','Nexo Ep.']
    y_values = data['criterio_fallecido'].value_counts().tolist()

    print(x_values)

    plt.bar(x_values, y_values)
    plt.ylabel('Numero de personas')
    plt.xlabel('Criterio de fallecimiento')
    plt.title('Cantidad de personas segun su criterio de fallecimiento')

    plt.xticks(rotation=15)
    plt.savefig(path)
    plt.show()

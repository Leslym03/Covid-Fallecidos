import matplotlib.pyplot as plt

def criterio_fallecidos_pie(path, data):
    x_values = ['Virologico', 'SINADEF','Inv. Ep.', 'Serologico','Clinico', 'Radiologico','Nexo Ep.']
    y_values = data['criterio_fallecido'].value_counts().tolist()

    print(x_values)
    plt.pie(y_values, labels = x_values)
    plt.title('Cantidad de personas segun su criterio de fallecimiento')

    plt.savefig(path)
    plt.show()
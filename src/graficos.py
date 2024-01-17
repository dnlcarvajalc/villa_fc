import matplotlib.pyplot as plt



def graficar(deudores, acreedores):
    """Funcion en donde se calcula la cantidad de personas que hay en diccionarios de 
        pagos y se grafican    

    Args:
        deudores (dict): Diccionario con las personas que deben. 
        acreedores (dict): Diccionario con las personas que estan al dia.
    """
    cantidad_deudores = len(deudores)
    cantidad_acreedores = len(acreedores)
    fig, ax = plt.subplots()
    pagos = ['Personas que no pagaron', 'Personas que si pagan',]
    cantidades = [cantidad_deudores, cantidad_acreedores]
    bar_labels = ['red', 'blue']
    bar_colors = ['tab:red', 'tab:blue']

    ax.bar(pagos, cantidades, label=bar_labels, color=bar_colors)

    ax.set_ylabel('CANTIDAD DE NIÑOS')
    ax.set_title('BALANCE DE PAGOS')
    
    plt.show()
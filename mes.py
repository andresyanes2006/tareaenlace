meses = {
    'enero': 31,
    'febrero': 28,
    'marzo': 31,
    'abril': 30,
    'mayo': 31,
    'junio': 30,
    'julio': 31,
    'agosto': 31,
    'septiembre': 30,
    'octubre': 31,
    'noviembre': 30,
    'diciembre': 31
}

# Definir un diccionario de festivos (puedes agregar los festivos que desees)
festivos = {
    'enero': ['Año Nuevo, lunes 9-dia de los reyes magos'],
    'febrero': ['no hay festivos'],
    'marzo': ['lunes 20-dia de san jose'],
    'abril':['domingo 2-domingo de ramos, jueves 6-jueves santo, viernes 7-viernes santo'],
    'mayo':['lunes 1-dia de trabajo, lunes 22-dia de la ascension '],
    'junio':['lunes 12-corpus christi, lunes 19-sagrado conrazon'],
    'julio':['lunes 3-san pedron y san pablo, jueves 20-dia de la independencia'],
    'agosto':['lunes 7-batalla de boyaca, lunes 21-la asuncion de la virgen'],
    'septiembre':['no hay festivos'],
    'octubre':['lunes 16-dia de la rosa'],
    'noviembre':['lunes 6-todos los santos, lunes 13-independencia de cartagena'],
    'diciembre': ['viernes 8-dia de la inmaculada concepcion, lunes 25-dia de navidad']
}
mes = input("Por favor, ingresa un mes en minúsculas: ")

if mes in meses:
    num_dias = meses[mes]
    if mes in festivos:
        festivo = festivos[mes]
        print(f"El mes de {mes} tiene {num_dias} días y los festivos son: {', '.join(festivo)}")
    else:
        print(f"El mes de {mes} tiene {num_dias} días.")
else:
    print("Mes no válido. Por favor, ingresa un mes válido en minúsculas.")
import pandas as pd

def preparar_datos(
    genero,
    etnia,
    discapacidad,
    estado,
    rangoedad,
    departamento,
    municipio,
    bancarizado,
    cantidad
):
    datos = pd.DataFrame([{
        "genero": genero,
        "etnia": etnia,
        "discapacidad": discapacidad,
        "estadobeneficiario": estado,
        "rangoedad": rangoedad,
        "nombredepartamentoatencion": departamento,
        "nombremunicipioatencion": municipio,
        "bancarizado": bancarizado,
        "cantidaddebeneficiarios": cantidad
    }])

    return datos

# -*- coding: utf-8 -*-
import random
import string
from memory_profiler import profile

_FIELD_NAMES = [
    "id",
    "nombreUnidadEconomica",
    "razonSocial",
    "codigoClasseActividad",
    "nombreClasseActividad",
    "descricionEstratoOcupado",
    "tipoVialidad",
    "nombreVialidad",
    "tipoVialidad1",
    "nombreVialidad1",
    "tipoVialidad2",
    "nombreVialidad2",
    "tipoVialidad3",
    "nombreVialidad3",
    "numeroExteriorKilometro",
    "letraExterior",
    "edificio",
    "edificioPiso",
    "numeroInterior",
    "letraInterior",
    "tipoAsentamientoHumano",
    "nombreAsentamientoHumano",
    "tipoCentroComercial",
    "corredorIndustrialOuMercadoPublico",
    "numeroLocal",
    "codigoPostal",
    "claveEntidad",
    "entidadFederativa",
    "claveMunicipio",
    "municipio",
    "claveLocalidad",
    "localidad",
    "areaGeoestadistica",
    "manzana",
    "numeroTelefono",
    "correoElectronico",
    "sitioInternet",
    "tipoEstablecimiento",
    "latitud",
    "longitud",
    "fechaIncorporacionDENUE"
]


@profile
def _create_random_string(size):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))


@profile
def create_random_json(fields, field_value_size=20):
    result = {}
    for field in fields:
        result[field] = _create_random_string(field_value_size)
    return result


@profile
def create_random_json_list(size):
    results = []
    for i in range(size):
        results.append(create_random_json(fields=_FIELD_NAMES))
    return results


if __name__ == '__main__':
    l = create_random_json_list(700000)
    print(len(l))


# size = 700000
# Filename: test.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     50 3123.121 MiB    0.000 MiB   @profile
#     51                             def _create_random_string(size):
#     52 3123.121 MiB    0.000 MiB       return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))


# Filename: test.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     55 3123.121 MiB    0.000 MiB   @profile
#     56                             def create_random_json(fields, field_value_size=20):
#     57 3123.121 MiB    0.000 MiB       result = {}
#     58 3123.121 MiB    0.000 MiB       for field in fields:
#     59 3123.121 MiB    0.000 MiB           result[field] = _create_random_string(field_value_size)
#     60 3123.121 MiB    0.000 MiB       return result


# Filename: test.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     63   16.215 MiB    0.000 MiB   @profile
#     64                             def create_random_json_list(size):
#     65   16.215 MiB    0.000 MiB       results = []
#     66 3123.121 MiB 3106.906 MiB       for i in range(size):
#     67 3123.121 MiB    0.000 MiB           results.appe

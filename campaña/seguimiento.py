import pandas as pd
from sqlalchemy import NVARCHAR, Integer


def importa_seguimiento(gc, engine):
    # SEGUIMIENTO
    ws_seguimiento = gc.open_by_key('1MWRkLjB3hpuCUX8UNlOqCqQHg_XT4HdqPuI2SXdd8BY').sheet1
    data = pd.DataFrame(ws_seguimiento.get_all_records())
    data.columns = ['Marca temporal', 'Usuario Evaluador', 'Perfil Evaluador', 'SN - Cod',
                    'Fecha llamada', 'Usuario Asesor', 'Teléfono Cliente', 'Nombre Cliente',
                    'TMO', 'SOT - Caso', 'Motivo', 'Detalle llamada',
                    'NO INGRESA TIPIFICACION',
                    'NO TIPIFICA DE FORMA COMPLETA',
                    'CUANDO NO SE DERIVA LA GESTION REALIZADA PARA SU ATENCION',
                    'CUANDO SE DERIVA UNA GESTION DE MANERA INCORRECTA',
                    'INGRESA DE MANERA INCORRECTA LOS DATOS EN EL APLICATIVO',
                    'NO INGRESA_INGRESA LOS DATOS EN EL APLICATIVO DE MANERA PARCIAL',
                    'VALIDACION DE LOS DATOS',
                    'PLANTILLA INCORRECTA O IMCOMPLETA',
                    'UTILIZACIÓN DE APLICACIONES',
                    'ESCRITURA INCOHERENTE',
                    'PRESENTA FALTAS ORTOGRAFICAS',
                    'Observaciones']

    data.to_sql('SEGUIMIENTO',
                con=engine,
                if_exists='replace',
                dtype={'Marca temporal': NVARCHAR(length=100),
                       'Usuario Evaluador': NVARCHAR(length=100),
                       'Perfil Evaluador': NVARCHAR(length=50),
                       'SN - Cod': NVARCHAR(length=20),
                       'Usuario Asesor': NVARCHAR(length=100),
                       'Teléfono Cliente': NVARCHAR(length=20),
                       'Nombre Cliente': NVARCHAR(length=100),
                       'TMO': Integer(),
                       'SOT - Caso': NVARCHAR(length=20),
                       'Motivo': NVARCHAR(length=100),
                       'Detalle llamada': NVARCHAR(length=3500),
                       'NO INGRESA TIPIFICACION': NVARCHAR(length=4),
                       'NO TIPIFICA DE FORMA COMPLETA': NVARCHAR(length=4),
                       'CUANDO NO SE DERIVA LA GESTION REALIZADA PARA SU ATENCION': NVARCHAR(length=4),
                       'CUANDO SE DERIVA UNA GESTION DE MANERA INCORRECTA': NVARCHAR(length=4),
                       'INGRESA DE MANERA INCORRECTA LOS DATOS EN EL APLICATIVO': NVARCHAR(length=4),
                       'NO INGRESA_INGRESA LOS DATOS EN EL APLICATIVO DE MANERA PARCIAL': NVARCHAR(length=4),
                       'VALIDACION DE LOS DATOS': NVARCHAR(length=4),
                       'PLANTILLA INCORRECTA O IMCOMPLETA': NVARCHAR(length=4),
                       'UTILIZACIÓN DE APLICACIONES': NVARCHAR(length=4),
                       'ESCRITURA INCOHERENTE': NVARCHAR(length=4),
                       'PRESENTA FALTAS ORTOGRAFICAS': NVARCHAR(length=4),
                       'Observaciones': NVARCHAR(length=3500),
                       'Fecha llamada': NVARCHAR(length=100)})

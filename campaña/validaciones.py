import pandas as pd
from sqlalchemy import NVARCHAR, Integer


def importa_validaciones(gc, engine):
    # VALIDACIONES
    ws_validaciones = gc.open_by_key('1jaYNOVyOTveMbCAOCOU5LsawoRZDtJD6rPIOT9-Wf50').sheet1
    data = pd.DataFrame(ws_validaciones.get_all_records())
    data.columns = ['Marca temporal', 'Usuario Evaluador', 'Perfil Evaluador', 'SN - Cod',
                    'Usuario Asesor', 'Teléfono Cliente', 'Nombre Cliente', 'TMO',
                    'SOT - Caso', 'Motivo', 'Detalle llamada',
                    '1.1 No identifica interlocutor',
                    '1.2 Cumplimiento de speech bienvenida-despedida',
                    '1.3 Utiliza un lenguaje inapropiado con el UF',
                    '1.4 No solicita tiempo de espera',
                    '1.5 Solicita tiempos de espera innecesarios',
                    '1.6 No retoma agradeciendo la espera',
                    '1.7 Excede el tiempo de espera permitido',
                    '1.8 No atiende la llamada en el tiempo establecido',
                    '1.9 Asesor tutea al cliente',
                    '2.1 No presta atencion a comentarios/solicitudes de UF',
                    '2.2 Solicitud de datos',
                    '2.3 Validacion de datos',
                    '2.4 Solicita_confirma mas de una vez una informacion innecesaria',
                    '3.1 Suministra informacion incompleta',
                    '3.2 Suministra informacion incorrecta',
                    '3.3 Cierre de sot_cambio de estado',
                    '3.4 Descartes con aplicativos',
                    '4.1 No tipifica de manera completa en aplicativos internos',
                    '4.2 No tipifica en aplicativos',
                    '4.3 Plantilla incorrecta',
                    '4.4 Tipifica de manera incorrecta en aplicativos',
                    '5.1 Manejo de clientes criticos_otras consultas',
                    '5.2 Demuestra mala actitud',
                    '5.3 Muletillas',
                    '5.4 Interrumpe al cliente',
                    '5.5 Lenguaje adecuado y entonacion de la  voz',
                    '6.1 Recomienda smart home',
                    'Mala Praxis', 'Observaciones', 'Fecha llamada']

    data.to_sql('VALIDACIONES',
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
                       'Motivo': NVARCHAR(length=200),
                       'Detalle llamada': NVARCHAR(length=3500),
                       '1.1 No identifica interlocutor': NVARCHAR(length=4),
                       '1.2 Cumplimiento de speech bienvenida-despedida': NVARCHAR(length=4),
                       '1.3 Utiliza un lenguaje inapropiado con el UF': NVARCHAR(length=4),
                       '1.4 No solicita tiempo de espera': NVARCHAR(length=4),
                       '1.5 Solicita tiempos de espera innecesarios': NVARCHAR(length=4),
                       '1.6 No retoma agradeciendo la espera': NVARCHAR(length=4),
                       '1.7 Excede el tiempo de espera permitido': NVARCHAR(length=4),
                       '1.8 No atiende la llamada en el tiempo establecido': NVARCHAR(length=4),
                       '1.9 Asesor tutea al cliente': NVARCHAR(length=4),
                       '2.1 No presta atencion a comentarios/solicitudes de UF': NVARCHAR(length=4),
                       '2.2 Solicitud de datos': NVARCHAR(length=4),
                       '2.3 Validacion de datos': NVARCHAR(length=4),
                       '2.4 Solicita_confirma mas de una vez una informacion innecesaria': NVARCHAR(length=4),
                       '3.1 Suministra informacion incompleta': NVARCHAR(length=4),
                       '3.2 Suministra informacion incorrecta': NVARCHAR(length=4),
                       '3.3 Cierre de sot_cambio de estado': NVARCHAR(length=4),
                       '3.4 Descartes con aplicativos': NVARCHAR(length=4),
                       '4.1 No tipifica de manera completa en aplicativos internos': NVARCHAR(length=4),
                       '4.2 No tipifica en aplicativos': NVARCHAR(length=4),
                       '4.3 Plantilla incorrecta': NVARCHAR(length=4),
                       '4.4 Tipifica de manera incorrecta en aplicativos': NVARCHAR(length=4),
                       '5.1 Manejo de clientes criticos_otras consultas': NVARCHAR(length=4),
                       '5.2 Demuestra mala actitud': NVARCHAR(length=4),
                       '5.3 Muletillas': NVARCHAR(length=4),
                       '5.4 Interrumpe al cliente': NVARCHAR(length=4),
                       '5.5 Lenguaje adecuado y entonacion de la  voz': NVARCHAR(length=4),
                       '6.1 Recomienda smart home': NVARCHAR(length=4),
                       'Mala Praxis': NVARCHAR(length=200),
                       'Observaciones': NVARCHAR(length=3500),
                       'Fecha llamada': NVARCHAR(length=100)})

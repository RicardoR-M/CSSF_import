import pandas as pd
from sqlalchemy import NVARCHAR, Integer


def importa_asot(gc, engine):
    # BO FASE AVERIAS
    pass
    # ws = gc.open_by_key('17Sw_NyA_dKZ2wGcQZa9qsE5U0JZi2vmj8U83CTuz-WE').sheet1
    # data = pd.DataFrame(ws.get_all_records())
    # data.columns = ['Marca temporal', 'Usuario Evaluador', 'Perfil Evaluador', 'SN - Cod',
    #                 'Fecha llamada', 'Usuario Asesor', 'Teléfono Cliente', 'Nombre Cliente',
    #                 'TMO', 'SOT - Caso', 'Motivo', 'Detalle llamada',
    #                 'SUMINISTRA INFORMACIÓN - SUMINISTRA INFORMACIÓN INCOMPLETA',
    #                 'SUMINISTRA INFORMACIÓN - SUMINISTRA INFORMACIÓN INCORRECTA',
    #                 'AMABILIDAD Y EMPATÍA - DEMUESTRA MALA ACTITUD',
    #                 'AMABILIDAD Y EMPATÍA - EXCESO DE CONFIANZA CON EL UF',
    #                 'ESCUCHA ACTIVA - NO PRESTA ATENCIÓN A COMENTARIOS/SOLICITUDES DE UF',
    #                 'ESCUCHA ACTIVA - SILENCIOS INCÓMODOS',
    #                 'ESCUCHA ACTIVA - SOLICITA/CONFIRMA MÁS DE UNA VEZ UNA INFORMACIÓN INNECESARIAMENTE',
    #                 'ABANDONO DE LLAMADA - ABANDONA AL CLIENTE EN LA ESPERA',
    #                 'ABANDONO DE LLAMADA - CUELGA DELIBERADAMENTE LA LLAMADA',
    #                 'ANALISIS DE CASO - NO IDENTIFICA DE FORMA COMPLETA EL MOTIVO DE LA INCIDENCIA / CASO',
    #                 'ANALISIS DE CASO - NO IDENTIFICA EL MOTIVO DE LA INCIDENCIA / CASO',
    #                 'ANALISIS DE CASO - NO IDENTIFICA EL NUMERO DEL CUAL LLAMA',
    #                 'MANEJO DE TIEMPOS - EXCEDE EL TIEMPO DE ESPERA PERMITIDO',
    #                 'MANEJO DE TIEMPOS - NO ATIENDE LA LLAMADA EN EL TIEMPO ESTABLECIDO',
    #                 'MANEJO DE TIEMPOS - SOLICITA TIEMPOS DE ESPERA INNECESARIOS',
    #                 'TIPIFICACIÓN - NO UTILIZA PLANTILLA CORRECTA PARA EL REGISTRO',
    #                 'TIPIFICACIÓN - TIPIFICA DE MANERA INCORRECTA / INCOMPLETA EN APLICATIVOS',
    #                 'CUMPLE CON EL PROCEDIMIENTO ESTABLECIDO - CUMPLIMIENTO DE SPEECH BIENVENIDA - DESPEDIDA',
    #                 'CUMPLE CON EL PROCEDIMIENTO ESTABLECIDO - DERIVACION CORRECTA CASOS',
    #                 'CUMPLE CON EL PROCEDIMIENTO ESTABLECIDO - DESCARTES PARA ENTREGA DE SOLUCION',
    #                 'CUMPLE CON EL PROCEDIMIENTO ESTABLECIDO - GESTIONA REAGENDAMIENTO',
    #                 'CUMPLE CON EL PROCEDIMIENTO ESTABLECIDO - NO CAMBIA ESTADO DE CASO',
    #                 'CUMPLE CON EL PROCEDIMIENTO ESTABLECIDO - NO TRABAJA VARIACIÓN/ INCIDENCIAS',
    #                 'CUMPLE CON EL PROCEDIMIENTO ESTABLECIDO - SOLICITUD Y VALIDACION DE LOS DATOS',
    #                 'CUMPLE CON EL PROCEDIMIENTO ESTABLECIDO - SONDEO CORRECTO Y COMPLETO',
    #                 'CUMPLE CON EL PROCEDIMIENTO ESTABLECIDO - UTILIZACIÓN DE APLICACIONES',
    #                 'Observaciones']
    #
    # data.to_sql('ASOT',
    #             con=engine,
    #             if_exists='replace',
    #             dtype={'Marca temporal': NVARCHAR(length=100),
    #                    'Usuario Evaluador': NVARCHAR(length=100),
    #                    'Perfil Evaluador': NVARCHAR(length=50),
    #                    'SN - Cod': NVARCHAR(length=20),
    #                    'Fecha llamada': NVARCHAR(length=100),
    #                    'Usuario Asesor': NVARCHAR(length=100),
    #                    'Teléfono Cliente': NVARCHAR(length=20),
    #                    'Nombre Cliente': NVARCHAR(length=100),
    #                    'TMO': Integer(),
    #                    'SOT - Caso': NVARCHAR(length=20),
    #                    'Motivo': NVARCHAR(length=100),
    #                    'Detalle llamada': NVARCHAR(length=3500),
    #                    'SUMINISTRA INFORMACIÓN - SUMINISTRA INFORMACIÓN INCOMPLETA': NVARCHAR(length=4),
    #                    'SUMINISTRA INFORMACIÓN - SUMINISTRA INFORMACIÓN INCORRECTA': NVARCHAR(length=4),
    #                    'AMABILIDAD Y EMPATÍA - DEMUESTRA MALA ACTITUD': NVARCHAR(length=4),
    #                    'AMABILIDAD Y EMPATÍA - EXCESO DE CONFIANZA CON EL UF': NVARCHAR(length=4),
    #                    'ESCUCHA ACTIVA - NO PRESTA ATENCIÓN A COMENTARIOS/SOLICITUDES DE UF': NVARCHAR(length=4),
    #                    'ESCUCHA ACTIVA - SILENCIOS INCÓMODOS': NVARCHAR(length=4),
    #                    'ESCUCHA ACTIVA - SOLICITA/CONFIRMA MÁS DE UNA VEZ UNA INFORMACIÓN INNECESARIAMENTE': NVARCHAR(length=4),
    #                    'ABANDONO DE LLAMADA - ABANDONA AL CLIENTE EN LA ESPERA': NVARCHAR(length=4),
    #                    'ABANDONO DE LLAMADA - CUELGA DELIBERADAMENTE LA LLAMADA': NVARCHAR(length=4),
    #                    'ANALISIS DE CASO - NO IDENTIFICA DE FORMA COMPLETA EL MOTIVO DE LA INCIDENCIA / CASO': NVARCHAR(length=4),
    #                    'ANALISIS DE CASO - NO IDENTIFICA EL MOTIVO DE LA INCIDENCIA / CASO': NVARCHAR(length=4),
    #                    'ANALISIS DE CASO - NO IDENTIFICA EL NUMERO DEL CUAL LLAMA': NVARCHAR(length=4),
    #                    'MANEJO DE TIEMPOS - EXCEDE EL TIEMPO DE ESPERA PERMITIDO': NVARCHAR(length=4),
    #                    'MANEJO DE TIEMPOS - NO ATIENDE LA LLAMADA EN EL TIEMPO ESTABLECIDO': NVARCHAR(length=4),
    #                    'MANEJO DE TIEMPOS - SOLICITA TIEMPOS DE ESPERA INNECESARIOS': NVARCHAR(length=4),
    #                    'TIPIFICACIÓN - NO UTILIZA PLANTILLA CORRECTA PARA EL REGISTRO': NVARCHAR(length=4),
    #                    'TIPIFICACIÓN - TIPIFICA DE MANERA INCORRECTA / INCOMPLETA EN APLICATIVOS': NVARCHAR(length=4),
    #                    'CUMPLE CON EL PROCEDIMIENTO ESTABLECIDO - CUMPLIMIENTO DE SPEECH BIENVENIDA - DESPEDIDA': NVARCHAR(length=4),
    #                    'CUMPLE CON EL PROCEDIMIENTO ESTABLECIDO - DERIVACION CORRECTA CASOS': NVARCHAR(length=4),
    #                    'CUMPLE CON EL PROCEDIMIENTO ESTABLECIDO - DESCARTES PARA ENTREGA DE SOLUCION': NVARCHAR(length=4),
    #                    'CUMPLE CON EL PROCEDIMIENTO ESTABLECIDO - GESTIONA REAGENDAMIENTO': NVARCHAR(length=4),
    #                    'CUMPLE CON EL PROCEDIMIENTO ESTABLECIDO - NO CAMBIA ESTADO DE CASO': NVARCHAR(length=4),
    #                    'CUMPLE CON EL PROCEDIMIENTO ESTABLECIDO - NO TRABAJA VARIACIÓN/ INCIDENCIAS': NVARCHAR(length=4),
    #                    'CUMPLE CON EL PROCEDIMIENTO ESTABLECIDO - SOLICITUD Y VALIDACION DE LOS DATOS': NVARCHAR(length=4),
    #                    'CUMPLE CON EL PROCEDIMIENTO ESTABLECIDO - SONDEO CORRECTO Y COMPLETO': NVARCHAR(length=4),
    #                    'CUMPLE CON EL PROCEDIMIENTO ESTABLECIDO - UTILIZACIÓN DE APLICACIONES': NVARCHAR(length=4),
    #                    'Observaciones': NVARCHAR(length=3500)})

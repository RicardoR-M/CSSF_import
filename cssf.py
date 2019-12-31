import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sqlalchemy import create_engine

from campaña.analisis_sot import importa_asot
from campaña.atf import importa_atf
from campaña.preventivo_hfc import importa_prevhfc
from campaña.repitencia_hfc import importa_repithfc
from campaña.validaciones import importa_validaciones
from campaña.seguimiento import importa_seguimiento

engine = create_engine('mssql+pymssql://***REMOVED***:123@10.197.91.1:1433/CLARO_CSSF')

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

gcreds = {
    "type": "service_account",
    "project_id": "***REMOVED***",
    "private_key_id": "***REMOVED***",
    "private_key": "***REMOVED***",
    "client_email": "cssf-653@***REMOVED***.iam.gserviceaccount.com",
    "client_id": "***REMOVED***",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/cssf-653%40***REMOVED***.iam.gserviceaccount.com"
}

credentials = ServiceAccountCredentials.from_json_keyfile_dict(gcreds, scope)
gc = gspread.authorize(credentials)

importa_atf(gc, engine)  # Sigma
importa_seguimiento(gc, engine)
importa_validaciones(gc, engine)  # Sigma
importa_asot(gc, engine)
importa_prevhfc(gc, engine)
importa_repithfc(gc, engine)
input('Todo OK, presiona cualquier tecla para salir.')

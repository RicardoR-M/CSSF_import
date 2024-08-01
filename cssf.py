import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sqlalchemy import create_engine

from campaña.analisis_sot import importa_asot
from campaña.atf import importa_atf
from campaña.preventivo_hfc import importa_prevhfc
from campaña.repitencia_hfc import importa_repithfc
from campaña.validaciones import importa_validaciones
from campaña.seguimiento import importa_seguimiento

engine = create_engine('mssql+pymssql://protected:protected@10.197.91.1:1433/CLARO_CSSF')

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

gcreds = {}

credentials = ServiceAccountCredentials.from_json_keyfile_dict(gcreds, scope)
gc = gspread.authorize(credentials)

importa_atf(gc, engine)  # Sigma
importa_seguimiento(gc, engine)
importa_validaciones(gc, engine)  # Sigma
importa_asot(gc, engine)
importa_prevhfc(gc, engine)
importa_repithfc(gc, engine)
input('Todo OK, presiona cualquier tecla para salir.')

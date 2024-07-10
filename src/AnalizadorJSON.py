import os
import sys
import ply.lex as lex
import ply.yacc as yacc

# Librerías para la interfaz gráfica
from PyQt6.QtCore import Qt, QSize, QRect
from PyQt6.QtGui import QIcon, QPainter, QAction, QGuiApplication, QPalette, QColor, QFont
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QHBoxLayout, QPlainTextEdit,
    QWidget, QSizePolicy,
    QLabel, QVBoxLayout,
    QToolBar, QStatusBar,
    QFileDialog, QMessageBox,
)


# Tokens del Lexer
tokens = ('DOS_PUNTOS', 'SALTO',
          'A_LLAVE', 'C_LLAVE',
          'A_CORCH', 'C_CORCH',
          'COMA', 'L_EMPRESAS',
          'VERSION', 'FIRMA_DIG', 'N_EMPRESA',
          'FUNDACION',
          'DIRECCION', 'CALLE', 'CIUDAD',
          'PAIS', 'I_ANUALES', 'PYME',
          'LINK', 'L_DEPARTAMENTOS',
          'NOMBRE', 'JEFE', 'L_SUBDEPARTAMENTOS',
          'L_EMPLEADOS',
          'EDAD', 'CARGO',
          'SALARIO', 'PROD_ANALYST',
          'PROJ_MANAGER', 'UX_DESIGNER',
          'MARKETING', 'DEVELOPER',
          'DEVOPS', 'DB_ADMIN',
          'ACTIVO', 'FECHA_CONTRAT',
          'L_PROYECTOS',
          'ESTADO', 'FECHA_INICIO',
          'FECHA_FIN', 'TO_DO',
          'IN_PROGRESS', 'CANCELED',
          'DONE', 'ON_HOLD', 'DATE', 'ERROR_DATE',
          'URL', 'FLOAT', 'ERROR_FLOAT',
          'INT', 'NULL', 'BOOL',
          'TAB', 'ESPACIO', 'STRING', 'ERROR',
          )

# Funciones del LEXER


def t_SALTO(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_DOS_PUNTOS(t):
    r':'
    return t


def t_A_LLAVE(t):
    r'{'
    return t


def t_C_LLAVE(t):
    r'}'
    return t


def t_A_CORCH(t):
    r'\['
    return t


def t_C_CORCH(t):
    r'\]'
    return t


def t_COMA(t):
    r','
    return t


def t_L_EMPRESAS(t):
    r'\"empresas\"'
    return t


def t_VERSION(t):
    r'\"versión\"'
    return t


def t_FIRMA_DIG(t):
    r'\"firma_digital\"'
    return t


def t_N_EMPRESA(t):
    r'\"nombre_empresa\"'
    return t


def t_FUNDACION(t):
    r'\"fundación\"'
    return t


def t_DIRECCION(t):
    r'\"dirección\"'
    return t


def t_CALLE(t):
    r'\"calle\"'
    return t


def t_CIUDAD(t):
    r'\"ciudad\"'
    return t


def t_PAIS(t):
    r'\"país\"'
    return t


def t_I_ANUALES(t):
    r'\"ingresos_anuales\"'
    return t


def t_PYME(t):
    r'\"pyme\"'
    return t


def t_LINK(t):
    r'\"link\"'
    return t


def t_NOMBRE(t):
    r'\"nombre\"'
    return t


def t_L_DEPARTAMENTOS(t):
    r'\"departamentos\"'
    return t


def t_JEFE(t):
    r'\"jefe\" '
    return t


def t_L_SUBDEPARTAMENTOS(t):
    r'\"subdepartamentos\"'
    return t


def t_L_EMPLEADOS(t):
    r'\"empleados\"'
    return t


def t_EDAD(t):
    r'\"edad\"'
    return t


def t_CARGO(t):
    r'\"cargo\"'
    return t


def t_SALARIO(t):
    r'\"salario\"'
    return t


def t_PROD_ANALYST(t):
    r'\"Product\sAnalyst\"'
    return t


def t_PROJ_MANAGER(t):
    r'\"Project\sManager\"'
    return t


def t_UX_DESIGNER(t):
    r'\"UX\sdesigner\"'
    return t


def t_MARKETING(t):
    r'\"Marketing\"'
    return t


def t_DEVELOPER(t):
    r'\"Developer\"'
    return t


def t_DEVOPS(t):
    r'\"Devops\"'
    return t


def t_DB_ADMIN(t):
    r'\"DB\sadmin\"'
    return t


def t_ACTIVO(t):
    r'\"activo\"'
    return t


def t_FECHA_CONTRAT(t):
    r'\"fecha_contratación\"'
    return t


def t_L_PROYECTOS(t):
    r'\"proyectos\"'
    return t


def t_ESTADO(t):
    r'\"estado\"'
    return t


def t_TO_DO(t):
    r'\"To\sdo\"'
    return t


def t_IN_PROGRESS(t):
    r'\"In\sprogress\"'
    return t


def t_CANCELED(t):
    r'\"Canceled\"'
    return t


def t_DONE(t):
    r'\"Done\"'
    return t


def t_ON_HOLD(t):
    r'\"On\shold\"'
    return t


def t_FECHA_INICIO(t):
    r'\"fecha_inicio\"'
    return t


def t_FECHA_FIN(t):
    r'\"fecha_fin\"'
    return t


def t_DATE(t):
    r'"((19|20)[0-9]{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])"'
    return t


def t_ERROR_DATE(t):  # Detecta todos los formatos inválidos de fecha
    r'"(\b\d{2}-\d{2}-\d{4}\b)"|(\b\d{2}-\d{2}-\d{4}\b)|(\b\d{4}-\d{2}-\d{2}\b)|"((1[1-8]|2[1-9])\d{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])"|"((19|20)\d{2})-(1[3-9]|2[0-9])-(0[1-9]|[12][0-9]|3[01])"|"((19|20)\d{2})-(0[1-9]|1[0-2])-(00|[3-9][0-9])"'
    window.output_text.insertPlainText("-----------------------------\n")
    window.output_text.insertPlainText(
        f"Error léxico: En la línea {t.lineno} el token DATE está mal escrito {t.value}\n")
    window.output_text.insertPlainText("-----------------------------\n")
    return t


def t_URL(t):  # ACEPTA URLS ABSOLUTAS
    r'\"(http|https|ftp|ftps)://[^/\s:]+(:\d+)?(/[^#\s]*)?(\#\S*)?\"'
    return t


def t_ERROR_FLOAT(t):
    r'\b\d+(\.(\d{1,}))+(\.(\d{1,}))+\b|\b\d+(\.(\d{1}|\d{3,}))+\b|\b\d+(\,(\d{1,}))+\b'
    window.output_text.insertPlainText("-----------------------------\n")
    window.output_text.insertPlainText(
        f"Error léxico: En la linea {t.lineno} FLOAT mal escrito {t.value}\n")
    window.output_text.insertPlainText("-----------------------------\n")
    return t


def t_FLOAT(t):
    # Coincidir con números de la forma 123.45, solo con 2 dígitos después de la coma
    r'\b\d+\.\d{2}\b'
    return t

# Regla para reconocer enteros


def t_INT(t):
    r'\d+'  # Coincidir con números enteros
    return t


def t_BOOL(t):
    r'true|false'
    return t


def t_NULL(t):
    r'null'
    return t


def t_TAB(t):
    r'\t'
    pass


def t_ESPACIO(t):
    r'\ '
    pass


t_ignore = '\r'


#Sacamos el window file de string para que en el documento traducido no copie todos los strings 
def t_STRING(t):
    r'\"([^\"\n\:]+)\"'
    #window.file.write(t.value)
    return t


def t_error(t):
    t.lexer.skip(1)


# Control de errores de token mal escrito
def t_ERROR(t):
    r'((?!=:\s*)([A-Za-z\s]+)(?=,|\n)|\'(\w+)\'(?=\s*:)|(?!=:\s*)\'([^,\n]+)|(?!=:\s*)"([^",\n]+)|"([^"\s\:]+(?=:))|(([^"\s\:]+))")'
    window.output_text.insertPlainText("-----------------------------\n")
    window.output_text.insertPlainText(
        f"Error léxico, en la línea {t.lineno} : Token mal escrito {t.value}\n")
    window.output_text.insertPlainText("-----------------------------\n")
    return t


# Construir Lexer
lexer = lex.lex()


def p_sigma(p):
    '''sigma : A_LLAVE empresas COMA version COMA firma_digital C_LLAVE
    | A_LLAVE version COMA empresas COMA firma_digital C_LLAVE
    | A_LLAVE version COMA firma_digital COMA empresas C_LLAVE
    | A_LLAVE firma_digital COMA empresas COMA version C_LLAVE
    | A_LLAVE firma_digital COMA version COMA empresas C_LLAVE
    | A_LLAVE empresas COMA firma_digital COMA version C_LLAVE'''


def p_empresas(p):
    '''empresas : L_EMPRESAS DOS_PUNTOS A_CORCH i_empresa empresa C_CORCH '''

def p_i_empresa(p):
    '''i_empresa :'''
    window.file.write(
        """\t<div style="border-color: gray; border-width: 1px; border-style:solid; padding:20px">\n\t"""
    )
def p_version(p):
    '''version : VERSION DOS_PUNTOS STRING
    | VERSION DOS_PUNTOS NULL'''


def p_firma_digital(p):
    '''firma_digital : FIRMA_DIG DOS_PUNTOS STRING
    | FIRMA_DIG DOS_PUNTOS NULL'''


def p_empresa(p):
    '''empresa : A_LLAVE nombre_empresa COMA fundacion COMA direccion i_anuales COMA pyme COMA i_link link COMA departamentos C_LLAVE c_empresa
    | A_LLAVE nombre_empresa COMA fundacion COMA direccion i_anuales COMA pyme COMA departamentos C_LLAVE c_empresa
    | A_LLAVE nombre_empresa COMA fundacion COMA direccion i_anuales COMA pyme COMA i_link link COMA departamentos C_LLAVE c_empresa COMA i_empresa empresa
    | A_LLAVE nombre_empresa COMA fundacion COMA direccion i_anuales COMA pyme COMA departamentos C_LLAVE c_empresa COMA i_empresa empresa'''

def p_i_link(p):
    '''i_link :'''
    window.file.write("\t\t\t\t<a href=")
    

def p_c_empresa(p):
    '''c_empresa :'''
    window.file.write("\t\t\t</div>\n")
    
    
def p_nombre_empresa(p):
    '''nombre_empresa : N_EMPRESA DOS_PUNTOS STRING'''
    window.file.write(f"\t\t\t<h1>\n\t\t\t\t\t{p[3]}\n\t\t\t\t</h1>\n")


def p_fundacion(p):
    '''fundacion : FUNDACION DOS_PUNTOS INT'''


def p_direccion(p):
    '''direccion : DIRECCION DOS_PUNTOS A_LLAVE direcciones C_LLAVE COMA
    | DIRECCION DOS_PUNTOS NULL COMA'''


def p_direcciones(p):
    '''direcciones : calle COMA ciudad COMA pais'''


def p_calle(p):
    '''calle : CALLE DOS_PUNTOS STRING'''


def p_ciudad(p):
    '''ciudad : CIUDAD DOS_PUNTOS STRING'''


def p_pais(p):
    '''pais : PAIS DOS_PUNTOS STRING'''


def p_i_anuales(p):
    '''i_anuales : I_ANUALES DOS_PUNTOS FLOAT'''


def p_pyme(p):
    '''pyme : PYME DOS_PUNTOS BOOL'''


def p_link(p):
    '''link : LINK DOS_PUNTOS URL
    | LINK DOS_PUNTOS NULL'''
    window.file.write(f"{p[3]}>Sitio Web</a>\n")


def p_departamentos(p):
    '''departamentos : L_DEPARTAMENTOS DOS_PUNTOS A_CORCH departamento C_CORCH'''


def p_departamento(p):
    '''departamento : A_LLAVE nombre_dpto COMA jefe COMA subdepartamentos C_LLAVE 
    | A_LLAVE jefe COMA nombre_dpto COMA subdepartamentos C_LLAVE
    | A_LLAVE jefe COMA subdepartamentos COMA nombre_dpto C_LLAVE
    | A_LLAVE nombre_dpto COMA subdepartamentos COMA jefe C_LLAVE
    | A_LLAVE subdepartamentos COMA jefe COMA nombre_dpto C_LLAVE
    | A_LLAVE subdepartamentos COMA nombre_dpto COMA jefe C_LLAVE 
    | A_LLAVE nombre_dpto COMA jefe COMA subdepartamentos C_LLAVE COMA departamento 
    | A_LLAVE jefe COMA nombre_dpto COMA subdepartamentos C_LLAVE COMA departamento 
    | A_LLAVE jefe COMA subdepartamentos COMA nombre_dpto C_LLAVE COMA departamento
    | A_LLAVE nombre_dpto COMA subdepartamentos COMA jefe C_LLAVE COMA departamento 
    | A_LLAVE subdepartamentos COMA jefe COMA nombre_dpto C_LLAVE COMA departamento 
    | A_LLAVE subdepartamentos COMA nombre_dpto COMA jefe C_LLAVE COMA departamento'''


def p_nombre_dpto(p):
    '''nombre_dpto : NOMBRE DOS_PUNTOS STRING'''
    window.file.write(f"\t\t\t\t<h2>\n\t\t\t\t\t{p[3]}\n\t\t\t\t</h2>\n")

def p_jefe(p):
    '''jefe : JEFE DOS_PUNTOS STRING
    | JEFE DOS_PUNTOS NULL '''


def p_subdepartamentos(p):
    '''subdepartamentos : L_SUBDEPARTAMENTOS DOS_PUNTOS A_CORCH subdepartamento C_CORCH'''


def p_subdepartamento(p):
    '''subdepartamento : A_LLAVE nombre_subdpto COMA jefe COMA empleados C_LLAVE
    | A_LLAVE nombre_subdpto COMA empleados COMA jefe C_LLAVE
    | A_LLAVE jefe COMA nombre_subdpto COMA empleados C_LLAVE
    | A_LLAVE jefe COMA empleados COMA nombre_subdpto C_LLAVE
    | A_LLAVE empleados COMA nombre_subdpto COMA jefe C_LLAVE
    | A_LLAVE empleados COMA jefe COMA nombre_subdpto C_LLAVE
    | A_LLAVE nombre_subdpto COMA jefe COMA empleados C_LLAVE COMA subdepartamento 
    | A_LLAVE nombre_subdpto COMA empleados COMA jefe C_LLAVE COMA subdepartamento 
    | A_LLAVE jefe COMA nombre_subdpto COMA empleados C_LLAVE COMA subdepartamento 
    | A_LLAVE jefe COMA empleados COMA nombre_subdpto C_LLAVE COMA subdepartamento
    | A_LLAVE empleados COMA nombre_subdpto COMA jefe C_LLAVE COMA subdepartamento
    | A_LLAVE empleados COMA jefe COMA nombre_subdpto C_LLAVE COMA subdepartamento
    | A_LLAVE nombre_subdpto COMA empleados C_LLAVE
    | A_LLAVE empleados COMA nombre_subdpto C_LLAVE
    | A_LLAVE nombre_subdpto COMA empleados C_LLAVE COMA subdepartamento 
    | A_LLAVE empleados COMA nombre_subdpto C_LLAVE COMA subdepartamento'''

def p_nombre_subdpto(p):
    '''nombre_subdpto : NOMBRE DOS_PUNTOS STRING'''
    window.file.write(f"\t\t\t\t<h3>\n\t\t\t\t\t{p[3]}\n\t\t\t\t</h3>\n")

def p_empleados(p):
    '''empleados : L_EMPLEADOS DOS_PUNTOS A_CORCH i_emp empleado c_emp C_CORCH
    | L_EMPLEADOS DOS_PUNTOS A_CORCH C_CORCH
    | L_EMPLEADOS DOS_PUNTOS NULL'''

def p_i_emp(p):
    '''i_emp :'''
    window.file.write("\t\t\t\t<ul>\n")
    

def p_c_emp(p):
    '''c_emp :'''
    window.file.write("\t\t\t\t</ul>\n")

def p_empleado(p):
    '''empleado : A_LLAVE nombre_emp COMA edad COMA cargo COMA salario COMA activo COMA fecha_contrat COMA proyectos C_LLAVE
    | A_LLAVE nombre_emp COMA edad COMA cargo COMA salario COMA activo COMA fecha_contrat COMA proyectos C_LLAVE COMA empleado '''

def p_nombre_emp(p):
    '''nombre_emp : NOMBRE DOS_PUNTOS STRING'''
    window.file.write(f"\t\t\t\t\t<li>\n\t\t\t\t\t\t{p[3]}\n\t\t\t\t\t</li>\n")
    
def p_edad(p):
    '''edad : EDAD DOS_PUNTOS INT
    | EDAD DOS_PUNTOS NULL '''


def p_cargo(p):
    '''cargo : CARGO DOS_PUNTOS cargos '''


def p_cargos(p):
    '''cargos : PROD_ANALYST
    | PROJ_MANAGER
    | MARKETING
    | DEVELOPER
    | DEVOPS
    | DB_ADMIN
    | UX_DESIGNER'''


def p_salario(p):
    '''salario : SALARIO DOS_PUNTOS FLOAT'''


def p_activo(p):
    '''activo : ACTIVO DOS_PUNTOS BOOL'''


def p_fecha_contrat(p):
    '''fecha_contrat : FECHA_CONTRAT DOS_PUNTOS DATE'''

def p_proyectos(p):
    '''proyectos : L_PROYECTOS DOS_PUNTOS A_CORCH i_prjct proyecto c_prjct C_CORCH
    | L_PROYECTOS DOS_PUNTOS NULL'''

def p_i_prjct(p):
    '''i_prjct :'''
    window.file.write("""\t\t\t\t\t\t<table style="border: black 2px solid;">\n\t\t\t\t\t\t\t<tbody>\n\t\t\t\t\t\t\t\t""")

def p_c_prjct(p):
    '''c_prjct :'''
    window.file.write("\n\t\t\t\t\t\t\t</tbody>\n\t\t\t\t\t\t</table>\n")

def p_proyecto(p):
    '''proyecto : A_LLAVE i_row nombre_prjct COMA estado COMA fecha_inicio COMA fecha_fin c_row C_LLAVE
    | A_LLAVE i_row nombre_prjct COMA estado COMA fecha_inicio c_row C_LLAVE
    | A_LLAVE i_row nombre_prjct COMA estado COMA fecha_inicio COMA fecha_fin c_row C_LLAVE COMA proyecto
    | A_LLAVE i_row nombre_prjct COMA estado COMA fecha_inicio c_row C_LLAVE COMA proyecto
    '''

def p_i_row(p):
    '''i_row :'''
    window.file.write("<tr>\n\t\t\t\t\t\t\t\t\t")

def p_c_row(p):
    '''c_row :'''
    window.file.write("\n\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t\t")

def p_nombre_prjct(p):
    '''nombre_prjct : NOMBRE DOS_PUNTOS STRING'''
    window.file.write(f"""<td style="border: black 1px solid;">\n\t\t\t\t\t\t\t\t\t\t{p[3]}\n\t\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t\t\t""")
def p_estado(p):
    '''estado : ESTADO DOS_PUNTOS estados
    | ESTADO DOS_PUNTOS NULL'''


def p_estados(p):
    '''estados : TO_DO
    | IN_PROGRESS
    | CANCELED
    | DONE
    | ON_HOLD'''
    window.file.write(f"""<td style="border: black 1px solid;">\n\t\t\t\t\t\t\t\t\t\t{p[1]}\n\t\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t\t\t""")

def p_fecha_inicio(p):
    '''fecha_inicio : FECHA_INICIO DOS_PUNTOS DATE '''
    window.file.write(f"""<td style="border: black 1px solid;">\n\t\t\t\t\t\t\t\t\t\t{p[3]}\n\t\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t\t\t""")

def p_fecha_fin(p):
    '''fecha_fin : FECHA_FIN DOS_PUNTOS DATE
    | FECHA_FIN DOS_PUNTOS NULL'''
    window.file.write(f"""<td style="border: black 1px solid;">\n\t\t\t\t\t\t\t\t\t\t{p[3]}\n\t\t\t\t\t\t\t\t\t</td>""")

def p_error(p):
    if p:
        window.output_text.insertPlainText(f"Error de sintaxis en línea {
            p.lineno}. Culpable: {p.value}\n")
        parser.errok()
        window.errores += 1
    else:
        window.output_text.insertPlainText("Fin del Archivo\n")


parser = yacc.yacc(errorlog= yacc.NullLogger())

# Interfaz Gráfica

# Variables de Direccionamiento para trabajar con las imágenes y Archivos
exe_dir = os.getcwd()
rel_path = os.path.join("icons", "")
test_rel = 'prueba'
testdir = (os.path.split(exe_dir))[0]
test_path = os.path.join(testdir, test_rel)
abs_path = os.path.join(exe_dir, rel_path)

# Color de la barra de número de Línea
lineBarColor = QColor("#AC87C5")
# Clase de la barra de Números de Línea (StackOverflow)


class Barra(QWidget):
    def __init__(self, parent=None):
        super(Barra, self).__init__(parent)
        self.editor = parent
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.editor.blockCountChanged.connect(self.update_width)
        self.editor.updateRequest.connect(self.update_on_scroll)
        self.update_width('1')

    def update_on_scroll(self, rect, scroll):
        if self.isVisible():
            if scroll:
                self.scroll(0, scroll)
            else:
                self.update()

    def update_width(self, string):
        width = self.fontMetrics().horizontalAdvance(str(string))+10
        if self.width() != width:
            self.setFixedWidth(width)

    def paintEvent(self, event):
        if self.isVisible():
            block = self.editor.firstVisibleBlock()
            height = self.fontMetrics().height()
            number = block.blockNumber()
            painter = QPainter(self)
            painter.fillRect(event.rect(), lineBarColor)
            painter.drawRect(0, 0, event.rect().width() -
                             1, event.rect().height() - 1)
            font = painter.font()

            current_block = self.editor.textCursor().block().blockNumber() + 1

            condition = True
            while block.isValid() and condition:
                block_geometry = self.editor.blockBoundingGeometry(block)
                offset = self.editor.contentOffset()
                block_top = block_geometry.translated(offset).top()
                number += 1

                rect = QRect(0, int(block_top), self.width() - 5, int(height))

                if number == current_block:
                    font.setBold(True)
                else:
                    font.setBold(False)

                painter.setFont(font)
                painter.drawText(
                    rect, Qt.AlignmentFlag.AlignRight, '%i' % number)

                if block_top > event.rect().bottom():
                    condition = False

                block = block.next()

            painter.end()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.json_name = "Empresa.json"
        self.codigo = ""
        # Crear Titulo y Ícono
        self.setWindowTitle("Analizador Sintáctico")
        self.setIconSize(QSize(256, 256))
        self.setWindowIcon(QIcon(os.path.join(abs_path+'Lp.ico')))
        self.setMinimumSize(QSize(1280, 720))
        self.setStyleSheet('''QMainWindow{
            background-color: rgb(189, 74, 189);
            }''')

        # Centrar Aplicación
        qr = self.frameGeometry()
        cp = QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # Editor de Texto
        labelInput = QLabel("Editor de Texto")
        labelInput.setFont(QFont('Unispace', 25))
        labelInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_text = QPlainTextEdit()
        self.input_text.setFont(QFont('FiraCode Nerd Font Mono', 14))
        self.input_text.setStyleSheet('''QPlainTextEdit{
            border: 1px solid;
            border-color:black;
            background-color: white;
            }''')
        self.input_text.setPlaceholderText("Esperando texto...")
        self.input_text.setSizePolicy(QSizePolicy.Policy.Expanding,
                                      QSizePolicy.Policy.Expanding)
        # Línea de Código
        self.num = Barra(self.input_text)

        # Consola de Salida (Solo Lectura)
        labelOutput = QLabel("Registro de Ejecución")
        labelOutput.setFont(QFont('Unispace', 25))
        labelOutput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_text = QPlainTextEdit()
        self.output_text.setFont(QFont('FiraCode Nerd Font Mono', 14))
        self.output_text.setStyleSheet('''QPlainTextEdit{
            border: 1px solid;
            border-color:black;
            background-color: white;
            }''')
        self.output_text.setReadOnly(True)
        self.output_text.setSizePolicy(QSizePolicy.Policy.Expanding,
                                       QSizePolicy.Policy.Expanding)

        # Añadir a la ventana ambas estructuras
        self.layout = QHBoxLayout()
        layoutI = QVBoxLayout()
        layoutD = QVBoxLayout()
        layoutText = QHBoxLayout()
        layoutI.addWidget(labelInput)
        layoutD.addWidget(labelOutput)
        layoutText.addWidget(self.num)
        layoutText.addWidget(self.input_text)
        layoutI.addLayout(layoutText)
        layoutD.addWidget(self.output_text)
        self.layout.addLayout(layoutI)
        self.layout.addLayout(layoutD)

        # Crear Barra de Herramientas
        toolbar = QToolBar()
        toolbar.setStyleSheet('''QToolBar{
            border: 1px solid;
            border-color:black;
            background-color: rgb(235, 160, 235);
            }''')
        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        toolbar.setIconSize(QSize(32, 32))
        toolbar.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.addToolBar(toolbar)
        self.setStatusBar(QStatusBar(self))

        # Crear Botones

        b_AbrirArch = QAction(
            QIcon(os.path.join(abs_path+'Abrir_Archivo.png')), "Abrir", self)
        b_AbrirArch.setStatusTip("Abrir un archivo")
        b_AbrirArch.triggered.connect(self.examinar)
        toolbar.addAction(b_AbrirArch)
        toolbar.addSeparator()

        b_Analizar = QAction(
            QIcon(os.path.join(abs_path+'Ejecutar_Analisis.png')), "Ejecutar", self)
        b_Analizar.setStatusTip("Ejecuta el análisis")
        b_Analizar.triggered.connect(self.ejecutar)
        toolbar.addAction(b_Analizar)
        toolbar.addSeparator()

        b_AbrirHTML = QAction(
            QIcon(os.path.join(abs_path+'Abrir_HTML.png')), "Abrir HTML", self)
        b_AbrirHTML.setStatusTip("Abré la ubicación del HTML")
        b_AbrirHTML.triggered.connect(self.encontrarHTML)
        toolbar.addAction(b_AbrirHTML)
        toolbar.addSeparator()

        b_GuardarJSON = QAction(
            QIcon(os.path.join(abs_path+'ImprimirJSON.png')), "Guardar JSON", self)
        b_GuardarJSON.setStatusTip("Crea un archivo JSON del editor")
        b_GuardarJSON.triggered.connect(self.guardar)
        toolbar.addAction(b_GuardarJSON)
        toolbar.addSeparator()

        b_Borrar = QAction(
            QIcon(os.path.join(abs_path+'Borrar.png')), "Borrar", self)
        b_Borrar.setStatusTip("Limpia la ventana")
        b_Borrar.triggered.connect(self.borrar)
        toolbar.addAction(b_Borrar)
        toolbar.addSeparator()

        b_Salir = QAction(
            QIcon(os.path.join(abs_path+'Salir.png')), "Salir", self)
        b_Salir.setStatusTip("Cierra la Aplicación")
        b_Salir.triggered.connect(self.salir)
        toolbar.addAction(b_Salir)

        # Dummy para generar correctamente la interfaz
        dummy = QWidget()
        dummy.setLayout(self.layout)
        self.setCentralWidget(dummy)

    # Definición de Acciones

    def examinar(self, s):
        dlg = QFileDialog()
        self.json_name, _ = dlg.getOpenFileName(
            self, "Seleccionar artículo", str(test_path), "JSON Files (*.json);;All Files (*)")

        if not self.json_name.endswith(".json"):
            error = QMessageBox.critical(
                self, 'Error de Archivo', 'Archivo con extensión incorrecta', QMessageBox.StandardButton.Close)

            if error == QMessageBox.StandardButton.Close:
                pass
        else:
            self.input_text.clear()
            self.output_text.clear()
            with open(self.json_name, "r", encoding="utf-8") as archivo:
                self.input_text.insertPlainText(archivo.read())

    def ejecutar(self, s):
        self.codigo = self.input_text.toPlainText()
        if self.codigo == "":
            error = QMessageBox.warning(
                self, 'Aviso', 'No hay texto cargado', QMessageBox.StandardButton.Close)

            if error == QMessageBox.StandardButton.Close:
                pass
        else:
            self.output_text.clear()
            self.errores = 0
            self.file = open(self.json_name.replace(".json", ".html"), "w")
            window.file.write("<!DOCTYPE html>\n\t<html>\n\t\t<head>\t</head>\n\t\t<body>\n\t\t")
            lexer.lineno = 1
            parser.parse(self.codigo)
            window.file.write("\n\t\t</body>\n\t</html>")
            self.file.close()
            if self.errores == 0:
                exito = QMessageBox.information(
                    self, 'Aviso', 'Análisis Exitoso', QMessageBox.StandardButton.Ok)

                if exito == QMessageBox.StandardButton.Ok:
                    pass
            else:
                error = QMessageBox.warning(self, 'Aviso', f'Analisis Finalizado, se encontraron errores {
                                            self.errores}', QMessageBox.StandardButton.Close)

                if error == QMessageBox.StandardButton.Close:
                    pass

    def encontrarHTML(self, s):
        os.startfile(str(test_path))

    def guardar(self, s):
        nuevojson = self.input_text.toPlainText()
        with open(self.json_name.replace(".json", " Modificado.json"), "w") as f:
            f.write(nuevojson)

    def borrar(self, s):
        self.input_text.clear()
        self.output_text.clear()

    def salir(self, s):
        confirm = QMessageBox.question(self, 'Cerrar Aplicación', '¿Está seguro que desea cerrar la ventana?',
                                       QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if confirm == QMessageBox.StandardButton.Yes:
            self.close()
        else:
            pass


app = QApplication([])

window = MainWindow()
window.show()

app.exec()

# Terminado el tutorial de PyQt6
# https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/
# Proyecto: Modernizar la interfaz del LexerParser
# https://coderslegacy.com/python/pyqt6-qlabel-widget/
# https://coderslegacy.com/python/pyqt6-qtextedit/
# Si es posible mejorar el código del LexerParser usando la bibliografía:
# https://ply.readthedocs.io/en/latest/ply.html

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

# Formato para XML
# Para darle jerarquía a los títulos
formato_imp = False
formato_sec = False
formato_inf = False

# Para darle jerarquía a las tablas
formato_head = False
formato_foot = False
formato_body = False

# Para diferenciar infos de section y article con los de media
formato_media = False

# Tokens del Lexer
tokens = ('DOC', 'TEXT', 'SALTO',
          'A_ARTICLE', 'C_ARTICLE',
          'A_INFO', 'C_INFO',
          'A_TITLE', 'C_TITLE',
          'A_EMAIL', 'C_EMAIL',
          'A_STREET', 'C_STREET',
          'A_CITY', 'C_CITY', 'A_STATE',
          'C_STATE', 'A_PHONE', 'C_PHONE',
          'A_COPY', 'C_COPY', 'A_YEAR',
          'C_YEAR', 'A_HOLDER', 'C_HOLDER',
          'A_AUTHOR', 'C_AUTHOR',
          'A_DATE', 'C_DATE',
          'A_FNAME', 'C_FNAME',
          'A_SNAME', 'C_SNAME',
          'A_SECT', 'C_SECT',
          'A_SIMSECT', 'C_SIMSECT',
          'A_ABSTRACT', 'C_ABSTRACT',
          'A_PARA', 'C_PARA',
          'A_SIMPARA', 'C_SIMPARA',
          'A_IMPORT', 'C_IMPORT',
          'A_COMMENT', 'C_COMMENT',
          'A_EMPHA', 'C_EMPHA',
          'A_MEDIA', 'C_MEDIA',
          'C_MEDIABRACKET',
          'A_IMAGE', 'C_IMAGE',
          'A_IMAGED', 'A_VIDEO',
          'C_VIDEO', 'A_VIDEOD',
          'C_URLLINK', 'URL', 'MURL',
          'A_LINK', 'C_LINK',
          'A_ILIST', 'C_ILIST',
          'A_ITEM', 'C_ITEM',
          'A_TABLE', 'C_TABLE',
          'A_TGROUP', 'C_TGROUP',
          'A_THEAD', 'C_THEAD',
          'A_TFOOT', 'C_TFOOT',
          'A_TBODY', 'C_TBODY',
          'A_ROW', 'C_ROW',
          'A_ENTRYTBL', 'C_ENTRYTBL',
          'A_ENTRY', 'C_ENTRY', 'ERROR',
          'A_ADDRESS', 'C_ADDRESS', 'TABULADO', 'ESPACIO',
          )

# Funciones del LEXER


def t_SALTO(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    window.file.write(os.linesep)


def t_DOC(t):
    r'<!DOCTYPE\s+article>'
    window.file.write("<!DOCTYPE html>")
    return t


def t_A_ARTICLE(t):
    r'<article>'
    window.file.write("<html>\n<head>\n</head>\n\t<body>")
    return t


def t_C_ARTICLE(t):
    r'</article>'
    window.file.write("\n\t</body>\n</html>")
    return t


def t_A_INFO(t):
    r'<info>'
    global formato_inf, formato_media
    if formato_media:
        formato_inf = True
        window.file.write(" ")
    else:
        formato_inf = True
        formato1 = """<p style="background-color: green"><font size ="8px" color = "white"> """
        window.file.write(formato1)
    return t


def t_C_INFO(t):
    r'</info>'
    global formato_inf, formato_media
    if formato_media:
        window.file.write(" ")
        formato_inf = False
    else:
        formato_inf = False
        window.file.write("</font>\n</p>")
    return t


def t_A_TITLE(t):
    r'<title>'
    global formato_imp, formato_sec, formato_inf
    if formato_inf:
        window.file.write(" ")
    else:
        if formato_imp:
            window.file.write("<h3>")
        else:
            if formato_sec:
                window.file.write("<h2>")
            else:
                window.file.write("<h1>")
    return t


def t_C_TITLE(t):
    r'</title>'
    global formato_imp, formato_sec, formato_inf
    if formato_inf:
        window.file.write(" ")
    else:
        if formato_imp:
            window.file.write("</h3>")
        else:
            if formato_sec:
                window.file.write("</h2>")
            else:
                window.file.write("</h1>")
    return t


def t_A_ADDRESS(t):
    r'<address>'
    return t


def t_C_ADDRESS(t):
    r'</address>'
    return t


def t_A_STREET(t):
    r'<street>'
    return t


def t_C_STREET(t):
    r'</street>'
    return t


def t_A_CITY(t):
    r'<city>'
    return t


def t_C_CITY(t):
    r'</city>'
    return t


def t_A_STATE(t):
    r'<state>'
    return t


def t_C_STATE(t):
    r'</state>'
    return t


def t_A_PHONE(t):
    r'<phone>'
    return t


def t_C_PHONE(t):
    r'</phone>'
    return t


def t_A_DATE(t):
    r'<date>'
    return t


def t_C_DATE(t):
    r'</date>'
    return t


def t_A_EMAIL(t):
    r'<email>'
    return t


def t_C_EMAIL(t):
    r'</email>'
    return t


def t_A_AUTHOR(t):
    r'<author>'
    return t


def t_C_AUTHOR(t):
    r'</author>'
    return t


def t_A_FNAME(t):
    r'<firstname>'
    return t


def t_C_FNAME(t):
    r'</firstname>'
    return t


def t_A_SNAME(t):
    r'<surname>'
    return t


def t_C_SNAME(t):
    r'</surname>'
    return t


def t_A_COPY(t):
    r'<copyright>'
    return t


def t_C_COPY(t):
    r'</copyright>'
    return t


def t_A_YEAR(t):
    r'<year>'
    return t


def t_C_YEAR(t):
    r'</year>'
    return t


def t_A_HOLDER(t):
    r'<holder>'
    return t


def t_C_HOLDER(t):
    r'</holder>'
    return t


def t_A_SECT(t):
    r'<section>'
    global formato_sec
    formato_sec = True
    window.file.write("<section>")
    return t


def t_C_SECT(t):
    r'</section>'
    global formato_sec
    formato_sec = False
    window.file.write("</section>")
    return t


def t_A_SIMSECT(t):
    r'<simplesect>'
    global formato_sec
    formato_sec = True
    window.file.write("<section>")
    return t


def t_C_SIMSECT(t):
    r'</simplesect>'
    global formato_sec
    formato_sec = False
    window.file.write("</section>")
    return t


def t_A_ABSTRACT(t):
    r'<abstract>'
    global formato_imp
    formato_imp = True
    return t


def t_C_ABSTRACT(t):
    r'</abstract>'
    global formato_imp
    formato_imp = False
    return t


def t_A_PARA(t):
    r'<para>'
    global formato_inf
    if formato_inf:
        window.file.write(" ")
    else:
        window.file.write("<p>")
    return t


def t_C_PARA(t):
    r'</para>'
    global formato_inf
    if formato_inf:
        window.file.write(" ")
    else:
        window.file.write("</p>")
    return t


def t_A_SIMPARA(t):
    r'<simpara>'
    global formato_inf
    if formato_inf:
        window.file.write(" ")
    else:
        window.file.write("<p>")
    return t


def t_C_SIMPARA(t):
    r'</simpara>'
    global formato_inf
    if formato_inf:
        window.file.write(" ")
    else:
        window.file.write("</p>")
    return t

# La  etiqueta important no tiene un igual en html, por lo que se decidio usar aside por sus mayor parecido


def t_A_IMPORT(t):
    r'<important>'
    global formato_imp
    formato_imp = True
    formato2 = """<aside style="background-color: red"><font color = "white"> """
    window.file.write(formato2)
    return t


def t_C_IMPORT(t):
    r'</important>'
    global formato_imp
    formato_imp = False
    window.file.write("\n</font>\n</aside>")
    return t

# Decidimos usar Negrita por razones estéticas


def t_A_COMMENT(t):
    r'<comment>'
    return t


def t_C_COMMENT(t):
    r'</comment>'
    return t


def t_A_EMPHA(t):
    r'<emphasis>'
    return t


def t_C_EMPHA(t):
    r'</emphasis>'
    return t


def t_C_MEDIABRACKET(t):
    r'/>'
    window.file.write(">")
    return t


def t_A_MEDIA(t):
    r'<mediaobject>'
    global formato_media
    formato_media = True
    return t


def t_C_MEDIA(t):
    r'</mediaobject>'
    global formato_media
    formato_media = False
    return t


def t_A_IMAGE(t):
    r'<imageobject>'
    return t


def t_C_IMAGE(t):
    r'</imageobject>'
    return t


def t_A_IMAGED(t):
    r'<imagedata\s+window.fileref='
    formatoimg = '''<img src='''
    window.file.write(formatoimg)
    return t


def t_A_VIDEO(t):
    r'<videoobject>'
    window.file.write("<video>")
    return t


def t_C_VIDEO(t):
    r'</videoobject>'
    window.file.write("</video>")
    return t


def t_A_VIDEOD(t):
    r'<videodata\s+window.fileref='
    formatovid = '''<source src='''
    window.file.write(formatovid)
    return t


def t_URL(t):  # ACEPTA URLS ABSOLUTAS
    r'\"(http|https|ftp|ftps)://[^/\s:]+(:\d+)?(/[^#\s]*)?(\#\S*)?\"'
    window.file.write(t.value)
    return t


def t_MURL(t):
    r'\"([\/*[a-zA-Z0-9]*\.(gif|jpg|jpeg|png|bmp|svg|mp4|avi|mov)?)\"'
    window.file.write(t.value)
    return t


def t_A_LINK(t):
    r'<link\s+xlink:href= '
    formato3 = """<a href= """
    window.file.write(formato3)
    return t


def t_C_URLLINK(t):
    r' >'
    formato4 = """ > """
    window.file.write(formato4)
    return t


def t_C_LINK(t):
    r'</link>'
    window.file.write("</a>")
    return t


def t_A_ILIST(t):
    r'<itemizedlist>'
    window.file.write("<ul>")
    return t


def t_C_ILIST(t):
    r'</itemizedlist>'
    window.file.write("</ul>")
    return t


def t_A_ITEM(t):
    r'<listitem>'
    window.file.write("<li>")
    return t


def t_C_ITEM(t):
    r'</listitem>'
    window.file.write("</li>")
    return t


def t_A_TABLE(t):
    r'<informaltable>'
    formato5 = '''<table style="border: black 2px solid;">'''
    window.file.write(formato5)
    return t


def t_C_TABLE(t):
    r'</informaltable>'
    window.file.write("</table>")
    return t


def t_A_TGROUP(t):
    r'<tgroup>'
    return t


def t_C_TGROUP(t):
    r'</tgroup>'
    return t


def t_A_THEAD(t):
    r'<thead>'
    global formato_head
    formato_head = True
    window.file.write("<thead>")
    return t


def t_C_THEAD(t):
    r'</thead>'
    global formato_head
    formato_head = False
    window.file.write("</thead>")
    return t


def t_A_TFOOT(t):
    r'<tfoot>'
    global formato_foot
    formato_foot = True
    window.file.write("<tfoot>")
    return t


def t_C_TFOOT(t):
    r'</tfoot>'
    global formato_foot
    formato_foot = False
    window.file.write("</tfoot>")
    return t


def t_A_TBODY(t):
    r'<tbody>'
    global formato_body
    formato_body = True
    window.file.write("<tbody>")
    return t


def t_C_TBODY(t):
    r'</tbody>'
    global formato_body
    formato_body = False
    window.file.write("</tbody>")
    return t


def t_A_ROW(t):
    r'<row>'
    window.file.write("<tr>")
    return t


def t_C_ROW(t):
    r'</row>'
    window.file.write("</tr>")
    return t


def t_A_ENTRYTBL(t):
    r'<entrytbl>'
    return t


def t_C_ENTRYTBL(t):
    r'</entrytbl>'
    return t


# No encontramos la exacta equivalente en HTML
def t_A_ENTRY(t):
    r'<entry>'
    global formato_body, formato_foot, formato_head
    formato6 = ''' <td style="border: black 1px solid;"> '''
    formato7 = ''' <th style="border: black 1px solid;"> '''
    if formato_foot:
        window.file.write(formato6)
    else:
        if formato_body:
            window.file.write(formato6)
        else:
            window.file.write(formato7)
    return t


def t_C_ENTRY(t):
    r'</entry>'
    global formato_body, formato_foot, formato_head

    if formato_foot:
        window.file.write('</td>')
    else:
        if formato_body:
            window.file.write('</td>')
        else:
            window.file.write('</th>')
    return t


def t_TAB(t):
    r'\t'
    window.file.write("\t")
    pass


def t_ESPACIO(t):
    r'\ '
    window.file.write(" ")
    pass


t_ignore = '\r'


def t_TEXT(t):
    r'[^<>]+'
    window.file.write(t.value)
    return t

# Control de errores de caracteres inválidos


def t_error(t):
    t.lexer.skip(1)


# Control de errores de token mal escrito
def t_ERROR(t):
    # esta expresion regular toma una cadena que comience por < seguida por caracteres que no sean >, termina en >,
    # si no hay ningun otro token que cumpla la condicion sera marcado como ERROR
    r'<[^>]+>'
    window.output_text.insertPlainText(
        f"Error léxico: Token mal escrito {t.value}\n")
    return t


# Construir Lexer
lexer = lex.lex()

# PARSER
# MAYUSCULA TERMINALES (TOKENS) minuscula no terminales


def p_sigma(p):
    '''sigma : DOC A_ARTICLE info title cont C_ARTICLE
    | DOC A_ARTICLE title cont C_ARTICLE
    | DOC A_ARTICLE info cont C_ARTICLE
    | DOC A_ARTICLE cont C_ARTICLE '''


def p_info(p):
    '''info : A_INFO dtinfo C_INFO '''


def p_dtinfo(p):
    '''dtinfo : title
       | author
       | abstract
       | abstract dtinfo
       | media
       | media dtinfo
       | title dtinfo
       | author dtinfo
       | address
       | copy
       | date
       | address dtinfo
       | copy dtinfo
       | date dtinfo '''


def p_title(p):
    '''title : A_TITLE  tlt C_TITLE '''


def p_tlt(p):
    '''tlt : TEXT
    | empha
    | link
    | email
    | TEXT tlt
    | empha tlt
    | link tlt
    | email tlt '''


def p_empha(p):
    '''empha : A_EMPHA sp C_EMPHA '''


def p_sp(p):
    ''' sp : TEXT sp
    | link sp
    | email sp
    | empha sp
    | comment sp
    | author sp
    | TEXT
    | link
    | email
    | empha
    | comment
    | author  '''


def p_link(p):
    '''link : A_LINK URL C_URLLINK sp C_LINK
     | A_LINK MURL C_URLLINK sp C_LINK '''


def p_email(p):
    '''email : A_EMAIL nm C_EMAIL '''


def p_nm(p):
    '''nm : TEXT
    | link
    | empha
    | comment
    | TEXT nm
    | link nm
    | empha nm
    | comment nm '''


def p_comment(p):
    '''comment : A_COMMENT sp C_COMMENT '''


def p_author(p):
    '''author : A_AUTHOR names C_AUTHOR '''


def p_names(p):
    '''names : fname
    | sname
    | fname names'''


def p_fname(p):
    '''fname : A_FNAME nm C_FNAME '''


def p_sname(p):
    '''sname : A_SNAME nm C_SNAME '''


def p_address(p):
    '''address : A_ADDRESS contad C_ADDRESS'''


def p_contad(p):
    '''contad : TEXT
        | street
        | city
        | state
        | street contad
        | city contad
        | state contad
        | phone
        | email
        | TEXT contad
        | phone contad
        | email contad '''


def p_street(p):
    '''street : A_STREET nm C_STREET '''


def p_city(p):
    '''city : A_CITY nm C_CITY '''


def p_state(p):
    '''state : A_STATE nm C_STATE '''


def p_phone(p):
    '''phone : A_PHONE nm C_PHONE '''


def p_copy(p):
    '''copy : A_COPY year holder C_COPY
    | A_COPY year C_COPY '''


def p_year(p):
    '''year : A_YEAR nm C_YEAR
        | A_YEAR nm C_YEAR year'''


def p_holder(p):
    '''holder : A_HOLDER nm C_HOLDER
    | A_HOLDER nm C_HOLDER holder '''


def p_date(p):
    '''date : A_DATE nm C_DATE'''


def p_cont(p):
    '''cont : data sections
    | data '''


def p_data(p):
    '''data : simpara
    | para
    | ilist
    | table
    | media
    | import
    | abstract
    | comment
    | simpara data
    | para data
    | ilist data
    | table data
    | media data
    | import data
    | abstract data
    | comment data '''


def p_simpara(p):
    '''simpara : A_SIMPARA sp C_SIMPARA '''


def p_para(p):
    '''para : A_PARA dtp C_PARA '''


def p_dtp(p):
    '''dtp : TEXT dtp
        | empha dtp
        | link dtp
        | email dtp
        | author dtp
        | comment dtp
        | ilist dtp
        | import dtp
        | table dtp
        | media dtp
        | TEXT
        | empha
        | link
        | email
        | author
        | comment
        | ilist
        | import
        | table
        | media '''

# <(￣︶￣)>


def p_ilist(p):
    '''ilist : A_ILIST item C_ILIST  '''


def p_item(p):
    '''item : A_ITEM dlist C_ITEM
    | A_ITEM dlist C_ITEM item '''


def p_dlist(p):
    '''dlist : import
    | para
    | simpara
    | ilist
    | table
    | media
    | comment
    | abstract
    | address
    | address dlist
    | import dlist
    | para dlist
    | simpara dlist
    | ilist dlist
    | table dlist
    | media dlist
    | comment dlist
    | abstract dlist '''


def p_import(p):
    '''import : A_IMPORT title data C_IMPORT
        | A_IMPORT  data C_IMPORT '''

# (っ˘̩╭╮˘̩)っ


def p_table(p):
    '''table : A_TABLE tabdata C_TABLE '''


def p_tabdata(p):
    '''tabdata : media tabdata
        | tgroup tabdata
        | tgroup
        | media '''


def p_media(p):
    '''media : A_MEDIA info extramedia C_MEDIA
    | A_MEDIA extramedia C_MEDIA '''


def p_extramedia(p):
    '''extramedia : video extramedia
        | image extramedia
        | image
        | video   '''


def p_video(p):
    '''video : A_VIDEO info A_VIDEOD URL C_MEDIABRACKET  C_VIDEO
    | A_VIDEO info A_VIDEOD MURL C_MEDIABRACKET  C_VIDEO
    | A_VIDEO  A_VIDEOD MURL C_MEDIABRACKET  C_VIDEO
    | A_VIDEO  A_VIDEOD URL C_MEDIABRACKET  C_VIDEO '''


def p_image(p):
    '''image : A_IMAGE info  A_IMAGED URL C_MEDIABRACKET C_IMAGE
    | A_IMAGE info  A_IMAGED MURL C_MEDIABRACKET C_IMAGE
    | A_IMAGE  A_IMAGED MURL C_MEDIABRACKET C_IMAGE
    | A_IMAGE  A_IMAGED URL C_MEDIABRACKET C_IMAGE '''


def p_tgroup(p):
    '''tgroup : A_TGROUP  thead tbody tfoot C_TGROUP
    | A_TGROUP  tbody  tfoot C_TGROUP
    | A_TGROUP  thead tbody  C_TGROUP
    | A_TGROUP  tbody  C_TGROUP '''


def p_thead(p):
    ''' thead : A_THEAD row C_THEAD'''


def p_row(p):
    '''row : A_ROW entry C_ROW row
    | A_ROW entrytbl C_ROW row
    | A_ROW entrytbl C_ROW
    | A_ROW entry C_ROW '''


def p_entry(p):
    '''entry : A_ENTRY dent C_ENTRY
    | A_ENTRY dent C_ENTRY entry
    | A_ENTRY dent C_ENTRY entrytbl '''


def p_dent(p):
    ''' dent : TEXT dent
    | ilist dent
    | import dent
    | para dent
    | simpara dent
    | media dent
    | comment dent
    | abstract dent
    | TEXT
    | ilist
    | import
    | para
    | simpara
    | media
    | comment
    | abstract '''


def p_abstract(p):
    '''abstract : A_ABSTRACT title dabs C_ABSTRACT
    | A_ABSTRACT dabs C_ABSTRACT'''


def p_dabs(p):
    ''' dabs : para dabs
    | simpara dabs
    | para
    | simpara '''


def p_entrytbl(p):
    '''entrytbl : A_ENTRYTBL thead tbody C_ENTRYTBL
    | A_ENTRYTBL thead tbody C_ENTRYTBL entry
    | A_ENTRYTBL thead tbody C_ENTRYTBL entrytbl'''


def p_tbody(p):
    ''' tbody : A_TBODY row C_TBODY '''


def p_tfoot(p):
    '''tfoot : A_TFOOT row C_TFOOT'''


def p_sections(p):
    ''' sections : sect sections
    | simsect sections
    | sect
    | simsect  '''


def p_sect(p):
    '''sect : A_SECT info title cont C_SECT
    | A_SECT info cont C_SECT
    | A_SECT title cont C_SECT
    | A_SECT cont C_SECT '''


def p_simsect(p):
    '''simsect : A_SIMSECT info title data C_SIMSECT
    | A_SIMSECT  title data C_SIMSECT
    | A_SIMSECT  info data C_SIMSECT
    | A_SIMSECT   data C_SIMSECT '''


def p_error(p):
    if p:
        window.output_text.insertPlainText(f"Error de sintaxis en línea {
            p.lineno}. Culpable: {p.value}\n")
        parser.errok()
        window.errores += 1
    else:
        window.output_text.insertPlainText("Fin del Archivo\n")


# ¬(;_;)¬

# construir el parser
# Esto para evitar que los warnings impidan la ejecucion del exe
parser = yacc.yacc(errorlog=yacc.NullLogger())

# Interfaz Gráfica

# Variables de Direccionamiento para trabajar con las imágenes y Archivos
exe_dir = os.getcwd()
rel_path = os.path.join("icons", "")
test_rel = 'prueba'
testdir = (os.path.split(exe_dir))[0]
test_path = os.path.join(testdir, test_rel)
abs_path = os.path.join(exe_dir, rel_path)

# Color de la barra de número de Línea
lineBarColor = QColor("#68A289")
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
        self.xml_Name = "ARTICULO.xml"
        self.codigo = ""
        self.errores = 0
        # Crear Titulo y Ícono
        self.setWindowTitle("Analizador Léxico Sintáctico")
        self.setIconSize(QSize(256, 256))
        self.setWindowIcon(QIcon(os.path.join(abs_path+'Lp.ico')))
        self.setMinimumSize(QSize(1280, 720))
        self.setStyleSheet('''QMainWindow{
            background-color: rgb(110,189,171);
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
            background-color: gray;
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
            QIcon(os.path.join(abs_path+'Correr_Analisis.png')), "Correr", self)
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

        b_GuardarXML = QAction(
            QIcon(os.path.join(abs_path+'ImprimirXML.png')), "Guardar XML", self)
        b_GuardarXML.setStatusTip("Crea un archivo xml del editor")
        b_GuardarXML.triggered.connect(self.guardar)
        toolbar.addAction(b_GuardarXML)
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
        self.xml_name, _ = dlg.getOpenFileName(
            self, "Seleccionar artículo", str(test_path), "XML Files (*.xml);;All Files (*)")

        if not self.xml_name.endswith(".xml"):
            error = QMessageBox.critical(
                self, 'Error de Archivo', 'Archivo con extensión incorrecta', QMessageBox.StandardButton.Close)

            if error == QMessageBox.StandardButton.Close:
                pass
        else:
            self.input_text.clear()
            self.output_text.clear()
            with open(self.xml_name, "r", encoding="utf-8") as archivo:
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
            self.file = open(self.xml_name.replace(".xml", ".html"), "w")
            lexer.lineno = 1
            parser.parse(self.codigo)
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
        nuevoXML = self.input_text.toPlainText()
        with open(self.xml_name.replace(".xml", " Modificado.xml"), "w") as f:
            f.write(nuevoXML)

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

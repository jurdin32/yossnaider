# -*- coding: utf-8 -*-
import datetime
import os

from arrow import utcnow, get
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import black, purple, white
from reportlab.pdfgen import canvas


# ======================= CLASE reportePDF =========================

class reportePDF(object):
    """Exportar una lista de diccionarios a una tabla en un
       archivo PDF."""

    def __init__(self, titulo, cabecera, datos, nombrePDF):
        super(reportePDF, self).__init__()

        self.titulo = str.upper(titulo)
        self.cabecera = cabecera
        self.datos = datos
        self.nombrePDF = nombrePDF

        self.estilos = getSampleStyleSheet()
        self.estilos.add(ParagraphStyle(name='Normal2',
                           fontSize=8,
                           leading=8)
        )

    @staticmethod
    def _encabezadoPiePagina(canvas, archivoPDF):
        """Guarde el estado de nuestro lienzo para que podamos aprovecharlo"""

        canvas.saveState()
        estilos = getSampleStyleSheet()

        alineacion = ParagraphStyle(name="alineacion", alignment=TA_RIGHT,
                                    parent=estilos["Normal"])

        # Encabezado


        # Pie de página
        fecha = utcnow().to("local").format("dddd, DD - MMMM - YYYY", locale="es")
        fechaReporte = fecha.replace("-", "de")
        piePagina = Paragraph(fechaReporte, estilos["Normal"])

        anchura, altura = piePagina.wrap(archivoPDF.width, archivoPDF.bottomMargin)
        piePagina.drawOn(canvas, archivoPDF.leftMargin, 15 * mm + (0.2 * inch))

        # Suelta el lienzo
        canvas.restoreState()

    def convertirDatos(self):
        """Convertir la lista de diccionarios a una lista de listas para crear
           la tabla PDF."""

        estiloEncabezado = ParagraphStyle(name="estiloEncabezado", alignment=TA_CENTER,
                                          fontSize=10, textColor=white,
                                          fontName="Helvetica-Bold",
                                          parent=self.estilos["Normal"])

        estiloNormal = self.estilos["Normal2"]
        estiloNormal.alignment = TA_LEFT

        claves, nombres = zip(*[[k, n] for k, n in self.cabecera])

        encabezado = [Paragraph(nombre, estiloEncabezado) for nombre in nombres]
        nuevosDatos = [tuple(encabezado)]

        for dato in self.datos:
            nuevosDatos.append([Paragraph(str(dato[clave]), estiloNormal) for clave in claves])

        return nuevosDatos

    def Exportar(self):
        """Exportar los datos a un archivo PDF."""

        alineacionTitulo = ParagraphStyle(name="centrar", alignment=TA_CENTER, fontSize=13,
                                          leading=10, textColor="#21618C",
                                          parent=self.estilos["Heading1"])

        self.ancho, self.alto = A4

        convertirDatos = self.convertirDatos()


        # tabla = Table(convertirDatos, colWidths=(self.ancho - 100) / len(self.cabecera), hAlign="CENTER")
        tabla=Table(convertirDatos)
        tabla.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), "#21618C"),
            ("ALIGN", (0, 0), (0, -1), "LEFT"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),  # Texto centrado y alineado a la izquierda
            ("INNERGRID", (0, 0), (-1, -1), 0.50, black),  # Lineas internas
            ("BOX", (0, 0), (-1, -1), 0.25, black),  # Linea (Marco) externa
        ]))

        historia = []
        historia.append(Paragraph(self.titulo, alineacionTitulo))
        historia.append(Spacer(1, 0.16 * inch))
        historia.append(tabla)

        archivoPDF = SimpleDocTemplate(self.nombrePDF, leftMargin=50, rightMargin=50, pagesize=A4,
                                       title="Reporte PDF", author="YOSSNAIDER")

        try:
            archivoPDF.build(historia, onFirstPage=self._encabezadoPiePagina,
                             onLaterPages=self._encabezadoPiePagina,
                             canvasmaker=numeracionPaginas)

            # +------------------------------------+
            return "Reporte generado con éxito."
        # +------------------------------------+
        except PermissionError:
            # +--------------------------------------------+
            return "Error inesperado: Permiso denegado."
        # +--------------------------------------------+


# ================== CLASE numeracionPaginas =======================

class numeracionPaginas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """Agregar información de la página a cada página (página x de y)"""
        numeroPaginas = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(numeroPaginas)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, conteoPaginas):
        self.drawRightString(204 * mm, 15 * mm + (0.2 * inch),
                             "Página {} de {}".format(self._pageNumber, conteoPaginas))

    # ===================== FUNCIÓN generarReporte =====================

def generarReporte(datos=[],titulo="",encabezados=(),nombrePDF=""):
    cabecera = (encabezados)
    ruta=os.path.dirname(__file__).replace("Productos","Reportes\\")+(nombrePDF+".pdf")
    if (os.path.exists(ruta)):
        hora=str(datetime.datetime.now().hour)+"-"+str(datetime.datetime.now().minute)+"-"+str(datetime.datetime.now().second)+"-"+str(datetime.datetime.now().second/1000).replace(".","")
        print("El Archivo ya existe,hora:",hora)
        ruta = os.path.dirname(__file__).replace("Productos", "Reportes\\") + (nombrePDF +"-"+hora+ ".pdf")

    nombrePDF = ruta
    print(datos,cabecera)
    reporte = reportePDF(titulo, cabecera, datos, nombrePDF).Exportar()
    os.popen(nombrePDF)
    return ruta
import os
import tempfile
from typing import List

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from fpdf import FPDF

from . import progress

MM_2_PT = 595 / 210
A4 = (210 * MM_2_PT, 297 * MM_2_PT)


class Margin:
    top: float
    bottom: float
    left: float
    right: float

    def __init__(self, top=0, bottom=0, left=0, right=0, all=None) -> None:
        if all is not None:
            self.top = all * MM_2_PT
            self.bottom = all * MM_2_PT
            self.left = all * MM_2_PT
            self.right = all * MM_2_PT
        else:
            self.top = top * MM_2_PT
            self.bottom = bottom * MM_2_PT
            self.left = left * MM_2_PT
            self.right = right * MM_2_PT


class Position:
    x: float
    y: float
    size: property

    def __init__(self, pageBox: property, h_align: str, v_align: str, margin: Margin) -> None:
        area_x = float(pageBox.getWidth()) - margin.left - margin.right
        area_y = float(pageBox.getHeight()) - margin.bottom - margin.top
        self.x = area_x * {'right': 1.0, 'center': 0.5, 'left': 0.0}.get(h_align) + margin.left
        self.y = area_y * {'top': 0.0, 'center': 0.5, 'bottom': 1.0}.get(v_align) + margin.bottom
        self.size = pageBox


def paged_pdf_writer(file: str, h_align: str, v_align: str, margin: Margin, font: str, font_size: int, format: str, add_blank) -> PdfFileWriter:
    pdf = PdfFileReader(file)
    output = PdfFileWriter()

    def paged_plain_pdf(text: str, position: Position) -> PdfFileReader:
        _, temp = tempfile.mkstemp()

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font(font, size=font_size)
        pdf.text(position.x / MM_2_PT, position.y / MM_2_PT, txt=text)
        pdf.output(temp, dest='F')

        new_pdf = PdfFileReader(temp)
        os.remove(temp)

        return new_pdf

    bar = progress.bar(range(pdf.getNumPages()), label="{} ".format(file), width=32)

    for i in bar:
        page = pdf.getPage(i)
        position = Position(page.mediaBox, h_align, v_align, margin)
        new_pdf = paged_plain_pdf(format.format(i + 1), position)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

    if add_blank:
        if not pdf.getNumPages() % 2 == 0:
            output.addBlankPage(A4)

    return output


def paged_pdfs_writer(files: List[str], h_align: str, v_align: str, margin: Margin, font: str, font_size: int, format: str, add_blank) -> List[PdfFileWriter]:
    outputs = []
    for i, file in enumerate(files):
        reformat = format.format(i, "{}")
        output = paged_pdf_writer(file, h_align, v_align, margin, font, font_size, reformat, add_blank)
        outputs.append(output)
    return outputs


def concat_pdfs_merger(paths) -> PdfFileMerger:
    merger = PdfFileMerger()
    for path in paths:
        merger.append(path)
    return merger

#!/usr/bin/env python3
"""Generate Mozone AI Research Paper — 55-page professional PDF using reportlab."""
import os, sys

# Add the content modules path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)

# Colors
ACCENT = HexColor("#00CCD6")
DARK = HexColor("#0A0A1A")
TEXT_COLOR = HexColor("#1A1A2E")
MUTED = HexColor("#666680")
BORDER = HexColor("#D0D0E0")
WHITE = white

OUTPUT = os.path.join(SCRIPT_DIR, "..", "public", "mozone-ai-research-paper.pdf")

def get_styles():
    s = getSampleStyleSheet()
    defs = [
        ("MzCoverTitle", 32, 40, TA_CENTER, DARK, "Helvetica-Bold", 0, 8),
        ("MzCoverSub", 14, 20, TA_CENTER, MUTED, "Helvetica", 0, 6),
        ("MzCoverMeta", 10, 14, TA_CENTER, MUTED, "Helvetica", 0, 4),
        ("MzH1", 22, 28, TA_LEFT, DARK, "Helvetica-Bold", 24, 14),
        ("MzH2", 16, 22, TA_LEFT, DARK, "Helvetica-Bold", 18, 10),
        ("MzH3", 13, 18, TA_LEFT, HexColor("#1A1A3E"), "Helvetica-Bold", 14, 8),
        ("MzBody", 10.5, 16, TA_JUSTIFY, TEXT_COLOR, "Helvetica", 0, 8),
        ("MzBullet", 10.5, 16, TA_LEFT, TEXT_COLOR, "Helvetica", 0, 4),
        ("MzCaption", 9, 12, TA_CENTER, MUTED, "Helvetica-Oblique", 0, 12),
        ("MzRef", 9, 13, TA_LEFT, TEXT_COLOR, "Helvetica", 0, 3),
    ]
    for name, sz, ld, al, tc, fn, sb, sa in defs:
        s.add(ParagraphStyle(name=name, fontSize=sz, leading=ld, alignment=al,
                             textColor=tc, fontName=fn, spaceBefore=sb, spaceAfter=sa))
    # Bullet with indent
    s["MzBullet"].leftIndent = 20
    s["MzBullet"].bulletIndent = 8
    # Ref with hanging indent
    s["MzRef"].leftIndent = 20
    s["MzRef"].firstLineIndent = -20
    return s

def make_table(headers, rows, col_widths=None):
    data = [headers] + rows
    if not col_widths:
        col_widths = [460 / len(headers)] * len(headers)
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#F0F2F5")),
        ("TEXTCOLOR", (0, 0), (-1, 0), DARK),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 9),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 8.5),
        ("LEADING", (0, 0), (-1, -1), 12),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, HexColor("#FAFBFC")]),
    ]))
    return t

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceAfter=12, spaceBefore=6)

def b(text): return f"<b>{text}</b>"
def i(text): return f"<i>{text}</i>"

def build_pdf():
    s = get_styles()
    story = []

    # Import all content sections
    from pdf_sections import (
        add_cover, add_toc, add_section1, add_section2, add_section3,
        add_section4, add_section5, add_section6, add_section7,
        add_section8, add_section9, add_section10, add_section11, add_section12
    )

    add_cover(story, s)
    add_toc(story, s)
    add_section1(story, s, make_table, hr)
    add_section2(story, s, make_table, hr)
    add_section3(story, s, make_table, hr)
    add_section4(story, s, make_table, hr)
    add_section5(story, s, make_table, hr)
    add_section6(story, s, make_table, hr)
    add_section7(story, s, make_table, hr)
    add_section8(story, s, make_table, hr)
    add_section9(story, s, make_table, hr)
    add_section10(story, s, make_table, hr)
    add_section11(story, s, make_table, hr)
    add_section12(story, s, make_table, hr)

    # Page number callback
    def add_page_number(canvas, doc):
        if doc.page > 2:  # Skip cover + TOC
            canvas.saveState()
            canvas.setFont("Helvetica", 8)
            canvas.setFillColor(MUTED)
            canvas.drawCentredString(A4[0]/2, 20*mm, f"Mozone AI Research Paper — Page {doc.page}")
            canvas.restoreState()

    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        leftMargin=25*mm, rightMargin=25*mm,
        topMargin=25*mm, bottomMargin=30*mm
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(f"PDF generated: {OUTPUT} ({doc.page} pages)")

if __name__ == "__main__":
    build_pdf()

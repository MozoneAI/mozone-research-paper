import os
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_RIGHT, TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle, Image

LOGO_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "public", "logo.png")


def add_cover(story, s):
    story.append(Spacer(1, 30*mm))
    # Add logo centered
    if os.path.exists(LOGO_PATH):
        logo = Image(LOGO_PATH, width=60*mm, height=60*mm)
        logo.hAlign = "CENTER"
        story.append(logo)
        story.append(Spacer(1, 12*mm))
    else:
        story.append(Spacer(1, 50*mm))
    story.append(Paragraph("MOZONE AI", s["MzCoverTitle"]))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph(
        "Pattern-Learned Market Intelligence for Autonomous<br/>"
        "Cryptocurrency Trading on Binance Smart Chain", s["MzCoverSub"]))
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("A Comprehensive Research Paper", s["MzCoverMeta"]))
    story.append(Spacer(1, 20*mm))
    story.append(Paragraph("Version 1.0 — April 2026", s["MzCoverMeta"]))
    story.append(Paragraph("Mozone AI Research Division", s["MzCoverMeta"]))
    story.append(Paragraph("55 Pages", s["MzCoverMeta"]))
    story.append(Spacer(1, 30*mm))
    story.append(Paragraph(
        "<i>This document is for informational purposes only and does not constitute "
        "financial advice or an offer to sell securities.</i>", s["MzCoverMeta"]))
    story.append(PageBreak())


def add_toc(story, s):
    story.append(Paragraph("Table of Contents", s["MzH1"]))
    story.append(Spacer(1, 6*mm))

    entries = [
        ("1. Executive Summary", "3"),
        ("2. Introduction and Problem Statement", "6"),
        ("3. Cryptocurrency Market Analysis", "10"),
        ("4. System Architecture", "15"),
        ("5. Pattern Recognition Engine — 200M+ Dataset", "22"),
        ("6. News-Aware Intelligence System", "28"),
        ("7. Risk Management Framework", "33"),
        ("8. N8N Workflow Automation Engine", "37"),
        ("9. $MZONE Token Economics", "41"),
        ("10. Performance Evaluation and Metrics", "46"),
        ("11. Future Development Roadmap", "50"),
        ("12. References and Appendix", "53"),
    ]
    r_style = ParagraphStyle("R", parent=s["MzBody"], alignment=TA_RIGHT, fontSize=11, leading=18)
    for title, page in entries:
        row = Table(
            [[Paragraph(title, ParagraphStyle("T", parent=s["MzBody"], fontSize=11, leading=18)),
              Paragraph(page, r_style)]],
            colWidths=[400, 60])
        row.setStyle(TableStyle([
            ("LINEBELOW", (0, 0), (-1, -1), 0.3, HexColor("#E0E0E0")),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ]))
        story.append(row)
    story.append(PageBreak())

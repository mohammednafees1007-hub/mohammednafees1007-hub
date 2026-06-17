from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    FrameBreak,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "Mohammed_Nafees_H_Resume.pdf"


CONTACT = (
    '+91 962-946-1267 | mohammednafees1007@gmail.com | '
    'Kumbakonam, Tamil Nadu, India | '
    'LinkedIn: https://www.linkedin.com/in/mohammed-nafees-h-7b3377306 | '
    'GitHub: https://github.com/mohammednafees1007-hub'
)


def p(text, style):
    return Paragraph(text, style)


def bullet(text, style):
    return Paragraph(f"- {text}", style)


def make_doc():
    margin = 0.43 * inch
    doc = BaseDocTemplate(
        str(OUT),
        pagesize=letter,
        leftMargin=margin,
        rightMargin=margin,
        topMargin=0.35 * inch,
        bottomMargin=0.35 * inch,
        title="Mohammed Nafees H Resume",
        author="Mohammed Nafees H",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="one", frames=[frame])])
    return doc


def styles():
    base = "Helvetica"
    return {
        "name": ParagraphStyle(
            "name",
            fontName="Helvetica-Bold",
            fontSize=17,
            leading=18,
            alignment=1,
            textColor=colors.HexColor("#111827"),
            spaceAfter=1,
        ),
        "headline": ParagraphStyle(
            "headline",
            fontName=base,
            fontSize=8.4,
            leading=9.5,
            alignment=1,
            textColor=colors.HexColor("#374151"),
            spaceAfter=2,
        ),
        "contact": ParagraphStyle(
            "contact",
            fontName=base,
            fontSize=7.2,
            leading=8.2,
            alignment=1,
            textColor=colors.HexColor("#1f2937"),
            spaceAfter=6,
        ),
        "section": ParagraphStyle(
            "section",
            fontName="Helvetica-Bold",
            fontSize=8.7,
            leading=9.6,
            textColor=colors.HexColor("#0f766e"),
            spaceBefore=4,
            spaceAfter=2,
        ),
        "body": ParagraphStyle(
            "body",
            fontName=base,
            fontSize=7.45,
            leading=8.55,
            textColor=colors.HexColor("#111827"),
            spaceAfter=2,
        ),
        "small": ParagraphStyle(
            "small",
            fontName=base,
            fontSize=7.15,
            leading=8.1,
            textColor=colors.HexColor("#111827"),
            spaceAfter=1.5,
        ),
        "item": ParagraphStyle(
            "item",
            fontName="Helvetica-Bold",
            fontSize=7.75,
            leading=8.6,
            textColor=colors.HexColor("#111827"),
            spaceBefore=1.5,
            spaceAfter=1,
        ),
    }


def build():
    s = styles()
    story = [
        p("MOHAMMED NAFEES H", s["name"]),
        p("Robotics, Embedded Systems, and AI/CV Engineering Student", s["headline"]),
        p(CONTACT, s["contact"]),
        p("PROFESSIONAL SUMMARY", s["section"]),
        p(
            "B.Tech Robotics & Artificial Intelligence student at SASTRA University, "
            "Class of 2028, building practical systems across robotics software, "
            "embedded hardware, and computer vision. Hands-on project work includes "
            "Arduino-Python autonomous navigation, YOLO/OpenCV/Keras fruit grading, "
            "and backend image-analysis pipelines with structured app-ready output.",
            s["body"],
        ),
        p("EDUCATION", s["section"]),
        p(
            "<b>SASTRA Deemed University</b> | B.Tech, Robotics & Artificial Intelligence | "
            "Aug 2024 - May 2028 | Tamil Nadu, India",
            s["body"],
        ),
        p("TECHNICAL SKILLS", s["section"]),
        p(
            "<b>Robotics Software:</b> ROS 2, Python, C/C++, Linux/Ubuntu, Git, "
            "A* path planning, controls basics, robot integration, sensor debugging",
            s["small"],
        ),
        p(
            "<b>Embedded Hardware:</b> Arduino, ESP32, STM32, Raspberry Pi 5, "
            "Raspberry Pi Zero 2 W, Pi Camera, GPIO, motor drivers, encoders, IR sensors",
            s["small"],
        ),
        p(
            "<b>AI & Computer Vision:</b> OpenCV, YOLOv8, Ultralytics, TensorFlow/Keras, "
            "CLIP, BLIP, Hugging Face Transformers, image classification, object detection",
            s["small"],
        ),
        p(
            "<b>Hardware & Tools:</b> I2C, UART, LiDAR, IMU, soldering, schematic reading, "
            "hardware bring-up, VS Code, CoppeliaSim, Fusion 360, EasyEDA/KiCad basics",
            s["small"],
        ),
        p("EXPERIENCE", s["section"]),
        p(
            "Industrial Robotics Engineering Project | Robotics Engineering Contributor | "
            "ROS 2, Controls, Embedded Integration",
            s["item"],
        ),
        bullet(
            "Contribute to ROS 2 based robotics workflows, controls-oriented development, "
            "embedded integration, sensor/actuator evaluation, and hardware coordination "
            "under professional constraints.",
            s["small"],
        ),
        bullet(
            "Coordinate component identification, evaluation, and procurement support for "
            "a project hardware budget of approximately Rs. 10 lakh while keeping project "
            "details confidential.",
            s["small"],
        ),
        p("PROJECTS", s["section"]),
        p(
            "Hadi Al Hajatron | Arduino, Python, IR Sensors, Encoders, A* Path Planning",
            s["item"],
        ),
        p(
            "GitHub: https://github.com/mohammednafees1007-hub/Hadi-Al-Hajatron",
            s["small"],
        ),
        bullet(
            "Engineered a 4x4 Arduino-Python autonomous grid-navigation robot with "
            "3 IR obstacle sensors, 60 cm calibrated movement steps, live mapping, "
            "map export, and A* route planning.",
            s["small"],
        ),
        p(
            "FruitVision AI - Fruit Quality Detector for SMS | YOLOv8x, Keras, CLIP, OpenCV",
            s["item"],
        ),
        p(
            "GitHub: https://github.com/mohammednafees1007-hub/fruit-quality-detector-for-sms",
            s["small"],
        ),
        bullet(
            "Developed a quality-first fruit grading system with image input workflows, "
            "YOLOv8x fruit-region detection, a 3-class Keras quality model, CLIP fruit "
            "naming support, A/B/C grade mapping, and annotated result output.",
            s["small"],
        ),
        p(
            "AI Image Analyzer | Python, YOLOv8n, OpenCV, BLIP, Transformers",
            s["item"],
        ),
        p(
            "GitHub: https://github.com/mohammednafees1007-hub/ai-image-analyzer",
            s["small"],
        ),
        bullet(
            "Created a 3-stage backend image-analysis pipeline for a larger Visage "
            "project with YOLOv8n object detection, 13 allowed object classes, "
            "privacy-safe face tokens, BLIP captions, and structured app-ready output.",
            s["small"],
        ),
        p(
            "Quadruped Robot | Inverse Kinematics, Robotics Controls, Embedded Integration",
            s["item"],
        ),
        bullet(
            "Implemented inverse-kinematics motion logic for leg movement, connecting "
            "control theory with practical actuation for stable quadruped locomotion.",
            s["small"],
        ),
        p("LEADERSHIP AND ENGINEERING HIGHLIGHTS", s["section"]),
        bullet(
            "Robotics Club member at SASTRA Deemed University, active in robotics learning, "
            "project building, experimentation, and applied technical development.",
            s["small"],
        ),
        bullet(
            "Comfortable with Linux robotics environments, hardware bring-up, sensor debugging, "
            "serial communication, rapid prototyping, AI model integration, and deployment-oriented project work.",
            s["small"],
        ),
    ]
    make_doc().build(story)


if __name__ == "__main__":
    build()

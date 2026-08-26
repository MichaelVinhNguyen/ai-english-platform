# -*- coding: utf-8 -*-
"""
backend/exams/__init__.py – Modular Standardized Exam Suite for All Levels (A1, A2, B1, B2, C1, C2)
"""
from backend.exams.a1_exam import A1_STANDARDIZED_EXAM_DATA
from backend.exams.a2_exam import A2_STANDARDIZED_EXAM_DATA
from backend.seed_b1_exam_data import B1_STANDARDIZED_EXAM_DATA
from backend.exams.b2_exam import B2_STANDARDIZED_EXAM_DATA
from backend.exams.c1_exam import C1_STANDARDIZED_EXAM_DATA
from backend.exams.c2_exam import C2_STANDARDIZED_EXAM_DATA

ALL_LEVELS_FOUR_SKILL_EXAM_DATA = {
    "A1": A1_STANDARDIZED_EXAM_DATA,
    "A2": A2_STANDARDIZED_EXAM_DATA,
    "B1": B1_STANDARDIZED_EXAM_DATA,
    "B2": B2_STANDARDIZED_EXAM_DATA,
    "C1": C1_STANDARDIZED_EXAM_DATA,
    "C2": C2_STANDARDIZED_EXAM_DATA
}

__all__ = [
    "A1_STANDARDIZED_EXAM_DATA",
    "A2_STANDARDIZED_EXAM_DATA",
    "B1_STANDARDIZED_EXAM_DATA",
    "B2_STANDARDIZED_EXAM_DATA",
    "C1_STANDARDIZED_EXAM_DATA",
    "C2_STANDARDIZED_EXAM_DATA",
    "ALL_LEVELS_FOUR_SKILL_EXAM_DATA"
]

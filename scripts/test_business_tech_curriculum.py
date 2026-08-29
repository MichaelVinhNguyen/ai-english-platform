# -*- coding: utf-8 -*-
"""
test_business_tech_curriculum.py – Test Business and Tech curriculum and exam bank
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.seed_level_curriculum_data import LEVEL_CURRICULUM_DATA
from backend.routers.level_curriculum import EXAM_BANK_30_TESTS

def verify_business_and_tech():
    print("=================================================================")
    print("VERIFYING BUSINESS AND TECH CURRICULUM AND EXAM BANK")
    print("=================================================================")
    
    # 1. Check Level Curriculum Data
    assert "BUSINESS" in LEVEL_CURRICULUM_DATA, "BUSINESS missing in LEVEL_CURRICULUM_DATA"
    assert "TECH" in LEVEL_CURRICULUM_DATA, "TECH missing in LEVEL_CURRICULUM_DATA"
    
    biz_modules = LEVEL_CURRICULUM_DATA["BUSINESS"]["modules"]
    tech_modules = LEVEL_CURRICULUM_DATA["TECH"]["modules"]
    
    print(f"[+] BUSINESS Modules count: {len(biz_modules)} (Expected: 30)")
    print(f"[+] TECH Modules count: {len(tech_modules)} (Expected: 30)")
    assert len(biz_modules) == 30, f"BUSINESS modules expected 30, got {len(biz_modules)}"
    assert len(tech_modules) == 30, f"TECH modules expected 30, got {len(tech_modules)}"
    
    # Check 8-stage keys in first module of each
    for stage_key in ["theory", "key_vocab", "grammar_point", "listening_task", "speaking_prompt", "writing_task", "dialogue", "practice_quiz"]:
        assert stage_key in biz_modules[0], f"Stage {stage_key} missing in Business module 1"
        assert stage_key in tech_modules[0], f"Stage {stage_key} missing in Tech module 1"
    print("[+] All 8 stages present in Business and Tech modules!")
    
    # 2. Check Exam Bank Data
    assert "BUSINESS" in EXAM_BANK_30_TESTS, "BUSINESS missing in EXAM_BANK_30_TESTS"
    assert "TECH" in EXAM_BANK_30_TESTS, "TECH missing in EXAM_BANK_30_TESTS"
    
    biz_tests = EXAM_BANK_30_TESTS["BUSINESS"]
    tech_tests = EXAM_BANK_30_TESTS["TECH"]
    
    print(f"[+] BUSINESS Exam Bank Tests count: {len(biz_tests)} (Expected: 30)")
    print(f"[+] TECH Exam Bank Tests count: {len(tech_tests)} (Expected: 30)")
    assert len(biz_tests) == 30, f"BUSINESS tests expected 30, got {len(biz_tests)}"
    assert len(tech_tests) == 30, f"TECH tests expected 30, got {len(tech_tests)}"
    
    # Check questions in first test
    print(f"[+] BUSINESS Test 1 questions: {len(biz_tests[0]['questions'])} questions")
    print(f"[+] TECH Test 1 questions: {len(tech_tests[0]['questions'])} questions")
    assert len(biz_tests[0]['questions']) == 30
    assert len(tech_tests[0]['questions']) == 30
    
    print("\n[SUCCESS] ALL BUSINESS AND TECH VERIFICATIONS PASSED 100%!")

if __name__ == "__main__":
    verify_business_and_tech()

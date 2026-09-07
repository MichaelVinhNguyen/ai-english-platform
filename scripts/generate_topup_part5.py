# -*- coding: utf-8 -*-
"""
Generates scripts/data/topup_part5_topics_41_to_45.py from data_41, data_42, data_43, data_44, data_45
"""
import sys
import os

from data_41 import get_41
from data_42 import get_42
from data_43 import get_43
from data_44 import get_44
from data_45 import get_45

def make_obj(item):
    w, ipa, pos, vn, def_en, ex, ex_vi, syns, colls, etym = item
    return {
        "word": w,
        "phonetic": ipa,
        "pos": pos,
        "meaning_vi": vn,
        "definition": def_en,
        "example": ex,
        "example_vi": ex_vi,
        "synonyms": syns,
        "collocations": colls,
        "etymology": etym
    }

def main():
    t41 = [make_obj(x) for x in get_41()]
    t42 = [make_obj(x) for x in get_42()]
    t43 = [make_obj(x) for x in get_43()]
    t44 = [make_obj(x) for x in get_44()]
    t45 = [make_obj(x) for x in get_45()]

    out_file = os.path.join(os.path.dirname(__file__), "data", "topup_part5_topics_41_to_45.py")
    
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nTop-up data for Topics 41 to 45 (100-word fulfillment)\n"""\n\n')
        f.write("TOPUP_PART5 = {\n")
        
        # Topic 41: Civil Engineering, Structural Design & Urban Planning
        f.write('    "Civil Engineering, Structural Design & Urban Planning": [\n')
        for item in t41:
            f.write(f"        {repr(item)},\n")
        f.write("    ],\n")
        
        # Topic 42: Industrial Robotics, Automation & Smart Manufacturing
        f.write('    "Industrial Robotics, Automation & Smart Manufacturing": [\n')
        for item in t42:
            f.write(f"        {repr(item)},\n")
        f.write("    ],\n")

        # Topic 43: Maritime Logistics, Shipping & Port Operations
        f.write('    "Maritime Logistics, Shipping & Port Operations": [\n')
        for item in t43:
            f.write(f"        {repr(item)},\n")
        f.write("    ],\n")

        # Topic 44: International Relations, Geopolitics & Diplomacy
        f.write('    "International Relations, Geopolitics & Diplomacy": [\n')
        for item in t44:
            f.write(f"        {repr(item)},\n")
        f.write("    ],\n")

        # Topic 45: TOEIC Business: Contracts, Sales & Negotiation
        f.write('    "TOEIC Business: Contracts, Sales & Negotiation": [\n')
        for item in t45:
            f.write(f"        {repr(item)},\n")
        f.write("    ],\n")

        f.write("}\n")

    print("Successfully generated TOPUP_PART5!")
    print(f"41: {len(t41)}, 42: {len(t42)}, 43: {len(t43)}, 44: {len(t44)}, 45: {len(t45)}")

if __name__ == "__main__":
    main()

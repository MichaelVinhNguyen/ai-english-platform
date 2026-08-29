import re

def find_views():
    for fn in ['frontend/js/app.js', 'frontend/js/platform_modules.js', 'frontend/js/toeic_ielts_exam_studio.js']:
        try:
            with open(fn, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            for idx, line in enumerate(lines):
                if 'registerView' in line:
                    print(f"{fn}:{idx+1}: {line.strip()}")
        except Exception as e:
            print(f"Error {fn}: {e}")

if __name__ == '__main__':
    find_views()

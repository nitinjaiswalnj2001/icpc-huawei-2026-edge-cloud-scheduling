#!/usr/bin/env python3
from pathlib import Path
import re, subprocess, sys, hashlib

ROOT = Path(__file__).resolve().parents[1]
checks = []

def ok(name, condition, detail=''):
    checks.append((name, bool(condition), detail))

# Required public surface.
for p in ['README.md','CITATION.cff','COPYRIGHT.md','final/final_submission.cpp',
          'experiments/validate_dataset.py','docs/REPOSITORY_MAP.md',
          'report/ICPC_Huawei_2026_Edge_Cloud_Scheduling_Technical_Report.pdf',
          'provenance/AI_ASSISTANCE.md']:
    ok(f'exists:{p}', (ROOT/p).exists())

# No internal stage clutter at root.
root_names = {p.name for p in ROOT.iterdir()}
for prefix in ['STAGE1_', 'STAGE2_', 'STAGE3_', 'STAGE4_', 'STAGE5_', 'STAGE6_', 'STAGE7_']:
    ok(f'no_root:{prefix}', not any(n.startswith(prefix) for n in root_names))
for n in ['PROJECT_TRACKER.md','COPY_PLAN_STAGE1.md','NAMING_CONVENTIONS.md','LICENSE_TODO.md']:
    ok(f'no_root:{n}', n not in root_names)

# Stage 3 dataset validator.
try:
    p = subprocess.run([sys.executable, str(ROOT/'experiments'/'validate_dataset.py')],
                       cwd=ROOT, capture_output=True, text=True, timeout=30)
    ok('dataset_validator', p.returncode == 0 and 'FAIL: 0' in p.stdout, p.stdout.strip())
except Exception as e:
    ok('dataset_validator', False, str(e))

# Final source syntax compilation.
try:
    p = subprocess.run(['g++','-std=c++17','-O2','-pipe','-fsyntax-only',str(ROOT/'final'/'final_submission.cpp')],
                       cwd=ROOT, capture_output=True, text=True, timeout=120)
    ok('final_cpp_syntax', p.returncode == 0, p.stderr.strip())
except Exception as e:
    ok('final_cpp_syntax', False, str(e))

# Final source hash must equal Stage 0 actual-resubmit hash.
expected = 'c00e883a1e053b941bbc6f2f22b51ac4887934d6adfadce9b7b32b4397b2a1a8'
actual = hashlib.sha256((ROOT/'final'/'final_submission.cpp').read_bytes()).hexdigest()
ok('final_source_sha256', actual == expected, actual)

# Markdown relative links.
md_files = list(ROOT.rglob('*.md'))
link_re = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
link_count = 0
bad = []
for f in md_files:
    text = f.read_text(errors='replace')
    for target in link_re.findall(text):
        target = target.strip().split('#',1)[0]
        if not target or target.startswith(('http://','https://','mailto:','#')):
            continue
        if target.startswith('<') and target.endswith('>'):
            target = target[1:-1]
        link_count += 1
        dest = (f.parent / target).resolve()
        if not dest.exists():
            bad.append(f'{f.relative_to(ROOT)} -> {target}')
ok('markdown_relative_links', not bad, f'{link_count} checked; ' + ('; '.join(bad) if bad else 'all resolve'))


# No private absolute working paths or archive ZIPs in public repository.
private_hits = []
for f in ROOT.rglob('*'):
    if not f.is_file() or f.suffix.lower() in {'.png','.jpg','.jpeg','.pdf','.docx'}:
        continue
    try:
        txt = f.read_text(errors='replace')
    except Exception:
        continue
    for marker in ['/'+'mnt'+'/data/', '/'+'Users'+'/']:
        if marker in txt:
            private_hits.append(f'{f.relative_to(ROOT)} contains {marker}')
zip_files = [str(f.relative_to(ROOT)) for f in ROOT.rglob('*.zip')]
ok('no_private_absolute_paths', not private_hits, '; '.join(private_hits))
ok('no_zip_archives', not zip_files, '; '.join(zip_files))

# Publication wording gates.
readme = (ROOT/'README.md').read_text()
ok('readme_score', '16315.7938558663' in readme)
ok('readme_scope_public', 'public-judge' in readme and 'hidden/system' in readme)
ok('readme_ai_disclosure', 'Development transparency' in readme)
ok('readme_report_link', 'Technical_Report.pdf' in readme)

passed = sum(v for _,v,_ in checks)
failed = len(checks)-passed
print(f'Stage 8 repository audit checks: {len(checks)}')
print(f'PASS: {passed}')
print(f'FAIL: {failed}')
for name, val, detail in checks:
    if not val:
        print(f'[FAIL] {name}: {detail}')
if failed:
    sys.exit(1)
print('Publication audit passed.')

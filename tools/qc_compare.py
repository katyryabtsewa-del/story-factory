"""Compare the script with the transcript of the narration; report skipped or garbled passages.
usage: qc_compare.py TRANSCRIPT.txt CH01.txt [CH02.txt ...]  (prints a markdown report)"""
import re, sys, difflib, pathlib

def words(text):
    return re.findall(r"[a-z0-9']+", text.lower().replace("-", " "))

script = []
for p in sys.argv[2:]:
    lines = pathlib.Path(p).read_text().splitlines()
    script += words("\n".join(l for l in lines if not l.startswith("# ")))
heard = words(pathlib.Path(sys.argv[1]).read_text())
sm = difflib.SequenceMatcher(None, script, heard, autojunk=False)
problems = []
for op, a1, a2, b1, b2 in sm.get_opcodes():
    if op == "equal":
        continue
    said, got = " ".join(script[a1:a2]), " ".join(heard[b1:b2])
    if any(ch.isdigit() for ch in got) and a2 - a1 <= 6:
        continue                      # "nineteen seventy nine" vs "1979" is fine
    if max(a2 - a1, b2 - b1) >= 3:    # ignore one- or two-word recognition noise
        ctx = " ".join(script[max(0, a1 - 6):a1])
        problems.append(f"- …{ctx} **[script: {said or '—'}] → [heard: {got or '—'}]**")
print(f"# Audio QC\n\nSimilarity: **{sm.ratio() * 100:.1f}%** ({len(script)} script words, {len(heard)} heard)\n")
print("\n".join(problems) if problems else "No skipped or garbled passages found.")

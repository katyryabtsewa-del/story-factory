"""Check episode chapters against channel/style-guide.md rules.
usage: lint_script.py CH01.txt [CH02.txt ...]  (prints a markdown report)"""
import re, sys, pathlib, collections

WPM = 156
BANNED = ["little did i know", "a testament to", "tapestry", "in that moment", "didn't know i was holding",
          "silence was deafening", "shivers down my spine", "every fiber of my being", "washed over me",
          "i couldn't help but", "palpable", "delve", "navigate", "journey", "it's worth noting", "a mix of",
          "the weight of", "unspoken", "eyes sparkled", "pounded in my chest", "time stood still",
          "and just like that", "little did they know"]
report, total, all_words, report_counts = [], 0, [], {}
for p in sys.argv[1:]:
    raw = pathlib.Path(p).read_text()
    lines = raw.splitlines()
    if not lines or not lines[0].startswith("# "):
        report.append(f"- {p}: first line must be '# Chapter title'")
    body = "\n".join(lines[1:])
    w = re.findall(r"[A-Za-z']+", body)
    total += len(w); all_words += [x.lower() for x in w]
    issues = []
    low = body.lower()
    for b in BANNED:
        if b in low: issues.append(f"cliché «{b}» ×{low.count(b)}")
    if "..." in body or "…" in body: issues.append(f"ellipsis ×{body.count('...') + body.count('…')}")
    dashes = body.count("—") + body.count(" - ")
    if dashes > 3: issues.append(f"dashes ×{dashes} (max 3)")
    digits = re.findall(r"\d+", body)
    if digits: issues.append(f"digits {digits[:5]} — write numbers as words")
    if re.search(r"[$%&#@*]", body): issues.append("symbols $%&#@* — write as words")
    abbr = re.findall(r"\b(?:Mr|Mrs|Ms|Dr|St|Ave|Jr|Sr)\.", body)
    if abbr: issues.append(f"abbreviations {abbr[:5]} — write Mister, Missus, Doctor, Saint…")
    t31 = low.count("thirty-one years")
    if t31: report_counts["thirty-one years"] = report_counts.get("thirty-one years", 0) + t31
    caps = [x for x in re.findall(r"\b[A-Z]{4,}\b", body)]
    if caps: issues.append(f"CAPS words {caps[:5]}")
    long_paras = sum(1 for para in body.split("\n\n") if len(para.split()) > 160)
    if long_paras: issues.append(f"{long_paras} paragraphs over 160 words")
    report.append(f"- **{pathlib.Path(p).name}**: {len(w)} words (~{len(w) / WPM:.1f} min)" +
                  (" — " + "; ".join(issues) if issues else " — ok"))
grams = collections.Counter(tuple(all_words[i:i + 5]) for i in range(len(all_words) - 4))
repeats = [(" ".join(g), c) for g, c in grams.most_common(15) if c >= 3]
print(f"# Lint\n\nTotal: **{total} words ≈ {total / WPM:.0f} min**\n")
print("\n".join(report))
for phrase, n in report_counts.items():
    if n > 5:
        print(f"\n«{phrase}» used {n} times in the episode (max 5)")
if repeats:
    print("\nRepeated 5-word phrases (≥3 times):")
    print("\n".join(f"- «{g}» ×{c}" for g, c in repeats))

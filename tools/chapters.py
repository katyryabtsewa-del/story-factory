"""Turn OUT.chapters.json into YouTube description timestamps. usage: chapters.py FILE.chapters.json"""
import sys, json
for ch in json.load(open(sys.argv[1])):
    s = int(ch["start"]); h, m, sec = s // 3600, s % 3600 // 60, s % 60
    print((f"{h}:{m:02d}:{sec:02d}" if h else f"{m:02d}:{sec:02d}") + f" {ch['title']}")

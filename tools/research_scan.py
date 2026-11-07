"""Scan competitor channels and find outlier videos (views >= 3x the channel's recent median).
usage: research_scan.py research/competitors.txt research/outliers-YYYY-MM-DD.md
competitors.txt: one channel id (UC...) per line, optional '# comment' after it."""
import sys, json, statistics, subprocess, datetime

ids = [l.split("#")[0].strip() for l in open(sys.argv[1]) if l.split("#")[0].strip()]
summary, outliers = [], []
for cid in ids:
    r = subprocess.run([sys.executable, "-m", "yt_dlp", "--flat-playlist", "-J", "--playlist-end", "40",
                        f"https://www.youtube.com/channel/{cid}/videos"], capture_output=True, text=True)
    if r.returncode != 0:
        print("skipped", cid, r.stderr.strip()[-200:], file=sys.stderr); continue
    d = json.loads(r.stdout)
    e = [x for x in d.get("entries") or [] if x.get("view_count") is not None]
    if len(e) < 5:
        continue
    views = [x["view_count"] for x in e]
    med = statistics.median(views)
    dur = statistics.mean([x.get("duration") or 0 for x in e]) / 60
    summary.append((d.get("channel"), d.get("channel_follower_count"), med, views[:10], dur))
    for x in e[:30]:
        if med and x["view_count"] >= 3 * med:
            outliers.append((x["view_count"] / med, d.get("channel"), x["view_count"], round((x.get("duration") or 0) / 60), x.get("title"), x["id"]))

today = datetime.date.today().isoformat()
out = [f"# Разведка {today}\n", "## Каналы\n", "| Канал | Подписчики | Медиана 40 видео | Медиана последних 10 | Средняя длина, мин |", "|---|---|---|---|---|"]
for ch, subs, med, last10, dur in sorted(summary, key=lambda s: -s[2]):
    out.append(f"| {ch} | {subs or '?'} | {int(med):,} | {int(statistics.median(last10)):,} | {dur:.0f} |")
out += ["\n## Видео-выбросы (≥3× медианы канала, среди 30 последних)\n", "| × | Канал | Просмотры | Мин | Название |", "|---|---|---|---|---|"]
for ratio, ch, v, mins, title, vid in sorted(outliers, reverse=True)[:40]:
    out.append(f"| {ratio:.1f} | {ch} | {v:,} | {mins} | [{title}](https://www.youtube.com/watch?v={vid}) |")
open(sys.argv[2], "w").write("\n".join(out) + "\n")
print(f"saved {sys.argv[2]}: {len(summary)} channels, {len(outliers)} outliers")

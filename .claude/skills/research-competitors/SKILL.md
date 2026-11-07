---
name: research-competitors
description: Scan competitor channels for outlier videos and update the niche patterns. Use before generating ideas, weekly, or when asked what is working in the niche right now.
---
# Разведка по конкурентам

1. `.venv/bin/python tools/research_scan.py research/competitors.txt research/outliers-$(date +%F).md`
   (если YouTube просит подтвердить, что вы не бот, — не обходить; работать с тем, что успело скачаться.)
2. Прочитай отчёт. Учти: старые видео успели набрать больше, поэтому самые полезные выбросы — среди 10 последних.
3. Для 10–15 лучших выбросов разбери **по названию**: кто рассказчик, кто злодей, сцена унижения, событие-обстановка, обещанная расплата. Сами видео не пересказывать и не копировать.
4. Допиши в `research/patterns.md` раздел с датой: что сейчас чаще всего выстреливает, что новое, что затухает. 5–10 пунктов.
5. Если находишь новый сильный канал в нише — добавь его id в `research/competitors.txt` с комментарием.

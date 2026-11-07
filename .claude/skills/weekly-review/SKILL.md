---
name: weekly-review
description: Weekly channel analytics review — pull YouTube stats, compare episodes, update what works. Use weekly or when the owner asks how the channel is doing.
---
# Недельный отчёт

1. Данные канала — через коннектор Windsor.ai `youtube` (get_connectors → get_fields → get_data): по каждому видео за последние 28 дней — просмотры, показы и CTR, средняя длительность просмотра, % просмотра, подписки. Если коннектор не подключён — дай владельцу ссылку на подключение (get_connector_connect_info) и остановись.
2. Сопоставь с эпизодами (`episodes/*/publish.md`): название, обложка, длина, злодей, механизм расплаты.
3. Запиши `analytics/weekly/ДАТА.md`: таблица видео, лучшие и худшие, 3–5 выводов.
4. Обнови `analytics/learnings.md`: подтверждённое — в «работает», опровергнутое — убрать. Только то, что видно на данных ≥3 видео.
5. Коротко доложи владельцу по-русски: что работает, что меняем в следующих эпизодах.

# Architecture

## End-to-end flow

```text
Form / Google Doc
→ Input Intake
→ Document Extraction
→ Input Precheck
→ P010 Prompt Router
→ Router Output Validator
→ Prompt Registry
→ Prompt Extractor
→ Prompt Builder
→ Prompt Build Validator
→ GigaChat
→ AI Result Gate
→ Google Doc Artifact
→ S2 Output
→ Automation Log
→ Human Review
→ Safe next action
```

## Contracts

Input Precheck возвращает качество входа, недостающие данные, безопасные и
заблокированные маршруты.

Router выбирает только `route_id` и `prompt_id`. При низком confidence или
mapping mismatch маршрут уходит в Human Review.

AI Result Gate отделяет ошибки от warnings. Даже технически корректный ответ
остаётся AI Draft.

Human Review сначала сохраняется в S2 Output и Automation Log. Только после
успешной записи выполняется следующий маршрут.

## Version lineage

```text
result_code
result_version
parent_result_code
previous_prompt_id
previous_route_id
previous_result_status
process_mode
```

## Fail-closed

Workflow блокирует пустой вход, failed extraction, unsafe route, низкий
confidence, незаменённый placeholder, некорректный AI result, потерю parent
result, ошибку storage и неизвестное Human Review decision.

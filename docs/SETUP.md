# Setup

## Import

Импортируйте:

```text
workflows/ai-requirements-workflow.template.json
```

## GigaChat

Настройте:

```text
GIGACHAT_AUTHORIZATION_KEY
GIGACHAT_RQUID
```

Authorization Key указывается без префикса `Basic` и не вставляется в JSON.

## Google credentials

После импорта назначьте собственные Google Drive, Google Docs и Google Sheets
OAuth credentials.

## Google Sheets

Создайте вкладки из:

```text
templates/google-sheets/input-registry.csv
templates/google-sheets/s2-output.csv
templates/google-sheets/automation-log.csv
```

Повторно выберите spreadsheet и sheet во всех Google Sheets nodes.

## Placeholders

```text
YOUR_SPREADSHEET_ID
YOUR_INPUT_REGISTRY_SHEET_ID
YOUR_S2_OUTPUT_SHEET_ID
YOUR_AUTOMATION_LOG_SHEET_ID
YOUR_PROMPT_LIBRARY_DOC_ID
YOUR_ARTIFACT_FOLDER_ID
```

## Prompt Library

Используйте маркеры:

```text
=== PROMPT_START: P001 ===
...
=== PROMPT_END: P001 ===
```

## Smoke test

Проверьте initial flow, запись артефакта, Human Review, а затем
`CONTINUE_WITH_NOTES` или `RERUN_AI` с созданием child result.

# Security

Не публикуются:

- GigaChat Authorization Key и access token;
- Google OAuth credentials;
- реальные Google resource IDs;
- webhook IDs;
- execution history и pinned data;
- `.n8n` database;
- raw exports до sanitization.

Public template contract:

```text
active = false
pinData = {}
credentials отсутствуют
webhookId отсутствует
instance metadata отсутствует
TLS verification не отключена
```

Перед push:

```bash
python scripts/audit_workflow.py workflows/ai-requirements-workflow.template.json
git diff --cached --check
```

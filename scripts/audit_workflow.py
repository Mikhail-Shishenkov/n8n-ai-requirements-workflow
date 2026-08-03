#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import re
import sys

parser = argparse.ArgumentParser()
parser.add_argument("workflow", type=Path)
args = parser.parse_args()

data = json.loads(args.workflow.read_text(encoding="utf-8-sig"))
text = json.dumps(data, ensure_ascii=False)
errors = []

if data.get("active") is True:
    errors.append("workflow_is_active")
if data.get("pinData"):
    errors.append("pin_data_is_not_empty")

for key in ("id", "versionId", "meta"):
    if key in data:
        errors.append(f"top_level_{key}_present")

checks = {
    "credential_references_present": '"credentials"' in text,
    "webhook_ids_present": '"webhookId"' in text,
    "literal_basic_authorization_present": bool(
        re.search(r"Basic\s+[A-Za-z0-9+/=]{40,}", text)
    ),
    "tls_verification_override_present": "allowUnauthorizedCerts" in text,
    "personal_name_present": bool(re.search(r"(?i)misha|Миш", text)),
}

errors.extend(name for name, failed in checks.items() if failed)

nodes = data.get("nodes", [])
names = [node.get("name") for node in nodes]
name_set = set(names)
edges = 0

if len(names) != len(name_set):
    errors.append("duplicate_node_names")

for source, groups in data.get("connections", {}).items():
    if source not in name_set:
        errors.append(f"missing_source:{source}")

    for outputs in groups.values():
        for group in outputs:
            edges += len(group)
            for connection in group:
                if connection.get("node") not in name_set:
                    errors.append(
                        f"missing_target:{connection.get('node')}"
                    )

print(f"nodes={len(nodes)}")
print(f"connections={edges}")
print(f"errors={len(errors)}")

for error in errors:
    print(f"ERROR: {error}")

if errors:
    sys.exit(1)

print("Public workflow audit passed.")

"""Load shared architecture rule configs from tools/architecture/."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

_CONFIG_DIR = Path(__file__).resolve().parent


def config_dir() -> Path:
    return _CONFIG_DIR


def load_json(name: str) -> Any:
    path = _CONFIG_DIR / name
    return json.loads(path.read_text(encoding="utf-8"))


def ch1_dec_order_expected() -> dict[str, list[str]]:
    data = load_json("ch1_dec_order.json")
    if not isinstance(data, dict):
        raise ValueError("ch1_dec_order.json must be a heading -> row list mapping")
    return {str(k): list(v) for k, v in data.items()}


def rule_registry() -> list[dict[str, Any]]:
    data = load_json("rule_registry.json")
    rules = data.get("rules", [])
    if not isinstance(rules, list):
        raise ValueError("rule_registry.json rules must be a list")
    return rules


def lexical_guardrails() -> dict[str, Any]:
    data = load_json("lexical_guardrails.json")
    if not isinstance(data, dict):
        raise ValueError("lexical_guardrails.json must be a mapping")
    return data

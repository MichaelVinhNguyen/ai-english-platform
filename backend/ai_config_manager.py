import json
import os
import time
from pathlib import Path
from typing import Dict, Any, List, Optional

CONFIG_FILE = Path(__file__).parent / "ai_config.json"

DEFAULT_PROFILES = [
    {
        "id": "gemini-flash-default",
        "name": "Google Gemini 2.5 Flash (Mặc Định Hệ Thống - Siêu Nhanh)",
        "provider": "gemini",
        "api_key": "AIzaSyAmw1VHga-G0fp6tOaoQPcmFUsVP6N-8vQ",
        "base_url": "",
        "model": "gemini-flash-latest",
        "is_active": True,
        "created_at": "2026-08-24T00:00:00Z"
    },
    {
        "id": "openai-gpt4o",
        "name": "OpenAI GPT-4o / GPT-4o-mini (Chính Thức)",
        "provider": "openai",
        "api_key": "",
        "base_url": "https://api.openai.com/v1",
        "model": "gpt-4o-mini",
        "is_active": False,
        "created_at": "2026-08-24T00:00:00Z"
    },
    {
        "id": "deepseek-r1",
        "name": "DeepSeek V3 / R1 (Mô Hình Suy Luận Cực Rẻ)",
        "provider": "deepseek",
        "api_key": "",
        "base_url": "https://api.deepseek.com/v1",
        "model": "deepseek-chat",
        "is_active": False,
        "created_at": "2026-08-24T00:00:00Z"
    },
    {
        "id": "groq-llama33",
        "name": "Groq Llama 3.3 70B (Tốc Độ Phản Hồi Dưới 0.5s)",
        "provider": "groq",
        "api_key": "",
        "base_url": "https://api.groq.com/openai/v1",
        "model": "llama-3.3-70b-versatile",
        "is_active": False,
        "created_at": "2026-08-24T00:00:00Z"
    },
    {
        "id": "anthropic-claude",
        "name": "Anthropic Claude 3.5 Sonnet / Haiku",
        "provider": "custom",
        "api_key": "",
        "base_url": "https://api.anthropic.com/v1",
        "model": "claude-3-5-sonnet-20241022",
        "is_active": False,
        "created_at": "2026-08-24T00:00:00Z"
    }
]

DEFAULT_CONFIG = {
    "provider": "gemini",
    "api_key": "AIzaSyAmw1VHga-G0fp6tOaoQPcmFUsVP6N-8vQ",
    "base_url": "",
    "model": "gemini-flash-latest",
    "tts_engine": "browser-neural",
    "temperature": 0.7,
    "max_tokens": 1024,
    "profiles": DEFAULT_PROFILES,
    "active_profile_id": "gemini-flash-default",
    "notes": "Hệ thống hỗ trợ cấu hình đa API ngoài (Gemini, OpenAI, DeepSeek, Groq, Claude, Custom API)."
}

def get_ai_config() -> Dict[str, Any]:
    if not CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                json.dump(DEFAULT_CONFIG, f, indent=2, ensure_ascii=False)
        except Exception:
            pass
        return DEFAULT_CONFIG.copy()
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            for k, v in DEFAULT_CONFIG.items():
                if k not in data:
                    data[k] = v
            if "profiles" not in data or not isinstance(data["profiles"], list) or len(data["profiles"]) == 0:
                data["profiles"] = DEFAULT_PROFILES
            return data
    except Exception:
        return DEFAULT_CONFIG.copy()

def save_ai_config(config_data: Dict[str, Any]) -> Dict[str, Any]:
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                merged = json.load(f)
        except Exception:
            merged = DEFAULT_CONFIG.copy()
    else:
        merged = DEFAULT_CONFIG.copy()

    merged.update(config_data)
    
    # If active_profile_id specified, sync top-level provider, api_key, model, base_url
    if "active_profile_id" in config_data:
        active_id = config_data["active_profile_id"]
        profiles = merged.get("profiles", [])
        for p in profiles:
            if p.get("id") == active_id:
                p["is_active"] = True
                merged["provider"] = p.get("provider", "gemini")
                merged["api_key"] = p.get("api_key", "")
                merged["base_url"] = p.get("base_url", "")
                merged["model"] = p.get("model", "gemini-flash-latest")
            else:
                p["is_active"] = False

    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(merged, f, indent=2, ensure_ascii=False)
    except Exception:
        pass
    return merged


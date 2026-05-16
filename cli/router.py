from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "presentation-pro-designer" / "scripts" / "route_request.py"
MANIFEST = ROOT / "skills" / "presentation-pro-designer" / "scripts" / "deck_manifest.py"

def route_text(text: str) -> dict:
    proc = subprocess.run([sys.executable, str(SCRIPT), text], capture_output=True, text=True, check=True)
    return json.loads(proc.stdout)

def route_file(path: Path) -> dict:
    proc = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True, check=True)
    return json.loads(proc.stdout)

def make_manifest(route: dict) -> dict:
    proc = subprocess.run([sys.executable, str(MANIFEST)], input=json.dumps(route), capture_output=True, text=True, check=True)
    return json.loads(proc.stdout)

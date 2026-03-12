#!/usr/bin/env python3
"""VoiceNotes triage CLI."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.voice_notes.cli import main


if __name__ == "__main__":
    raise SystemExit(main())

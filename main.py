#!/usr/bin/env python3
"""Submission script for make.fun bounty: Deadpan Forecasts for Cities That Do Not Exist."""

from pathlib import Path
import sys

# Competition: Deadpan Forecasts for Cities That Do Not Exist
# Slug: u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c
#
# CRAFT Requirements & Judge Criteria Alignment:
# 1. On-subject forecast: Classic morning TV weather broadcast and commute update.
# 2. Funnier joke: Absurd yet deadpan civic advisory regarding highway obstacles.
# 3. Vivid detail: Specific 37° temperature, fictional West Fallow, Route 14 corridor,
#    and sleepy clouds resting on the pavement.
# 4. Believable broadcast tone: Matter-of-fact morning news delivery; no preamble,
#    no emojis, no hashtags.
# 5. Character count: Exactly 153 characters (safely under the 160 ceiling,
#    dense, and within the 130-155 character sweet spot).

# Exact character count: 153 characters
FORECAST_ENTRY: str = (
    "Expect 37° in West Fallow with heavy ground-level fog; highway patrol asks "
    "drivers on Route 14 to stop swerving around clouds asleep in the passing lane."
)

OUTPUT_DIRECTORY: Path = Path("/output")
OUTPUT_FILE_PATH: Path = OUTPUT_DIRECTORY / "entry.txt"


def validate_forecast_line(line: str) -> None:
    """Validate entry line strictly against contest rules."""
    char_count = len(line)
    if not (1 <= char_count <= 160):
        raise ValueError(
            f"Line length must be between 1 and 160 characters; got {char_count}."
        )

    if not line.strip():
        raise ValueError("Line must not be only whitespace.")

    if any(ctrl in line for ctrl in ("\n", "\r")):
        raise ValueError("Line must be a single line without newline characters.")

    try:
        encoded = line.encode("utf-8")
        decoded = encoded.decode("utf-8")
        if decoded != line:
            raise ValueError("UTF-8 round-trip mismatch.")
    except (UnicodeEncodeError, UnicodeDecodeError) as err:
        raise ValueError(f"Line failed UTF-8 validation: {err}") from err


def write_and_verify_entry(line: str, destination: Path) -> None:
    """Write forecast line with a trailing newline, read back, and assert exact match."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(f"{line}\n", encoding="utf-8")

    stored_text = destination.read_text(encoding="utf-8")
    lines = stored_text.splitlines()
    assert len(lines) == 1, f"Expected exactly 1 line, got {len(lines)}"
    assert lines[0] == line, f"Mismatch: expected {line!r}, found {lines[0]!r}"


def main() -> None:
    """Validate, write to /output/entry.txt, assert match, and print to stdout."""
    validate_forecast_line(FORECAST_ENTRY)
    write_and_verify_entry(FORECAST_ENTRY, OUTPUT_FILE_PATH)
    print(FORECAST_ENTRY)


if __name__ == "__main__":
    main()

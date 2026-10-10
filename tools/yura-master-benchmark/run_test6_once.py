from __future__ import annotations

from pathlib import Path

import run_raw_once as base

TOOL_DIR = Path(__file__).resolve().parent

# Test 6 is intentionally isolated from the frozen Test 5 runner/config/instruction.
# Only Test-6-specific globals are overridden; inherited pipeline/QA behavior stays unchanged.
base.CONFIG_PATH = TOOL_DIR / "config_test6.json"
base.INSTRUCTION_PATH = TOOL_DIR / "codex_instruction_test6.md"
base.AUTHORITY_ROLES = {
    **base.AUTHORITY_ROLES,
    "visuals/yura/identity/master/YURA_VISUAL_MASTER.png": "AUTHOR-SELECTED WORKING MASTER EDIT BASE",
}

TEST6_REQUIRED_PROMPT_INVARIANTS = (
    "TEST 6 USES IMAGE 1 AS THE AUTHOR-SELECTED WORKING MASTER EDIT BASE.",
    "IMAGE 1 = YURA_VISUAL_MASTER.png — AUTHOR-SELECTED WORKING MASTER EDIT BASE.",
    "IMAGE 2 = YURA_BODY_GEOMETRY_GUIDE.png — BODY GEOMETRY CORRECTION AUTHORITY.",
    "PRESERVE IMAGE 1 FACE IDENTITY.",
    "PRESERVE IMAGE 1 OVERALL BUILD.",
    "PRESERVE IMAGE 1 CHEST APPEARANCE.",
    "PRESERVE IMAGE 1 THIGH FEMININE VOLUME AND CURVE.",
    "PRESERVE IMAGE 1 KNEE POSITION AND OVERALL LEG VISUAL BALANCE.",
    "PRESERVE IMAGE 1 SKIN APPEARANCE.",
    "PRESERVE IMAGE 1 GENERAL HAIR IDENTITY AND CURRENT HAIR LENGTH.",
    "DO NOT INTENTIONALLY LENGTHEN OR SHORTEN HAIR IN TEST 6.",
    "CROTCH/PELVIS BOUNDARY = CENTRAL MEDIAL-THIGH BIFURCATION / UPPER-LOWER BODY STRUCTURAL BOUNDARY.",
    "CROTCH/PELVIS BOUNDARY MUST BE AT 53.7037% OF CROWN-TO-SOLES BODY HEIGHT, MEASURED DOWNWARD FROM THE STRUCTURAL CROWN.",
    "CROTCH-TO-SOLES MUST BE 46.2963% OF CROWN-TO-SOLES BODY HEIGHT.",
    "THIS IS A MEASURABLE STRUCTURAL ANCHOR, NOT A QUALITATIVE AESTHETIC SUGGESTION.",
    "GARMENT LINES HAVE NO LANDMARK AUTHORITY.",
    "DO NOT USE THE WAISTLINE, SHORTS WAISTBAND, GARMENT HEM, NAVEL, OR HIP WIDEST POINT AS THE CROTCH/PELVIS BOUNDARY.",
    "MOVE THE STRUCTURAL BOUNDARY BY REDISTRIBUTING THE TORSO/PELVIS TRANSITION.",
    "DO NOT SOLVE THE TARGET BY CHANGING HEAD SIZE.",
    "DO NOT SOLVE THE TARGET BY LENGTHENING ONLY THIGHS OR SHINS.",
    "DO NOT MOVE THE KNEES OR SOLES MERELY TO MANIPULATE THE RATIO.",
    "DO NOT USE NONUNIFORM BODY SCALING OR COMPOSITION WARP.",
)

_TEST5_REFERENCE_SPECIFIC = {
    "FACE REFERENCE DEFINES FACIAL IDENTITY AND FACE-LOCAL GEOMETRY ONLY.",
    "FACE REFERENCE DOES NOT DEFINE HEAD-TO-BODY SCALE.",
    "FACE REFERENCE DOES NOT DEFINE HEAD VERTICAL SIZE FOR FULL-BODY PROPORTION.",
    "FACE REFERENCE DOES NOT DEFINE TOTAL HEAD COUNT.",
    "FACE REFERENCE DOES NOT DEFINE BODY PROPORTIONS.",
    "DO NOT INFER BODY PROPORTION FROM FACE REFERENCE CROP OR SCALE.",
    "DO NOT USE FACE REFERENCE CANVAS OCCUPANCY AS BODY GEOMETRY.",
    "FACE_REFERENCE -> BODY_PROPORTION = DENIED",
    "FACE_REFERENCE -> FULL_BODY_SCALE = DENIED",
    "FACE_REFERENCE -> CANVAS_OCCUPANCY = DENIED",
    "PRESERVE IMAGE 1 RELATIVE BODY-LANDMARK LAYOUT.",
    "USE IMAGE 2 FOR FACE IDENTITY ONLY.",
    "DO NOT RESCALE IMAGE 1 BODY GEOMETRY TO MATCH IMAGE 2.",
    "FACE REFERENCE PRESERVES FACE IDENTITY ONLY; BODY GEOMETRY GUIDE CONTROLS FULL-BODY HEAD SCALE AND INTERNAL BODY LANDMARK PLACEMENT.",
}

base.REQUIRED_PROMPT_INVARIANTS = tuple(
    value
    for value in base.REQUIRED_PROMPT_INVARIANTS
    if value not in _TEST5_REFERENCE_SPECIFIC
    and not value.startswith("TEST 5 USES IMAGE 1")
    and not value.startswith("IMAGE 1 = YURA_BODY_GEOMETRY_GUIDE.png")
    and not value.startswith("IMAGE 2 = YURA_FACE_REFERENCE.png")
) + TEST6_REQUIRED_PROMPT_INVARIANTS

_original_validate_runtime_config = base.validate_runtime_config


def validate_runtime_config_test6(config: dict) -> None:
    expected = [
        "visuals/yura/identity/master/YURA_VISUAL_MASTER.png",
        "visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png",
    ]
    if config.get("image_reference_order") != expected:
        raise RuntimeError(
            "Test 6 image_reference_order must be Working Master first, Body Geometry Guide second"
        )

    # Reuse every existing Test-5-era QA/Composition validation unchanged.
    # Temporarily substitute only the old reference-order value so the inherited
    # validator can check the rest of the config without duplicating that logic.
    saved = config["image_reference_order"]
    config["image_reference_order"] = [
        "visuals/yura/identity/body/YURA_BODY_GEOMETRY_GUIDE.png",
        "visuals/yura/identity/face/YURA_FACE_REFERENCE.png",
    ]
    try:
        _original_validate_runtime_config(config)
    finally:
        config["image_reference_order"] = saved

    test6 = config.get("test6") or {}
    if test6.get("working_master_sha256") != (
        "81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d"
    ):
        raise RuntimeError("Test 6 working_master_sha256 mismatch")
    if float(test6.get("boundary_from_structural_crown_ratio", -1)) != 0.537037:
        raise RuntimeError("Test 6 boundary_from_structural_crown_ratio must be 0.537037")
    if float(test6.get("crotch_to_soles_ratio", -1)) != 0.462963:
        raise RuntimeError("Test 6 crotch_to_soles_ratio must be 0.462963")
    if int(test6.get("minimum_paid_samples", -1)) != 1:
        raise RuntimeError("Test 6 minimum_paid_samples must be 1")
    if int(test6.get("maximum_paid_samples", -1)) != 5:
        raise RuntimeError("Test 6 maximum_paid_samples must be 5")
    if test6.get("hair_length_change_allowed") is not False:
        raise RuntimeError("Test 6 hair_length_change_allowed must be false")


base.validate_runtime_config = validate_runtime_config_test6

_original_main = base.main


def main() -> int:
    # Fail closed on exact Working Master bytes before entering the inherited pipeline.
    root = Path(base.run(["git", "rev-parse", "--show-toplevel"], TOOL_DIR).stdout.strip())
    master = root / "visuals/yura/identity/master/YURA_VISUAL_MASTER.png"
    actual = base.sha256_file(master)
    expected = "81ac67b8395d5e3b49abcd75db77d420aa9cab94bcff4b582eaaed13bfeaf94d"
    if actual.lower() != expected:
        raise RuntimeError(
            f"Test 6 Working Master SHA mismatch: expected={expected} actual={actual}"
        )
    return _original_main()


if __name__ == "__main__":
    raise SystemExit(main())

# TEXT-ONLY DIAGNOSTIC PROTOCOL

Status: **SHARED TEMPORARY VALIDATION ROUTE / NOT VISUAL AUTHORITY**

## 1. Purpose

This directory is a temporary text-only validation workbench used before a character's final visual specification is consolidated into that character's formal identity / part directories.

```text
visuals/execution/text-only-root/**
= shared temporary text-only validation workspace

visuals/<character>/identity/**
= character-specific formal visual authority / final consolidation target

tools/**
= paid or production execution routes where separately defined
```

This route is intentionally character-independent and may be reused for YURA or other characters.

Do not grow this directory into a second permanent visual-authority tree.

## 2. Minimal workspace rule

Keep the tracked workspace minimal.

Default tracked contents:

```text
TEXT_ONLY_DIAGNOSTIC_PROTOCOL.md
<CHARACTER>_VISUAL_TEXT.md
```

Run-specific Codex instructions, generated images, notes, and temporary inspection artifacts do not need to become permanent repository files unless the author explicitly requests that.

When switching characters, replace the active character Visual Text rather than duplicating the protocol.

## 3. Appearance-source boundary

For a text-only generation run, use exactly one active character Visual Text file in this directory as the appearance source.

Example:

```text
YURA_VISUAL_TEXT.md
```

Do not supply character image references during the text-only phase unless the author explicitly changes the test design.

Do not append appearance rescue wording from Master images, Face references, Body references, past generated images, Memory, story, manuscript, character prose, Git history, or unrelated specification files.

Allowed additional generation instructions are operational only, for example:

```text
requested view
crop / framing
single-character constraint
neutral pose / expression
camera direction
plain background
diagnostic status
```

If the active Visual Text itself contains the fixed composition for the current baseline, do not override that composition unless the current Run instruction explicitly requires another view.

## 4. Generator boundary

The text-only phase uses the explicitly selected non-paid / diagnostic generator for that Run.

For the current Codex validation design:

```text
Codex-native image generation = USE when available in the active Codex session
paid OpenAI image generation = DO NOT USE before the text-only gate passes
image reference = NONE
```

If the selected diagnostic generator is unavailable, stop. Do not silently substitute a paid or different generator.

Generator availability is an environment condition, not a Visual Text quality result.

## 5. Execution-state classification

Use these states strictly:

```text
SOURCE_BLOCKED
= required current-main file / hash verification failed

ENVIRONMENT_BLOCKED
= sources verified, but the selected diagnostic generator is unavailable

GENERATED / QUALIFY
= an image was generated and passed the current Run's behavioral gate

GENERATED / NOT QUALIFY
= an image was generated and materially failed the current Run's behavioral gate
```

Rules:

```text
No generated image -> never label QUALIFY or NOT QUALIFY.
ENVIRONMENT_BLOCKED does not reset or increment a repeatability count.
SOURCE_BLOCKED does not test Visual Text quality.
Only an inspected generated image may affect qualification.
```

## 6. Fixed-condition discipline

A repeatability claim is valid only under an unchanged active Visual Text and unchanged material Run conditions.

A material Visual Text edit creates a new fixed condition and resets any qualification count associated with the previous condition.

Do not rescue a single failed output by adding ad-hoc appearance wording outside the active Visual Text. If a generated result exposes a real specification weakness, strengthen the Visual Text and restart the fixed condition.

## 7. Inspection rule

After each generated image, inspect only what the current Run is intended to test.

At minimum record:

```text
requested view / framing achieved
text-only character identity behavior
current target defect or ambiguity behavior
visibility / occlusion compensation if relevant
visual naturalness
other material visible issues
```

Minor unrelated awkwardness may be tolerated in an early diagnostic run if the tested behavior is interpretable and the Run-specific gate allows it.

## 8. PASS -> next route

The text-only gate definition is Run-specific.

Only after the author-approved repeatability gate passes may the workflow move to the next route, including a paid-generation route where applicable.

A text-only PASS validates specification strength / repeatability only. It does not automatically promote generated images, hidden geometry, or unresolved parts into formal Visual Authority.

## 9. Cleanup / consolidation

This directory is temporary by design.

When a character's relevant Master / part specifications are stabilized:

```text
1. consolidate accepted character-specific rules into that character's formal identity / part directories
2. remove obsolete character-specific temporary Visual Text copies from this root
3. keep only the shared protocol when it remains useful for future characters
```

Do not preserve duplicate character Authority here after formal consolidation.

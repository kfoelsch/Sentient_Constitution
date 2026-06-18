"""Paths for Sentient Constitution Chapter Five (index + constitutional band files)."""

from __future__ import annotations

CH5_INDEX = "core_05-05_definitions_a_independent.md"
CH5_PART_A = CH5_INDEX  # alias for legacy imports

CH5_BAND_O = "core_05o_oversight_definitions.md"
CH5_BAND_P = "core_05p_participation_definitions.md"
CH5_BAND_A = "core_05a_accountability_definitions.md"
CH5_BAND_C = "core_05c_continuity_definitions.md"
CH5_BAND_I = "core_05i_integrative_definitions.md"

CH5_BANDS: tuple[str, ...] = (
    CH5_BAND_O,
    CH5_BAND_P,
    CH5_BAND_A,
    CH5_BAND_C,
    CH5_BAND_I,
)

CH5_ALL: tuple[str, ...] = (CH5_INDEX, *CH5_BANDS)

# Retired paths (archive only — do not use in live corpus)
CH5_PART_B_RETIRED = "core_05-05_definitions_b_semi_independent.md"
CH5_PART_C_RETIRED = "core_05-05_definitions_c_dependent_clusters.md"

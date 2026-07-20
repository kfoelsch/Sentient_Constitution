"""Paths for Sentient Constitution Chapter Five (index + apex + band files)."""

from __future__ import annotations

CH5_INDEX = "core_05_definitions_home.md"
CH5_PART_A = CH5_INDEX  # alias for legacy imports

CH5_BAND_O = "core_05defs_oversight.md"
CH5_BAND_P = "core_05defs_participation.md"
CH5_BAND_A = "core_05defs_accountability.md"
CH5_BAND_C = "core_05defs_continuity.md"
CH5_BAND_I = "core_05defs_integrative.md"
CH5_BAND_M = "core_05defs_performance.md"

CH5_AIM_F = "core_05apex_flourishing_aim.md"
CH5_AIM_G = "core_05apex_continuity_aim.md"

CH5_LEG_A = "core_05apex_accountability_leg.md"
CH5_LEG_O = "core_05apex_oversight_leg.md"
CH5_LEG_P = "core_05apex_participation_leg.md"
CH5_LEG_T = "core_05apex_timeliness_leg.md"

CH5_BANDS: tuple[str, ...] = (
    CH5_BAND_A,
    CH5_BAND_C,
    CH5_BAND_I,
    CH5_BAND_O,
    CH5_BAND_P,
)

CH5_DEFS: tuple[str, ...] = (
    *CH5_BANDS,
    CH5_BAND_M,
)

CH5_AIMS: tuple[str, ...] = (
    CH5_AIM_F,
    CH5_AIM_G,
)

CH5_LEGS: tuple[str, ...] = (
    CH5_LEG_A,
    CH5_LEG_O,
    CH5_LEG_P,
    CH5_LEG_T,
)

# Apex = constitutional aim heads + Tetrad leg heads (O/M/A/C + decomposition + family rollups)
CH5_APEX: tuple[str, ...] = (*CH5_AIMS, *CH5_LEGS)

CH5_ALL: tuple[str, ...] = (CH5_INDEX, *sorted(CH5_APEX), *CH5_DEFS)

# Retired paths (archive only — do not use in live corpus)
CH5_PART_B_RETIRED = "core_05-05_definitions_b_semi_independent.md"
CH5_PART_C_RETIRED = "core_05-05_definitions_c_dependent_clusters.md"

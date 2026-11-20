"""Paths for Sentient Constitution Chapter Three (index + apex + band files)."""

from __future__ import annotations

CH5_INDEX = "core_03.000_definitions_home.md"
CH5_PART_A = CH5_INDEX  # alias for legacy imports

CH5_BAND_O = "subcore_03.085_band_oversight.md"
CH5_BAND_P = "subcore_03.090_band_participation.md"
CH5_BAND_A = "subcore_03.070_band_accountability.md"
CH5_BAND_C = "subcore_03.075_band_continuity.md"
CH5_BAND_I = "subcore_03.080_band_integrative.md"
CH5_BAND_M = "subcore_03.095_band_performance.md"

CH5_AIM_F = "subcore_03.050_apex_flourishing_aim.md"
CH5_AIM_G = "subcore_03.045_apex_continuity_aim.md"

CH5_LEG_A = "subcore_03.040_apex_accountability_leg.md"
CH5_LEG_O = "subcore_03.055_apex_oversight_leg.md"
CH5_LEG_P = "subcore_03.060_apex_participation_leg.md"
CH5_LEG_T = "subcore_03.065_apex_timeliness_leg.md"

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

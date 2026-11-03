# Project Vision — Terrain Intelligence

**NASA Space Apps Challenge 2026**
*"Identify Earth Locations that Analog the Permanent Moon Base Locations and Mars"*

> [!NOTE]
> This document describes the **intended direction** of the project. It is not a description of a completed system.

---

## Problem Statement

Landing and base site selection for lunar and Martian missions depends on topography, geology, environment, and resource availability. Before deploying hardware or personnel to the Moon or Mars, space agencies use **terrestrial analog sites** — locations on Earth that reproduce specific properties of planetary environments — to test equipment, validate methodologies, and train crews.

However, as the NASA challenge statement notes, analog sites are **"not entirely well characterized."** Current limitations include:

1. **Narrow selection**: The same handful of well-known sites (Atacama, Devon Island, Death Valley) are used repeatedly, potentially overlooking better-suited or more accessible alternatives.
2. **Single-score comparisons**: Existing tools often produce a single "similarity score" that collapses multi-dimensional differences into one number, hiding critical trade-offs.
3. **No mission specificity**: A site suitable for rover mobility testing may be unsuitable for habitat siting or geological exploration, but most comparisons do not account for mission objectives.
4. **Under-reported limitations**: Few tools explicitly state *where an analog fails* — which properties cannot be matched on Earth (gravity, atmospheric pressure, radiation) and which are data-limited.
5. **Uncertainty ignored**: Measurements from different instruments, resolutions, and planetary bodies carry different error profiles that are rarely propagated into results.

---

## Why This Matters

### For Space Agencies
Mischaracterized analogs waste field campaigns, produce misleading equipment tests, and create false confidence in mission readiness. Rigorous, mission-specific analog characterization reduces risk.

### For Researchers
A transparent, multi-dimensional comparison framework enables scientists to select sites based on the specific property they need to study, rather than relying on legacy choices.

### For the Broader Community
Democratizing analog identification with open data and open methods allows institutions with limited field budgets — including those outside traditional space-faring nations — to identify local analog candidates.

---

## Proposed Solution Direction

Terrain Intelligence aims to be a **scientific comparison and discovery tool** that:

1. **Compares terrain, thermal, and geological properties** between Earth sites and lunar/Martian target environments using matched-baseline, multi-scale analysis.
2. **Operates per mission objective** — applying different constraints and weightings for rover mobility, habitat siting, geological exploration, or astronaut training.
3. **Reports a vector of similarities, not a single score** — preserving dimensionality and allowing users to see which properties match and which do not.
4. **Explicitly flags analog failures** — properties where no Earth site can match the target (gravity, pressure, radiation, PSR temperatures) and properties where data is insufficient.
5. **Quantifies uncertainty** — using spatial block bootstrap and measurement-error propagation to produce confidence intervals, not false precision.
6. **Presents findings on interactive maps** with scientific context, not just colored pins.

### What We Will NOT Build

- A single "best analog" ranking without stated assumptions
- An unsupervised ML model claiming to discover analog quality
- A system that presents hypotheses as validated results
- A tool that fabricates or interpolates planetary data

---

## Intended Users

| User | Need |
|------|------|
| **Planetary scientists** | Rigorous, per-property analog comparison with uncertainty |
| **Mission planners** | Mission-specific site screening with hard constraints |
| **Field campaign organizers** | Candidate site identification with accessibility metadata |
| **Students and educators** | Interactive exploration of Earth-Moon-Mars comparisons |
| **Hackathon judges** | Clear, honest, scientifically grounded demonstration |

---

## Expected Scientific Value

1. **Methodological**: A transparent, reproducible framework for multi-dimensional analog comparison that can be reused beyond this challenge.
2. **Analytical**: Characterization of under-studied candidate sites (e.g., Lonar Crater, Ladakh) as screening hypotheses with explicit evidence levels.
3. **Critical**: Honest documentation of what analog comparison *cannot* tell us — a contribution often missing from analog tools.

---

## MVP Scope (Hackathon)

> [!IMPORTANT]
> The MVP is deliberately narrow. A credible answer to one question is better than a superficial answer to many.

**One question**: *"For a lunar south-polar rover-mobility test objective, which of a small set of Earth sites best match on terrain, where do they fail, and how certain are we?"*

- **Target**: One lunar south-polar region (e.g., Shackleton-rim tile set)
- **Earth candidates**: 4–5 sites (Lonar, Ladakh, Iceland lava field, Haughton/Devon Island, Atacama or Death Valley)
- **Dimensions**: Terrain (Tier A), Thermal (Tier B, simple), Geology (Tier C, qualitative)
- **Output**: Vector similarity per site, failure-analysis card, uncertainty bands
- **Stretch**: Second mission profile (habitat siting); Mars comparison

---

*Document status: Pre-hackathon draft. Last updated: November 2026.*

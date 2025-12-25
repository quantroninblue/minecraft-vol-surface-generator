# Minecraft Vol Surface Generator

This is a small research playground that uses Minecraft-style procedural terrain ideas to generate synthetic implied volatility surfaces and stress-test trading strategies inside them.

The core idea is to treat volatility surfaces as terrain rather than just numbers, and then explore what kinds of “market worlds” a strategy struggles in.

---

## What’s in here

- A procedural volatility surface generator (Perlin / fBM style noise)
- “Hostile” regime injectors (skew flips, convexity traps, tail pockets)
- A simple stress engine that runs a strategy across many alternate volatility worlds
- Visualizations of volatility surfaces as 3D terrain
- An animated “living” volatility world
- Tools to extract basic failure fingerprints from the generated worlds

---

## Why this exists

Mostly curiosity 🙂

I wanted to play with the idea of:

- What if we could generate alternate market regimes the same way games generate worlds?
- What kinds of volatility geometry does a strategy dislike?
- Can we see those failure zones visually?

So this repo is more of a sandbox for experimenting with those ideas.

---

## Getting started

Open the demo notebook:

notebooks/demo.ipynb


At the very top you can control how many worlds to generate:

```python
N_WORLDS = 300

Smaller numbers run quickly for demos, larger numbers give smoother distributions.

The notebook will:

Show a static volatility “terrain”

Generate an animated living world (GIF)

Build a small world library

Run a simple stress test

Plot a failure atlas and fingerprint map



Notes

This is not meant to be production-grade trading software.

It’s a research toy / visualization sandbox.

The goal is to explore geometry and structure, not optimize real trades.

Thanks for checking it out!

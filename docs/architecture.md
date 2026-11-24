# BhoomiAI architecture

BhoomiAI uses a React/TypeScript frontend, Flask REST backend, and MySQL in production. SQLite is the local fallback.

## Production safeguards

- Seed land records are explicitly marked `demo` and cannot be used as ownership evidence.
- Soil values remain `null` until a measured or authorized source is imported.
- Open-Meteo is fetched live but failures return an unavailable status.
- Crop recommendations are explainable heuristics with low confidence.
- Market prices are not fabricated; their integration remains `not_configured` until credentials/data access is configured.

# Social-Strata

> AI-powered social media growth toolkit — caption generation, semantic hashtag clustering, and brand strategy for any niche business.

---

## What is this?

Most small businesses waste hours writing captions and guessing which hashtags to use. Social-Strata takes that off their plate. You tell it your brand, your niche, and what you're posting — it handles the rest.

Built on real ML (not just prompt templates). Hashtags are clustered by semantic meaning using embeddings, so recommendations are actually relevant — not just popular. Captions are generated with brand tone in mind. Everything is cloud-native, multi-tenant, and built to support any niche.

This started as a real problem I was solving for [MimHijab](https://mimhijab.com), a modest fashion brand I was consulting for. It turned into something bigger.

---

## What it does

- **Caption Generator** — brand-aware, tone-matched captions using Claude API
- **Semantic Hashtag Clustering** — embeddings-based clustering to surface non-obvious, high-relevance hashtags (not just the obvious ones everyone uses)
- **Brand Profile System** — stores business context (niche, tone, audience) so every output is on-brand
- **Multi-business support** — built for agencies and consultants managing multiple brands

---

## Tech Stack

| Layer | Tool |
|---|---|
| ML / Embeddings | Python, Sentence Transformers |
| Vector Storage | Supabase pgvector |
| Relational Storage | Supabase PostgreSQL |
| Caption Generation | Claude API (Anthropic) |
| Web UI | Streamlit |
| Design | Claude Design |

---

## System Architecture

See [`/docs/architecture.md`](docs/architecture.md) for the full system design.

```
User Input (brand + post context)
        │
        ▼
  Streamlit UI
        │
   ┌────┴────┐
   │         │
Caption   Hashtag
Generator Clusterer
(Claude   (Embeddings
  API)     + pgvector)
   │         │
   └────┬────┘
        │
   Supabase DB
   (PostgreSQL
   + pgvector)
        │
        ▼
  Output to User
```

---

## Project Structure

```
social-strata/
├── README.md
├── PRD.md
├── requirements.txt
├── .env.example
├── /docs
│   ├── architecture.md
│   └── system-design.md
├── /design
│   └── mockups/
├── /src
│   ├── app.py            ← Streamlit UI
│   ├── captions.py       ← Claude API integration
│   └── embeddings.py     ← Hashtag clustering logic
└── /data
    └── schema.sql        ← Supabase table definitions
```

---

## Status

| Phase | Status |
|---|---|
| Project planning + architecture | ✅ Done |
| Supabase schema setup | 🔄 In progress |
| Embeddings + clustering module | 🔜 Up next |
| Claude API caption generator | 🔜 Upcoming |
| Streamlit UI | 🔜 Upcoming |
| Claude Design mockups | 🔜 Upcoming |

---

## Background

I'm an MS Engineering Management student at Purdue (ECE/AI focus), interning as an Engineering PM at Blue Ridge Automation while building toward an AI PM career. This project sits at the intersection of what I'm learning — ML fundamentals, product thinking, and real user problems.

The first user was Shahnaz Islam, founder of MimHijab. The insights from that real use case shaped everything about how this tool is designed.

---

## PRD

See [`PRD.md`](PRD.md) for full product requirements, user stories, and success metrics.

---

*Built by Syeda — [GitHub](https://github.com/meownager) · [LinkedIn](https://www.linkedin.com/in/syeda-mon)*

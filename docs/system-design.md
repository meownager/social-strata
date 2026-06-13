# System Design — Social-Strata

**Version:** 1.0  
**Author:** Syeda  
**Last Updated:** June 2026

---

## Problem Being Solved

Small niche businesses need brand-aware social media content fast. The technical challenge: generic AI tools don't know your brand. We fix that by persisting brand context and using semantic ML (not keyword matching) to make every output actually relevant.

---

## Functional Requirements

- User can create and save a business profile (name, niche, tone, audience)
- User can input post context and receive a brand-aware caption
- User can receive hashtag recommendations clustered by semantic meaning
- System supports multiple businesses (multi-tenant by design)
- All data persists in the cloud — nothing stored locally

## Non-Functional Requirements

- Caption output in < 30 seconds end-to-end
- Hashtag clusters: minimum 3 groups, 5-8 tags per group
- Cloud-only: Supabase as single source of truth
- Open source: clean code, documented, reproducible

---

## Constraints

- Solo developer, 1-2 hrs/week — must stay simple and modular
- No paid infrastructure in v1 — Supabase free tier + Anthropic API (pay per use)
- Python only — no separate backend framework
- Beginner-friendly codebase — prioritize readability over cleverness

---

## Embedding Pipeline Design

This is the core ML work. Here's how it works step by step:

```
Post context (text input)
        │
        ▼
Sentence Transformer model
(all-MiniLM-L6-v2)
        │
        ▼
384-dimensional vector
        │
        ▼
pgvector similarity search
(cosine distance against hashtag_embeddings table)
        │
        ▼
Top N similar hashtags returned
        │
        ▼
Cosine similarity grouping
(cluster into 3-5 semantic groups)
        │
        ▼
Output: hashtag clusters
```

**Why embeddings over keyword matching:**  
Keyword matching returns obvious hashtags everyone uses. Embeddings capture *meaning* — so a post about "breathable summer hijabs" surfaces tags like `#modestfashionista` and `#summerstyle` that are semantically related but not literal keyword matches. That's the competitive edge.

---

## Caption Prompt Architecture

The prompt sent to Claude API is structured — not just "write a caption." Brand context is injected dynamically:

```
System: You are a social media copywriter for [business_name], 
        a [niche] brand. Tone: [tone]. Target audience: [audience].
        Write Instagram captions that sound human, not AI-generated.

User:   Post context: [user input]
        Write a caption under 150 words. Include a CTA.
```

This is prompt engineering with intent — every variable comes from the saved business profile.

---

## Database Schema Design

Three tables. Clean separation of concerns:

```
businesses          hashtags              generated_content
──────────          ────────              ─────────────────
id (PK)             id (PK)               id (PK)
name                tag                   business_id (FK)
niche               niche                 post_context
tone                embedding (vector)    caption
audience            created_at            hashtag_clusters
created_at                                created_at
```

The `hashtags` table is pre-seeded with niche-relevant hashtags per vertical (fashion, food, fitness, etc.) — each one embedded at seed time. At query time, we search this table by vector similarity.

---

## Trade-off Analysis

| Trade-off | Option A | Option B | Decision |
|---|---|---|---|
| UI framework | Streamlit | FastAPI + React | Streamlit — faster to build, Python-only |
| Embedding model | OpenAI embeddings | Sentence Transformers | Sentence Transformers — free, runs in cloud env |
| Vector DB | Pinecone | Supabase pgvector | pgvector — one less service, simpler stack |
| Caption model | GPT-4 | Claude API | Claude — better instruction following for brand voice |

---

## Scaling Path (Not v1, but designed for it)

1. **More niches:** Seed the hashtag table with more verticals — no code change needed
2. **Better embeddings:** Swap `all-MiniLM-L6-v2` for a larger model without changing pipeline
3. **Auth:** Add Supabase Auth (built-in) when moving toward multi-user public access
4. **Engagement prediction:** Add a `performance` table to store real engagement data, train a prediction model on top

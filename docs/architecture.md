# System Architecture — Social-Strata

**Version:** 1.0  
**Author:** Syeda  
**Last Updated:** June 2026

---

## Overview

Social-Strata is a cloud-native, multi-tenant AI toolkit. There's no local storage — everything lives in Supabase. The system has two core AI pipelines: caption generation (Claude API) and hashtag clustering (embeddings + pgvector). A Streamlit frontend ties it together for non-technical users.

---

## High-Level Architecture

```
┌─────────────────────────────────────────┐
│              Streamlit UI               │
│  (Business profile · Post input · Output│
└────────────────┬────────────────────────┘
                 │
        ┌────────┴────────┐
        │                 │
        ▼                 ▼
┌──────────────┐  ┌─────────────────────┐
│ Caption      │  │ Hashtag Clusterer   │
│ Generator    │  │                     │
│              │  │ 1. Embed query      │
│ Claude API   │  │ 2. Search pgvector  │
│ + brand      │  │ 3. Cluster results  │
│   context    │  │ 4. Return groups    │
└──────┬───────┘  └────────┬────────────┘
       │                   │
       └─────────┬─────────┘
                 │
                 ▼
┌────────────────────────────────────────┐
│              Supabase                  │
│                                        │
│  PostgreSQL tables:                    │
│  - businesses (profiles)               │
│  - generated_content (history)         │
│  - hashtags (seed + embeddings)        │
│                                        │
│  pgvector extension:                   │
│  - hashtag_embeddings (vector col)     │
└────────────────────────────────────────┘
```

---

## Components

### 1. Streamlit UI (`src/app.py`)
- Entry point for the user
- Three screens: Business Profile Setup → Post Context Input → Output Display
- Calls caption and hashtag modules, renders results
- No business logic lives here — pure interface

### 2. Caption Generator (`src/captions.py`)
- Pulls business profile from Supabase
- Constructs a prompt: niche + tone + audience + post context
- Calls Claude API (`claude-sonnet-4-6`)
- Returns caption ready to copy-paste
- Saves output to `generated_content` table

### 3. Hashtag Clusterer (`src/embeddings.py`)
- Takes post context as input
- Generates embedding vector using Sentence Transformers
- Queries pgvector for semantically similar hashtags
- Clusters results using cosine similarity grouping
- Returns 3-5 semantic clusters with 5-8 hashtags each

### 4. Supabase (Storage Layer)
- PostgreSQL for relational data (business profiles, content history)
- pgvector for vector similarity search (hashtag embeddings)
- All reads/writes go through Supabase Python client
- No local files, no local DB

---

## Data Model

### `businesses`
```sql
id          UUID PRIMARY KEY
name        TEXT NOT NULL
niche       TEXT
tone        TEXT
audience    TEXT
created_at  TIMESTAMP
```

### `hashtags`
```sql
id          UUID PRIMARY KEY
tag         TEXT NOT NULL
niche       TEXT
embedding   VECTOR(384)   ← pgvector column
created_at  TIMESTAMP
```

### `generated_content`
```sql
id              UUID PRIMARY KEY
business_id     UUID REFERENCES businesses(id)
post_context    TEXT
caption         TEXT
hashtag_clusters JSONB
created_at      TIMESTAMP
```

---

## API Design

### Caption Generation
```
Input:  business_id + post_context (string)
Output: caption (string)
Flow:   Fetch profile → Build prompt → Call Claude API → Return + save
```

### Hashtag Clustering
```
Input:  post_context (string)
Output: clusters (list of lists of hashtags)
Flow:   Embed input → pgvector similarity search → Group by cosine similarity → Return
```

---

## Key Design Decisions

| Decision | Choice | Why |
|---|---|---|
| Storage | Supabase | PostgreSQL + pgvector in one place, free tier, no local dependency |
| Embeddings | Sentence Transformers (`all-MiniLM-L6-v2`) | Lightweight, fast, good semantic quality for short text |
| Caption model | Claude API | Best instruction-following for brand-aware generation |
| UI | Streamlit | Fastest path to a usable interface in pure Python |
| Vector dimensions | 384 | Matches `all-MiniLM-L6-v2` output, efficient for pgvector |

---

## What I'd Revisit as This Grows

- **Caching:** Right now every caption request hits the Claude API. At scale, cache similar inputs.
- **Embedding model:** `all-MiniLM-L6-v2` is great for MVP but a niche-fine-tuned model would improve hashtag relevance.
- **Multi-platform:** Schema supports it but UI and prompt templates are Instagram-first in v1.
- **Auth:** No user auth in v1 — business profiles are identified by UUID. Real auth needed before any public deployment.

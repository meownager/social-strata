# Product Requirements Document — Social-Strata

**Version:** 1.0  
**Author:** Syeda  
**Last Updated:** June 2026  
**Status:** Active

---

## Problem Statement

Small and mid-size businesses — especially niche brands in underserved markets like modest fashion, cultural food, or community retail — spend significant time on social media content with little strategic guidance. They either post inconsistently, use the wrong hashtags, or produce captions that don't reflect their brand voice. The tools available (Canva, Later, Hootsuite) help with scheduling and design, but none provide AI-driven, brand-aware content intelligence tailored to niche audiences.

The cost of not solving this: low engagement, wasted effort, and missed growth — especially for early-stage brands that can't afford a full-time social media manager.

---

## Goals

1. Reduce time spent on caption writing by 70% for small business owners
2. Increase hashtag relevance (measured by engagement rate on posts using Social-Strata recommendations vs. baseline)
3. Support multi-business use — one tool usable across any niche, not just fashion
4. Give non-technical users a clean, no-learning-curve experience
5. Demonstrate measurable engagement lift within 30 days of use (target: 15% improvement)

---

## Non-Goals

- **Not a scheduling tool** — we don't post on your behalf; that's a separate product category
- **Not an analytics dashboard** — we generate content, we don't track performance (v1)
- **Not Instagram-only** — architecture is platform-agnostic, but v1 focuses on Instagram format
- **Not a paid SaaS** — this is an open-source portfolio project; monetization is out of scope
- **Not a design tool** — we don't generate images or graphics

---

## Users

### Primary User: Small Business Owner / Solo Founder
- Runs a niche brand (fashion, food, lifestyle, community)
- Non-technical, time-poor
- Needs fast, on-brand content without hiring a social media manager

### Secondary User: Digital Marketing Consultant / Agency
- Manages multiple brand accounts
- Needs consistent, brand-differentiated output across clients
- Values efficiency and customization per brand

---

## User Stories

### Business Owner
- As a small business owner, I want to input my brand name and niche so that the tool understands my context before generating anything
- As a small business owner, I want to describe what I'm posting and get a ready-to-use caption so that I don't have to write from scratch
- As a small business owner, I want hashtag suggestions that are specific to my niche so that I reach the right audience, not just the biggest one
- As a small business owner, I want my brand profile saved so that I don't have to re-enter my information every time

### Consultant
- As a consultant managing multiple brands, I want to switch between business profiles easily so that I can generate content for each client without confusion
- As a consultant, I want to see clustered hashtag groups so that I can rotate sets across posts and maximize algorithmic reach

---

## Requirements

### P0 — Must Have
- [ ] Business profile creation (name, niche, tone, target audience)
- [ ] Caption generation using Claude API with brand context injected into prompt
- [ ] Hashtag generation using semantic embeddings — not keyword matching
- [ ] Hashtag clustering — group by meaning so user can rotate sets
- [ ] Supabase storage for business profiles and generated content history
- [ ] Streamlit UI — simple, functional, no design knowledge required to use

### P1 — Nice to Have
- [ ] Tone selector (e.g. professional, playful, Gen Z, luxury)
- [ ] Post type selector (product, lifestyle, social proof, event)
- [ ] Hashtag relevance score displayed per cluster
- [ ] Export output as text file

### P2 — Future Consideration
- [ ] Multi-platform output formatting (TikTok, LinkedIn, Twitter)
- [ ] Engagement prediction model (which caption/hashtag combo is likely to perform better)
- [ ] Fine-tuned caption model on brand's historical post data
- [ ] Analytics integration (pull real engagement data to close the feedback loop)

---

## Success Metrics

### Leading Indicators (within 2 weeks of use)
- Caption generation: time from input to usable output < 30 seconds
- Hashtag clusters: minimum 3 distinct semantic clusters per query
- UI completion rate: user successfully generates output on first attempt > 90%

### Lagging Indicators (30 days post-use)
- Engagement rate lift: 15%+ improvement on posts using Social-Strata output vs. baseline
- Return usage: user generates content again within 7 days of first use
- Profile reuse: user saves and reuses brand profile instead of re-entering data

---

## Open Questions

| Question | Owner | Blocking? |
|---|---|---|
| What embedding model gives best results for niche hashtag clustering? | Engineering | Yes |
| How many hashtag clusters should we surface per query? | Product | No |
| Should saved profiles be editable or versioned? | Product | No |
| What's the right prompt structure for brand-aware captions? | Engineering | Yes |

---

## Timeline

| Phase | Scope | Target |
|---|---|---|
| Phase 1 | Supabase schema + business profile storage | Week 1 |
| Phase 2 | Embeddings module + hashtag clustering | Week 2-3 |
| Phase 3 | Claude API caption generator | Week 3-4 |
| Phase 4 | Streamlit UI wiring everything together | Week 4-5 |
| Phase 5 | Claude Design mockups + README polish | Week 5-6 |

---

*This PRD is a living document — updated as the project evolves.*

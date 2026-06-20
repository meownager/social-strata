# Product Requirements Document: Social-Strata

**Version:** 1.1
**Last Updated:** June 2026
**Status:** Active planning

## Problem Statement

Small business owners often need to promote products on Instagram, but many do not have the time, technical comfort, or marketing background to understand which captions, hashtags, and content angles are likely to work.

Most caption tools start with text. Social-Strata starts with the product photo. The product image becomes the first source of context, then the system builds relevance around the product and returns simple, copy-ready output.

## Product Goal

Social-Strata should help a non-technical user move from product photo to usable Instagram content with the least possible friction.

The Phase 1 goal is:

> A user uploads a product photo and receives one catchy caption plus 5 or 6 relevant hashtags.

## Primary Users

### Small Business Owner

- Sells products through Instagram or wants to start doing so
- Does not want to learn complicated marketing tools
- Needs fast, practical content support
- Wants captions and hashtags that feel relevant to the actual product

### Solo Founder Or Local Seller

- Works with limited time and limited budget
- May not have a social media manager
- Wants simple output that can be copied and used immediately

## User Experience Principles

- The user should only need to upload a product photo to begin.
- Optional fields are allowed, but the app should still work without them.
- Outputs should be short, clear, and easy to copy.
- The app should avoid technical language in the user interface.
- The system should explain less and produce more.
- The product should stay cloud-based, with no heavy local files stored in the repo.

## Phase 1 Scope

### Must Have

- Product photo upload
- Product context identification from the uploaded image
- Product relevance profile
- Catchy caption output
- 5 or 6 relevant hashtag outputs
- Simple Streamlit interface
- Supabase table for storing generated outputs
- `.env.example` for required cloud credentials

### Should Have

- Optional business name input
- Optional product note input
- Copy-friendly output formatting
- Basic error handling for missing or unsupported images
- A clear record of generated output in the database

### Could Have

- Tone selector
- Product category correction by the user
- Download or copy buttons
- Basic feedback field so users can rate usefulness

## Phase 1 Non-Goals

- No automatic Instagram posting
- No Instagram scraping
- No paid infrastructure requirement
- No full analytics dashboard
- No advanced photo editing
- No user account system in the first build
- No heavy image storage inside GitHub

## Phase 2 Scope

Phase 2 focuses on product photo and design support.

Planned capabilities:

- Suggest product photography improvements
- Suggest background and composition changes
- Generate product styling recommendations
- Explore AI-assisted image enhancement using a free or free-tier model where possible

## Phase 3 Scope

Phase 3 focuses on SQL-based marketing analysis.

Planned capabilities:

- Store generated captions and hashtags over time
- Store product category and relevance data
- Optionally store user-entered Instagram performance metrics
- Use SQL to analyze patterns across product categories, captions, hashtags, and performance
- Turn findings into future strategy recommendations

## Success Metrics

### Phase 1 Product Metrics

- User can complete the workflow without technical help
- Image upload to output takes less than 30 seconds for normal use
- Output includes exactly one caption and 5 or 6 hashtags
- User can copy the result without editing the format

### Future Impact Metrics

- Caption reuse rate
- Hashtag reuse rate
- User feedback score
- Optional engagement metrics such as likes, saves, comments, and reach
- Performance changes by product category over time

## Risks And Mitigations

| Risk | Why It Matters | Mitigation |
|---|---|---|
| Instagram data access is limited | Direct scraping can be unreliable and risky | Phase 1 uses product relevance logic instead of scraping |
| Image model quality varies | Wrong product identification creates weak outputs | Let users correct product category later |
| Free-tier limits | Free APIs may have quotas | Keep model calls minimal and design fallback logic |
| Output sounds generic | The product loses value if captions feel copied | Use product relevance fields before generating text |
| Scope creep | The project has multiple future phases | Keep Phase 1 focused on upload, caption, hashtags |

## Open Questions

| Question | Owner | Blocking? |
|---|---|---|
| Which free or free-tier multimodal model should be used first? | Engineering | Yes |
| Should the user be able to correct the detected product category in Phase 1? | Product | No |
| What fields are required in the first Supabase schema? | Engineering | Yes |
| Should image files be stored immediately or only metadata at first? | Product and Engineering | No |
| What feedback metric should be collected first? | Product | No |

## Build Order

1. Clean documentation and architecture
2. Update database schema for image-first workflow
3. Build Streamlit upload page
4. Connect image understanding service
5. Build relevance engine
6. Generate caption and hashtags
7. Save output metadata to Supabase
8. Add tests for relevance and output formatting
9. Deploy a free hosted demo

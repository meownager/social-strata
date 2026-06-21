# Social-Strata

Social-Strata is an AI-assisted product relevance tool for small business owners who want better Instagram content without needing to understand social media trends, AI tools, or technical workflows.

The user uploads a product photo. The application identifies the product context, builds relevance around it, and returns copy-ready marketing output that can be used on Instagram.

Phase 1 focuses on one simple promise:

> Upload a product photo and get a catchy caption plus 5 or 6 relevant hashtags.

## What It Does

Social-Strata helps small business owners turn product photos into simple Instagram-ready content.

The first version will:

- Accept a product image upload
- Identify the likely product category and visual context
- Build a relevance profile for the product
- Generate one catchy caption
- Generate 5 or 6 focused hashtags
- Save useful output data to a cloud database for future analysis

The end user should not need to know how the system works. They should only need to upload, review, copy, and use.

## Why This Project Exists

Small business owners often have good products but limited time to think through positioning, captions, hashtags, and content strategy. Many of them are not technical. Many also do not know which Instagram trends matter for their product category.

Social-Strata is designed to support that user with a straightforward workflow and practical output.

This project is not trying to replace the business owner. It is meant to support them by reducing the time between having a product photo and having usable social media content.

## Target Users

Social-Strata is for:

- Small business owners
- Solo founders
- Local product-based businesses
- Instagram sellers
- Handmade product creators
- Niche brands with limited marketing support
- Non-technical users who want clear, copy-ready help

## Product Flow

```text
User uploads product photo
        |
        v
Image understanding layer
        |
        v
Product relevance engine
        |
        v
Caption generator
        |
        v
Hashtag generator
        |
        v
Copy-ready Instagram output
```

## Product Phases

### Phase 1: Caption And Hashtag Support

The first phase focuses on the core user workflow.

Input:

- Product photo
- Optional short business or product note

Output:

- One catchy Instagram caption
- Five or six relevant hashtags
- Simple layout that is easy to copy

Phase 1 is about proving that the product can take a photo and return something useful quickly.

### Phase 2: Product Design And Photography Enhancement

The second phase will help users improve the product photo before posting.

Planned direction:

- Product photo enhancement
- Product styling suggestions
- Background and composition recommendations
- Optional AI-assisted visual editing using a free or free-tier model where possible

The goal is to help small business owners make their products look more professional without needing advanced editing skills.

### Phase 3: SQL-Based Marketing Analysis

The third phase adds a data layer so the product can become smarter over time.

The app will store generated outputs and optional user-entered performance data in a cloud database. SQL will be used to answer questions like:

- Which product categories are used most often?
- Which caption styles are generated most often?
- Which hashtags are repeatedly selected?
- Which products or content styles perform better over time?
- What patterns suggest better Instagram positioning?

This phase turns Social-Strata from a generator into a learning system.

## Planned Architecture

```text
Streamlit App
    |
    |-- Product image upload
    |
    |-- Image understanding service
    |       |
    |       `-- Product category, visible attributes, style notes
    |
    |-- Product relevance engine
    |       |
    |       `-- Audience, angle, tone, use case, hashtag themes
    |
    |-- Output generation
    |       |
    |       |-- Caption
    |       `-- Hashtags
    |
    `-- Supabase
            |
            |-- Product context
            |-- Generated outputs
            `-- Future performance metrics
```

## Tech Direction

| Layer | Planned Tooling |
|---|---|
| User interface | Streamlit |
| Cloud database | Supabase PostgreSQL |
| Cloud file storage | Supabase Storage |
| Data analysis | SQL |
| Image understanding | Free or free-tier multimodal model |
| Relevance logic | Product category, audience, tone, and hashtag rules |
| Deployment | Free cloud hosting where possible |

The project direction is cloud-based. Heavy product images and generated assets should not be stored in the GitHub repo.

## Current Status

| Area | Status |
|---|---|
| Product direction | Updated |
| README | Updated |
| PRD | Updated |
| Architecture docs | Updated |
| Database schema | Supabase-ready |
| Streamlit app | Working locally |
| Image upload workflow | Working locally |
| Caption output | Working locally |
| Hashtag output | Working locally |
| Supabase setup guide | Added |
| SQL analysis layer | Future phase |
| Product photo enhancement | Future phase |

## Repository Structure

```text
social-strata/
|-- README.md
|-- PRD.md
|-- PROJECT_PLAN.md
|-- requirements.txt
|-- .env.example
|-- docs/
|   |-- architecture.md
|   |-- supabase-setup.md
|   `-- system-design.md
`-- data/
    `-- schema.sql
```

Application code lives under `src/`. Supabase setup details are documented in `docs/supabase-setup.md`.

## Long-Term Goal

The long-term goal for Social-Strata is to become a practical AI support tool for small businesses that want stronger Instagram content from product photos.

The project starts with captions and hashtags, then grows into product photo improvement and SQL-based marketing analysis.

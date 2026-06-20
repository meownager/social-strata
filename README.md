# Social-Strata

Social-Strata is an AI-assisted support application for small business owners who want to promote their products on Instagram but do not always have the time, tools, or working knowledge to keep up with fast-changing social media trends.

The goal is simple: a user uploads a product photo, and the application helps them understand how to position that product online. In the first version, Social-Strata will return a catchy caption and a focused set of relevant hashtags that the user can copy and use right away.

This project is also part of my journey as a technical product manager and AI product builder. I am using it to connect real user needs, applied AI, cloud tools, SQL analysis, and measurable product impact.

## Why This Project Exists

Small business owners often have good products but limited time to think through content strategy. Many of them are not technical, and many do not want a complicated dashboard. They need something practical, direct, and useful.

Social-Strata is being built for that user.

The product asks one simple thing from the user:

> Upload the product photo you want to promote.

Then the application does the thinking in the background:

- Understands what the product likely is
- Builds product relevance around the image
- Connects the product to likely Instagram positioning
- Generates a caption that sounds usable, not generic
- Suggests 5 or 6 hashtags that support both the product and the caption

## Target Users

Social-Strata is for:

- Small business owners
- Solo founders
- Local brands
- Product-based Instagram sellers
- Creators who sell handmade or niche products
- Non-technical users who want copy-ready marketing help

The user should not need to understand AI, prompts, SQL, or social media algorithms to use the app.

## Product Vision

Social-Strata will grow in phases.

### Phase 1: Caption And Hashtag Support

The first phase focuses on the simplest useful workflow.

User flow:

```text
Upload product photo
        ↓
Identify product context
        ↓
Build relevance
        ↓
Generate caption
        ↓
Generate 5 or 6 relevant hashtags
        ↓
Copy and use on Instagram
```

Phase 1 output:

- One catchy Instagram caption
- Five or six relevant hashtags
- Simple copy-friendly layout

### Phase 2: Product Design And Photography Enhancement

The second phase will focus on helping small business owners improve how their product looks before they post it.

Planned direction:

- Product photo enhancement
- Product styling suggestions
- Background and composition improvement ideas
- AI-assisted visual recommendations

The goal is to help users present their products better without needing advanced photography or editing skills.

### Phase 3: SQL-Based Marketing Analysis

The third phase will focus on learning from data over time.

Social-Strata will store useful marketing and output data in a cloud database. This will make it possible to analyze patterns such as:

- Which product categories are used most often
- Which hashtags appear in stronger outputs
- Which caption styles are reused by users
- How engagement data changes over time if users choose to track it
- What patterns might suggest better Instagram positioning

This is where SQL becomes part of the product learning loop. Instead of learning SQL through random examples, this project will use SQL to answer real product and marketing questions.

## What Makes Social-Strata Different

Social-Strata is not meant to be another generic caption generator.

The focus is on product relevance.

A normal caption tool might take a short sentence and generate marketing text. Social-Strata starts with the product image, builds context around what the product is, and then creates outputs that match that context.

The long-term goal is to make the application useful for real business owners while also showing how AI product thinking can move from idea to working system to measurable impact.

## Planned Architecture

```text
Product Photo Upload
        ↓
Image Understanding Layer
        ↓
Product Relevance Engine
        ↓
Caption Generator
        ↓
Hashtag Generator
        ↓
Cloud Database For Saved Outputs And Analysis
        ↓
Simple User Interface
```

## Tech Direction

| Layer | Planned Tooling |
|---|---|
| User Interface | Streamlit |
| Cloud Database | Supabase PostgreSQL |
| Data Analysis | SQL |
| Image Understanding | Free or free-tier multimodal model during development |
| Relevance Logic | Product category, audience, tone, trend, and hashtag rules |
| Deployment | Free cloud hosting where possible |

The project will stay cloud-based. Local storage is not part of the product direction.

## Current Status

| Area | Status |
|---|---|
| Product direction | In progress |
| README and roadmap | Updated |
| Database schema | Initial draft |
| Streamlit app | Planned |
| Image upload workflow | Planned |
| Caption output | Planned |
| Hashtag output | Planned |
| SQL analysis layer | Future phase |
| Product photo enhancement | Future phase |

## Repository Structure

```text
social-strata/
├── README.md
├── PRD.md
├── requirements.txt
├── .env.example
├── docs/
│   ├── architecture.md
│   └── system-design.md
└── data/
    └── schema.sql
```

As the application is built, source code will be added under `src/` and the documentation will be updated to match the working product.

## Learning Goals

This project is designed to show growth across product and engineering skills:

- Defining a real user problem
- Designing an AI-assisted workflow for non-technical users
- Building a simple web application
- Working with cloud databases
- Learning SQL through real product data
- Thinking about AI model selection and tradeoffs
- Measuring product usefulness over time
- Turning a product idea into a portfolio-ready GitHub project

## Long-Term Goal

The long-term goal for Social-Strata is to become a practical AI support tool for small businesses that want better Instagram content without needing a social media team.

The project starts small with captions and hashtags, but it is designed to grow into a broader product relevance and marketing intelligence system.

## Author

Built by Syeda as part of a technical product management and AI product engineering portfolio.

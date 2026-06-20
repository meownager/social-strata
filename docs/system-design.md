# System Design: Social-Strata

## Problem Being Solved

Social-Strata helps non-technical small business owners create better Instagram content from product photos.

The system starts with an image, builds product relevance, then generates a caption and hashtags that match the product context.

## Functional Requirements

### Phase 1

- User can upload a product photo
- User can optionally add a short product or business note
- System can identify basic product context
- System can create a product relevance profile
- System can return one caption
- System can return 5 or 6 hashtags
- System can save generated output metadata to Supabase

### Future Phases

- System can suggest product photography improvements
- System can support AI-assisted image enhancement
- System can store optional Instagram performance data
- System can support SQL analysis over product and marketing data

## Non-Functional Requirements

- Simple enough for non-technical users
- Phase 1 output should appear in under 30 seconds for normal use
- Cloud-based storage for data and future assets
- No heavy files stored in GitHub
- Free or free-tier services wherever possible
- Modular design so models can change later

## Core Data Objects

### Product Context

This is what the image understanding layer returns.

Example:

```json
{
  "product_category": "handmade candle",
  "visible_attributes": ["glass jar", "neutral label", "warm tone"],
  "style": "minimal and cozy",
  "likely_use_case": "home decor or gifting",
  "confidence": "medium"
}
```

### Relevance Profile

This is what the relevance engine builds from the product context.

Example:

```json
{
  "audience": "home decor shoppers and gift buyers",
  "buyer_intent": "comfort, atmosphere, thoughtful gifting",
  "caption_angle": "make the room feel warmer",
  "tone": "warm and simple",
  "hashtag_themes": ["home decor", "candles", "cozy lifestyle", "small business"]
}
```

### Generated Output

This is what the user sees.

Example:

```json
{
  "caption": "A small detail that changes the whole mood of the room.",
  "hashtags": ["#handmadecandle", "#cozyhome", "#homedecor", "#smallbusiness", "#giftideas"]
}
```

## Relevance Engine Design

The relevance engine is the most important part of the product.

It should not simply ask for a caption from the image model. It should first organize the product context into fields that explain why the output makes sense.

Suggested internal steps:

1. Identify product category
2. Extract visible product attributes
3. Guess likely audience
4. Identify buyer intent
5. Select caption angle
6. Select hashtag themes
7. Generate caption and hashtags from those fields

This makes the system easier to debug and easier to improve in future phases.

## Caption Design

The caption should be created from the relevance profile.

Rules for Phase 1:

- Return one caption only
- Keep it short
- Avoid sounding too corporate
- Avoid overpromising
- Match the product category and audience
- Make it easy to copy

## Hashtag Design

The hashtag output should be limited to 5 or 6 hashtags.

Hashtag mix:

- 1 or 2 product category hashtags
- 1 or 2 audience or lifestyle hashtags
- 1 small business or niche hashtag
- 1 caption-angle hashtag if useful

The goal is not maximum quantity. The goal is relevance.

## Database Design Direction

Phase 1 should store generated output data, even before full analytics exists.

Suggested tables:

- `generated_outputs`
- `product_contexts`
- `user_feedback` later
- `instagram_metrics` later

The early schema should support SQL questions like:

```sql
select product_category, count(*)
from generated_outputs
group by product_category
order by count(*) desc;
```

Future SQL questions:

```sql
select product_category, avg(likes) as avg_likes
from instagram_metrics
group by product_category
order by avg_likes desc;
```

## Model Selection Direction

The model choice should follow the product need.

For Phase 1, the model needs to understand product images well enough to create useful product context. It does not need to do everything.

Selection criteria:

- Has a free or free-tier option
- Accepts image input
- Works from a hosted app
- Has simple Python support
- Can be replaced later without rewriting the whole app

The code should hide model-specific details behind an image understanding function so the rest of the app does not depend on one provider.

## Why SQL Matters Here

SQL is how Social-Strata becomes measurable.

At first, SQL will help answer simple product questions:

- What product categories are users uploading?
- What caption angles are most common?
- What hashtags are generated most often?

Later, SQL can connect outputs to performance:

- Which hashtags appear in higher-performing posts?
- Which product categories get better engagement?
- Which caption tones are associated with more saves or comments?

This turns the project from a one-time generator into a product learning loop.

## System Boundaries

### In Scope For Phase 1

- Product image upload
- Product context extraction
- Relevance profile
- Caption and hashtag generation
- Supabase metadata storage

### Out Of Scope For Phase 1

- Instagram scraping
- Automatic posting
- Account management
- Paid marketing analytics
- Advanced image editing
- Full strategy recommendations

## Build Principle

Start with a working small system. Then improve the model, relevance logic, storage, and analysis one layer at a time.

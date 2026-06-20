# Social-Strata: Project Plan

## 1. Vision

Social-Strata is a product relevance tool for small business owners who need practical Instagram content support. The user uploads a product photo, and the app returns content that is easy to understand, easy to copy, and relevant to the product.

The long-term idea is not just caption generation. The long-term idea is a small business support system that connects product images, social media positioning, visual improvement, and SQL-based learning over time.

## 2. What We Are Building First

The first version is intentionally small.

The user uploads one product photo. The app identifies the product context, builds a relevance profile, then returns:

- One catchy caption
- Five or six relevant hashtags

The result should feel useful to a non-technical person within one screen.

## 3. Why This Order

The product has three natural layers:

1. Content support
2. Product photo support
3. Marketing analysis

Caption and hashtag support comes first because it gives the user immediate value. Photo enhancement comes second because the user needs better visual presentation. SQL analysis comes third because meaningful analysis needs stored data over time.

## 4. Phase 1 Scope

### User Workflow

```text
Open app
   |
Upload product photo
   |
Optionally add product note
   |
Click generate
   |
Review caption and hashtags
   |
Copy output for Instagram
```

### System Workflow

```text
Image upload
   |
Image understanding
   |
Product relevance profile
   |
Caption generation
   |
Hashtag generation
   |
Save output metadata to Supabase
   |
Display copy-ready result
```

### Phase 1 Deliverables

- Streamlit app
- Product image upload component
- Relevance engine module
- Caption generation module
- Hashtag generation module
- Supabase schema for generated outputs
- Basic tests for relevance and output formatting
- README and architecture docs that match the working product

## 5. Phase 1 Non-Goals

- No Instagram scraping
- No automatic posting
- No paid subscription requirement
- No full user accounts
- No advanced analytics dashboard
- No image editing yet
- No local storage of heavy image files

## 6. Phase 2 Plan

Phase 2 adds product design and photography support.

Planned features:

- Product photo quality feedback
- Suggestions for lighting, background, framing, and styling
- AI-assisted product image enhancement if a free or free-tier option is practical
- Before and after comparison if image editing becomes available

Phase 2 success means the user not only gets better captions and hashtags, but also understands how to make the product look better before posting.

## 7. Phase 3 Plan

Phase 3 adds SQL-based marketing analysis.

Planned features:

- Store generated output history
- Store product relevance fields
- Store optional user-entered Instagram metrics
- Analyze content patterns using SQL
- Identify which product categories, caption angles, and hashtags appear strongest over time

This is the phase where the product becomes a learning system.

## 8. Tech Stack

| Layer | Tool |
|---|---|
| App interface | Streamlit |
| Cloud database | Supabase PostgreSQL |
| Cloud file storage | Supabase Storage |
| SQL learning and analysis | PostgreSQL SQL |
| Image understanding | Free or free-tier multimodal model |
| Deployment | Free cloud hosting where possible |

## 9. Risks And Mitigations

### Risk: Instagram research can become messy

Direct scraping is not the Phase 1 path. Phase 1 will use a relevance engine built from product category, audience, tone, visual attributes, and hashtag themes. Instagram data access can be revisited later through safe and approved methods.

### Risk: The model may misread the image

Phase 1 should keep the product category visible in the output and later allow the user to correct it. This makes the system easier to debug and more trustworthy.

### Risk: The app becomes too complicated for the end user

Every screen should be judged by one question: can a non-technical small business owner understand what to do next?

### Risk: Free cloud tools have limits

The system should keep calls small, store only what is needed, and avoid heavy assets in GitHub.

## 10. First Build Sequence

1. Update docs and schema
2. Add Streamlit app shell
3. Add image upload
4. Add placeholder relevance engine
5. Add caption and hashtag outputs
6. Connect Supabase for output metadata
7. Replace placeholder image understanding with a free-tier multimodal call
8. Add tests
9. Deploy a demo

## 11. Definition Of Done For Phase 1

Phase 1 is done when a user can open the app, upload a product image, click one button, and receive one caption plus 5 or 6 hashtags in a copy-friendly format.

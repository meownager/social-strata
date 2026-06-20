# Architecture: Social-Strata

## What We Are Building

Social-Strata is an image-first social media support tool for small business owners. The user uploads a product photo, and the system returns a caption and hashtags that are built around the product context.

The architecture is designed to stay simple in Phase 1 while leaving room for product photo enhancement and SQL-based marketing analysis later.

## End-To-End Flow

```text
Product photo upload
        |
        v
Streamlit UI
        |
        v
Image understanding
        |
        v
Product relevance engine
        |
        +----------------+
        |                |
        v                v
Caption generator   Hashtag generator
        |                |
        +--------+-------+
                 |
                 v
        Copy-ready output
                 |
                 v
              Supabase
```

## Components

### 1. Streamlit UI

Streamlit is the user-facing app. It keeps the interface simple:

- Upload product photo
- Optional product or business note
- Generate output
- Copy caption and hashtags

The UI should avoid technical language. The user should not need to understand AI models, SQL, or backend services.

### 2. Image Understanding Layer

This layer looks at the uploaded product image and extracts useful context.

Example fields:

- Product category
- Visible product attributes
- Style or aesthetic
- Likely use case
- Possible audience
- Confidence or uncertainty notes

Phase 1 can use a free or free-tier multimodal model. The implementation should keep this layer replaceable so the model can change later.

### 3. Product Relevance Engine

This is the core of Social-Strata.

The relevance engine turns product context into marketing context. It should produce fields like:

- Product category
- Buyer intent
- Audience type
- Caption angle
- Tone
- Hashtag themes
- Differentiators

This layer matters because it prevents the app from becoming a generic caption generator.

### 4. Caption Generator

The caption generator uses the relevance profile to produce one Instagram-ready caption.

The caption should be:

- Short enough to use immediately
- Catchy but not exaggerated
- Connected to the product
- Suitable for a small business voice

### 5. Hashtag Generator

The hashtag generator returns 5 or 6 hashtags.

The hashtags should connect to:

- The product category
- The caption angle
- The likely audience
- The broader Instagram positioning

The app should avoid returning a long list of weak hashtags.

### 6. Supabase

Supabase is the cloud data layer.

Phase 1 stores generated output metadata. Later phases can store image references, user feedback, and performance metrics.

The GitHub repo should store code and lightweight docs only. Heavy images and generated assets belong in cloud storage.

## Data Flow

```text
Uploaded image
   |
Temporary processing in app session
   |
Image understanding result
   |
Product relevance profile
   |
Caption and hashtags
   |
Supabase row for generated output
   |
User copies result
```

## Cloud Storage Boundary

The product direction is cloud-based.

- Code lives in GitHub.
- Generated metadata lives in Supabase PostgreSQL.
- Product images, if stored later, live in Supabase Storage.
- Heavy images should not be committed to GitHub.

## Future Architecture

### Phase 2 Extension

```text
Product photo
   |
Image quality review
   |
Design and styling suggestions
   |
Optional AI enhancement
   |
Improved product image for posting
```

### Phase 3 Extension

```text
Generated outputs
   |
Optional user-entered Instagram metrics
   |
SQL analysis
   |
Marketing pattern discovery
   |
Future strategy recommendations
```

## Design Principle

Each layer should do one clear job. That makes the system easier to explain, test, replace, and improve.

# Supabase Setup

Social-Strata uses Supabase as the cloud database for generated social media outputs.

The goal is simple: the app should save useful generated results without storing heavy product images in GitHub or local project files.

## What Supabase Does In This Project

Supabase is a cloud platform built on PostgreSQL. For Social-Strata, it gives the app a place to save structured data that can later be analyzed with SQL.

In Phase 1, Supabase stores:

- Product category
- Detected product attributes
- Relevance profile
- Caption
- Hashtags
- Full copy-ready social media post
- Creation time

In Phase 3, this same database will support marketing analysis through SQL.

## Local Environment Variables

The app reads Supabase settings from a local `.env` file.

The `.env` file should stay on the local machine and should never be committed to GitHub.

Required values:

```bash
SUPABASE_URL=https://your-project-ref.supabase.co
SUPABASE_KEY=your_anon_public_key_here
```

For this project, the URL format is:

```bash
SUPABASE_URL=https://vwdawxydupkgjeolooiu.supabase.co
```

The key should be the anon or publishable key from Supabase. Do not use the service role key in the Streamlit app.

## Database Table

The Phase 1 table is `public.generated_outputs`.

It is created from:

```text
data/schema.sql
```

Run that SQL in the Supabase SQL Editor before testing the app connection.

## Row Level Security

Supabase uses Row Level Security, also called RLS, to control who can read and write data.

For this Phase 1 app, the anon key needs permission to insert generated outputs and read from the table for the connection check.

The current setup allows:

- Insert generated outputs
- Read generated outputs for connection checks and future review

This is acceptable for the early prototype because the app does not have user accounts yet. Later, when business accounts are added, the policy should become stricter so each business can only access its own rows.

## Connection Test

Run the app locally:

```bash
streamlit run src/app.py
```

Then use the sidebar button:

```text
Check Supabase connection
```

Expected success message:

```text
Supabase is connected.
```

## Save Test

To confirm the full save flow:

1. Upload a product image.
2. Add an optional product note.
3. Generate the caption and hashtags.
4. Confirm the app says the output was saved to the database.

Then check Supabase with:

```sql
select id, product_category, caption, hashtags, created_at
from public.generated_outputs
order by created_at desc
limit 5;
```

If rows appear, the Streamlit app and Supabase database are connected correctly.

## Free-Tier Notes

This setup is designed for free-tier use:

- Streamlit Community Cloud for public app hosting
- Supabase free plan for cloud database storage
- Local `.env` for secrets during development

To stay free, do not enable paid Supabase features or billing upgrades unless the product later needs them.

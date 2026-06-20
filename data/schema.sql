-- Social-Strata Database Schema
-- Run this in the Supabase SQL Editor.

-- Required for UUID generation in PostgreSQL.
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Each generated app result starts with an uploaded product image.
-- Phase 1 stores metadata and optional cloud storage paths, not heavy files in GitHub.
CREATE TABLE IF NOT EXISTS product_uploads (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  image_path TEXT,
  original_filename TEXT,
  product_note TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Product context extracted from the image understanding layer.
CREATE TABLE IF NOT EXISTS product_contexts (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  upload_id UUID REFERENCES product_uploads(id) ON DELETE CASCADE,
  product_category TEXT,
  visible_attributes JSONB,
  style_notes TEXT,
  likely_use_case TEXT,
  confidence TEXT,
  raw_model_response JSONB,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Relevance profile used to generate the final caption and hashtags.
CREATE TABLE IF NOT EXISTS relevance_profiles (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  upload_id UUID REFERENCES product_uploads(id) ON DELETE CASCADE,
  audience TEXT,
  buyer_intent TEXT,
  caption_angle TEXT,
  tone TEXT,
  hashtag_themes JSONB,
  differentiators JSONB,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Copy-ready output shown to the user.
CREATE TABLE IF NOT EXISTS generated_outputs (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  upload_id UUID REFERENCES product_uploads(id) ON DELETE CASCADE,
  product_context_id UUID REFERENCES product_contexts(id) ON DELETE SET NULL,
  relevance_profile_id UUID REFERENCES relevance_profiles(id) ON DELETE SET NULL,
  caption TEXT NOT NULL,
  hashtags JSONB NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Optional user feedback for improving output quality later.
CREATE TABLE IF NOT EXISTS user_feedback (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  generated_output_id UUID REFERENCES generated_outputs(id) ON DELETE CASCADE,
  usefulness_rating INTEGER CHECK (usefulness_rating BETWEEN 1 AND 5),
  feedback_note TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- Phase 3 table for manually entered Instagram metrics.
CREATE TABLE IF NOT EXISTS instagram_metrics (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  generated_output_id UUID REFERENCES generated_outputs(id) ON DELETE CASCADE,
  likes INTEGER,
  comments INTEGER,
  saves INTEGER,
  reach INTEGER,
  impressions INTEGER,
  recorded_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_product_contexts_upload_id ON product_contexts(upload_id);
CREATE INDEX IF NOT EXISTS idx_relevance_profiles_upload_id ON relevance_profiles(upload_id);
CREATE INDEX IF NOT EXISTS idx_generated_outputs_upload_id ON generated_outputs(upload_id);
CREATE INDEX IF NOT EXISTS idx_instagram_metrics_generated_output_id ON instagram_metrics(generated_output_id);

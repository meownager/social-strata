-- Social-Strata Database Schema
-- Run this in the Supabase SQL Editor.

-- Required for UUID generation in PostgreSQL.
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Phase 1 stores one copy-ready social media result per generation.
-- Images stay out of GitHub and heavy local storage. The app stores only the
-- product context, relevance profile, final post, and hashtags needed for reuse.
CREATE TABLE IF NOT EXISTS generated_outputs (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  product_category TEXT NOT NULL,
  visible_attributes JSONB DEFAULT '[]'::jsonb,
  style_notes TEXT,
  likely_use_case TEXT,
  confidence TEXT,
  audience TEXT,
  buyer_intent TEXT,
  caption_angle TEXT,
  tone TEXT,
  hashtag_themes JSONB DEFAULT '[]'::jsonb,
  campaign_style TEXT,
  event_details JSONB DEFAULT '{}'::jsonb,
  caption TEXT NOT NULL,
  hashtags JSONB NOT NULL,
  social_media_post TEXT NOT NULL,
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
-- This will support SQL analysis without depending on paid Instagram APIs.
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

CREATE INDEX IF NOT EXISTS idx_generated_outputs_product_category ON generated_outputs(product_category);
CREATE INDEX IF NOT EXISTS idx_generated_outputs_campaign_style ON generated_outputs(campaign_style);
CREATE INDEX IF NOT EXISTS idx_generated_outputs_created_at ON generated_outputs(created_at);
CREATE INDEX IF NOT EXISTS idx_instagram_metrics_generated_output_id ON instagram_metrics(generated_output_id);

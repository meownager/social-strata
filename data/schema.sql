-- Social-Strata Database Schema
-- Run this in Supabase SQL Editor

-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Business profiles
CREATE TABLE businesses (
  id          UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name        TEXT NOT NULL,
  niche       TEXT,
  tone        TEXT,
  audience    TEXT,
  created_at  TIMESTAMP DEFAULT now()
);

-- Hashtag seed table with embeddings
CREATE TABLE hashtags (
  id          UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  tag         TEXT NOT NULL,
  niche       TEXT,
  embedding   VECTOR(384),
  created_at  TIMESTAMP DEFAULT now()
);

-- Generated content history
CREATE TABLE generated_content (
  id                UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  business_id       UUID REFERENCES businesses(id),
  post_context      TEXT,
  caption           TEXT,
  hashtag_clusters  JSONB,
  created_at        TIMESTAMP DEFAULT now()
);

-- Index for fast vector similarity search
CREATE INDEX ON hashtags USING ivfflat (embedding vector_cosine_ops);

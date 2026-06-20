"""Placeholder relevance logic for the first runnable Social-Strata slice.

This module is intentionally simple. It gives the Streamlit app a working
product flow before external image models and database services are added.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ProductContext:
    product_category: str
    visible_attributes: list[str]
    style_notes: str
    likely_use_case: str
    confidence: str


@dataclass(frozen=True)
class RelevanceProfile:
    audience: str
    buyer_intent: str
    caption_angle: str
    tone: str
    hashtag_themes: list[str]


@dataclass(frozen=True)
class GeneratedOutput:
    caption: str
    hashtags: list[str]


CATEGORY_KEYWORDS: dict[str, list[str]] = {
    "candle": ["candle", "scent", "soy", "wax"],
    "jewelry": ["jewelry", "ring", "necklace", "bracelet", "earring"],
    "skincare": ["skin", "cream", "serum", "lotion", "soap"],
    "modest fashion": ["hijab", "abaya", "dress", "scarf", "modest"],
    "coffee": ["coffee", "mug", "beans", "latte"],
    "bakery": ["cake", "cookie", "bread", "bakery", "cupcake"],
}


HASHTAG_BANK: dict[str, list[str]] = {
    "candle": ["#handmadecandle", "#cozyhome", "#homedecor", "#giftideas", "#smallbusiness"],
    "jewelry": ["#handmadejewelry", "#minimaljewelry", "#everydaystyle", "#giftideas", "#smallbusiness"],
    "skincare": ["#skincare", "#selfcare", "#glowingskin", "#cleanbeauty", "#smallbusiness"],
    "modest fashion": ["#modestfashion", "#hijabstyle", "#everydaymodesty", "#minimalstyle", "#smallbusiness"],
    "coffee": ["#coffeelover", "#coffeetime", "#localcoffee", "#morningroutine", "#smallbusiness"],
    "bakery": ["#freshbaked", "#bakerylove", "#sweettreats", "#localbakery", "#smallbusiness"],
    "product": ["#smallbusiness", "#shoplocal", "#productphotography", "#giftideas", "#supportsmallbusiness"],
}


def identify_product_context(filename: str, image_size: tuple[int, int], product_note: str = "") -> ProductContext:
    """Infer basic product context from filename and optional user note."""
    text = f"{Path(filename).stem} {product_note}".lower()
    product_category = "product"

    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            product_category = category
            break

    width, height = image_size
    orientation = "portrait" if height > width else "landscape" if width > height else "square"

    return ProductContext(
        product_category=product_category,
        visible_attributes=[orientation, "uploaded product photo"],
        style_notes="Clean product-focused visual. More detailed image understanding will be added in the next build step.",
        likely_use_case=_likely_use_case(product_category),
        confidence="starter",
    )


def build_relevance_profile(context: ProductContext, product_note: str = "") -> RelevanceProfile:
    """Turn product context into marketing relevance fields."""
    category = context.product_category

    if category == "candle":
        return RelevanceProfile(
            audience="home decor shoppers and thoughtful gift buyers",
            buyer_intent="comfort, atmosphere, and gifting",
            caption_angle="make an ordinary room feel warmer",
            tone="warm and calm",
            hashtag_themes=["home decor", "candles", "cozy lifestyle", "small business"],
        )
    if category == "jewelry":
        return RelevanceProfile(
            audience="style-conscious shoppers looking for everyday pieces",
            buyer_intent="personal style, gifting, and small details",
            caption_angle="small detail that completes the look",
            tone="polished and simple",
            hashtag_themes=["jewelry", "style", "gifting", "small business"],
        )
    if category == "skincare":
        return RelevanceProfile(
            audience="self-care buyers and beauty shoppers",
            buyer_intent="routine, care, and confidence",
            caption_angle="make self-care feel easy and consistent",
            tone="fresh and reassuring",
            hashtag_themes=["skincare", "self care", "beauty", "small business"],
        )
    if category == "modest fashion":
        return RelevanceProfile(
            audience="modest fashion shoppers looking for comfort and style",
            buyer_intent="coverage, confidence, and everyday wear",
            caption_angle="feel put together without overthinking the outfit",
            tone="confident and graceful",
            hashtag_themes=["modest fashion", "hijab style", "everyday style", "small business"],
        )
    if category == "coffee":
        return RelevanceProfile(
            audience="coffee lovers and local cafe customers",
            buyer_intent="routine, energy, and comfort",
            caption_angle="turn the day around with a better cup",
            tone="friendly and warm",
            hashtag_themes=["coffee", "morning routine", "local business", "small business"],
        )
    if category == "bakery":
        return RelevanceProfile(
            audience="local food lovers and gift buyers",
            buyer_intent="treats, celebration, and comfort",
            caption_angle="bring something sweet to the moment",
            tone="warm and inviting",
            hashtag_themes=["bakery", "dessert", "local food", "small business"],
        )

    note_hint = f" inspired by {product_note.strip()}" if product_note.strip() else ""
    return RelevanceProfile(
        audience="small business customers and product discovery shoppers",
        buyer_intent=f"discovering a useful or thoughtful product{note_hint}",
        caption_angle="help the product feel clear, useful, and worth noticing",
        tone="clear and friendly",
        hashtag_themes=["small business", "product discovery", "shop local", "gift ideas"],
    )


def generate_output(context: ProductContext, profile: RelevanceProfile) -> GeneratedOutput:
    """Generate one caption and 5 or 6 hashtags from the relevance profile."""
    category = context.product_category
    caption = (
        f"A simple product with a clear purpose: {profile.caption_angle}. "
        f"Made for people who care about {profile.buyer_intent}."
    )
    hashtags = HASHTAG_BANK.get(category, HASHTAG_BANK["product"])

    return GeneratedOutput(caption=caption, hashtags=hashtags[:6])


def _likely_use_case(category: str) -> str:
    use_cases = {
        "candle": "home decor, gifting, and cozy lifestyle content",
        "jewelry": "everyday styling, gifting, and outfit detail content",
        "skincare": "self-care routines and beauty content",
        "modest fashion": "outfit styling and everyday fashion content",
        "coffee": "daily routine and local cafe content",
        "bakery": "food, celebration, and local treat content",
    }
    return use_cases.get(category, "product promotion and small business content")

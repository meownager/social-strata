"""Starter relevance logic for the first runnable Social-Strata slice.

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


@dataclass(frozen=True)
class EventDetails:
    location: str = ""
    dates: str = ""
    time: str = ""
    closing_line: str = ""


CATEGORY_KEYWORDS: dict[str, list[str]] = {
    "candle": ["candle", "scent", "soy", "wax"],
    "jewelry": ["jewelry", "ring", "necklace", "bracelet", "earring"],
    "skincare": ["skin", "cream", "serum", "lotion", "soap"],
    "hijab": ["hijab", "khimar", "shayla"],
    "modest fashion": ["abaya", "dress", "scarf", "modest"],
    "coffee": ["coffee", "mug", "beans", "latte"],
    "bakery": ["cake", "cookie", "bread", "bakery", "cupcake"],
}


FABRIC_KEYWORDS: dict[str, list[str]] = {
    "modal": ["modal"],
    "satin": ["satin"],
    "chiffon": ["chiffon"],
    "jersey": ["jersey"],
    "silk": ["silk"],
}


STYLE_KEYWORDS: dict[str, list[str]] = {
    "printed": ["print", "printed"],
    "lace": ["lace"],
    "summer": ["summer", "heat", "breathable", "lightweight"],
    "non-slip": ["non-slip", "nonslip", "no slip"],
}


HASHTAG_BANK: dict[str, list[str]] = {
    "candle": ["#handmadecandle", "#cozyhome", "#homedecor", "#giftideas", "#smallbusiness"],
    "jewelry": ["#handmadejewelry", "#minimaljewelry", "#everydaystyle", "#giftideas", "#smallbusiness"],
    "skincare": ["#skincare", "#selfcare", "#glowingskin", "#cleanbeauty", "#smallbusiness"],
    "hijab": ["#hijab", "#hijabfashion", "#hijabstyle", "#modesty", "#modestfashion"],
    "modest fashion": ["#modestfashion", "#hijabstyle", "#everydaymodesty", "#minimalstyle", "#smallbusiness"],
    "coffee": ["#coffeelover", "#coffeetime", "#localcoffee", "#morningroutine", "#smallbusiness"],
    "bakery": ["#freshbaked", "#bakerylove", "#sweettreats", "#localbakery", "#smallbusiness"],
    "product": ["#smallbusiness", "#shoplocal", "#productphotography", "#giftideas", "#supportsmallbusiness"],
}


def identify_product_context(filename: str, image_size: tuple[int, int], product_note: str = "") -> ProductContext:
    """Infer starter product context from filename and optional user note."""
    text = f"{Path(filename).stem} {product_note}".lower()
    product_category = "product"

    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            product_category = category
            break

    width, height = image_size
    orientation = "portrait" if height > width else "landscape" if width > height else "square"
    attributes = [orientation, "uploaded product photo"]
    attributes.extend(_matching_labels(text, FABRIC_KEYWORDS))
    attributes.extend(_matching_labels(text, STYLE_KEYWORDS))

    return ProductContext(
        product_category=product_category,
        visible_attributes=attributes,
        style_notes=_style_notes(product_category, attributes),
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
    if category == "hijab":
        return RelevanceProfile(
            audience="students, working women, and modest fashion shoppers",
            buyer_intent=_hijab_buyer_intent(context.visible_attributes),
            caption_angle=_hijab_caption_angle(context.visible_attributes),
            tone="confident, comfortable, simple, and graceful",
            hashtag_themes=["hijab", "hijab fashion", "hijab style", "modesty", "modest fashion"],
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
    if context.product_category == "hijab":
        caption = _hijab_caption(context, profile)
    else:
        caption = (
            f"A simple product with a clear purpose: {profile.caption_angle}. "
            f"Made for people who care about {profile.buyer_intent}."
        )

    hashtags = _hashtags_for_context(context)
    return GeneratedOutput(caption=caption, hashtags=hashtags[:6])


def format_event_block(event_details: EventDetails) -> str:
    """Format optional event details for copy-ready Instagram captions."""
    lines = []
    if event_details.location.strip():
        lines.append(f"Location: {event_details.location.strip()}")
    if event_details.dates.strip():
        lines.append(f"Dates: {event_details.dates.strip()}")
    if event_details.time.strip():
        lines.append(f"Time: {event_details.time.strip()}")
    if event_details.closing_line.strip():
        lines.append(event_details.closing_line.strip())
    return "\n".join(lines)


def append_event_details(caption: str, event_details: EventDetails) -> str:
    """Append event information only when the user provides it."""
    event_block = format_event_block(event_details)
    if not event_block:
        return caption
    return f"{caption}\n\n{event_block}"


def _matching_labels(text: str, options: dict[str, list[str]]) -> list[str]:
    return [label for label, keywords in options.items() if any(keyword in text for keyword in keywords)]


def _style_notes(category: str, attributes: list[str]) -> str:
    if category == "hijab":
        details = ", ".join(attribute for attribute in attributes if attribute not in {"portrait", "landscape", "square", "uploaded product photo"})
        if details:
            return f"Hijab product with {details} details. Position around comfort, practical styling, and everyday elegance."
        return "Hijab product. Position around comfort, practical styling, and everyday elegance."
    return "Clean product-focused visual. More detailed image understanding will be added in the next build step."


def _hijab_buyer_intent(attributes: list[str]) -> str:
    intent = ["comfort", "modesty", "everyday elegance"]
    if "modal" in attributes:
        intent.append("soft breathable fabric")
    if "satin" in attributes:
        intent.append("smooth polished styling")
    if "chiffon" in attributes:
        intent.append("lightweight drape")
    if "summer" in attributes:
        intent.append("heat-friendly wear")
    return ", ".join(intent)


def _hijab_caption_angle(attributes: list[str]) -> str:
    if "summer" in attributes or "modal" in attributes:
        return "stay cool and put together without compromising comfort"
    if "satin" in attributes:
        return "add a polished finish to everyday modest outfits"
    if "chiffon" in attributes:
        return "keep the look light, graceful, and easy to style"
    return "feel comfortable and confident in everyday modest style"


def _hijab_caption(context: ProductContext, profile: RelevanceProfile) -> str:
    fabric = next((attribute for attribute in context.visible_attributes if attribute in FABRIC_KEYWORDS), "hijab")
    if fabric == "modal":
        return (
            "Meet your new everyday staple: soft modal that breathes with you, "
            "drapes beautifully, and keeps you feeling confident through busy summer days."
        )
    if fabric == "satin":
        return (
            "Soft shine, smooth drape, and an easy polished finish. "
            "A satin hijab made for days when simple still needs to feel special."
        )
    if fabric == "chiffon":
        return (
            "Light, graceful, and easy to style. "
            "A chiffon hijab made for effortless modest looks from morning to evening."
        )
    return f"A hijab made for {profile.buyer_intent}. {profile.caption_angle.capitalize()}."


def _hashtags_for_context(context: ProductContext) -> list[str]:
    hashtags = list(HASHTAG_BANK.get(context.product_category, HASHTAG_BANK["product"]))
    for attribute in context.visible_attributes:
        if attribute in FABRIC_KEYWORDS:
            fabric_tag = f"#{attribute.title().replace(' ', '')}Hijab"
            if fabric_tag not in hashtags:
                hashtags.append(fabric_tag)
    return hashtags


def _likely_use_case(category: str) -> str:
    use_cases = {
        "candle": "home decor, gifting, and cozy lifestyle content",
        "jewelry": "everyday styling, gifting, and outfit detail content",
        "skincare": "self-care routines and beauty content",
        "hijab": "everyday modest fashion content for school, work, events, and daily wear",
        "modest fashion": "outfit styling and everyday fashion content",
        "coffee": "daily routine and local cafe content",
        "bakery": "food, celebration, and local treat content",
    }
    return use_cases.get(category, "product promotion and small business content")

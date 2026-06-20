from __future__ import annotations

from PIL import Image
import streamlit as st

from relevance_engine import (
    EventDetails,
    append_event_details,
    build_relevance_profile,
    generate_output,
    identify_product_context,
)


st.set_page_config(page_title="Social-Strata", page_icon="SS", layout="centered")

st.title("Social-Strata")
st.caption("Upload a product photo and generate a caption plus focused hashtags.")

uploaded_file = st.file_uploader(
    "Upload a product photo",
    type=["png", "jpg", "jpeg", "webp"],
)

product_note = st.text_input(
    "Optional product note",
    placeholder="Example: handmade candle, satin hijab, skincare serum",
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded product photo", width="stretch")

    with st.expander("Optional event details"):
        event_location = st.text_input("Event location", placeholder="Example: Al-Huda, Fishers")
        event_dates = st.text_input("Event dates", placeholder="Example: June 19 and 26, 2026")
        event_time = st.text_input("Event time", placeholder="Example: 1 PM - 4 PM")
        event_closing = st.text_input("Closing line", placeholder="Example: See you there")

    if st.button("Generate caption and hashtags", type="primary"):
        context = identify_product_context(
            filename=uploaded_file.name,
            image_size=image.size,
            product_note=product_note,
        )
        profile = build_relevance_profile(context, product_note=product_note)
        output = generate_output(context, profile)
        event_details = EventDetails(
            location=event_location,
            dates=event_dates,
            time=event_time,
            closing_line=event_closing,
        )
        caption = append_event_details(output.caption, event_details)

        st.subheader("Product Context")
        st.write(f"Product category: {context.product_category.title()}")
        st.write(f"Likely use case: {context.likely_use_case}")

        st.subheader("Caption")
        st.text_area("Copy caption", caption, height=160)

        st.subheader("Hashtags")
        st.text_area("Copy hashtags", " ".join(output.hashtags), height=90)

        with st.expander("Relevance profile"):
            st.write(f"Audience: {profile.audience}")
            st.write(f"Buyer intent: {profile.buyer_intent}")
            st.write(f"Caption angle: {profile.caption_angle}")
            st.write(f"Tone: {profile.tone}")
            st.write(f"Hashtag themes: {', '.join(profile.hashtag_themes)}")
else:
    st.info("Upload a product photo to start.")

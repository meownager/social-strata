from src.relevance_engine import (
    EventDetails,
    append_event_details,
    build_relevance_profile,
    format_event_block,
    generate_output,
    identify_product_context,
)


def test_generates_copy_ready_output_for_known_category() -> None:
    context = identify_product_context(
        filename="handmade-candle.jpg",
        image_size=(800, 1000),
        product_note="soy candle for cozy home decor",
    )
    profile = build_relevance_profile(context)
    output = generate_output(context, profile)

    assert context.product_category == "candle"
    assert output.caption
    assert 5 <= len(output.hashtags) <= 6
    assert all(tag.startswith("#") for tag in output.hashtags)


def test_unknown_product_still_gets_output() -> None:
    context = identify_product_context(filename="photo.jpg", image_size=(1000, 1000))
    profile = build_relevance_profile(context)
    output = generate_output(context, profile)

    assert context.product_category == "product"
    assert output.caption
    assert len(output.hashtags) == 5


def test_hijab_is_product_and_modal_is_fabric_attribute() -> None:
    context = identify_product_context(
        filename="printed-modal-lace-hijab.jpg",
        image_size=(900, 1200),
        product_note="soft breathable modal hijab for students and working women",
    )
    profile = build_relevance_profile(context)
    output = generate_output(context, profile)

    assert context.product_category == "hijab"
    assert "modal" in context.visible_attributes
    assert "lace" in context.visible_attributes
    assert "students" in profile.audience
    assert "soft modal" in output.caption
    assert "#ModalHijab" in output.hashtags


def test_hijab_fabric_can_change_without_changing_product_category() -> None:
    context = identify_product_context(
        filename="soft-satin-hijab.jpg",
        image_size=(900, 1200),
        product_note="satin hijab for polished everyday wear",
    )
    profile = build_relevance_profile(context)
    output = generate_output(context, profile)

    assert context.product_category == "hijab"
    assert "satin" in context.visible_attributes
    assert "polished" in output.caption
    assert "#SatinHijab" in output.hashtags


def test_event_details_are_appended_only_when_provided() -> None:
    caption = "Meet your new everyday staple."
    empty_details = EventDetails()
    event_details = EventDetails(
        location="Al-Huda, Fishers",
        dates="June 19 and 26, 2026",
        time="1 PM - 4 PM",
        closing_line="See you there",
    )

    assert append_event_details(caption, empty_details) == caption

    event_block = format_event_block(event_details)
    caption_with_event = append_event_details(caption, event_details)

    assert "Location: Al-Huda, Fishers" in event_block
    assert "Dates: June 19 and 26, 2026" in caption_with_event
    assert "Time: 1 PM - 4 PM" in caption_with_event
    assert caption_with_event.startswith(caption)

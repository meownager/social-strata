from src.relevance_engine import build_relevance_profile, generate_output, identify_product_context


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

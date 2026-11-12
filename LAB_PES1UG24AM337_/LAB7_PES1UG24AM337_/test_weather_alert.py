from hypothesis import given, strategies as st
from weather_alert import parse_reading, wind_category, rainfall_spread


@given(st.text() | st.none())
def test_parse_reading_no_crash(s):
    try:
        parse_reading(s)
    except Exception as e:
        assert False, f"parse_reading crashed with: {type(e).__name__}: {e}"


@given(st.text() | st.none())
def test_wind_category_no_crash(s):
    try:
        result = wind_category(s)
        assert result in ("warning", "advisory", "none", "invalid")
    except Exception as e:
        assert False, f"wind_category crashed with: {type(e).__name__}: {e}"


@given(st.text() | st.none())
def test_rainfall_spread_no_crash(s):
    try:
        rainfall_spread(s)
    except Exception as e:
        assert False, f"rainfall_spread crashed with: {type(e).__name__}: {e}"
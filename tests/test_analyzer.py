import pandas as pd
import pytest
from player_stats.analyzer import PlayerStatsAnalyzer

@pytest.fixture
def sample_df():
    data = {
        "short_name": ["A Player", "B Player", "C Player"],
        "pace": [90, 80, 70],
        "player_positions": ["ST", "CM", "ST"],
    }
    return pd.DataFrame(data)

def test_top_players(sample_df):
    analyzer = PlayerStatsAnalyzer(sample_df)
    top = analyzer.top_players("pace", n=2)
    assert len(top) == 2
    assert top.iloc[0]["pace"] == 90

def test_average_attribute_by_position(sample_df):
    analyzer = PlayerStatsAnalyzer(sample_df)
    avg = analyzer.average_attribute_by_position("pace", "ST")
    assert avg == pytest.approx((90 + 70) / 2)

def test_find_player(sample_df):
    analyzer = PlayerStatsAnalyzer(sample_df)
    result = analyzer.find_player("B pl")
    assert len(result) == 1
    assert result.iloc[0]["short_name"] == "B Player"

def test_invalid_attribute(sample_df):
    analyzer = PlayerStatsAnalyzer(sample_df)
    with pytest.raises(ValueError):
        analyzer.top_players("not_real_column")

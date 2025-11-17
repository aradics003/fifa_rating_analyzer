import os
import pandas as pd
from player_stats.loader import PlayerDataLoader
from player_stats.analyzer import PlayerStatsAnalyzer

def test_integration_real_csv():
    path = "FC26_20250921.csv"
    assert os.path.exists(path)

    loader = PlayerDataLoader(path)
    df = loader.load()

    analyzer = PlayerStatsAnalyzer(df)

    # Test basic real-data functionality
    top = analyzer.top_players("pace", n=3)
    assert len(top) == 3

    # There should be multiple midfielders
    avg = analyzer.average_attribute_by_position("passing", "CM")
    assert avg > 0

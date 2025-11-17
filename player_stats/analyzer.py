class PlayerStatsAnalyzer:
    def __init__(self, df):
        self.df = df

    def top_players(self, attribute, n=5):
        """
        Returns the top N players for a given numeric attribute.
        """
        if attribute not in self.df.columns:
            raise ValueError(f"Unknown attribute: {attribute}")

        return (
            self.df[["short_name", attribute]]
            .dropna()
            .sort_values(attribute, ascending=False)
            .head(n)
        )

    def average_attribute_by_position(self, attribute, position):
        """
        Computes the average of an attribute for a given position.
        """
        pos_df = self.df[self.df["player_positions"].str.contains(position, na=False)]
        if pos_df.empty:
            raise ValueError("No players found for this position")

        return pos_df[attribute].astype(float).mean()

    def find_player(self, name):
        """
        Case-insensitive partial name search.
        """
        result = self.df[self.df["short_name"].str.contains(name, case=False, na=False)]
        return result

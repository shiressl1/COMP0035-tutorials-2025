from importlib import resources
from pathlib import Path

import pandas as pd

from activities import data


def describe(df):
    """Uses pandas methods to describe the contents of a dataframe and prints the results

        Args:
           df (pd.DataFrame): Pandas dataframe

    """
    print("Shape: \n", df.shape)
    print("First 3 lines: \n", df.head(3))
    # Not complete! Follow the rest of the activities.


def main():
    # Activity 1: Method using importlib resources
    data_file_csv = resources.files(data).joinpath("paralympics_raw.csv")

    # Activity 1: Method using Pathlib.Path
    # Don't mix methods, this is just to show you different approaches!
    # data_file_xlsx = Path(__file__).parent.parent.joinpath("data", "paralympics_all_raw.xlsx")
    data_file_xlsx = resources.files(data).joinpath("paralympics_all_raw.xlsx")

    # Activity 2: Create a dataframe by reading in the data from csv
    paralympics_df = pd.read_csv(data_file_csv)

    # Activity 2: Create two further dataframes by reading in the data from xlsx
    games_df = pd.read_excel(data_file_xlsx, sheet_name="games")
    teams_df = pd.read_excel(data_file_xlsx, sheet_name="team_codes")

    # Activity 3: Describe the dataframe using pandas functions
    describe(paralympics_df)
    describe(games_df)
    describe(teams_df)


if __name__ == "__main__":
    main()

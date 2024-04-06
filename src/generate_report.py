"""
Generate report

Functions for assisting in generating reports.


"""
# import pandas as pd


def check_for_categorical(df, threshold=30, file=None):
    """
    check if there are

    Input:
        df: 2D pandas dataframe
        threshold (int, default 30):
            max number of unique values to show value counts
        file (str filepath, default None):
            if present, output is saved to a txt file, returns None

    Returns:
        if file=None, returns str
        if file, generates .txt file and returns None
    """

    output_string = ""

    for column in df.columns:
        unique_value_counts = df[column].value_counts().shape[0]

        header_string = f"{column:<15} {str(df[column].dtype):<15} " \
            f"{unique_value_counts}"

        if unique_value_counts > threshold:
            output_string += header_string + "\n"
        elif unique_value_counts <= threshold:

            output_string += "\n" + header_string + "\n"

            output_string += str(df[column].value_counts()) + "\n"

    if file:

        with open(file, mode='a', encoding="utf-8") as f:

            print(output_string, file=f)

    else:
        return output_string

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
            if present, report output is saved to a txt file
            if not present, report output is printed to stdout

    Returns:

        lst of categories that fall under threshold of unique responses
    """

    cat_list = []

    output_string = ""

    for column in df.columns:
        unique_value_counts = df[column].value_counts().shape[0]

        header_string = f"{column:<15} {str(df[column].dtype):<15} " \
            f"{unique_value_counts}"

        if unique_value_counts > threshold:
            output_string += header_string + "\n"
        elif unique_value_counts <= threshold:

            output_string += "\n" + header_string + "\n"

            output_string += str(df[column].value_counts()) + "\n\n"

            cat_list.append(column)

    if file:

        with open(file, 'a', encoding="utf-8") as f:

            print(output_string, file=f)

    else:
        print(output_string)

    return cat_list

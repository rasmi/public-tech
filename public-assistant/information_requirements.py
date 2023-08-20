"""Information requirements for each program."""
import io

import pandas as pd
import pdfplumber
import requests


def load_snap() -> str:
    """Load SNAP info requirements from PDF guide into a markdown table."""

    # pylint: disable-next=line-too-long
    snap_guide_url = "https://www.nyc.gov/assets/hra/downloads/pdf/services/accessibility/W-129G%20(E)%20SNAP%20Documentation%20Guide%20English%202015%20VERIFIED.pdf"
    snap_pdf = requests.get(snap_guide_url)

    with pdfplumber.open(io.BytesIO(snap_pdf.content)) as pdf:
        table_rows = []
        column_names = []
        for page in pdf.pages[:2]:
            table = page.extract_table()
            column_names = table[0]
            table_rows.extend(table[1:])

    guide_table = pd.DataFrame(table_rows, columns=column_names)
    guide_table["Helpful Tips"] = guide_table["Helpful Tips"].str.replace("\n", " ")
    guide_table["Eligibility Factor"] = guide_table["Eligibility Factor"].str.replace(
        "\n", ": ", 1
    )
    guide_table["Eligibility Factor"] = guide_table["Eligibility Factor"].str.replace(
        "\n", " "
    )
    guide_table["Suggested Documentation"] = guide_table[
        "Suggested Documentation"
    ].str.replace("\n", " ")

    guide_markdown = guide_table.to_markdown(index=False)

    return guide_markdown

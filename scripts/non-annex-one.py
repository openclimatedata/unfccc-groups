# Non Annex I parties

import pandas as pd

from shortcountrynames import to_name
from util import to_code, root


url = ("http://unfccc.int/parties_and_observers/"
       "parties/non_annex_i/items/2833.php")

non_annex_one = pd.read_html(url, attrs={'class': "list_table"})[0]

non_annex_one = non_annex_one.iloc[1:, 1]

non_annex_one.name = "Name"

non_annex_one = non_annex_one.apply(lambda x: x.replace(" **", ""))

non_annex_one.index = non_annex_one.apply(to_code)

non_annex_one = pd.Series(
    [to_name(code) for code in non_annex_one.index],
    index=non_annex_one.index
)

non_annex_one.index.name = "Code"
non_annex_one.name = "Name"

non_annex_one.to_csv(root / "data/non-annex-one.csv", header=True)

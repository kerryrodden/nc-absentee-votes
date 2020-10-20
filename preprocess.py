import pandas as pd

df = pd.read_csv("absentee_20201103.csv", encoding="ISO-8859-1")

grouped = df.groupby(["county_desc", "race", "ethnicity", "ballot_req_type", "ballot_request_party", "ballot_rtn_status"], as_index=False)["voter_reg_num"].count().rename(columns={"voter_reg_num": "count"})
grouped.to_csv("absentee_20201103_aggregated.csv", index=False)

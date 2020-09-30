# North Carolina Absentee Votes

Aggregated data on absentee ballots returned for the November 2020 election in North Carolina. As of late September, these represent vote-by-mail only, but early voting should also be represented when it starts in mid-October.

The original data is from the [North Carolina State Board of Elections](https://www.ncsbe.gov/results-data/absentee-data) and is updated daily. Their excellent website contains many useful aggregations of the data; this repo contains my own custom aggregation of the data, created via a Github Action.

Fields in the custom aggregation are: county name, race, ethnicity, ballot request party, and ballot return status. This makes it possible to analyze whether ballots are being accepted at different rates across groups.

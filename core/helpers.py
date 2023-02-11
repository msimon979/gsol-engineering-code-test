def overlap_calculator(latest_campaign, start_date, end_date):
    latest_start = max(latest_campaign.start_date, start_date)
    earliest_end = min(latest_campaign.end_date, end_date)

    delta = (earliest_end - latest_start).days + 1
    overlap = max(0, delta)

    return overlap

def estimate_shipping_time(month, day):
    est = 10
    if month == "December":
        est = est + 5
        if day >= 25:
            est = est + 5
    elif day <= 7:
        est = est - 3
    return est
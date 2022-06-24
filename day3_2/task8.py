def month_days(year, month):
    if month in {"Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"}:
        return 31
    elif month in {"Apr", "Jun", "Sen", "Noy"}:
        return 30
    else:
        if year % 4 == 0:
            return 29
        return 28

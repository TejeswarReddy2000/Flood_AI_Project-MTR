from datetime import date

def generate_flood_report(state, start_date, end_date, area):
    today = date.today()

    if area > 100:
        severity = "High"
    elif area > 20:
        severity = "Moderate"
    else:
        severity = "Low"

    report = f"""
Flood Analysis Report
Date Generated: {today}

State: {state}
Monitoring Period: {start_date} to {end_date}

Estimated Flooded Area: {area:.2f} sq km
Severity Level: {severity}

Summary:
The satellite analysis indicates {severity.lower()} flood conditions
in {state}. Authorities and residents should remain alert
and follow safety advisories.
"""
    return report

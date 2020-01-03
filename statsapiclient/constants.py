# flake8: noqa

API_HOST = "https://statsapi.web.nhl.com"
NHL_HOST = "http://www.nhl.com"

HEADERS = {
    "user-agent": ("Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"),
    "Dnt": ("1"),
    "Accept-Language": ("en"),
    "origin": ("https://statsapi.web.nhl.com"),
    "referer": ("https://www.nhl.com/"),
}

SCHEDULE_PARAMS = "schedule.teams,schedule.linescore,schedule.decisions,schedule.scoringplays"

SCHEDULE_DATE_FORMAT = {
    "display": "YYYY-MM-DD",
    "format": "%Y-%m-%d"
}

SEASON_YEARS = {
    "2019": "20192020",
    "2018": "20182019",
    "2017": "20172018",
    "2016": "20162017",
    "2015": "20152016",
    "2014": "20142015",
    "2013": "20132014",
}

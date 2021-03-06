from statsapiclient.schedule import Schedule


dates = [{
    "games": [
        {"gamePk": 1},
        {"gamePk": 2},
    ]
}, {
    "games": [
        {"gamePk": 3},
        {"gamePk": 4},
    ]
}]


class TestSchedule:
    def test_single_date(self):
        schedule = Schedule('2011-01-01')

        assert schedule.params["startDate"] == schedule.params["endDate"]

    def test_date_range(self):
        schedule = Schedule('2011-01-01', '2011-01-02')

        assert schedule.params["startDate"] != schedule.params["endDate"]

    def test_single_date_games(self):
        schedule = Schedule('2011-01-01')
        # TODO: Is it better to mock `fetch_json` here?
        schedule.games = [dates[0]["games"]]

        assert len(schedule.games) == 1

    def test_multiple_dates_get_games(self):
        schedule = Schedule('2011-01-01', '2011-01-02')
        # TODO: Is it better to mock `fetch_json` here?
        schedule.games = dates[0]["games"] + dates[1]["games"]

        assert len(schedule.games) == 4

from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSES_PER_RACE = 250_000
    SPONSORS = {
        "Oracle": {1: 1_500_000, 2: 800_000},
        "Honda": {8: 20_000, 10: 10_000}
    }

    @property
    def sponsors(self):
        return self.SPONSORS

    @property
    def expenses(self):
        return self.EXPENSES_PER_RACE

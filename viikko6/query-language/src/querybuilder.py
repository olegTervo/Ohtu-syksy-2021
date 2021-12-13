from matchers import And, HasAtLeast, PlaysIn, Not, All, HasFewerThan, Or

class QueryBuilder:
    def __init__(self):
        self._matchers = [All()]

    def playsIn(self, team):
        self._matchers.append(PlaysIn(team))
        return self

    def hasAtLeast(self, val, atr):
        self._matchers.append(HasAtLeast(val, atr))
        return self

    def hasFewerThan(self, val, atr):
        self._matchers.append(HasFewerThan(val, atr))
        return self

    def oneOf(self, *matchers):
        self._matchers.append(Or(*matchers))
        return self

    def build(self):
        ret = And(*self._matchers)
        self._matchers = [All()]
        
        return ret

class Grammar:
    def __init__(self, *rules):
        self.rules = tuple(self._parse(rule) for rule in rules)
        self._first = None
        self._follow = None

    def _parse(self, rule):
        def div(rule):
            name, *arr = rule
            return (name, arr)

        return div(tuple(rule.replace(" ", "").replace("|", "->").split("->")))

    def __str__(self):
        mstr = f""
        for name, arr in self.rules:
            mstr += f"\n{name} ->"
            for elt in arr:
                mstr += f" {elt} |"
            mstr = mstr[:-1]

        if self._first:
            mstr += "\n\n"
            for k, v in self._first.items():
                mstr += f"Premier ({k}) = "
                mstr += "{"
                for elt in v:
                    mstr += f"{elt}, "
                mstr = mstr[:-2] + "}\n"
        if self._follow:
            mstr += "\n"
            for k, v in self._follow.items():
                mstr += f"Suivant ({k}) = "
                mstr += "{"
                for elt in v:
                    mstr += f"{elt}, "
                mstr = mstr[:-2] + "}\n"

        return mstr

    def is_terminal(self, symbol):
        return symbol.islower()

    def one_is_empty(self, table):
        for k, v in table.items():
            if len(v) == 0:
                return True
        return False

    def first(self):
        table = {key: [] for key, _ in self.rules}
        # init
        for name, arr in self.rules:
            if "ε" in arr:
                table[name].append("ε")
            for rule in arr:
                for r in rule:
                    if not r in table.keys():
                        table[r] = r

        # nieme
        old = None
        cont = True  # pour faire un tour de plus que l'algo normal
        while self.one_is_empty(table) or cont:
            if old == table and not cont:
                break
            if old != table:
                cont = True
            else:
                cont = False
            old = table
            for name, rules in self.rules:
                for rule in rules:
                    table[name] += [e for e in table[rule[0]] if e != "ε"]

                    for idx, y in enumerate(rule):
                        if not "ε" in table[y]:
                            break
                        if idx + 1 < len(rule):
                            next_ = rule[idx + 1]
                            table[name] += [e for e in table[next_] if e != "ε"]
                        if idx + 1 == len(rule):
                            pass
                            table[name].append("ε")
            table = {key: list(set(table[key])) for key in table}
            old = {key: list(set(old[key])) for key in old}

        table = {
            key: sorted(list(set(table[key]))) for key in table if not key.islower()
        }

        self._first = table
        return self._first

    def follow(self):
        if not self._first:
            self.first()

        table = {key: [] for key, _ in self.rules}

        S, _ = self.rules[0]
        table[S].append("$")

        # nieme
        old = None
        cont = True  # pour faire un tour de plus que l'algo normal

        i = 0
        while old != table or i < 4:
            old = table
            i += 1
            for name, rules in self.rules:
                for rule in rules:
                    taille = len(rule)
                    # ne rien faire
                    if self.is_terminal(rule):
                        pass
                    # aM
                    elif taille == 2:
                        a = rule[0]
                        M = rule[1]
                        table[M] += table[name]

                    # aMB & AM
                    elif taille == 3:

                        a = "ε"
                        M = rule[0]
                        B = rule[1]

                        if self.is_terminal(B):
                            table[M].append(B)
                        else:
                            premierB = self._first[B]
                            table[M] += [e for e in premierB if e != "ε"]
                            if "ε" in premierB:
                                r2 = rule[2]
                                if self.is_terminal(r2):
                                    table[M].append(r2)
                                else:
                                    table[M] += table[r2]

                        a = rule[0]
                        M = rule[1]
                        B = rule[2]

                        premierB = self._first[B]
                        table[M] += [e for e in premierB if e != "ε"]
                        if "ε" in premierB:
                            table[M] += table[name]

                        a = rule[0] + rule[1]
                        M = rule[2]

                        table[M] += table[name]

                    elif taille == 4:
                        a = rule[0]
                        M = rule[1]
                        B = rule[2]

                        if self.is_terminal(B):
                            table[M].append(B)
                        else:
                            premierB = self._first[B]
                            table[M] += [e for e in premierB if e != "ε"]
                            if "ε" in premierB:
                                r3 = rule[3]
                                if self.is_terminal(r3):
                                    table[M].append(r3)
                                else:
                                    table[M] += table[r3]

                        a = rule[0] + rule[1]
                        M = rule[2]
                        B = rule[3]

                        if self.is_terminal(B):
                            table[M].append(B)
                        else:
                            premierB = self._first[B]
                            table[M] += [e for e in premierB if e != "ε"]
                    # aMB
                    else:
                        nb = taille - 1
                        print("nsp")

            table = {key: list(set(table[key])) for key in table}
            old = {key: list(set(old[key])) for key in old}

        table = {key: sorted(list(set(table[key]))) for key in table}

        self._follow = table
        return self._follow

    def first_follow(self):
        if not self._first:
            self.first()
        if not self._follow:
            self.follow()
        return (self._first, self._follow)


g1 = Grammar("S -> ABC", "A -> a | ε", "B -> bBAb | c", "C -> cA | ε")
g1.first_follow()
print(g1)

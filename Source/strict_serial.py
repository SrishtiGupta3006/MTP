# Source/strict_serial.py

class StrictSerialEnforcer:
    """
    Strict Serial Enforcer
    """

    def __init__(self, dfas):
        assert isinstance(dfas, list) and len(dfas) > 0, "No DFAs provided"

        self.dfas = dfas
        self.n = len(dfas)

        # One buffer σci and one state qi per DFA
        self.sigma_c = {i: [] for i in range(self.n)}
        self.q = {i: dfas[i].q0 for i in range(self.n)}

        self.output = []

    def delta_star(self, dfa, q, word):

        for a in word:
            q = dfa.d(q, a)
        return q

    def step(self, a):

        sigma = [a]          # σ ← a
        released = []

        for i, dfa in enumerate(self.dfas):
            sigma_next = []  # σ' ← ε
            qi = self.q[i]
            sigma_ci = self.sigma_c[i]

            for e in sigma:
                new_state = self.delta_star(dfa, qi, sigma_ci + [e])

                if dfa.F(new_state):
                    qi = new_state
                    sigma_next.extend(sigma_ci + [e])
                    sigma_ci.clear()
                else:
                    sigma_ci.append(e)

            # Update local state and buffer
            self.q[i] = qi
            self.sigma_c[i] = sigma_ci

            sigma = sigma_next

            if not sigma:
                break

        # Release only after the last enforcer
        if sigma:
            released.extend(sigma)
            self.output.extend(sigma)

        return released

def solution(n):
    # Generate solutions with backtracking. At any time, # closed parens remaining >= # open parens remaining

    def backtrack(n_open, n_closed):
        sols = set()

        if n_open == 0 and n_closed == 0: sols.add("")
        else:
            if n_open > 0:
                try_open = backtrack(n_open - 1, n_closed)
                for e in try_open: sols.add('(' + e)
            if n_closed > 0 and n_closed > n_open:
                try_closed = backtrack(n_open, n_closed - 1)
                for e in try_closed: sols.add(')' + e)

        return sols

    return list(backtrack(n, n))

from typing import List, Set, Tuple

def parse_clause(line: str) -> frozenset:
    literals = list(map(int, line.strip().split()))
    return frozenset(lit for lit in literals if lit != 0)

def resolve(c1: frozenset, c2: frozenset) -> Set[frozenset]:
    resolvents = set()
    for lit in c1:
        if -lit in c2:
            new_clause = (c1.union(c2)) - {lit, -lit}
            resolvents.add(frozenset(new_clause))
    return resolvents

def resolution_algorithm(clauses: List[frozenset]) -> str:
    new = set()
    clauses_set = set(clauses)
    while True:
        pairs = [(c1, c2) for idx, c1 in enumerate(clauses) for c2 in clauses[idx+1:]]
        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            for r in resolvents:
                if not r:
                    return "Formula este NESATISFIABILA (contradicție găsită)."
                if r not in clauses_set:
                    new.add(r)
        if new.issubset(clauses_set):
            return "Formula este SATISFIABILA (nu s-a putut obține contradicție)."
        clauses.extend(new)
        clauses_set.update(new)
        new.clear()

def main():
    print("Introdu clauze în formatul: 1 -2 0 (0 marchează sfârșitul clauzei).")
    print("Apasă ENTER fără nimic pentru a termina introducerea.
")

    clauses = []
    while True:
        line = input("Clauză: ").strip()
        if not line:
            break
        clause = parse_clause(line)
        if clause:
            clauses.append(clause)

    result = resolution_algorithm(clauses)
    print("\nRezultat:")
    print(result)

if __name__ == "__main__":
    main()
    
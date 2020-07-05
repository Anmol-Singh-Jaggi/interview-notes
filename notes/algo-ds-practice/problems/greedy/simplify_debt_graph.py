"""
Given a number of friends who have to give or take some amount of money from one another.
Design an algorithm by which the total cash flow among all the friends is minimized.

SOLUTION:
Greedy approach!

For all the persons involved, first compute the net credit flow for that person.
For example, if a person has to pay 10 and 20 to B and C, but also receieve 5 and 10 from D and E,
then net credit flow of A = (5+10) - (10+20) = -15. Meaning that A will ultimately have to give 15 to others.
Once, we have computed the net credit flow, then divide this into 2 lists - one for +ve flow and one for -ve.

Now, choose any one person from each of those lists and sort out their difference.
For example, A = -15, B = 40. Then A will give 15 to B => A becomes 0 and B becomes 25.
Once a person's flow becomes 0, remove it from the list.
At each step one person will be removed from either list.
Complexity -> O(E+V)

Note that the sum of the 2 lists will be 0.

TODO:
https://stackoverflow.com/questions/15723165/algorithm-to-simplify-a-weighted-directed-graph-of-debts
https://www.alexirpan.com/2016/05/10/may-10.html
"""
from ds.graph.graph_core import GraphCore


def simplify_debt_graph(debt_graph: GraphCore):
    credit_flow = {}
    for vert in debt_graph.vertices:
        credit_flow[vert] = 0
    for src, edges in debt_graph.get_all_edges().items():
        for neigh, edge in edges.items():
            wt = edge["weight"]
            credit_flow[src] -= wt
            credit_flow[neigh] += wt
    debtors = []
    creditors = []
    for vert, flow in credit_flow.items():
        if flow < 0:
            debtors.append([vert, -flow])
        else:
            creditors.append([vert, flow])
    assert sum(map(lambda item: item[1], debtors)) == sum(
        map(lambda item: item[1], creditors)
    )
    simplified_graph = GraphCore()
    for vert in debt_graph.vertices:
        simplified_graph.add_vertex(vert)
    debtors_idx = 0
    creditors_idx = 0
    while debtors_idx < len(debtors) and creditors_idx < len(creditors):
        debtor = debtors[debtors_idx]
        creditor = creditors[creditors_idx]
        min_flow = min(debtor[1], creditor[1])
        simplified_graph.add_edge(debtor[0], creditor[0], min_flow)
        debtor[1] -= min_flow
        creditor[1] -= min_flow
        if debtor[1] == 0:
            debtors_idx += 1
        if creditor[1] == 0:
            creditors_idx += 1
    assert debtors_idx == len(debtors)
    assert creditors_idx == len(creditors)
    return simplified_graph


def main():
    debt_graph = GraphCore()
    debt_graph.add_edge(0, 1, 1000)
    debt_graph.add_edge(1, 2, 5000)
    debt_graph.add_edge(0, 2, 2000)
    simplified = simplify_debt_graph(debt_graph)
    print(simplified)


main()

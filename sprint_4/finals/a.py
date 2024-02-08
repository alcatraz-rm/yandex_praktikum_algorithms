

def add_doc_to_index(doc: str, index: dict, i: int):
    doc = doc.lower().split()
    for word in doc:
        if word in index:
            if i in index[word]:
                index[word][i] += 1
            else:
                index[word][i] = 1
        else:
            index[word] = {i: 1}


def get_top_n_relevant(doc: str, index: dict, n: int = 5) -> list:
    doc = doc.lower().split()
    results_to_relevance = {}

    for word in set(doc):
        for d in index.get(word, []):
            if d in results_to_relevance:
                results_to_relevance[d] += index[word][d]
            else:
                results_to_relevance[d] = index[word][d]

    return sorted(results_to_relevance.items(), key=lambda x: (-x[1], x[0]))[:n]


index = {}

for i in range(int(input())):
    add_doc_to_index(input(), index, i + 1)

for _ in range(int(input())):
    relevant_docs = get_top_n_relevant(input(), index)
    for d in relevant_docs:
        if d[1] != 0:
            print(d[0], end=' ')
    print()

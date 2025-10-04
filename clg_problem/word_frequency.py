# from collections import Counter

# def count_word_frequency(sentence):
#     words = sentence.lower().split()
#     word_count = Counter(words)
#     return word_count
    
# sentence = input()
# word_frequency = count_word_frequency(sentence)

# #* it returns dictionary with the collection.counter class 
# # print(word_frequency)

# # so we iterate this as dictionary

# for word, count in word_frequency.items():
#     print(f"{word} : {count}")
    



vertices = ['P', 'Q', 'R', 'S', 'T', 'U']
adj_list = {vertex: [] for vertex in vertices}
edges = [
    ('P', 'Q'),
    ('P', 'S'),
    ('P', 'T'),
    ('Q', 'S'),
    ('S', 'R'),
    ('S', 'T'),
    ('S', 'U'),
    ('R', 'U'),
    ('T', 'U'),
    ('U', 'S')
]
for src, dest in edges:
    adj_list[src].append(dest)
def is_complete_directed():
    n = len(vertices)
    for i in range(n):
        for j in range(n):
            if i != j:  # Skip self-loops
                u = vertices[i]
                v = vertices[j]
                # Check if there is an edge from u to v
                edge_uv = v in adj_list[u]
                # Check if there is an edge from v to u
                edge_vu = u in adj_list[v]
                if edge_uv == edge_vu:  
                    return False
    return True
if is_complete_directed():
    print("The graph is a complete directed graph (tournament).")
else:
    print("The graph is not a complete directed graph (tournament).")
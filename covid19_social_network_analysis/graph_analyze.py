import sys
import networkx as nx
import matplotlib.pyplot as plt

def load_node_weights(infile, k=10):
    dct = {}
    with open(infile) as fr:
        for line in fr:
            arr = line.strip().split('\t')
            dct[arr[0]] = int(arr[1])
    sorted_dct = sorted(dct.items(), key=lambda x:x[1], reverse=True)
    topk = [x for x,y in sorted_dct[:k]]
    return dct, topk

if __name__ == '__main__':
    prefix = sys.argv[1]

    edge_file = prefix + '.edges'
    G = nx.read_weighted_edgelist(
        edge_file,
        delimiter = '\t',
        create_using = nx.Graph(),
        nodetype=str
        )
    #nx.draw_networkx(G)
    #plt.show()
    print(nx.info(G))

    #print('Average clustering coefficient:{0:.3f}'.format(nx.clustering(G, 'coronavirus')))
    #print('Average clustering coefficient:{0}'.format(nx.average_clustering(G)))
    #print('Closeness Centrality:{0}'.format(nx.closeness_centrality(G)))
    scores = nx.closeness_centrality(G)
    sorted_scores = sorted(scores.items(), key=lambda x:x[1], reverse=True)

    print('top 3:')
    for k, v in sorted_scores[:3]:
        print(k)


    s = 0
    for k, v in sorted_scores:
        s += v
    print('Average Closeness Centrality:{0:.3f}'.format(s/len(sorted_scores)))

    #print('Betweenness Centrality:{0}'.format(nx.betweenness_centrality(G)))
    #print('Eigenvector Centrality:{0}'.format(nx.eigenvector_centrality(G)))


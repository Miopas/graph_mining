import sys
import networkx as nx
from pyvis.network import Network

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
    outfile = sys.argv[2]
    #heading = sys.argv[3]
    heading = None

    edge_file = prefix + '.edges'
    node_file = prefix + '.nodes'
    node_weights, topk = load_node_weights(node_file)

    got_net = Network(height="750px", width="100%", font_color="#1a2a3a", heading=heading)
    # set the physics layout of the network
    #got_net.barnes_hut()
    #got_net.hrepulsion()

    fr = open(edge_file)
    for line in fr:
        src, dst, w = line.strip().split('\t')
        src_node_color = '#f67e2a'
        dst_node_color = '#f67e2a'
        edge_color = '#fcba5d'
        src_vis = False
        dst_vis = False
        edge_vis = False
        #if src not in topk:
        #    #src_node_color = '#f8d29d'
        #    #edge_color = '#f8d29d'
        #    src_vis = True
        #    edge_vis = True
        #if dst not in topk:
        #    dst_vis = True
        #    edge_vis = True
        #    #dst_node_color = '#f8d29d'
        #    #edge_color = '#f8d29d'

        got_net.add_node(src, src.title(), title=src, value=node_weights[src], shape='circle', color=src_node_color, hidden=src_vis)
        got_net.add_node(dst, dst.title(), title=dst, value=node_weights[dst], shape='circle', color=dst_node_color, hidden=dst_vis)
        got_net.add_edge(src, dst, value=w, color=edge_color, hidden=edge_vis)
    fr.close()
    
    neighbor_map = got_net.get_adj_list()
    
    # add neighbor data to node hover data
    for node in got_net.nodes:
        node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
        node["value"] = len(neighbor_map[node["id"]])
    
    got_net.show(outfile)

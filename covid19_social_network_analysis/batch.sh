for i in 01 02 03 04 05 06 07;
do
	echo $i
	python graph_analyze.py top_edge_10/${i}
done

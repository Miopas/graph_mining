layer_type=GCN
nlayers=2
hidden=8

python train.py --layer_type ${layer_type} --nlayers ${nlayers} --hidden ${hidden} > res_${layer_type}_${nlayers}_${hidden}.log


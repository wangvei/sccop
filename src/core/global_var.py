#Grid
cutoff = 8
num_min_atom = 5
num_max_atom = 10
grain = [.5, .5, 1.2]
plane_upper = [100, 100, 1]

#Dimension
num_dim = 2
add_vacuum = True
vacuum_space = 15
puckered = True
thickness = 0.1

#Recycling
num_recycle = 1
num_ml_list = [1]
num_poscars = 12
num_optims = 6
vasp_time_limit = 480

#Initial Samples
component = 'XXX'
num_latt = 72
num_Rand = 120
num_ave_sg = 10
num_cores = 4
num_per_sg = 5
len_mu = 5
len_lower = 4
len_upper = 6
len_sigma = 1
ang_mu = 90
ang_sigma = 20
system_weight = [1/4, 0, 1/4, 1/4, 0, 1/4, 0]

#Training
train_batchsize = 64
train_epochs = 120
use_pretrain_model = True

#Searching
T = .1
decay = .95
latt_steps = 3
sa_steps = 100
num_jump = 2
num_path = 360
sa_cores = 2
min_bond = 1.2

#Sample Select
num_models = 5
num_components = 2
num_clusters = 60
ratio_min_energy = 0.5

#Server
num_gpus = 2
gpu_node = 'node151'
nodes = [131, 132, 133, 134, 135, 136]
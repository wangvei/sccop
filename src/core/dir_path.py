#Save directory
poscar_path = 'data/poscar' 
model_path = 'data/ppmodel'
search_path = 'data/search'
vasp_out_path = 'data/vasp_out'
grid_path = 'data/grid'
grid_prop_path = 'data/grid/property'
grid_poscar_path = 'data/grid/poscar'
ccop_out_path = 'data/poscar/CCOP'
optim_strs_path = 'data/poscar/optim_strs'
optim_strs_sym_path = 'data/poscar/optim_strs_sym'
init_strs_path = 'data/poscar/initial_strs'

#DFT directory
vasp_files_path = 'libs/VASP_inputs'
sing_point_energy_path = 'libs/VASP_inputs/SinglePointEnergy'

#File
log_file = 'data/system.log'
elements_file = 'data/elements.dat'
atom_init_file = 'data/atom_init.dat'
KPOINTS_file = 'vasp/KPOINTS'
bandconf_file = 'vasp/bandconf'
pretrain_model = 'database/mp_20/pretrain_model/model_best.pth.tar'

#Property file
optim_vasp_path = f'{vasp_out_path}/optim_strs'
dielectric_path = f'{optim_vasp_path}/dielectric'
elastic_path = f'{optim_vasp_path}/elastic'
energy_path = f'{optim_vasp_path}/energy'
pbe_band_path = f'{optim_vasp_path}/pbe_band'
phonon_path = f'{optim_vasp_path}/phonon'
thermalconductivity_path = f'{optim_vasp_path}/thermalconductivity'

#Adsorp file
adsorp_path = 'data/adsorp'
anode_strs_path = f'{adsorp_path}/anode_strs'
anode_energy_path = f'{adsorp_path}/anode_energy'
adsorp_strs_path = f'{adsorp_path}/adsorp_strs'
adsorp_energy_path = f'{adsorp_path}/adsorp_energy'
adsorp_analysis_path = f'{adsorp_path}/adsorp_analysis'
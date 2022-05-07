# Crystal-Combinatiorial-Optimization-Program

晶体组合优化程序(Crystal-Combinatiorial-Optimization-Program, CCOP)是基于Python3与PyTorch编写的机器学习加速结构搜索程序。目前正在开发中，如有需要可联系邮箱lcn1996@mail.ustc.edu.cn进行交流。

## 环境

shell版本: bash

python版本: python3.5及以后。需要有pytorch, DPT, phonopy, pymatgen库

## 程序启动

连接GPU节点ssh node151，进入/local/ccop，挂起nohup python src/main.py >& log &

## VASP计算

目前可计算

1. 结构优化(libs/VASP_inputs/Optimization)
2. 声子谱(libs/VASP_inputs/Phonon), 需安装Phonopy, 运行完毕后会直接输出声子谱图(利用libs/scripts/plot-phonon-band.py)
3. PBE能带(libs/VASP_inputs/ElectronicStructure), 运行完毕后会直接输出能带图(利用libs/scripts/plot-energy-band.py)
4. 三阶力常数(libs/VASP_inputs/ThirdOrder)，需自行安装thirdorder库并zip打包后放进该目录内。运行完毕后会输出FORCE_CONSTANTS_3RD
5. 热导率。需自行安装ShengBTE软件。需要用到声子谱计算输出的FORCE_CONSTANTS文件与三阶力常数文件FORCE_CONSTANTS_3RD。

注：所有计算的布里渊区路径均由pymatgen生成
依赖包：pymatgen seekpath
pip install seekpath
pip install pymatgen-analysis-diffusion


## 节点通信
节点之间需要ssh免密连接

配置方法：
1. cd ~/.ssh
2. 生成密钥对 ssh-keygen -t rsa -b 4096

更新密钥：
1. ssh-copy-id -i ~/.ssh/id_rsa.pub user@node
2. ssh-copy-id -i ~/.ssh/id_rsa.pub user@node
3. ...

## scp 自动连接
vi /etc/ssh/ssh_config
修改 StrictHostKeyChecking 为 no


## 
Z:.5hV=]Jgx@2~39B)cC

## 预训练模型
pip install -U jarvis-tools
二维材料数据来自：dft_2d twod_matpd c2db
#!/bin/bash

#SBATCH --job-name=Ancestor-spades
#SBATCH --partition=commons
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --threads-per-core=1
#SBATCH --mem-per-cpu=2000m
#SBATCH --time=08:10:00
#SBATCH --mail-type=ALL
 
echo "My job ran on:"
echo $SLURM_NODELIST

module load GCC/5.4.0

spades.py -k 21,33,55,77,99 --isolate --pe1-1 /scratch/hm22/Xinhao/AncT4-11_R1_001.fastq.gz --pe1-2 /scratch/hm22/Xinhao/AncT4-11_R2_001.fastq.gz --pe2-1 /scratch/hm22/Xinhao/AncT4-11-2-_R1_001.fastq.gz --pe2-2 /scratch/hm22/Xinhao/AncT4-11-2-_R2_001.fastq.gz -o ancestorT4-11_denovo


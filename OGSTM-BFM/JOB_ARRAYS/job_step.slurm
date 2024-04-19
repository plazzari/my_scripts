#! /bin/bash

#SBATCH --job-name=MITgcm-BFM
#SBATCH -N17 -n 800 
#SBATCH --ntasks-per-node=48
#SBATCH --time=24:00:00
#SBATCH --mem=350gb
#SBATCH --account=icei_Rosati
#SBATCH --partition=g100_usr_prod
#SBATCH --mail-type=ALL
##SBATCH --mail-user=

echo $SLURM_JOB_ID
echo $SLURM_ARRAY_JOB_ID
echo $SLURM_ARRAY_TASK_ID
echo $SLURM_ARRAY_TASK_COUNT
echo $SLURM_ARRAY_TASK_MAX
echo $SLURM_ARRAY_TASK_MIN

cd $SLURM_SUBMIT_DIR

#module purge
module load intel/oneapi-2021--binary
module load intelmpi/oneapi-2021--binary
module load mkl/oneapi-2021--binary
module load gsl/2.7--intel--2021.4.0
module load netcdf-fortran/4.5.3--intel-oneapi-mpi--2021.4.0--intel--2021.4.0

source /g100_work/OGS21_PRACE_P/COPERNICUS/py_env_3.6.8/bin/activate
export PYTHONPATH=$PYTHONPATH:/g100_work/OGS21_PRACE_P/COPERNICUS/bit.sea

ulimit -s unlimited

date

python setup_launch.py          --iteration ${SLURM_ARRAY_TASK_ID} --months_increment 2
python generate_bfm_friendly.py --iteration ${SLURM_ARRAY_TASK_ID} --months_increment 2 --output_nectdf True

mpirun -np 800 ./mitgcmuv

cp STDOUT.0000 STDOUT.0000_${SLURM_ARRAY_TASK_ID}
cp STDERR.0000 STDERR.0000_${SLURM_ARRAY_TASK_ID}

date


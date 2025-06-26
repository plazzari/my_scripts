#! /bin/bash

#SBATCH --job-name=TEST
#SBATCH -N1 
#SBATCH --ntasks-per-node=1
#SBATCH --time=00:01:00
#SBATCH --mem=10gb
#SBATCH --account=OGS_test2528
#SBATCH --partition=g100_usr_prod
##SBATCH --mail-type=ALL
##SBATCH --mail-user=


cd $SLURM_SUBMIT_DIR

M_I=12 # Month increment

TID=$((SLURM_ARRAY_TASK_ID))
TID_p1=$((SLURM_ARRAY_TASK_ID+1))

if [ $M_I -lt 12 ]; then
    n_postproc=$((12/M_I))
    resto=$((SLURM_ARRAY_TASK_ID%n_postproc))
    n_years=$((TID*M_I/12))
    sim_iteration=$((SLURM_ARRAY_TASK_ID-n_years)) # for each year one step is for postoproc
elif [ $M_I -eq 12 ]; then
    resto=$((TID_p1%2))
    sim_iteration=$((SLURM_ARRAY_TASK_ID/2))
else
    echo Not Tested!
    n_postproc=$((M_I/12))
    resto=$((TID_p1%n_postproc))
fi

do_postproc=0

if [ $resto -eq 0 ]; then
    if [ $SLURM_ARRAY_TASK_ID -gt 0 ]; then
       do_postproc=1
    fi
fi


################## JOB OPTIONS: RUN or POSTPROC #########################################


if [ $((do_postproc)) -eq 0 ]; then

############################### RUN #####################################################

	echo SLURM_ARRAY_TASK_ID $SLURM_ARRAY_TASK_ID computing: $sim_iteration
        python setup_launch.py --iteration ${sim_iteration} --months_increment ${M_I}

############################### END RUN #################################################

else

############################### POSTPROC ################################################

	postproc_year=$(head -n 1 Start_End_Times | cut -c 1-4)
	echo SLURM_ARRAY_TASK_ID $SLURM_ARRAY_TASK_ID postproc: year ${postproc_year}

############################### END POSTPROC ############################################

fi


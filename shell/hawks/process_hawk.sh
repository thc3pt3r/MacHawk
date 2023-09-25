# process_hawk.sh
# Modulo de adquisición de procesos en ejecución
source ./hawks/general_hawk.sh
grab_running_process(){
    P_file=$1/ps_ouput.txt
    sudo ps -axo user,pid,ppid,%cpu,%mem,start,time,command  > $P_file
}
run_process_hawk(){
    dst_dir=$1/"Process_hawk"
    create_output_dir $dst_dir
    if [ $? -eq 0 ]; then
        echo "create_output_dir executed successfully."
    else
        echo "create_output_dir encountered an error."
    fi
    echo "============================================================"
    echo "Acquiring Running Process"
    grab_running_process $dst_dir
    
}
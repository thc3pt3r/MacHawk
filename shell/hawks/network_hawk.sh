# network_hawk.sh
#Modulo para adquisición de evidencia realacionada con networking
source ./hawks/general_hawk.sh

get_network_stat(){
    N_file=$1/netstat.txt
    sudo netstat -na > $N_file

}

#Esta función busca  todos los archivos que tengan
# alguna conexion IPV4, IPV6, HP-UX X25 abierta

get_lsof_output(){
    L_file=$1/lsof.txt
    sudo lsof -i > $L_file
}

#función de ejecución principal del modulo
run_Network_triage(){
    dst_dir=$1/"Networking_hawk"
    create_output_dir $dst_dir
    if [ $? -eq 0 ]; then
        echo "create_output_dir executed successfully."
    else
        echo "create_output_dir encountered an error."
    fi
    echo "=================================================="
    echo "Acquiring network statistics"
    get_network_stat $dst_dir
    echo "=================================================="
    echo "Acquiring Files with Open connections"
    get_lsof_output $dst_dir
    echo "=================================================="
}
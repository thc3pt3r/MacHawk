# system_hawk.sh

#Moduclo de adquisición forense sobre información del sistema
source ./hawks/general_hawk.sh

# Tiny executions
grab_mad_path(){
    MP_file=$1/mad_paths.txt
    IFS=':' read -ra paths <<< "$PATH"
    for path in "${paths[@]}"; do
        cd "$path" || continue
        echo "$path"
        ls -altR
    done > "$MP_file"    
}
grab_etc_listing(){
    E_file=$1/listing.txt
    sudo sudo ls -altR /etc/ > $E_file    
}
grab_hosts_content(){
    H_file=$1/hosts.txt
    sudo sudo cat /etc/hosts > $H_file
}

# Main execution
run_system_hawk(){
    parent_dst_dir=$1/"System_hawk"
    create_output_dir $parent_dst_dir
    if [ $? -eq 0 ]; then
        echo "create_output_dir executed successfully."
    else
        echo "create_output_dir encountered an error."
    fi
    echo "************************************************************"
    echo "Acquiring Mad Paths"
    grab_mad_path $parent_dst_dir
    echo "************************************************************"
    echo "Acquiring ETC Listing"
    grab_etc_listing $parent_dst_dir
    echo "************************************************************"
    echo "Acquiring Hosts file Content "
    grab_hosts_content $parent_dst_dir
}
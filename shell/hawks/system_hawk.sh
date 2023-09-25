# system_hawk.sh

#Moduclo de adquisición forense sobre información del sistema
source ./hawks/general_hawk.sh

# Tiny executions
grab_mad_path(){
    MP_file=$1/Previous_Logged_Users.txt
    IFS=':' read -ra paths <<< "$PATH"
    for path in "${paths[@]}"; do
        cd "$path" || continue
        echo "$path"
        ls -altR
    done > "$MP_file"    
}
grab_etc_listing(){
    ETL_file=$1/Etc_Listing.txt
    sudo sudo ls -altR /etc/ > $ETL_file
}
grab_hosts_content(){
    HO_file=$1/hosts_content.txt
    sudo sudo cat /etc/hosts > $HO_file
}

# Main execution
run_system_hawk(){
    dst_dir=$1/"System_hawk"
    create_output_dir $dst_dir
    if [ $? -eq 0 ]; then
        echo "create_output_dir executed successfully."
    else
        echo "create_output_dir encountered an error."
    fi
    echo "************************************************************"
    echo "Acquiring Mad Paths"
    grab_mad_path $dst_dir
    echo "************************************************************"
    echo "Acquiring ETC Listing"
    grab_etc_listing $dst_dir
    echo "************************************************************"
    echo "Acquiring Hosts file Content "
    grab_hosts_content $dst_dir
}
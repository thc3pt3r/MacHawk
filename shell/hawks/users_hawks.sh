# users_hawks.py
# Modulo de adquisición forense de actividades realacionas a usuarios.
#Long Description Here
source ./hawks/general_hawk.sh

# Tiny executions
grab_previous_logged_users(){
     PU_file=$1/Previous_Logged_Users.txt
    sudo last  > $PU_file
}
grab_active_logged_users(){
    AU_file=$1/Active_Users.txt
    sudo w  > $AU_file
}
grab_cleaned_user_list(){
    #This function print the existing user, clening those account that are system accounts.
    CUL_file=$1/last_output.txt
    sudo dscl . list /Users UniqueID | grep -v ^_  > $CUL_file
}
grab_complete_user_list(){
    #This function print the existing user, clening those account that are system accounts.
    COUL_file=$1/last_output.txt
    sudo dscl . list /Users UniqueID > $COUL_file
}

# Main execution
run_users_hawk(){
      dst_dir=$1/"Users_hawk"
    create_output_dir $dst_dir
    if [ $? -eq 0 ]; then
        echo "create_output_dir executed successfully."
    else
        echo "create_output_dir encountered an error."
    fi
    echo "============================================================"
    echo "Acquiring Previous logged users"
    grab_previous_logged_users $dst_dir
    echo "============================================================"
    echo "Acquiring Active logged users"
    grab_active_logged_users $dst_dir
    echo "============================================================"
    echo "Acquiring User list"
    grab_complete_user_list $dst_dir
    echo "============================================================"
    echo "Acquiring cleaned User list"
    grab_cleaned_user_list $dst_dir
}
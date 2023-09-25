# persistance_hawk.sh

#Modulo para adquisición de evidencia relacionada con actividades de persistencia.
source ./hawks/general_hawk.sh

grab_launchAgents(){
    src_dir="/Library/LaunchAgents/"
    dst_dir=$1/"Persistance_hawk/LaunchAgents"
     if [ -d "$dst_dir" ]; then
        echo "El directorio de destino '$dst_dir' ya existe. Saliendo."
        #return 1
    fi

    #rsync -avXpoglt -- "$src_dir" "$dest_dir"
    rsync -aX -- "$src_dir" "$dst_dir"

    if [ $? -eq 0 ]; then
        echo "Directorio '$src_dir' copiado a '$dst_dir' exitosamente!"
    else
        echo "Ocurrió un error al copiar el directorio '$src_dir' a '$dst_dir'."
    fi
}

grab_LaunchDeamon(){
    src_dir="/Library/LaunchDaemons/"
    dst_dir=$1/"Persistance_hawk/LaunchDaemons"
     if [ -d "$dst_dir" ]; then
        echo "El directorio de destino '$dst_dir' ya existe. Saliendo."
        #return 1
    fi

    #rsync -avXpoglt -- "$src_dir" "$dest_dir"
    rsync -aX -- "$src_dir" "$dst_dir"

    if [ $? -eq 0 ]; then
        echo "Directorio '$src_dir' copiado a '$dst_dir' exitosamente!"
    else
        echo "Ocurrió un error al copiar el directorio '$src_dir' a '$dst_dir'."
    fi

}


run_persistance_hawk(){
    dst_dir=$1/"Persistance_hawk"
    create_output_dir $dst_dir
    if [ $? -eq 0 ]; then
        echo "create_output_dir executed successfully."
    else
        echo "create_output_dir encountered an error."
    fi
    echo "============================================================"
    echo "Acquiring LaunchAgent"
    grab_launchAgents $dst_dir
    echo "============================================================"
    echo "Acquiring LaunchDeamon"
    grab_LaunchDeamon $dst_dir
    echo "============================================================"
}
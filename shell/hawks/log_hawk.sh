# log_hawk.sh
# Modulo para la adquisición de carpetas y/o archivos de log en un sistema operativo MAC
source ./hawks/general_hawk.sh
grab_logs(){
#Esta función se encarga de realizar la copia de la carpeta /var/log
#    -a combina -t, -p, -o, -g, -l, y otras opciones para copiar archivos, carpetas y atributos, y preservar fechas de modificación, permisos, propietario, grupo, enlaces simbólicos, etc.
#    -v se ha omitido en esta versión porque rsync ya proporciona información detallada sobre la copia de archivos en modo verbose por defecto.
#    -X se utiliza para copiar archivos ocultos.
#    -p es necesario para preservar los permisos.
#    -o es necesario para preservar el propietario.
#    -g es necesario para preservar el grupo.
#    -l es necesario para preservar los enlaces simbólicos.
#    -t es necesario para preservar las fechas de modificación.
    src_dir="/var/log/"
    dest_dir=$1

    if [ -d "$dest_dir" ]; then
        echo "El directorio de destino '$dest_dir' ya existe. Saliendo."
        return 1
    fi

    #rsync -avXpoglt -- "$src_dir" "$dest_dir"
    rsync -a -- "$src_dir" "$dest_dir"

    if [ $? -eq 0 ]; then
        echo "Directorio '$src_dir' copiado a '$dest_dir' exitosamente!"
    else
        echo "Ocurrió un error al copiar el directorio '$src_dir' a '$dest_dir'."
    fi
}
run_Logs_triage(){
    dst_dir=$1/"Logs_hawk"
    create_output_dir $dst_dir
    if [ $? -eq 0 ]; then
        echo "create_output_dir executed successfully."
    else
        echo "create_output_dir encountered an error."
    fi
    grab_logs $dst_dir
    
}



# general_hawk.sh
# Modulo con funciones generales.  Las mismas pueden ser utilizadas por modulos personales

create_output_dir() {
    directory=$1
    if [ -d $directory ]; then
        echo "El directorio $directory ya existe. No se crea."
    else
        mkdir "$directory" || { echo "There was an error creating the directory."; exit 1; }
        echo "Directory '$directory' created successfully."
    fi
}
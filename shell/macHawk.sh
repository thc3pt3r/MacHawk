#!/bin/bash

# Programa para realizar un triage de Incident response en equipo MacOs
# importación de los distintos modulos
source ./hawks/general_hawk.sh
source ./hawks/log_hawk.sh
source ./hawks/network_hawk.sh
source ./hawk/persistance_hawk.sh
#Fin importacion de modulos
#funciones
mostrar_ayuda() {
    clear
    echo " === MacHawk - Triage de equipos MacOs  by Deloitte ARG CIR TEAM === "
    echo "Uso: macHack.sh [opción]"
    echo "Opciones:"
    echo "  -h, --help          Show this help."
    echo "  -c, --complete      Run a complete IR Triage collection."
    echo "  -p, --partial       Run a partial IR Triage collection."
    echo "  -q, --quit          Exit the program."
    echo " ============================================================ "
    
}
run_complete_triage(){
    clear
    echo "Ejecutando Triage Completo"
    echo "============================================================"
    echo "Creating the Triage Folder"    
    # Get the current datetime in a specific format (e.g., YYYYMMDD_HHMMSS)
    datetime=$(date +'%Y%m%d_%H%M%S')
    parent_dir="Triage_Collection_$datetime"
    create_output_dir $parent_dir
    echo "============================================================"
    echo "Executing Log triage"    
    run_Logs_triage $parent_dir
    echo "============================================================"
    echo "Executing Networking triage"
    run_Network_triage $parent_dir
    echo "============================================================"
    echo "Executing Persistance triage"
    run_persistance_hawk $parent_dir
    echo "============================================================"
    echo "============================================================"
    echo "Compresing Output Directory"
    compress_Triage_Output $parent_dir

    exit 0
    
}
run_partial_triage(){
    clear
    echo "Ejecutando Triage Completo"
    exit 0
    
}

#loop principal
if [ "$1" == "-h" ] || [ "$1" == "--help"]; then
    mostrar_ayuda
    exit 0
fi
while true; do
    case "$1" in
        -com|--complete)
            run_complete_triage
            ;;
        -p|--partial)
            run_partial_triage
            ;;
        -q|--quit)
            echo "Goodbye!"
            exit 0
            ;;
        *)
            mostrar_ayuda
            exit 1
            ;;
    esac
done
package controlador;
import modelo.*;
import vista.VistaUser;
import java.util.HashMap;
import java.util.Map;


public class Controlador {
    private BD_students BaseDatos = new BD_students();
    public void Ejecutar() {
        boolean inProgram = true;
        while (inProgram) {
            int r = VistaUser.Menu();
            switch (r) {
                case 1:
                // mostrar todo los estudiantes
                for(int Clave : BaseDatos.GetBaseDatos().keySet()){
                    Estudiante Valor = BaseDatos.GetBaseDatos().get(Clave);
                    VistaUser.MostrarDatos(Clave, Valor);
                }
                    break;
                case 2:

                // mostrar los 3 mejores promedios
                HashMap <Integer,Estudiante> baseMejor = BaseDatos.getMejoresEstudiantes();
                for(int clave : baseMejor.keySet()){
                    Estudiante valor = baseMejor.get(clave);
                    VistaUser.MostrarDatos(clave, valor);
                }
                break;
                case 3:
                //Agregar un nuevo estudiante
                Estudiante e = VistaUser.CrearEstudiante();
                BaseDatos.AgregarEstudiante(e);
                break;
                case 4:
                //Editar Estudiante
                int c = VistaUser.EditarKey();
                boolean encontrado = false;
                for(Map.Entry<Integer,Estudiante> entry: BaseDatos.GetBaseDatos().entrySet()){
                    if (c == entry.getKey()){
                        e = VistaUser.CrearEstudiante();
                        BaseDatos.GetBaseDatos().put(c, e);
                        encontrado = true;
                        break;
                    }
                }
                if (encontrado == false) {
                    VistaUser.MensajeError();
                }
                break;
                case 5:
                c = VistaUser.EditarKey();
                encontrado = false;
                for (Map.Entry<Integer,Estudiante> entry : BaseDatos.GetBaseDatos().entrySet()) {
                    if (c == entry.getKey()){
                        BaseDatos.GetBaseDatos().remove(c);
                        encontrado = true;
                        break;
                    }
                }
                if( encontrado == false){
                    VistaUser.MensajeError();
                }
                break;
                case 6:
                //Consultar Un estudiante
                c = VistaUser.EditarKey();
                if (BaseDatos.GetBaseDatos().containsKey(c)){
                    Estudiante x = BaseDatos.GetBaseDatos().get(c);
                    VistaUser.MostrarDatos(c, x);
                }else{
                    VistaUser.MensajeError();
                }
                
                break;
                case 7:
                    inProgram = false;
            }
        }
    }
}

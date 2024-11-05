package controlador;

import modelos.*;
import vista.VistaUser;
import java.util.ArrayList;

public class Controlador {
    private BD_Estudiantes base_estudiante = new BD_Estudiantes();

    public void Ejecutar() {
        boolean inprogram = true;
        while (inprogram) {
            int r = VistaUser.Menu();
            switch (r) {
                case 1:
                    // Mostrar todos los estudiantes
                    for (Estudiantes e : base_estudiante.getBd_Estudiantes()) {
                        VistaUser.ImprimirDatos(e);
                    }
                    break;
                case 2:
                    ArrayList<Estudiantes> mejores = base_estudiante.getMejoresESTUDIANTES();
                    for (Estudiantes es : mejores) {
                        VistaUser.ImprimirDatos(es);
                    }

                    break;
                case 3:
                    // Agregar Estudiante
                    Estudiantes e = VistaUser.CrearUsuario();
                    base_estudiante.AñadirCompra(e);
                    break;
                case 4:
                    // salir
                    inprogram = false;
            }
        }

    }

}

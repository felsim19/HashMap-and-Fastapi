package modelo;

import java.util.HashMap;
import java.util.Map;

public class BD_students {
    private static int contador = 1;
    public HashMap<Integer, Estudiante> BaseDatos = new HashMap<>();

    public BD_students() {
        AgregarEstudiante(new Estudiante("felipe", "Sierra", "Decimo", 3.4, 4.5, 3.1));
        AgregarEstudiante(new Estudiante("david", "carrillo", "noveno", 4.3, 4.5, 4.1));
        AgregarEstudiante(new Estudiante("mateo", "gamboa", "decimo", 4.3, 4.7, 4.2));
        AgregarEstudiante(new Estudiante("julian", "carrillo", "noveno", 3.3, 3.5, 3.1));
        AgregarEstudiante(new Estudiante("duvan", "pihedraita", "decimo", 3.3, 3.7, 3.2));
    }

    public void AgregarEstudiante(Estudiante e) {
        GetBaseDatos().put(contador++, e);
    }

    public HashMap<Integer, Estudiante> getMejoresEstudiantes() {
        int conmejores = 1;
        HashMap<Integer, Estudiante> mejores = new HashMap<>();
        HashMap<Integer, Estudiante> copia = new HashMap<>(BaseDatos);
        for (int i = 0; i < 3; i++) {
            int key = 0;
            Estudiante mayor = new Estudiante( "Null", "Null", "Null",0,0,0);
            for (Map.Entry<Integer, Estudiante> entry : copia.entrySet()) {
                if (entry.getValue().getPromedio() > mayor.getPromedio()) {
                    mayor = entry.getValue();
                    key = entry.getKey();
                }
            }
            mejores.put(conmejores++, mayor);
            copia.remove(key);
        }
        return mejores;
    }

    public HashMap<Integer, Estudiante> GetBaseDatos() {
        return BaseDatos;
    }

}

package modelos;

import java.util.ArrayList;

public class BD_Estudiantes {
    public ArrayList<Estudiantes> listaEstudiantes = new ArrayList<>();

    public BD_Estudiantes() {
        listaEstudiantes.add(new Estudiantes("Julian", "Sierra", "Decimo", 4.3, 4.1, 4.4));
        listaEstudiantes.add(new Estudiantes("Felipe", "Martinez", "Decimo", 4.7, 4.8, 4.9));
        listaEstudiantes.add(new Estudiantes("Mateo", "Gamboa", "Noveno", 3.7, 3.8, 3.9));
        listaEstudiantes.add(new Estudiantes("David", "Carrillo", "octavo", 2.7, 2.8, 2.9));
        listaEstudiantes.add(new Estudiantes("Miguel", "serna", "septimo", 4.7, 3.8, 2.9));
    }

    public void AñadirCompra(Estudiantes e) {
        listaEstudiantes.add(e);
    }

    public ArrayList<Estudiantes> getBd_Estudiantes() {
        return listaEstudiantes;
    }

    public ArrayList<Estudiantes> getMejoresESTUDIANTES() {
        ArrayList<Estudiantes> copia = new ArrayList<>();
        ArrayList<Estudiantes> mejores = new ArrayList<>();
        for (Estudiantes e : listaEstudiantes) {
            copia.add(e);
        }
        for (int i = 0; i < 3; i++) {
            Estudiantes mayor = new Estudiantes( "Null", "Null", "Null", -1, -1, -1);
            for (Estudiantes e : copia) {
                if (e.getPromedio() > mayor.getPromedio()) {
                    mayor = e;
                }

            }
            mejores.add(mayor);
            copia.remove(mayor);

        }
        return mejores;
    }

}

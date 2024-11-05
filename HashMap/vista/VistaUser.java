package vista;
import java.util.Scanner;
import controlador.Controlador;
import modelo.Estudiante;

public class VistaUser {
    private static Scanner scan = new Scanner(System.in);
    private static  Controlador c = new Controlador();

    public static void Ejecutar(){
        c.Ejecutar();
    }

    public static int Menu(){
        System.out.println("Bienvenido usuario\n1.Mostrar Todos los estudiantes\n2.Mostrar los 3 mejores promedios\n3.Agregar un estudiante\n4.Editar Usuario\n5.Eliminar Estudiante\n6.Consultar Estudiante\n7.salir");
        int r = scan.nextInt();
        scan.nextLine();
        return r;
    }
    
    public static void MostrarDatos(int clave, Estudiante e){
        System.out.println("Esta es la informacion del estudiante de la clave : " + clave);
        System.out.println("El Nombre es : " + e.getNombre());
        System.out.println("El Apellido es : " + e.getApellido());
        System.out.println("El Curso al que asiste es :  " + e.getCurso());
        System.out.println("La Nota numero 1 es : " + e.getNota1());
        System.out.println("La Nota numero 2 es : " + e.getNota2());
        System.out.println("La Nota numero 3 es : " + e.getNota3());
        System.out.println("El Promedio del estudiantes es : " + e.getPromedio());
        System.out.println("El resultado de aprobado es : " + e.getAprobo() + "\n");
    }

    public static Estudiante CrearEstudiante(){
        System.out.println("Ingrese el nombre del estudiante ");
        String nombre = scan.nextLine();
        System.out.println("Ingrese el apellido del estudiante ");
        String apellido = scan.nextLine();
        System.out.println("Ingrese el curso del estudiante ");
        String curso = scan.nextLine();
        double nota1 = RecibirNota("Ingrese la nota uno ");
        double nota2 = RecibirNota("Ingrese la nota dos ");
        double nota3 = RecibirNota("Ingrese la nota tres ");
        Estudiante UsuarioNuevo = new Estudiante(nombre, apellido, curso, nota1, nota2, nota3);
        return UsuarioNuevo;
    }

    public static double RecibirNota(String mensaje){
        while (true) {
            System.out.println(mensaje);
            double nota = scan.nextDouble();
            scan.nextLine();
            if (nota < 1 || nota > 5) {
                System.out.println("La nota no puede ser mayor de 5 o inferior a 1");
            }else{
                return nota;
            }
        }
    }

    public static int EditarKey(){
        System.out.println("Ingrese la clave que desea editar ");
        int c = scan.nextInt();
        scan.nextLine();
        return c;
    }

    public static void MensajeError(){
        System.out.println("El codigo del estudiante no existe ");
    }


}

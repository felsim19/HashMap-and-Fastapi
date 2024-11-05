package vista;
import java.util.Scanner;
import controlador.Controlador;
import modelos.Estudiantes;

public class VistaUser {
    private static Scanner scan = new Scanner(System.in);
    private static Controlador c = new Controlador();
    public static void Ejecutar(){
        c.Ejecutar();
    }
    public static int Menu(){
        System.out.println("Bienevenido usuario\n1.Mostrar Todos los estudiantes\n2.Mostrar los 3 mejores promedios\n3.Agregar un estudiante\n4.salir");
        int r = scan.nextInt();
        scan.nextLine();
        return r;
    }
    public static void ImprimirDatos(Estudiantes e){
        System.out.println("Informacion Estudiantes");
        System.out.println("El codigo es " + e.getCodigo());
        System.out.println("El nombre es " + e.getNombre());
        System.out.println("El apellido es " + e.getApellido());
        System.out.println("El curso es " + e.getCurso());
        System.out.println("La nota uno es " + e.getNota1());
        System.out.println("La nota dos es " + e.getNota2());
        System.out.println("La nota tres es " + e.getNota3());
        System.out.println("El promedio es " + e.getPromedio());
        System.out.println("El aprobado es " + e.getAprobo());
    }
    
    public static Estudiantes CrearUsuario(){
            System.out.println("Ingrese Su nombre ");
            String nombre = scan.nextLine();
            System.out.println("Ingrese Su Apellido ");
            String apellido = scan.nextLine();
            System.out.println("Ingrese Su Curso ");
            String curso = scan.nextLine();
            double nota1 = SolicitarNota("Ingrese la nota uno");
            double nota2 = SolicitarNota("Ingrese la nota dos");
            double nota3 = SolicitarNota("Ingrese la nota tres");
            Estudiantes nuevoestudiantes = new Estudiantes(nombre, apellido, curso, nota1, nota2, nota3);
            return nuevoestudiantes;
    } 
    
    public static double SolicitarNota(String mensaje){
        while (true) {
        System.out.println(mensaje);
        Double nota = scan.nextDouble();
        scan.nextLine();
        if(nota < 1.0 || nota > 5.0){
            System.out.println("Las notas no pueden ser mayores a 5 o menos a 1");
        }else{
            return nota;
        }
        }
    }
}

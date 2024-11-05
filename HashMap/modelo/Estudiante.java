package modelo;

public class Estudiante{
    private String Nombre;
    private String Apellido;
    private String Curso;
    private double nota1;
    private double nota2;
    private double nota3;

    public Estudiante(){
    }

    public Estudiante(String nombre, String apellido, String curso, double nota1, double nota2, double nota3) {
        setNombre(nombre);
        setApellido(apellido);
        setCurso(curso);
        setNota1(nota1);
        setNota2(nota2);
        setNota3(nota3);
        getPromedio();
        getAprobo();
    }

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String nombre) {
        this.Nombre = nombre;
    }

    public String getApellido() {
        return Apellido;
    }

    public void setApellido(String apellido) {
        this.Apellido = apellido;
    }

    public String getCurso() {
        return Curso;
    }

    public void setCurso(String curso) {
        this.Curso = curso;
    }

    public double getNota1() {
        return nota1;
    }

    public void setNota1(double nota1) {
        this.nota1 = nota1;
    }

    public double getNota2() {
        return nota2;
    }

    public void setNota2(double nota2) {
        this.nota2 = nota2;
    }

    public double getNota3() {
        return nota3;
    }

    public void setNota3(double nota3) {
        this.nota3 = nota3;
    }

    public double getPromedio() {
        return (nota1 + nota2 + nota3) / 3;
    }

    public boolean getAprobo() {
        return getPromedio() >= 3.5;
    }
    
}

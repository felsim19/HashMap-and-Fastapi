package modelos;

public class Estudiantes {
    private static int Codigo = 0;
    private int id;
    private String Nombre;
    private String Apellido;
    private String Curso;
    private double Nota1;
    private double Nota2;
    private double Nota3;
    
    public Estudiantes( String nombre, String apellido, String curso, double nota1, double nota2, double nota3) {
        setCodigo();
        setNombre(nombre);
        setApellido(apellido);
        setCurso(curso);
        setNota1(nota1);
        setNota2(nota2);
        setNota3(nota3);
    }

    public int getCodigo() {
        return id;
    }
    public void setCodigo() {
        this.id = ++ Codigo;
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
        return Nota1;
    }
    public void setNota1(double nota1) {
        this.Nota1 = nota1;
    }
    public double getNota2() {
        return Nota2;
    }
    public void setNota2(double nota2) {
        this.Nota2 = nota2;
    }
    public double getNota3() {
        return Nota3;
    }
    public void setNota3(double nota3) {
        this.Nota3 = nota3;
    }
    public double getPromedio() {
        double n1 = getNota1();
        double n2 = getNota2();
        double n3 = getNota3();
        double Promedio = (n1+n2+n3)/3;
        return Promedio;
    }
    public Boolean getAprobo() {
        boolean Aprovo = false;
        if(getPromedio() >= 3.5){
            Aprovo = true;
        }
        return Aprovo;
    }
}

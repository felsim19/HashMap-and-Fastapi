import java.util.HashMap;

public class EjemploHashMap {
    public static void main(String[] args) {
        //crear un HashMap
        HashMap<String, Double > valores = new HashMap<>();

        //Agregar Valores
        valores.put("Felipe", 15.2);
        valores.put("Mateo", 19.2);
        valores.put("david", 5.8);

        // Verificar si una clave existe en el HashMap
        if (valores.containsKey("Felipe")) {
            System.out.println("Felipe está en el JSON");
        }else{
            System.out.println("No esta");
        }

        //iterar Valores
        for(String clave : valores.keySet()){
            double valor = valores.get(clave);
            System.out.printf("claves: %s y Valores: %f ||\n", clave,valor);
        }

        // Eliminar una entrada del HashMap
        valores.remove("Felipe");

        //Actualizar
        valores.put("david", 8.8);

        // Tamaño del HashMap
        System.out.println("Tamaño del HashMap: " + valores.size());
        for(double clave : valores.values()){
            System.out.println("la clave " + clave);
        }
    }   
}
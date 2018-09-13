# pyton

doubleMe x = x + x
doubleUs x y = x*2 + y*5

factorial::Int->Int
factorial 0 = 1
factorial n = n* factorial(n-1)

cuadrado::Int->Int
cuadrado x = x * x		

vec = [4,6,9,8,7]
ra = [5,8,9,11]

sec = [-3..3]


se=[1,5..20]
vc = [20,18..1]

c = [x | x <-[1,3..15]]
o = [x+x | x <-[1..12]]
m = [x*x|x<-[1..10]]


public static void main(String[] args) {
        // TODO code application logic here

        String a = "he1la";
        char cadena[] = new char[a.length()];
        cadena = a.toCharArray();
        String tex = "hrueba de texto ";
        char texto[] = new char[tex.length()];
        texto = tex.toCharArray();
        // bad match table
        int correr [] = new int [a.length()];
        
        
        for (int i = 0; i < tex.length(); i++) {
//            System.out.print(texto[i]);
            for (int j = 0; j < a.length(); j++) {
                if (texto[i] == cadena[j]) {
                    System.out.println(" Correcdt " + cadena[j]);                // coincidencias de letras
                }
            }

        }
        
    }

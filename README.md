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

        String a = "he1lo";
        char patron[] = new char[a.length()];
        patron = a.toCharArray();
        String tex = "prueba de texto ";
        char texto[] = new char[tex.length()];
        texto = tex.toCharArray();
        // bad match table
        int corro [] = new int [patron.length];
        char sub[]= new char[patron.length];
        boolean d = false;
        for (int m =0; m< patron.length; m++){
            System.out.println(patron[m]);
            for (int j =0; j< patron.length; j++){
                System.out.println("un "+ sub[j]);
                if(patron[m]==sub[j]){
                    System.out.println("ya existe");
                     d =true;
//                    corro[m] = patron.length-m-1;
                }else{
                    if(d==true){
//                      sub[m]=patron[m];
                    System.out.println("valor "+ sub[m]+ " " +j);  
                    }else{
                    
                      sub[m]=patron[m];
//                    j = patron.length+1;
                    }
                }
                
            }  
        
        }
        for (int m =0; m< patron.length; m++){
            
            System.out.println("/"+sub[m]);
        
        }
        
        
//        for (int i = (patron.length-1); i < texto.length; i++) {
//            System.out.println("primera "+i);
//            for (int j = a.length()-1; j > 0; j--) {
//                System.out.println("2da "+j);
//                if (texto[i] == patron[j]) {
//                    System.out.println(" coincide " + patron[j]);                // coincidencias de letras
//                }else{
//                    System.out.println("No "+ texto[i] + " " + patron[j]);
//                    j=0;
//                }   
//            }
//             i = al salto  corro[] 
//        }
        
    }
    
}

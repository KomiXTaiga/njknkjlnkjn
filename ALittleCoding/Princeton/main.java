public class main{
    public static void main(String[] args) {
        double b = Double.parseDouble(args[0]);
        double c = Double.parseDouble(args[1]);
        double discriminat = b*b -4.0*c;
        double d = Math.sqrt(discriminat);
        System.out.println((-b+d)/2.0);
        System.out.println((-b-d)/2.0);
    }
}
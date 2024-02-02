import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import edu.princeton.cs.algs4.StdOut;

public class Permutation {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java Permutation <int> <path>");
            return;
        }

        int k = Integer.parseInt(args[0]);
        String path = args[1];
        RandomizedQueue<String> rq = new RandomizedQueue<>();

        try {
            File file = new File(path);
            Scanner scanner = new Scanner(file);
            while (scanner.hasNext()) {
                String item = scanner.next();
                rq.enqueue(item);
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + path);
            return;
        }

        for (int i = 0; i < k; i++) {
            if (!rq.isEmpty()) {
                StdOut.println(rq.dequeue());
            }
        }
    }
}

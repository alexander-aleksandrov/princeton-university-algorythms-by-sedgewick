import java.util.Arrays;

public class BruteCollinearPoints {
    private int numberOfSegments = 0;
    private LineSegment[] lineSegments;

    public BruteCollinearPoints(Point[] points) {
        validateInput(points);
        
        lineSegments = new LineSegment[points.length];
        int i = 0;  
        while (i < points.length) {
            int j = i + 1;
            while (j < points.length) {
                int k = j + 1;
                while (k < points.length) {
                    Point p = points[i];
                    Point q = points[j];
                    Point r = points[k];

                    if (isCollinear(p, q, r)) {
                        
                        int m = k + 1;
                        while (m < points.length) {
                            Point s = points[m];
                            if (isCollinear(p, q, s)) addSegment(p, q, r, s);
                                                       
                            m++;
                        }
                    }
                    k++;
                }
                j++;
            }
            i++;
        }

    }    
    
    // the number of line segments
    public int numberOfSegments() {
        return numberOfSegments;
    }
    
    private void validateInput(Point[] points) {
        if (points == null) throw new IllegalArgumentException("The input argument is null");
        for (Point point : points) if (point == null) throw new IllegalArgumentException("The input contains null points");

        for (int i = 0; i < points.length; i++)
            for (int j = i+1; j < points.length; j++)
                if (points[i].compareTo(points[j]) == 0)
                    throw new IllegalArgumentException("The input contains repeated points");
    }
    
    private boolean isCollinear(Point p, Point q, Point r) {
        return Double.compare(p.slopeTo(q), p.slopeTo(r)) == 0;
    }
    // the line segments
    public LineSegment[] segments() {
        return Arrays.copyOfRange(lineSegments, 0, numberOfSegments());
    }
    
    private void addSegment(Point p, Point q, Point r, Point s) {

        // Finding the most separated set of points
        Point[] collinearPoints = {p, q, r, s};
        Arrays.sort(collinearPoints);
        Point minPoint = collinearPoints[0];
        Point maxPoint = collinearPoints[3];

        lineSegments[numberOfSegments++] = new LineSegment(minPoint, maxPoint);
    }

    public static void main(String[] args) {
        Point[] points = new Point[4];
        points[0] = new Point(1, 1);
        points[1] = new Point(2, 2);
        points[2] = new Point(3, 3);
        points[3] = new Point(4, 4);
        BruteCollinearPoints bruteCollinearPoints = new BruteCollinearPoints(points);
        System.out.println(bruteCollinearPoints.numberOfSegments());
        LineSegment[] lineSegments = bruteCollinearPoints.segments();
        for (int i = 0; i < lineSegments.length; i++) {
            System.out.println(lineSegments[i]);
        }
    }

 }
 
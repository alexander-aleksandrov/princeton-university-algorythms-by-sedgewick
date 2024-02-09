import java.util.Arrays;
import java.util.Stack;


public class FastCollinearPoints {
    private int numberOfSegments = 0;
    private LineSegment[] lineSegments;
    private Segment[] lineSegmentsInternal;
    

    public FastCollinearPoints(Point[] points) {
        validateInput(points);
        numberOfSegments = 0;
        lineSegments = new LineSegment[points.length];
        lineSegmentsInternal = new Segment[points.length];

        for (Point p : points) {
            Point[] pointsCopy = Arrays.copyOf(points, points.length);
            Arrays.sort(pointsCopy, p.slopeOrder());    
            Point[] slopes = Arrays.copyOfRange(pointsCopy, 1, pointsCopy.length);

            for(int i = 0; i < slopes.length - 2; i++) {
                Point q = slopes[i];
                Point[] candidates = Arrays.copyOfRange(slopes, i+1, slopes.length);
                Point[] collinearPoints = findCollinearSequence(p, q, candidates);
                
                if (collinearPoints.length >= 4) {
                    addSegment(collinearPoints);
                    break;
                }
            }
        }
        
    }
    
    private void addSegment(Stack<Point> collinearPoints) {
        addSegment(collinearPoints.toArray(new Point[0]));
    }

    private void addSegment(Point[] ps) {
        Arrays.sort(ps);
        Segment s = new Segment(ps[0], ps[ps.length - 1]);

        if (!isIncluded(s)) {
            lineSegmentsInternal[numberOfSegments] = s;
            lineSegments[numberOfSegments] = new LineSegment(s.minPoint, s.maxPoint);
            numberOfSegments++;
        }
    }

    private boolean isIncluded(Segment s) {
        for (int i = 0; i < numberOfSegments; i++)
            if (s.equals(lineSegmentsInternal[i]))
                return true;
        return false;
    }

    private Point[] findCollinearSequence(Point p, Point q, Point[] candidates) {
        Stack<Point> collinearPoints = new Stack<Point>();
        collinearPoints.push(p);
        collinearPoints.push(q);

        for (Point r : candidates)
            if (areCollinear(p, collinearPoints.peek(), r))
                collinearPoints.push(r);
            else
                break;

        return collinearPoints.toArray(new Point[0]);
    }
    
    public int numberOfSegments() {
        return numberOfSegments;
    }

    // the line segments
    public LineSegment[] segments() {
        return Arrays.copyOfRange(lineSegments, 0, numberOfSegments());
    }

    private boolean areCollinear(Point p1, Point p2, Point p3) {
        return (Double.compare(p1.slopeTo(p2), p1.slopeTo(p3)) == 0);
    }
    
    private void validateInput(Point[] points) {
        if (points == null) throw new IllegalArgumentException("The input argument is null");
        for (Point point : points) if (point == null) throw new IllegalArgumentException("The input contains null points");

        for (int i = 0; i < points.length; i++)
            for (int j = i+1; j < points.length; j++)
                if (points[i].compareTo(points[j]) == 0)
                    throw new IllegalArgumentException("The input contains repeated points");
    }

    public static void main(String[] args) {
        Point[] points = new Point[8];
        points[0] = new Point(10000, 0);
        points[1] = new Point(0, 10000);
        points[2] = new Point(3000, 7000);
        points[3] = new Point(7000, 3000);
        points[4] = new Point(20000, 21000);
        points[5] = new Point(3000, 4000);
        points[6] = new Point(14000, 15000);
        points[7] = new Point(6000, 7000);
        FastCollinearPoints fastCollinearPoints = new FastCollinearPoints(points);
        System.out.println(fastCollinearPoints.numberOfSegments());
        LineSegment[] lineSegments = fastCollinearPoints.segments();
        for (int i = 0; i < lineSegments.length; i++) {
            System.out.println(lineSegments[i]);
        }
    }

    private class Segment {
        public Point minPoint, maxPoint;

        public Segment(Point minPoint, Point maxPoint) {
            this.minPoint = minPoint;
            this.maxPoint = maxPoint;
        }

        public boolean equals(Segment other) {
            return ((minPoint.compareTo(other.minPoint) == 0) && (maxPoint.compareTo(other.maxPoint) == 0));
        }
    }
}

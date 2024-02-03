import java.util.Iterator;
import java.util.NoSuchElementException;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdOut;

public class RandomizedQueue<Item> implements Iterable<Item> {
    private Item[] array;
    private Integer[] deletedPlaces;
    private int deletedTail;
    private int tail;
    private int size;

    
    public RandomizedQueue() {
        array = (Item[]) new Object[1];
        deletedPlaces = new Integer[1];
        deletedTail = 0;
        tail = 0;
        size = 0;
    }

    
    
    private void resize(int capacity) {
        Item[] temp = (Item[]) new Object[capacity];

        Integer[] deletedTemp = new Integer[capacity];
    
        System.arraycopy(array, 0, temp, 0, array.length);
        System.arraycopy(deletedPlaces, 0, deletedTemp, 0, deletedPlaces.length);
        array = temp;
        deletedPlaces = deletedTemp;
    }



    public boolean isEmpty() {
        return size == 0;
    }

    public int size() {
        return size;
    }

    public void enqueue(Item item) {
        if (item == null) {
            throw new IllegalArgumentException("Item is null");
        }
        if (deletedTail > 0) {
            array[deletedPlaces[--deletedTail]] = item;
        } else {     
            if (tail == array.length) { 
                resize(2 * array.length);
            }
            array[tail++] = item;
        }
        size++;
    }

    public Item dequeue() {
        if (isEmpty()) {
            throw new NoSuchElementException("RandomizedQueue is empty");
        }
        int index = StdRandom.uniform(tail);
        while (array[index] == null) {
            index = StdRandom.uniform(tail);
        }
        if (deletedTail == deletedPlaces.length) {
            resize(2 * array.length); // Note: You might want to adjust this logic
        }
        deletedPlaces[deletedTail++] = index;
        Item item = array[index];
        array[index] = null;
        size--;
        return item;
    }

    public Item sample() {
        if (isEmpty()) {
            throw new NoSuchElementException("RandomizedQueue is empty");
        }
        int index;
        do {
            index = StdRandom.uniform(tail);
        } while (array[index] == null);
        return array[index];
    }

    @Override
    public Iterator<Item> iterator() {
        return new RandomizedQueueIterator();
    }

    private class RandomizedQueueIterator implements Iterator<Item> {
        private final Item[] shuffledArray;
        private int currentIndex = 0;

        
        public RandomizedQueueIterator() {
            shuffledArray = (Item[]) new Object[size];
            int index = 0;
            for (Item item : array) {
                if (item != null) {
                    shuffledArray[index++] = item;
                }
            }
            StdRandom.shuffle(shuffledArray);
        }

        @Override
        public boolean hasNext() {
            return currentIndex < size;
        }

        @Override
        public Item next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            return shuffledArray[currentIndex++];
        }
    }

    public static void main(String[] args) {
        RandomizedQueue<Integer> queue = new RandomizedQueue<>();
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        for (int item : queue) {
            StdOut.println(item);
        }
        System.out.println(queue.sample());
        System.out.println(queue.dequeue());
        System.out.println(queue.size());
        System.out.println(queue.isEmpty());
    }
}

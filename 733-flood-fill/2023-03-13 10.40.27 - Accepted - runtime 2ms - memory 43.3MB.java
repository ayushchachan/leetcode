import java.util.HashSet;
import java.util.LinkedList;
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if (image[sr][sc] == color) return image;

        int m = image.length;
        int n = image[0].length;

        LinkedList<Integer> Q = new LinkedList<>();
        HashSet<Integer> visited = new HashSet<>();
        int pixel = index(n, sr, sc);


        Q.add(pixel);


        while (!Q.isEmpty()) {
            pixel = Q.removeFirst();
            visited.add(pixel);

            int c = pixel % n;
            int r = (pixel - c) / n;

            if (r > 0 && image[r][c] == image[r - 1][c] && !visited.contains(index(n, r - 1, c))) {
                int newpixel = index(n, r - 1, c);
                Q.add(newpixel);
            }

            if (c < image[0].length - 1 && image[r][c] == image[r][c + 1] && !visited.contains(index(n, r, c + 1))) {
                int newpixel = index(n, r, c + 1);
                Q.add(newpixel);
            }

            if (c > 0 && image[r][c] == image[r][c - 1] && !visited.contains(index(n, r, c - 1))) {
                int newpixel = index(n, r, c - 1);
                Q.add(newpixel);
            }

            if (r < image.length - 1 && image[r][c] == image[r + 1][c] && !visited.contains(index(n, r + 1, c))) {
                int newpixel = index(n, r + 1, c);
                Q.add(newpixel);
            }

            image[r][c] = color;
        }
        return image;
    }

    public int index(int n, int r, int c) {
        return r*n + c;
    }
}

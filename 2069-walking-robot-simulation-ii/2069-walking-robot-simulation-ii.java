class Robot {
    int width, height;
    int x, y;
    int dir; // 0=East, 1=North, 2=West, 3=South

    int[][] dirs = {{1,0}, {0,1}, {-1,0}, {0,-1}};
    String[] dirNames = {"East", "North", "West", "South"};

    public Robot(int width, int height) {
        this.width = width;
        this.height = height;
        this.x = 0;
        this.y = 0;
        this.dir = 0; // East
    }

    public void step(int num) {
        int perimeter = 2 * (width + height) - 4;
        num %= perimeter;

        // special case: full cycle
        if (num == 0) num = perimeter;

        while (num > 0) {
            int nx = x + dirs[dir][0];
            int ny = y + dirs[dir][1];

            // if out of bounds → turn left (counterclockwise)
            if (nx < 0 || nx >= width || ny < 0 || ny >= height) {
                dir = (dir + 1) % 4;
            } else {
                x = nx;
                y = ny;
                num--;
            }
        }
    }

    public int[] getPos() {
        return new int[]{x, y};
    }

    public String getDir() {
        return dirNames[dir];
    }
}
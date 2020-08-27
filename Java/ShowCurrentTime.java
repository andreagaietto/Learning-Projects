public class ShowCurrentTime {
    public static void main(String[] args) {

        // obtain the total milliseconds since Midnight, Jan 1 1970
        long totalMilliseconds = System.currentTimeMillis();
       // total seconds
        long totalSeconds = totalMilliseconds / 1000;
        // obtain current second
        long currentSecond = totalSeconds % 60;
        //obtain total minutes
        long totalMinutes = totalSeconds / 60;
        //obtain current minute
        long currentMinutes = totalMinutes % 60;
        //obtain total hours
        long totalHours = totalMinutes / 60;
        //obtain current hour
        long currentHour = totalHours % 24;

        //display results
        System.out.println("Current time is " + currentHour + ":"
        + currentMinutes + ":" + currentSecond + " GMT");

    }
}
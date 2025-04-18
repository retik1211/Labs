class AnalogClock {
    private int hourHand; // Угол часовой стрелки (0-360)
    private int minuteHand; // Угол минутной стрелки (0-360)

    public AnalogClock(int hourHand, int minuteHand) {
        this.hourHand = hourHand;
        this.minuteHand = minuteHand;
    }

    public int getHourHand() {
        return hourHand;
    }

    public int getMinuteHand() {
        return minuteHand;
    }
}

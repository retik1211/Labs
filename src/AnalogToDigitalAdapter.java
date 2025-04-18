class AnalogToDigitalAdapter implements DigitalClock {
    private AnalogClock analogClock;

    public AnalogToDigitalAdapter(AnalogClock analogClock) {
        this.analogClock = analogClock;
    }

    @Override
    public String getTime() {
        // Преобразуем углы стрелок в часы и минуты
        int hours = (analogClock.getHourHand() / 30) % 12; // 360 градусов = 12 часов, 1 час = 30 градусов
        int minutes = (analogClock.getMinuteHand() / 6) % 60; // 360 градусов = 60 минут, 1 минута = 6 градусов

        // Форматируем время в строку "HH:MM"
        return String.format("%02d:%02d", hours, minutes);
    }
}

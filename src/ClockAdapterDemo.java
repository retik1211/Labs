public class ClockAdapterDemo {
    public static void main(String[] args) {
        // Создаем часы со стрелками
        AnalogClock analogClock = new AnalogClock(90, 180); // Часовая стрелка на 90 градусов (3 часа), минутная на 180 градусов (30 минут)

        // Создаем адаптер
        DigitalClock digitalClock = new AnalogToDigitalAdapter(analogClock);

        // Получаем время в цифровом формате
        System.out.println("Время в цифровом формате: " + digitalClock.getTime());
    }
}

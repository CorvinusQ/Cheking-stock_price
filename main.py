# Проверка стоимости акций с помощью Python
import yfinance as yf

# Запрашивает у пользователя имя акции
STK =input('Введите название: ')

# Получение исторических данных о рынке
data = yf.Ticker(STK).history(period="1d")

# Извлечение последней рыночной стоимости
last_market_price = data['Close'].iloc[-1]

# Отображение последней рыночной цены
print('Последняя рыночная стоимость акции:', last_market_price)

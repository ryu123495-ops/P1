stock_prices = {
    "삼성전자": 78000,
    "SK하이닉스": 195000,
    "NAVER": 215000,
    "카카오": 48000,
    "현대차": 250000
}

customers = [
    {
        "name": "김철수",
        "stocks": [
            {"name": "삼성전자", "buy_price": 70000, "quantity": 10},
            {"name": "NAVER", "buy_price": 230000, "quantity": 5},
            {"name": "카카오", "buy_price": 45000, "quantity": 20}
        ]
    },
    {
        "name": "이영희",
        "stocks": [
            {"name": "SK하이닉스", "buy_price": 170000, "quantity": 8},
            {"name": "삼성전자", "buy_price": 82000, "quantity": 15}
        ]
    },
    {
        "name": "박민수",
        "stocks": [
            {"name": "현대차", "buy_price": 220000, "quantity": 4},
            {"name": "카카오", "buy_price": 55000, "quantity": 30},
            {"name": "NAVER", "buy_price": 200000, "quantity": 3}
        ]
    }
]

for customer in customers:
    investment = 0
    current_value = 0

    for stock in customer["stocks"]:
        investment += stock["buy_price"] * stock["quantity"]
        current_value += stock_prices[stock["name"]] * stock["quantity"]

    profit = current_value - investment

    print(f"\n{customer['name']}")
    print(f"투자원금: {investment:,}원")
    print(f"평가금액: {current_value:,}원")
    print(f"수익금: {profit:,}원")


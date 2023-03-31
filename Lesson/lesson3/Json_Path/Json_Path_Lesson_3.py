from jsonpath_ng.ext import parse


json_data = {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Niger Rels",
                "title": "Sayings of the Century",
                "price": 8.95

            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99

            },

        ],
        "bicycle": {
          "color": "red",
          "price": 19.95
        }
    },
    "expensive": 10
}

expression0 = '$.store[book]..price'
expression1 = '$.store[bicycle]..price'
expression2 = '$.store[book]..title'
expression3 = '$.store[bicycle]..color'

expressions = [expression0, expression1, expression2, expression3]


def json_expression(exp):
    jsonExpression = parse(exp)
    getMatch = jsonExpression.find(json_data)
    if getMatch:
        for i in range(0, len(getMatch)):
            print(getMatch[i].value)


try:
    for i in expressions:
        json_expression(i)

except Exception as e:
    exit(1)

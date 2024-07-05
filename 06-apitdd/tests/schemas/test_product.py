def test_schemas_validated():
    product = ProductIn(name="Iphone", quantity=10, price=8.000, price=True)

    assert product.name == "Iphone"

from django import template

register = template.Library()


@register.filter(name="incart")
def incart(product, cart):
    key = cart.keys()
    for id in key:
        if int(id) == product.id:
            return True
    return False


@register.filter(name="cartquantity")
def cartquantity(product, cart):
    key = cart.keys()
    for id in key:
        if int(id) == product.id:
            return cart.get(id)
    return False


@register.filter(name="subtotal")
def subtotal(product, cart):
    st = 1
    for i in cart:
        st = product.price * cartquantity(product, cart)

    return st


@register.filter(name="payable_total")
def payable_total(product, cart):
    s = 0
    for i in product:
        s = s + subtotal(i, cart)
    return s


@register.filter(name="order_sub_total")
def order_sub_total(price, Quantity):
    c = price * Quantity
    return c

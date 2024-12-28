from django.core.management.base import BaseCommand
from api.models import Customer, Product, Order
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create initial data for the CRM system'

    def handle(self, *args, **kwargs):
        # Create a user
        user = User.objects.create_user(username='john_doe', password='password123')

        # Create a customer linked to the user
        customer = Customer.objects.create(user=user, phone='1234567890', address='123 Street Name')

        # Create some products
        product1 = Product.objects.create(name='Product A', price=100.00, stock=50)
        product2 = Product.objects.create(name='Product B', price=200.00, stock=30)

        # Create an order
        order = Order.objects.create(customer=customer)
        order.product.add(product1, product2)

        # Save the order
        order.save()

        # Output to confirm the data creation
        self.stdout.write(self.style.SUCCESS('Successfully created initial data:'))
        self.stdout.write('Customer: ' + str(customer))
        self.stdout.write('Product1: ' + str(product1))
        self.stdout.write('Product2: ' + str(product2))
        self.stdout.write('Order: ' + str(order))

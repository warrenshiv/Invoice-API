from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Invoice, InvoiceDetail
from rest_framework import status

class InvoiceAPITest(APITestCase):

    def setUp(self):
        # Create an invoice and its details for use in tests
        self.invoice = Invoice.objects.create(date='2024-04-17', customer_name='John Doe')
        self.invoice_detail = InvoiceDetail.objects.create(
            invoice=self.invoice,
            description='Test Product',
            quantity=10,
            unit_price=9.99,
            price=99.90
        )
    
    def test_create_invoice(self):
        """
        Ensure we can create a new invoice object.
        """
        url = reverse('invoice-list-create')
        data = {
            'date': '2024-04-19',
            'customer_name': 'Jane Doe',
            'details': [
                {
                    'description': 'New Service',
                    'quantity': 5,
                    'unit_price': 50.00,
                    'price': 250.00
                }
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 2)

    def test_get_invoice(self):
        """
        Ensure we can retrieve an invoice.
        """
        url = reverse('invoice-retrieve-update-destroy', args=[self.invoice.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['customer_name'], 'John Doe')  # Verify the data

    def test_update_invoice(self):
        """
        Ensure we can update an invoice.
        """
        url = reverse('invoice-retrieve-update-destroy', args=[self.invoice.id])
        data = {
            'date': '2024-04-18',
            'customer_name': 'Updated Name',
            'details': [
                {
                    'id': self.invoice_detail.id,
                    'description': 'Updated Product',
                    'quantity': 20,
                    'unit_price': 19.99,
                    'price': 399.80
                }
            ]
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_invoice = Invoice.objects.get(id=self.invoice.id)
        self.assertEqual(updated_invoice.customer_name, 'Updated Name')  # Verify update

    def test_delete_invoice(self):
        """
        Ensure we can delete an invoice.
        """
        url = reverse('invoice-retrieve-update-destroy', args=[self.invoice.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Invoice.objects.count(), 0)

    def test_list_invoices(self):
        """
        Ensure we can list all invoices.
        """
        url = reverse('invoice-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Since only one invoice was created in setUp

# Additional test cases for failure modes and edge cases should also be considered

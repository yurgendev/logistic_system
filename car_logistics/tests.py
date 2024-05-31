from unittest import mock
from django.test import TestCase
from django.utils import timezone
from .models import Auction, Warehouse, Company, Customer, Account, Lot


class AuctionModelTest(TestCase):
    def test_string_representation(self):
        auction = Auction(name="copartino")
        self.assertEqual(str(auction), auction.name)


class WarehouseModelTest(TestCase):
    def test_string_representation(self):
        warehouse = Warehouse(name="Test Warehouse")
        self.assertEqual(str(warehouse), warehouse.name)


class CompanyModelTest(TestCase):
    def test_string_representation(self):
        company = Company(name="Test Company")
        self.assertEqual(str(company), company.name)


class CustomerModelTest(TestCase):
    def test_string_representation(self):
        customer = Customer(name="Test Customer")
        self.assertEqual(str(customer), customer.name)


class AccountModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="Test Customer")

    def test_string_representation(self):
        account = Account(name="Test Account", customer=self.customer)
        self.assertEqual(str(account), account.name)


class LotModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="Test Customer")
        self.account = Account.objects.create(name="Test Account", customer=self.customer)
        self.auction = Auction.objects.create(name="Test Auction")
        self.warehouse = Warehouse.objects.create(name="Test Warehouse")
        self.company = Company.objects.create(name="Test Company")

    def test_lot_creation(self):
        lot = Lot.objects.create(
            auto="Test Auto",
            vin="12345678901234567",
            lot="Test Lot",
            account=self.account,
            auction=self.auction,
            url="http://test.com",
            customer=self.customer,
            company=self.company,
            price=100.00,
            keys=True,
            line="Test Line",
            booking_number="Test Booking Number",
            container="Test Container",
            date_purchase=timezone.now().date(),
        )
        self.assertEqual(lot.status, 'new')
        self.assertEqual(lot.get_wait_days(), 0)


class LotModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="Test Customer")
        self.account = Account.objects.create(name="Test Account", customer=self.customer)
        self.auction = Auction.objects.create(name="Test Auction")
        self.warehouse = Warehouse.objects.create(name="Test Warehouse")
        self.company = Company.objects.create(name="Test Company")

    def test_lot_moves_to_archived_after_30_days(self):
        lot = Lot.objects.create(
            auto="Test Auto",
            vin="12345678901234567",
            lot="Test Lot",
            account=self.account,
            auction=self.auction,
            url="http://test.com",
            customer=self.customer,
            company=self.company,
            price=100.00,
            keys=True,
            line="Test Line",
            booking_number="Test Booking Number",
            container="Test Container",
            date_purchase=timezone.now().date(),
        )
        lot.update_status('unloaded')
        lot.status_changed = timezone.now() - timezone.timedelta(days=31)
        lot.date_unloaded = timezone.now().date()
        lot.save()

        # Move time forward by 31 days
        with mock.patch('django.utils.timezone.now', return_value=timezone.now() + timezone.timedelta(days=31)):
            lot.move_to_next_status()

        self.assertEqual(lot.status, 'archived')




class LotModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="Test Customer")
        self.account = Account.objects.create(name="Test Account", customer=self.customer)
        self.auction = Auction.objects.create(name="Test Auction")
        self.warehouse = Warehouse.objects.create(name="Test Warehouse")
        self.company = Company.objects.create(name="Test Company")

    def test_get_wait_days(self):
        lot = Lot.objects.create(
            auto="Test Auto",
            vin="12345678901234567",
            lot="Test Lot",
            account=self.account,
            auction=self.auction,
            url="http://test.com",
            customer=self.customer,
            company=self.company,
            price=100.00,
            keys=True,
            line="Test Line",
            booking_number="Test Booking Number",
            container="Test Container",
            date_purchase=timezone.now().date(),
        )

        # Test for 'new' status
        lot.update_status('new')
        self.assertEqual(lot.get_wait_days(), 0)

        # Test for 'dispatched' status
        lot.update_status('dispatched')
        self.assertEqual(lot.get_wait_days(), 0)

        # Test for 'terminal' status
        lot.update_status('terminal')
        self.assertEqual(lot.get_wait_days(), 0)

        # Test for 'loading' status
        lot.update_status('loading')
        self.assertEqual(lot.get_wait_days(), 0)

        # Test for 'shipped' status
        lot.update_status('shipped')
        self.assertEqual(lot.get_wait_days(), 0)

        # Test for 'unloaded' status
        lot.update_status('unloaded')
        self.assertEqual(lot.get_wait_days(), 0)

        # Test for 'archived' status
        lot.update_status('archived')
        self.assertEqual(lot.get_wait_days(), 0)
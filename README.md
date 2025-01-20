## Settings

 

### **Required Settings**

| Setting                     | Description                                                                                          |
|-----------------------------|------------------------------------------------------------------------------------------------------|
| `PAYPAL_PAYFLOW_VENDOR_ID`  | Your merchant login ID created when you registered the account with PayPal.                         |
| `PAYPAL_PAYFLOW_PASSWORD`   | Your merchant password.                                                                             |

### **Optional Settings**

| Setting                        | Description                                                                                          | Default Value   |
|--------------------------------|------------------------------------------------------------------------------------------------------|-----------------|
| `PAYPAL_PAYFLOW_CURRENCY`      | The 3-character currency code to use for transactions.                                               | `'USD'`         |
| `PAYPAL_PAYFLOW_USER`          | The ID of the user authorized to process transactions. If you only have one user, use `VENDOR_ID`.   | Same as `VENDOR_ID` |
| `PAYPAL_PAYFLOW_PARTNER`       | The ID provided by a PayPal reseller. If your account was created directly with PayPal, use `'PayPal'`. | `'PayPal'`      |
| `PAYPAL_PAYFLOW_PRODUCTION_MODE` | Whether to use PayPal’s production servers. Set to `True` in production environments.              | `False`         |
| `PAYPAL_PAYFLOW_DASHBOARD_FORMS` | Display forms on the transaction detail page for capturing, voiding, or crediting transactions.    | `False`         |

### **Example Configuration**

Add the following to your `settings.py` file:

```python
PAYPAL_PAYFLOW_VENDOR_ID = "your_vendor_id"
PAYPAL_PAYFLOW_PASSWORD = "your_password"

# Optional settings
PAYPAL_PAYFLOW_CURRENCY = "USD"
PAYPAL_PAYFLOW_USER = "your_user_id"  # Only required if different from VENDOR_ID
PAYPAL_PAYFLOW_PARTNER = "PayPal"
PAYPAL_PAYFLOW_PRODUCTION_MODE = True  # Set to True in production
PAYPAL_PAYFLOW_DASHBOARD_FORMS = True  # Enable transaction management forms

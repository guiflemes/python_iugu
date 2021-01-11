## Info

This is not complete yet new releases with more functionality coming soon


## Iugu

This provides Python Async and Typed REST APIs to create, process and manage payments on IUGU  to Python Version 3.7 >
    
  ## Installation
pip install python-iugu
  
  ## How to Use
You should create an iugu instance using your [api token](https://dev.iugu.com/reference#section-criando-suas-chaves-de-api-api-tokens):


  ```python
from python_iugu import config  
  
config(token=IUGU_API_TOKEN)
```

Now you can use the instance to iniciate the module you want:

Exemplo:

**Create Invoice**

```python
from python_iugu import InvoiceService  
from python_iugu import invoice_request  
from python_iugu import utils_request  
  
new_invoice = invoice_request.InvoiceRequest(  
    email="xxxx@testinvoice.com",  
    due_date="2021-01-10",  
    payer=invoice_request.Payer(  
        name="xxxxx",  
        cpf_cnpj="xxxxxxxx",  
        phone_prefix="xx",  
        phone="xxxxxxx",  
        email="xxxxxx",  
        address=invoice_request.Address(  
            zip_code="xxxxxx",  
            street="xxxxx",  
            number="xxxxx",  
            district="xxxxx",  
            city="xxxx",  
            state="xxxx",  
            country="xx"  
  )  
    ),  
    items=[  
        invoice_request.Item(  
            description="test",  
            quantity=1,  
            price_cents=100  
  )  
    ],  
    custom_variables=[  
        utils_request.CustomVariable(  
            name="xxx",  
            value="xx"  
  )  
    ]  
)  
  
i = InvoiceService().create(new_invoice)

```

**List Customer**

```python
from python_iugu import CustomerService  
  
c = CustomerService().list() 

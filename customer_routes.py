from fastapi import APIRouter, Depends
from app.auth import verify_api_key

from app.controllers.customer_controller import CustomerController
from app.schemas.customer import CustomerCreate, CustomerResponse


customer_routes = APIRouter(
    prefix="/customers",
    tags=["Customers"],
    dependencies=[Depends(verify_api_key)],
)

controller = CustomerController()


@customer_routes.post(
    "",
    response_model=CustomerResponse,
    status_code=201,
)
def create_customer(data: CustomerCreate):
    return controller.create(data)


@customer_routes.get(
    "/{customer_id}",
    response_model=CustomerResponse,
)
def get_customer(customer_id: int):
    return controller.get(customer_id)

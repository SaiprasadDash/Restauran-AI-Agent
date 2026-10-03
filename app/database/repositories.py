from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models import Order, SupportTicket


def get_order_by_order_id(
    db: Session,
    order_id: str,
) -> Order | None:
    statement = select(Order).where(
        Order.order_id == order_id
    )

    return db.scalar(statement)


def get_order_status(
    db: Session,
    order_id: str,
) -> str | None:
    order = get_order_by_order_id(db, order_id)

    if order is None:
        return None

    return order.status


def create_support_ticket(
    db: Session,
    ticket: SupportTicket,
) -> SupportTicket:

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return ticket